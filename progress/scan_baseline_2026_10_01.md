# Línea base — EBC CRM al 2026-10-01

**Workflow:** `workflows/01_scan.md` · **Tarea:** `O1-001` · **Responsable:** Nicolás

## Fuente

| | |
|---|---|
| Dump | `tmp/ebc_2026_10_01.gz` (TablePlus export, DB origen `y6zc6y8JIaricrm`) |
| Fecha de generación del dump | 2026-10-01 09:43 UTC-5 |
| Último registro en el dump | 2026-09-22 02:15 (última `customers.created_at`) |
| Primer registro en el dump | 2021-01-31 22:31 |
| Base local | MySQL 8.0 container `ebc-mysql` · DB `ebc_aricrm` · 210 tablas |
| Totales | 58,737 customers · 15 estados · 20+ fuentes |

> **Nota de desfase:** el dump cierra el 22 sep 2026. Los números abajo son el "estado al corte del 22 sep", no estrictamente al 1 oct. Hay 9 días de ciego — a validar con un dump nuevo si Alejandro reporta actividad reciente.

---

## Universo total

### Customers por fuente

| id | Fuente | Customers | % |
|---:|---|---:|---:|
| 1 | Jivo Chat | 24,994 | 42.5% |
| 14 | Feria ESS | 17,848 | 30.4% |
| 22 | **Google Maps** | **7,232** | **12.3%** |
| 4 | GestResponse - Landing Page | 3,903 | 6.6% |
| 10 | **Meta Ads - EBL** | **1,244** | **2.1%** |
| 15 | Feria ESS Corp | 1,170 | 2.0% |
| 13 | **Meta Ads - EBC** | **1,113** | **1.9%** |
| 17 | Feria FISE | 358 | 0.6% |
| 2 | Correo Electrónico | 315 | 0.5% |
| 20 | GetResponse - Invertek | 174 | 0.3% |
| 5 | SellerChat EBL | 125 | 0.2% |
| 11 | Google Ads | 74 | 0.1% |
| 21 | Base EBL | 54 | 0.1% |
| 7 | LP - Variadores | 44 | 0.1% |
| 6 | SellerChat EBC | 30 | 0.1% |
| 9 | LP - Importador Eléctrico | 27 | 0.0% |
| 8 | LP - Teltonika | 15 | 0.0% |
| — | (NULL) | 14 | 0.0% |
| 18 | LP - Webinar Altus | 3 | 0.0% |

### Customers por estado (universo total)

| id | Estado | Customers | % |
|---:|---|---:|---:|
| 1 | Nuevo | 31,497 | 53.6% |
| 4 | GANADO | 21,638 | 36.8% |
| 2 | Seguimiento | 2,371 | 4.0% |
| 9 | Datos incorrectos | 1,545 | 2.6% |
| 7 | No contesta | 745 | 1.3% |
| 5 | Sin interés | 249 | 0.4% |
| 8 | Mal calificado | 138 | 0.2% |
| 11 | Interés calificado | 130 | 0.2% |
| 14 | Intento de contacto | 119 | 0.2% |
| 15 | Asistirá | 98 | 0.2% |
| 6 | PERDIDO | 97 | 0.2% |
| 13 | Cierre (ganado - perdido) | 53 | 0.1% |
| 10 | Nueva conversión | 20 | 0.0% |
| — | (NULL) | 14 | 0.0% |
| 12 | Propuesta enviada | 12 | 0.0% |
| 3 | En Negociación | 11 | 0.0% |

> ⚠️ **Caveat crítico:** 21,479 de los 21,638 `GANADO` provienen de `Jivo Chat`. Es casi seguro que la integración Jivo marca conversaciones cerradas como `GANADO` automáticamente — **no son ventas reales**. Cualquier métrica de conversión que lea `status_id=4` sin filtrar origen va a estar inflada ~130x.

---

## Foco del contrato — Meta Ads - EBC (source_id=13)

