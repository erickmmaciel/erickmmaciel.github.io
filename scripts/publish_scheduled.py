#!/usr/bin/env python3
"""Publica posts agendados cujo dia já chegou.

Lê _scheduled/schedule.json. Para cada post com published:false e date <= hoje:
  - move _scheduled/<slug>/ -> blog/<slug>/
  - insere o card no topo de blog/index.html
  - insere a URL no sitemap.xml (antes de </urlset>)
  - insere a entrada BlogPosting no schema Blog (após '"blogPost": [')
  - marca published:true no schedule.json

Roda no GitHub Actions (cron). Idempotente: rodar de novo não republica nada.
Imprime "PUBLISHED <slug>" para cada post publicado; nada se não houver nada a fazer.
"""
import json
import shutil
import datetime
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
QUEUE = ROOT / "_scheduled"
SCHEDULE = QUEUE / "schedule.json"
BLOG_INDEX = ROOT / "blog" / "index.html"
SITEMAP = ROOT / "sitemap.xml"

CARDS_MARKER = '<div class="blog-posts">'
SCHEMA_ANCHOR = '"blogPost": ['
SITEMAP_ANCHOR = "</urlset>"


def card_html(entry: dict) -> str:
    return f"""
        <a href="/blog/{entry['slug']}/" class="blog-post-card">
          <div>
            <div class="post-card-meta">
              <span class="post-card-tag">{entry['card_tag']}</span>
              <span class="post-card-sep">·</span>
              <span class="post-card-date">{entry['card_date']}</span>
            </div>
            <h2 class="post-card-title">{entry['card_title']}</h2>
            <p class="post-card-desc">{entry['card_desc']}</p>
          </div>
          <span class="post-card-arrow" aria-hidden="true">→</span>
        </a>
"""


def schema_entry(entry: dict) -> str:
    headline = entry["headline"].replace('"', '\\"')
    return f"""
    {{
      "@type": "BlogPosting",
      "headline": "{headline}",
      "url": "https://erick2m.com/blog/{entry['slug']}/"
    }},"""


def sitemap_entry(entry: dict) -> str:
    return f"""  <url>
    <loc>https://erick2m.com/blog/{entry['slug']}/</loc>
    <lastmod>{entry['date']}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
"""


def main() -> int:
    if not SCHEDULE.exists():
        print("no schedule.json — nothing to do")
        return 0

    schedule = json.loads(SCHEDULE.read_text(encoding="utf-8"))
    today = datetime.date.today()
    published_any = False

    for entry in schedule:
        if entry.get("published"):
            continue
        due = datetime.date.fromisoformat(entry["date"])
        if due > today:
            continue

        slug = entry["slug"]
        src = QUEUE / slug
        dst = ROOT / "blog" / slug
        if not src.exists():
            print(f"WARN: queued folder missing for {slug}, skipping", file=sys.stderr)
            continue
        if dst.exists():
            print(f"WARN: destination already exists for {slug}, skipping move", file=sys.stderr)
        else:
            shutil.move(str(src), str(dst))

        # blog index: insert card right after the container marker (newest on top)
        idx = BLOG_INDEX.read_text(encoding="utf-8")
        if CARDS_MARKER in idx and f'/blog/{slug}/' not in idx:
            idx = idx.replace(CARDS_MARKER, CARDS_MARKER + card_html(entry), 1)
        # blog schema: insert BlogPosting after the array opener
        if SCHEMA_ANCHOR in idx and f'"https://erick2m.com/blog/{slug}/"' not in idx:
            idx = idx.replace(SCHEMA_ANCHOR, SCHEMA_ANCHOR + schema_entry(entry), 1)
        BLOG_INDEX.write_text(idx, encoding="utf-8")

        # sitemap: insert before closing tag
        sm = SITEMAP.read_text(encoding="utf-8")
        if f'/blog/{slug}/' not in sm:
            sm = sm.replace(SITEMAP_ANCHOR, sitemap_entry(entry) + SITEMAP_ANCHOR, 1)
            SITEMAP.write_text(sm, encoding="utf-8")

        entry["published"] = True
        published_any = True
        print(f"PUBLISHED {slug}")

    if published_any:
        SCHEDULE.write_text(json.dumps(schedule, ensure_ascii=False, indent=2), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
