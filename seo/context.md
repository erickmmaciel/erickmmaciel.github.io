# Contexto — 2M Marketing (erick2m.com)

> Fonte de verdade do produto para o SEO autopilot. Tudo aqui vem do código do repo ou da página viva, com a fonte ao lado. Nunca de memória. Atualizar quando um fato mudar (ver Daily · fact check).

Última reconstrução: 2026-11-16

## O produto

**2M Marketing** — consultoria e assessoria de mídia paga de Erick Maciel, especializada em conectar o investimento em anúncios ao **resultado financeiro real** (receita fechada no CRM), não a cliques/CPL.
- Fonte: `llms.txt`, `index.html` (JSON-LD ProfessionalService), `README.md`
- Razão social: Erick Maciel Marketing LTDA · CNPJ 62.099.457/0001-52 (`index.html` JSON-LD)
- Posicionamento central: "Mídia paga conectada ao financeiro" (`index.html` <title>)
- Canais que gerencia: Meta Ads, Google Ads, LinkedIn Ads (`llms.txt`, páginas de serviço)

## Quem compra (ICP)

Fonte: `llms.txt` (seção "Quem atendemos")
- Empresas médias/grandes, faturamento > R$ 500k/ano
- Investimento mínimo em mídia: R$ 30k/mês
- B2B e B2C de ticket alto (> R$ 500/venda)
- CRM ativo: HubSpot, RD Station ou Salesforce
- Segmentos: SaaS, educação, serviços financeiros, saúde, imobiliário, indústria B2B, franquias

**Não atende:** e-commerce, política/eleições, empresas sem CRM, verba < R$ 30k/mês.

## Serviços (3 produtos — ATUAL, fonte: index.html § 03, nov/2026)

As ofertas foram renomeadas (reposicionamento). Nomes atuais na home:
1. **Diagnóstico** (pontual) — "para fundamentar uma decisão": analiso a operação e organizo prioridades, para quem já tem quem execute.
2. **Implementação** (por projeto) — "para conectar a estrutura": estruturo as conexões entre anúncios e processo comercial e preparo a continuidade com o responsável. (Era "Consultoria".)
3. **Gestão de Receita Rastreável** (recorrente · **oferta principal**) — "para conduzir continuamente": assumo a gestão das campanhas e uso a leitura comercial para orientar as decisões. (Era "Assessoria".)

Preços: "os valores de cada caminho são apresentados na conversa comercial, conforme o escopo" (index.html § 03). Mínimo R$ 30k/mês em mídia (llms.txt).
⚠️ `llms.txt` ainda usa os nomes antigos (Diagnóstico/Consultoria/Assessoria) — desatualizado; a home manda. Páginas que refletem as ofertas (/precos/, /google-ads/, /meta-ads/, /linkedin-ads/) devem usar os nomes atuais.

## Páginas de serviço (dinheiro)

- `/google-ads/` — Google Ads para B2B
- `/meta-ads/` — Meta Ads com integração CRM
- `/linkedin-ads/` — LinkedIn Ads para B2B

## Diferenciais (fonte: llms.txt)

- Rastreamento do clique à venda fechada no CRM
- Otimização por receita real, não por CPL
- Experiência com operações de R$ 700k+/mês em mídia
- Relatórios em linguagem financeira (CAC, LTV, payback, ROI/canal)
- Google Partner certificado

## Conversão (a ação que conta)

**WhatsApp / contato direto.** CTA principal → `https://wa.me/5555920002140` (presente na home e no blog). Secundário: `mailto:contato@erick2m.com`.

## Stack / como o site é feito

Fonte: `README.md` + inspeção do repo
- HTML estático puro, CSS sem framework, GitHub Pages (CNAME `erick2m.com`), deploy em push na `main`.
- Fontes: Instrument Serif + Inter Tight + JetBrains Mono (Google Fonts).
- GTM: `GTM-N7KQK6L`.
- Páginas = pasta + `index.html`. Blog idem (`blog/<slug>/index.html`).
- Posts agendados: `_scheduled/schedule.json` + `scripts/publish_scheduled.py` (bloqueado em robots.txt via `/_scheduled/`).
- SEO por página: `<title>`, `<meta description>`, `<link canonical>`, OG/Twitter, JSON-LD (ProfessionalService na home; Article + BreadcrumbList nos posts). Sitemap manual em `sitemap.xml`. `llms.txt` para crawlers de IA. `robots.txt` libera GPTBot/ChatGPT-User/PerplexityBot/ClaudeBot/Google-Extended/Bingbot; bloqueia CCBot.

## Contato

WhatsApp +55 (55) 9 2000-2140 · contato@erick2m.com · linkedin.com/in/erickmmaciel · RS, Brasil (Santo Ângelo).

## Lacunas de dados (fontes não conectadas nesta execução)

- **Google Search Console** — sem acesso. Desbloquearia: queries reais, posições, impressões, CTR, cobertura de indexação. Toda priorização de "página 2 → página 1" depende disso.
- **Ahrefs/Semrush** — sem acesso. Desbloquearia: volume, dificuldade, backlinks, gaps de concorrentes.
- **Analytics (GA4)** — sem acesso direto (só GTM instalado). Desbloquearia: conversões em WhatsApp por página.
