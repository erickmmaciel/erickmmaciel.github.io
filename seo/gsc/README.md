# Dados do Google Search Console (export CSV)

O autopilot lê os dados reais de busca daqui toda semana. Sem estes arquivos, a priorização de "página 2 → página 1" e a checagem de indexação ficam cegas.

## Como exportar (leva ~2 min, repetir 1x por semana)

1. Abra o [Search Console](https://search.google.com/search-console) na propriedade `erick2m.com`.
2. Menu **Desempenho → Resultados da pesquisa**.
3. No topo, defina o período em **Últimos 3 meses** (ou "16 meses" na primeira vez).
4. Ligue as 4 métricas: **Cliques, Impressões, CTR médio, Posição média** (clique nos cartões).
5. Botão **Exportar** (canto superior direito) → **CSV** (baixa um `.zip`).
6. Descompacte e **jogue os CSVs aqui dentro de `seo/gsc/`**, sobrescrevendo os anteriores. Depois faça commit/push (ou me avise que eu faço).

## Arquivos que o export gera (nomes podem vir em PT)

| Arquivo | Conteúdo | Uso no autopilot |
|---|---|---|
| `Consultas.csv` / `Queries.csv` | query, cliques, impressões, CTR, posição | achar queries em posição 8–20 (página 2) para empurrar |
| `Páginas.csv` / `Pages.csv` | URL, cliques, impressões, CTR, posição | quais páginas convertem tráfego; CTR baixo = reescrever title/description |
| `Datas.csv` / `Dates.csv` | data, cliques, impressões | tendência semana a semana no relatório |
| `Países.csv` / `Countries.csv` | país | confirmar foco BR |
| `Dispositivos.csv` / `Devices.csv` | desktop/mobile | — |

## Convenção

- Pode deixar o nome original do export; eu identifico pelo conteúdo das colunas.
- Se preferir, renomeie o principal para `queries.csv` e `pages.csv`.
- Não precisa limpar nem editar: eu leio o CSV cru.
- **Não contém dado sensível** (é agregado de busca), então pode versionar no repo sem problema.

## Alternativa

Se um dia quiser automatizar, dá para trocar por um conector MCP do Search Console (autorizado via `/mcp`) e aposentar o export manual.
