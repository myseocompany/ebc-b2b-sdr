# EBC — B2B SDR

Repositorio del proyecto **Eléctricas BC Corp (Miami, FL — FTZ)**: estrategia + código del sistema de reactivación comercial digital.

Operado bajo el **MySEO Marketing Harness** (desplegado localmente aquí; archivos raíz = gobernanza).

## Inicio

Todo LLM debe comenzar en `AGENTS.md` y seguir el orden de lectura indicado allí.

## Documento base

`PROPUESTA.md` — contrato vigente (1 oct → 31 dic 2026, 3 olas de 30 días).

## Estructura

- Archivos raíz: identidad, políticas, memoria, fuentes, tareas, decisiones y propuesta.
- `context/`: marcos de referencia (Revenue Architecture).
- `workflows/`: procedimientos operativos (SCAN → CONFIGURE → INSTALL → LAUNCH → MONITOR → REPORT).
- `templates/`: formatos reutilizables (aprobaciones, experimentos, reporte semanal).
- `progress/`: evidencia temporal, handoffs, snapshots semanales.
- `evals/`: pruebas de comportamiento del harness.
- `scripts/`: verificaciones deterministas.
- `tmp/`: dumps, PDFs fuente, artefactos locales. **Gitignored.**
- `.local/`: credenciales de servicios locales (MySQL EBC). **Gitignored.**

## Infraestructura local

- MySQL 8 con dump de AriCRM EBC: contenedor `ebc-mysql`, bind `127.0.0.1:3307`, DB `ebc_aricrm`.
- Credenciales en `.local/mysql.env` (chmod 600).
