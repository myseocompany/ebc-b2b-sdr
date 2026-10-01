# DECISIONS

## Registro

| Fecha | Decisión | Responsable | Fundamento | Impacto |
| --- | --- | --- | --- | --- |
| 2026-09-08 | El harness de MySEO vive en archivos Markdown, estructura del repositorio y verificaciones locales. | MySEO | Debe controlar al LLM que opera sobre el repositorio y permanecer independiente del modelo. | Las plataformas externas son herramientas; no constituyen el harness. |
| 2026-09-08 | Separar siempre adquisición, retención y expansión. | MySEO | Marco Revenue Architecture. | Estrategias, métricas y reportes deben clasificar cada resultado. |
| 2026-10-01 | Desplegar el harness MySEO embebido en el repo `ebc-b2b-sdr` (single-client). | Nicolás | EBC requiere repositorio dedicado para estrategia + código; estructura `clients/<cliente>/` innecesaria. | Gobernanza (POLICIES, DECISIONS, TASKS) y código conviven en el mismo repo; `tmp/` y `.local/` gitignored. |
| 2026-10-01 | Retirar la política "no cargar información del cliente en herramientas externas sin autorización". | Nicolás | Los agentes IA procesan sin retener datos de leads; la restricción generaba fricción operativa. | Permite usar datos del dump directamente en el flujo con LLMs. Permanece la prohibición de incluir PII en entregables públicos. |
| 2026-10-01 | Contrato EBC vigente: 1 oct → 31 dic 2026 (90 días, 3 olas). | Nicolás + Alejandro | Confirmación verbal sobre `Propuesta_EBC_Miami_ver3.pdf`. | Reemplaza el rango "1 sep – 31 nov" indicado al margen del PDF ver3. |

Agregar nuevas decisiones sin reescribir el historial. Si una decisión cambia, añadir una fila que indique cuál reemplaza.