Validación de los números de la propuesta (`PROPUESTA.md §1`):

| Estado | Propuesta (12 may) | Dump (22 sep) | Δ |
|---|---:|---:|---:|
| Nuevo | 565 | **561** | −4 |
| Seguimiento | 213 | **212** | −1 |
| No contesta | 187 | **187** | 0 |
| Mal calificado | 79 | **79** | 0 |
| Datos incorrectos | 26 | **26** | 0 |
| Sin interés | 19 | **19** | 0 |
| Intento de contacto | 11 | **11** | 0 |
| Perdido | 5 | **5** | 0 |
| Nueva conversión | 4 | **4** | 0 |
| Interés calificado | 3 | **6** | +3 |
| En Negociación | 1 | **2** | +1 |
| **GANADO** | **0** | **1** | **+1 ⚠️** |
| **TOTAL** | **1,113** | **1,113** | **0** |

### Hallazgos

- **Volumen total exacto** a la propuesta (1,113). Entre mayo y septiembre no entraron leads nuevos de Meta Ads EBC (`new customers Meta EBC last 30 days = 0`), lo que sugiere que la pauta se pausó o no está capturando — a validar.
- **1 GANADO existe** en Meta Ads EBC. Hay que ver el detalle de ese registro antes de la primera reunión (ID, fecha de cierre, valor, responsable).
- **Avance mínimo** entre mayo y septiembre: 4 leads se movieron de Nuevo → Seguimiento/calificación. Confirma el diagnóstico de "capacidad de gestión".
- **Cola de Ola 1 congelada:** 561 Nuevo + 212 Seguimiento + 11 Intento = **784 leads vivos Meta EBC** (vs 778 propuestos).

---

## Fuera de alcance explícito — Meta Ads - EBL (source_id=10)

| Estado | n |
|---|---:|
| Nuevo | 356 |
| No contesta | 229 |
| Seguimiento | 212 |
| Sin interés | 86 |
| Intento de contacto | 73 |
| Interés calificado | 71 |
| Asistirá | 54 |
| PERDIDO | 37 |
| **GANADO** | **35** |
| Mal calificado | 31 |
| Cierre (ganado - perdido) | 24 |
| Datos incorrectos | 17 |
| Propuesta enviada | 6 |
| En Negociación | 6 |
| Nueva conversión | 5 |
| (NULL) | 2 |
| **TOTAL** | **1,244** |

- **35 GANADO reales** sobre 1,244 leads = **2.8% conversión bruta**.
- EBL ya tiene un sistema que convierte. Es un punto de comparación útil para calibrar expectativas de EBC.
- **Pendiente:** confirmar con Alejandro si EBL está dentro de alcance o fuera. En la propuesta no se menciona.

---

## Base histórica — Google Maps (source_id=22)

| Estado | n |
|---|---:|
| Nuevo | 7,180 |
| Seguimiento | 19 |
| Asistirá | 10 |
| Intento de contacto | 8 |
| PERDIDO | 6 |
| Sin interés | 3 |
| Interés calificado | 3 |
| Mal calificado | 1 |
| Propuesta enviada | 1 |
| GANADO | 1 |
| **TOTAL** | **7,232** |

- Propuesta dice **6,527** contactos GMB; el dump muestra **7,232 customers** con `source_id=22` y **6,541** en la tabla raw `apify_google_maps_results`. La diferencia (705) probablemente son contactos agregados entre mayo y septiembre vía `apify_google_maps_runs` (346 runs registradas).
- **99.3% está en Nuevo** → base casi completamente sin tocar. Confirma el diagnóstico "activo sin activar" de la propuesta.
- Esta es la cola priorizada para el **bot WhatsApp de Ola 1** (cuota 50–100/sem).

---

## Actividad reciente (últimos 30 días del dump: 22 ago → 22 sep)

| Métrica | Valor |
|---|---:|
| Nuevos customers (todas las fuentes) | 5 |
| Nuevos customers Meta Ads EBC | 0 |
| Nuevos customers Meta Ads EBL | 0 |
| Cotizaciones en tabla `quotes` | 0 (tabla vacía) |

