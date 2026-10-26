# TASKS

## Convención

Estados: `pendiente`, `en_progreso`, `en_revision`, `bloqueada`, `completa`.

| ID | Ola | Resultado esperado | Estado | Responsable | Siguiente acción | Criterio de terminado |
| --- | --- | --- | --- | --- | --- | --- |
| O1-001 | Ola 1 | Snapshot línea base 2026-10-01 (customers por fuente/estado, 1,113 Meta EBC confirmados, 6,527 GMB) | completa | Nicolás | — | ✓ `progress/scan_baseline_2026_10_01.md` creado con cifras + queries SQL + preguntas pendientes |
| O1-002 | Ola 1 | Reducir pauta Meta Ads a ~$751.800 COP/mes | pendiente | Nicolás | Preparar `templates/APPROVAL.md` con audiencia/presupuesto nuevos; esperar aprobación Alejandro | Aprobación registrada + cambio ejecutado en Business Manager + evidencia |
| O1-003 | Ola 1 | Contratar SDR dedicado LATAM (4h/día, modalidad prestación servicios) | en_progreso | Alejandro + Nicolás | Revisar `progress/sdr_propuesta_contratacion.md`; definir con EBC quién factura + accesos; publicar vacante | Candidato firmando acuerdo con fecha de inicio tras prueba paga de 1 semana |
| O1-004 | Ola 1 | Simplificar CRM a 3 estados operativos (Nuevo, Cotizado, Seguimiento) | pendiente | Nicolás | Diseñar migración de los 15 estados actuales → 3 sin perder histórico | Script de migración testeado + plan de rollback |
| O1-005 | Ola 1 | Bot WhatsApp activación GMB (cuota 50–100/semana) | pendiente | Nicolás | Especificar flujo conversacional + handoff al SDR | Primer envío piloto a 50 contactos aprobado y ejecutado |
| O1-006 | Ola 1 | Dashboard de pendientes diarios para Alejandro | pendiente | Nicolás | Boceto + queries base | Alejandro lo usa cada mañana y lo valida en reunión semanal |
| O1-007 | Ola 1 | Guion de llamada SDR con dos vías (lead de pauta / frío) alineado a los lineamientos de EBC | en_revision | Nicolás | Validar con EBC los 5 pendientes del documento (consultor comercial, mínimos, crédito, marcas, tiempos de despacho) | Guion aprobado por Alejandro + SDR entrenado sobre él |
| H-001 | Harness | Validar que el harness instalado opera correctamente para EBC | en_progreso | Nicolás | Completar primera reunión semanal usando `templates/WEEKLY_REPORT.md` | Primer reporte semanal generado con datos reales |

No marcar una tarea `completa` sin enlazar evidencia o resultado verificable.

## Metas por mes (de `PROPUESTA.md`)

| Mes | Rango | Cotizaciones | Ventas | Hitos |
| --- | --- | --- | --- | --- |
| Mes 1 | 1 oct → 28 oct | 8–12 | 0–1 | 565 Nuevo contactados; 200+ GMB conversando |
| Mes 2 | 29 oct → 25 nov | 10–15 | 1–3 | Primer cierre del sistema digital; tasa respuesta leads nuevos > 80% |
| Mes 3 | 26 nov → 31 dic | 10–15 | 2–4 | Tasa cierre 25–30%; segundo SDR si capacidad lo exige |