- La propuesta dice "0 cotizaciones generadas en el mes, 2 propuestas enviadas, 0 ventas atribuibles". El dump confirma: `quotes` vacía, 0 Meta Ads nuevos. Las "2 propuestas" probablemente son los 2 customers hoy en estado `Propuesta enviada` (12 total; vendrían de otros meses).
- Que `Meta Ads EBC/EBL = 0 nuevos` en los últimos 30 días sugiere que la pauta estuvo pausada o la integración se rompió. **Validar con Alejandro.**

---

## Queries SQL reproducibles

Ejecutar sobre el container `ebc-mysql` (`127.0.0.1:3307`, DB `ebc_aricrm`). Credenciales en `.local/mysql.env`.

```sql
-- Universo
SELECT COUNT(*) FROM customers;
SELECT MIN(created_at), MAX(created_at) FROM customers;

-- Por fuente
SELECT cso.id, cso.name, COUNT(*) AS n
FROM customers c LEFT JOIN customer_sources cso ON cso.id = c.source_id
GROUP BY cso.id, cso.name ORDER BY n DESC;

-- Por estado
SELECT cs.id, cs.name, COUNT(*) AS n
FROM customers c LEFT JOIN customer_statuses cs ON cs.id = c.status_id
GROUP BY cs.id, cs.name ORDER BY n DESC;

-- Meta Ads EBC (foco contrato)
SELECT cs.name AS status, COUNT(*) AS n
FROM customers c LEFT JOIN customer_statuses cs ON cs.id = c.status_id
WHERE c.source_id = 13
GROUP BY cs.name ORDER BY n DESC;

-- Meta Ads EBL (fuera de alcance explícito)
SELECT cs.name AS status, COUNT(*) AS n
FROM customers c LEFT JOIN customer_statuses cs ON cs.id = c.status_id
WHERE c.source_id = 10
GROUP BY cs.name ORDER BY n DESC;

-- Google Maps (base histórica)
SELECT cs.name AS status, COUNT(*) AS n
FROM customers c LEFT JOIN customer_statuses cs ON cs.id = c.status_id
WHERE c.source_id = 22
GROUP BY cs.name ORDER BY n DESC;

-- Jivo Chat GANADO = probable falso positivo
SELECT cso.name AS source, COUNT(*) AS n
FROM customers c LEFT JOIN customer_sources cso ON cso.id = c.source_id
WHERE c.status_id = 4
GROUP BY cso.name ORDER BY n DESC;

-- Actividad últimos 30 días del dump
SELECT COUNT(*) FROM customers WHERE created_at >= '2026-08-22';
SELECT COUNT(*) FROM customers WHERE created_at >= '2026-08-22' AND source_id = 13;
SELECT COUNT(*) FROM customers WHERE created_at >= '2026-08-22' AND source_id = 10;
```

---

## Lo que esta línea base habilita

1. Medir avance de Ola 1 contra el estado del 22 sep (no 1 oct — ver caveat arriba).
2. Separar KPIs reales vs ruido Jivo Chat en reportería semanal.
3. Diseñar la cola de ataque del SDR: 784 Meta EBC vivos + 7,180 GMB sin tocar.
4. Entender el benchmark EBL para calibrar expectativas de cierre.

## Preguntas pendientes para la primera reunión con Alejandro

- ¿Qué pasó con la pauta Meta Ads EBC/EBL entre agosto y septiembre? (0 leads nuevos)
- ¿El GANADO Meta EBC #1 es venta real? (ID, fecha, valor, responsable)
- ¿Está EBL dentro de alcance del contrato EBC o es otra entidad / otro contrato?
- ¿Cómo se registran las cotizaciones si `quotes` está vacía? ¿Hay otra fuente?
- ¿Los 21,479 GANADO de Jivo Chat son auto-cierres de conversación o ventas reales?
