# Brief de contexto — Eléctricas BC Corp. (EBC)

**Versión 1.0 · 26 de octubre de 2026 · Documento de contexto para LLM**

> **Para qué sirve este archivo.** Es el paquete mínimo de contexto que necesita cualquier LLM —en este repositorio o en una herramienta externa— para trabajar sobre la cuenta de Eléctricas BC Corp. sin inventar datos ni malinterpretar el contrato. Está escrito para pegarse completo en una conversación nueva.
>
> **Fuentes:** `PROPUESTA.md` (contrato), `progress/scan_baseline_2026_10_01.md` (dump CRM 2026-10-01), `progress/2026-10-20_reporte-semanal-myseo-ebc.md` (operación), `progress/guion_llamada_sdr_ebc_v2.md` (discurso comercial), `DECISIONS.md`, `TASKS.md`, `POLICIES.md`.
>
> **No contiene datos personales.** Ni nombres de leads, ni teléfonos, ni correos, ni enlaces a registros del CRM. Es deliberado: este documento se puede pegar en cualquier herramienta. Si alguien lo amplía, mantener esa regla.

---

## 1. Cómo leer este documento

Está ordenado de lo más estable a lo más volátil:

| Sección | Qué contiene | Vida útil |
|---|---|---|
| 2–4 | Quién es EBC, el diagnóstico y el contrato | Estable hasta el 31 de diciembre de 2026 |
| 5 | Estado de la operación | Cambia cada semana |
| 6 | Datos y fuentes disponibles | Cambia cuando se refresca el dump o se arregla un conector |
| 7–9 | Vocabulario, roles y pendientes | Estable, pero los pendientes se cierran de a poco |

Tres marcas se usan en todo el texto y hay que respetarlas al razonar sobre esta cuenta:

- **Hecho verificado** — tiene fuente, fecha y método. Se puede afirmar.
- **Inferencia** — lectura razonable de un hecho, pero no comprobada. Se debe marcar como tal.
- **Pendiente** — no se sabe. No se rellena con una suposición plausible.

---

## 2. Qué es Eléctricas BC Corp.

### Hechos verificados

| | |
|---|---|
| **Qué vende** | Material eléctrico industrial de automatización y control: contactores, relés bimetálicos y térmicos, variadores de frecuencia, material de control |
| **Dónde está** | Miami, Florida (EE. UU.), zona franca / FTZ |
| **Desde cuándo** | Constituida en Estados Unidos desde 2001 |
| **Portafolio** | Más de 5.000 referencias activas con inventario disponible para entrega inmediata (no contra pedido a fábrica) |
| **Marcas ancla** | Relpol (contactores, relés) e Invertek (variadores). Aparecen también Teltonika y Altus en fuentes históricas del CRM |
| **A quién le vende** | Empresas de Centroamérica y Sudamérica que importan desde EE. UU., más mercado doméstico en Florida/EE. UU. |
| **Ticket promedio** | USD 3.000 (referencia de la propuesta) |
| **Ventas anuales** | USD 300K (referencia de la propuesta). Objetivo de crecimiento declarado: 20% |

### El rasgo que define todo lo demás

**EBC despacha desde Miami, no desde el país del cliente.** Esto no es un detalle logístico: es el filtro comercial principal. Un prospecto interesado que no puede o no quiere importar desde Estados Unidos no es un prospecto. Por eso el perfil de cliente ideal se define por capacidad de importar antes que por interés en el producto.

### Entidad relacionada — no confundir

Existe **Eléctricas Bogotá Ltda. (EBL)**, con operación y stock en Colombia. Es una entidad distinta con su propio flujo de leads en el mismo CRM (`Meta Ads - EBL`, 1.244 leads al corte del 22 sep). **EBL está fuera del alcance explícito de este contrato** y su inclusión es un pendiente con el cliente. Dos consecuencias prácticas:

- Cualquier cifra del CRM debe filtrar por fuente, o mezcla las dos operaciones.
- Nada de lo que se diga en nombre de EBC puede prometer stock en Bogotá ni en el país del prospecto.

### Perfil de cliente ideal (ICP)

- **Tipos de negocio:** tableristas, integradores, importadores, distribuidores, almacenes eléctricos.
- **Perfil comercial:** proyectos activos, compradores recurrentes, referencias comerciales verificables.
- **Requisito duro:** dispuesto a importar, o con experiencia previa importando, y consciente de que el material sale de Miami.
- **Ventana:** se prioriza decisión de compra en los próximos 2 meses.

Los tres criterios con los que se califica en la llamada: ¿ha importado alguna vez?, ¿tiene agencia de transporte o agente de carga?, ¿implementa el material o lo comercializa?

---

## 3. El diagnóstico — por qué existe este contrato

**El problema de EBC no es de adquisición. Es de capacidad de gestión.**

La pauta ya entregó 1.113 leads de Meta Ads. Con dos personas dedicadas al cierre, no hay forma aritmética de procesar ese inventario acumulado más el flujo nuevo. El resultado observado al momento de la propuesta (mayo 2026), confirmado por el dump de octubre:

| Indicador | Valor |
|---|---:|
| Leads Meta Ads EBC acumulados | 1.113 |
| En estado `Nuevo`, sin un solo contacto | 565 (50,8%) |
| En `Seguimiento` sin avance documentado | 213 (19,1%) |
| **Leads vivos pero abandonados** | **778 (70%)** |
| Leads que llegaron al final del embudo | 8 (0,72%) |
| Cotizaciones generadas en el último mes | 0 |
| Ventas atribuibles a digital | 0 |
| Contactos históricos de Google Maps sin gestionar | 6.527 (7.232 en el dump) |

**Inferencia central de la propuesta, y sigue siendo la hipótesis de trabajo:** como el equipo de cierre solo alcanza a responder a los más insistentes —que suelen ser curiosos del catálogo—, se concluyó que «los leads son malos». Lo más probable es lo contrario: los compradores reales están enterrados en los 565 que nunca recibieron contacto.

De ahí la tesis del contrato:

> **Primero procesar lo que ya hay. Después optimizar lo que entra.**

Corolario operativo: pautar más sobre este sistema sería desperdiciar inversión, y filtrar más en origen descartaría leads útiles que ya están dentro sin procesar.

---

## 4. El contrato

### Marco

| | |
|---|---|
| **Proveedor** | MySEO (agencia). Responsable: Nicolás |
| **Cliente** | Eléctricas BC Corp. |
| **Período** | 1 de octubre → 31 de diciembre de 2026 (90 días) |
| **Emisión de la propuesta** | 12 de mayo de 2026. Fechas confirmadas verbalmente el 1 de octubre de 2026 |
| **Naturaleza de los 90 días** | Período mínimo de evaluación: antes de ese plazo no hay base estadística para juzgar el sistema |

### Las tres olas

| Ola | Fechas | Objetivo | Metas |
|---|---|---|---|
| **Ola 1 — Procesar inventario** | 1 → 28 oct | Procesar los 778 leads vivos y activar conversación con parte de los 6.527 históricos | 8–12 cotizaciones · 0–1 ventas · 565 `Nuevo` contactados · 200+ GMB conversando |
| **Ola 2 — Calificar adquisición** | 29 oct → 25 nov | Que los leads nuevos sean comprables, no curiosos | 10–15 cotizaciones · 1–3 ventas · >80% de respuesta en leads nuevos |
| **Ola 3 — Sostener y escalar** | 26 nov → 31 dic | Sistema funcionando con resultados medibles | 10–15 cotizaciones · 2–4 ventas · tasa de cierre 25–30% |

⚠️ **Las olas no coinciden con el calendario.** El Mes 1 cierra el **miércoles 28 de octubre**; el Mes 2 abre el jueves 29. Cualquier corte mensual que use «fin de mes calendario» mete tres días del Mes 2 dentro del Mes 1.

### Palancas de la Ola 1

- **SDR dedicado desde la semana 1** (junior remoto LATAM). *Sin este recurso la propuesta no es viable.* Tercerizado y facturado aparte a EBC.
- Calificación retroactiva masiva de los 565 `Nuevo`: secuencia única de WhatsApp + llamada; tras tres intentos sin respuesta pasa a `No contesta`.
- Auditoría del CRM: reducir de 15 estados a tres operativos (**Nuevo, Cotizado, Seguimiento**).
- Recordatorios automáticos a los 7 días sin toque, y dashboard diario de pendientes para el cierre comercial.
- Bot de WhatsApp sobre la base de Google Maps, cuota de 50–100 contactos/semana, con derivación en tiempo real al SDR.
- **Reducción temporal de pauta** a ~$751.800 COP/mes mientras se procesa el inventario (vuelve a ~$1.503.600 en la Ola 2).
- Modelo Sprint: sesiones intensivas donde el bot prospecta y el SDR pasa el lead caliente a llamada inmediata. Producto ancla: Relpol → contactores.

### Honorarios

| Concepto | Valor |
|---|---:|
| Fee mensual de agencia | $3.500.000 COP · *cobrado a Eléctricas Bogotá Ltda.* |
| SDR dedicado (obligatorio desde el mes 1) | $1.500.000 COP/mes · *facturado aparte por EBC* |
| Pauta dedicada a EBC | ~$1.503.600 COP/mes (~USD 400), mitad de los $5M COP brutos compartidos con EBL |

TRM de referencia: $3.759 COP/USD al 12 de mayo de 2026.

### Reparto de responsabilidades

| Agencia (MySEO) | EBC |
|---|---|
| Estrategia de adquisición y conversión | **Cierre comercial** |
| Google Ads, Meta Ads, WhatsApp outbound | SLA de seguimiento (<24 h al primer contacto) |
| Creatividades, copy, landings | Carga de cotizaciones y ventas en el CRM |
| Configuración y mantenimiento del CRM | Decisiones de producto y pricing |
| Automatizaciones y recordatorios | — |
| Coordinación y supervisión del SDR | — |
| Activación de la base histórica | — |
| Reportería semanal de embudo | — |

### SLA que asume EBC

- Primer contacto a lead nuevo en **menos de 24 horas hábiles**.
- Actualización del estado del lead en el CRM dentro de 48 horas de cada interacción.
- Reunión semanal de revisión de embudo (30 min).
- Registro de cotizaciones enviadas y ventas cerradas en el CRM.

> Si EBC incumple sistemáticamente el SLA, los leads se consideran entregados y la responsabilidad del no-cierre no es de la agencia.

### Condiciones de salida (preaviso de 30 días, sin penalidad)

| La agencia puede salir si | EBC puede salir si |
|---|---|
| Después de 90 días, EBC incumple el SLA en más del 30% de los leads entregados | Después de 90 días, no hay mínimo 8 cotizaciones/mes sostenidas |
| Se toman decisiones unilaterales de pauta o canal que contradicen la estrategia acordada | La conversión de lead a cotización está por debajo del 15% sobre leads calificados |

---

## 5. Estado de la operación

**Último corte verificado: 7–14 de octubre de 2026** (seis días con actividad: 7, 8, 9, 10, 13 y 14). Fuente: `progress/2026-10-20_reporte-semanal-myseo-ebc.md`.

| Indicador | Plan | Real | Lectura |
|---|---:|---:|---|
| Contactados / tipificados | 195/sem | 156 | 80% del plan. Gestión total, no solo Ola 1 |
| Gestión diaria | 39/día | 26/día | 67%. Afectada por inducción y doble tipificación en dos CRM |
| Leads con interés calificado (MQL) | — | 3 | 1,9% de los contactados |
| Handoffs al cierre | 5–10/sem | 5 | Verificados uno a uno en el CRM |
| Cotizaciones | 2–5/sem | 5 reportadas | **Autoreporte, sin registro trazable** |
| Ventas confirmadas | 0–1/mes | **0** | Los «GANADO» del CRM de esa semana son falsos positivos |

**Avance del Mes 1 con ese corte:** 156 de 565 contactados (28% del hito con la mitad del mes transcurrida), 5 de 8–12 cotizaciones, 0 de 0–1 ventas.

### Advertencias que hay que arrastrar a cualquier análisis

1. **Solo 20 de los 156 contactos gestionados pertenecen al alcance de la Ola 1.** El resto fueron leads internacionales asignados durante la semana. El 80% de cumplimiento es gestión total, no cumplimiento verificable de la Ola 1.
2. **Las cotizaciones son autoreporte.** Hoy no hay registro formal ni trazable de cotización, así que no se pueden auditar ni medir contra el SLA de 24 horas.
3. **Dos «GANADO» del CRM no son ventas:** los produjo una automatización que mueve «Llamada Efectiva → GANADO».
4. **No hay corte semanal de octubre.** Tres métricas del plan (SLA <15 min, cotización <24 h, seguimientos vencidos) no son medibles con los registros actuales.
5. **El SDR aún no está contratado en firme** (tarea `O1-003`, en progreso). La propuesta lo declara recurso crítico, no opcional.

---

## 6. Los datos — qué hay, qué falla y qué no se puede usar

### El CRM

**AriCRM** (`app.aricrm.co`), DB de origen `y6zc6y8JIaricrm`. Tablas relevantes: `customers` (`source_id`, `status_id`, `created_at`), `customer_sources`, `customer_statuses`. Al corte del dump: **58.737 customers**, 15 estados, 20+ fuentes.

Fuentes principales:

| `source_id` | Fuente | Customers | Rol en el contrato |
|---:|---|---:|---|
| 13 | **Meta Ads - EBC** | 1.113 | Foco del contrato |
| 22 | **Google Maps** | 7.232 | Base histórica para el bot de WhatsApp (99,3% sin tocar) |
| 10 | Meta Ads - EBL | 1.244 | Fuera de alcance explícito |
| 1 | Jivo Chat | 24.994 | Ruido (ver abajo) |
| 14 | Feria ESS | 17.848 | Histórico |

### ⚠️ Los tres caveats que invalidan análisis si se ignoran

1. **`GANADO` no significa venta.** 21.479 de los 21.638 registros en `GANADO` vienen de Jivo Chat: la integración marca conversaciones cerradas como ganadas. Cualquier tasa de conversión que lea `status_id = 4` sin filtrar por fuente queda inflada unas 130 veces.
2. **La tabla `quotes` está vacía.** No hay registro estructurado de cotizaciones. Las cifras de cotizaciones del reporte son autoreporte del equipo.
3. **La pauta no estaba entrando leads.** Cero leads nuevos de Meta Ads EBC y EBL en los últimos 30 días del dump (22 ago → 22 sep). O la pauta estuvo pausada, o la integración se rompió. **Pendiente de validar.**

### Estado de las fuentes al 26 de octubre de 2026

| Fuente | Estado | Qué permite |
|---|---|---|
| Dump local MySQL (`ebc-mysql`, DB `ebc_aricrm`, `127.0.0.1:3307`) | Disponible. **Último registro: 22 sep 2026** | Línea base histórica completa. **Cero cobertura de octubre** |
| Conector MCP `ariCRM` (producción) | **Caído, error 503.** El CRM web responde 200: el fallo es del conector, no del servicio | Sería la única fuente con actividad de octubre por fecha |
| Conector MCP `AriChat MQE` | Responde, **pero no es el CRM de EBC** | **No usar para EBC.** Devuelve 147.599 contactos y un pipeline distinto (`Demo`, `Ganado Maquinas`, `Int 1`, `Posventa`); EBC tiene 58.737 contactos y estados que ahí no existen |
| Meta Ads / Google Ads | Por conectar | Costo por lead, pivot geográfico |

**Consecuencia práctica:** hoy no se puede producir un corte semanal de octubre con dato verificado. Para cerrarlo hace falta reconectar el conector de `ariCRM` o generar un dump fresco. Mientras eso no exista, la respuesta correcta a «dame las cifras de la semana» es decir que no hay acceso al dato, no estimarlas.

### Jerarquía de fuentes (de mayor a menor autoridad)

1. Contratos, aprobaciones formales y fuentes operativas del cliente.
2. Exportes reproducibles y bases auditadas.
3. Entrevistas y actas validadas.
4. Informes internos y análisis derivados.
5. Investigación externa vigente y citada.
6. Memoria del LLM o conocimiento no verificado.

---

## 7. Vocabulario y reglas de lectura

Estas distinciones no son estilísticas. Confundirlas produce reportes falsos.

| Regla | Por qué |
|---|---|
| **Origen del lead ≠ segmento del lead** | Son campos independientes. «Meta Ads» es origen; «tablerista» es segmento |
| **Adquisición ≠ retención ≠ expansión** | Son corrientes de crecimiento distintas, no canales ni segmentos. No se suman sin definir la base en riesgo |
| **Un clic, una conversación, una solicitud o un documento no son una venta** | Ni una conversión final. Y una aprobación no es ingreso cobrado |
| **Cotización reportada ≠ cotización registrada** | Hoy en EBC solo existe la primera |
| **Contactado y tipificado son el mismo conteo** | Presentarlos como dos métricas simula el doble de trabajo |
| **Cada cifra lleva fuente, periodo y método** | Sin eso no se publica |
| **Las estimaciones se marcan como estimaciones** | Igual los supuestos y las inferencias |

Las cuatro métricas universales con las que se mira cualquier etapa: **volumen** (cuántos entran), **conversión** (qué porcentaje avanza), **tiempo** (cuánto tarda) y **valor** (ingreso neto o margen, cuando haya fuente confiable).

Método de trabajo de la agencia: `SCAN → CONFIGURE → INSTALL → LAUNCH → MONITOR`.

---

## 8. Personas y roles

| Quién | Rol |
|---|---|
| **Alejandro** | EBC. Contraparte principal, cierre comercial, decisiones de producto y pricing |
| **Maquencie Ramos** | EBC. Cierre comercial. *(En `PROPUESTA.md` aparece escrito «Mackenzie»; la grafía correcta es Maquencie)* |
| **Nicolás** | MySEO. Responsable del contrato y de la operación |
| **SDR** | Por contratar. Junior remoto LATAM, dedicado a calificación y seguimiento sobre la base existente |
| **Consultor comercial** | Figura a la que el SDR agenda las reuniones. **Pendiente: definir quién es** |

El SDR califica y entrega; no vende. **No aprueba precios, descuentos, mínimos de compra, plazos de entrega, disponibilidad ni condiciones de crédito.** Eso lo define EBC.

---

## 9. Lo que todavía no se sabe

Nada de esto se debe rellenar con una suposición. Son preguntas abiertas con el cliente.

### Comerciales

| Pendiente | Por qué importa |
|---|---|
| Quién es el consultor comercial y cuál es su agenda | Todo el guion de llamada y los correos cierran agendando con él |
| Mínimos de compra por línea | Una nota al margen del PDF menciona USD 3.000, sin confirmar. La propuesta habla de entrada desde USD 100 en Relpol y sin mínimos para envío doméstico en EE. UU. Está sin resolver |
| Condiciones de pago y crédito | El SDR recibe la pregunta en casi toda llamada |
| Marcas sobre las que se puede afirmar representación oficial | Hoy no se puede decir «distribuidor oficial» de ninguna marca sin confirmación escrita |
| Tiempos reales de despacho desde Miami | Es el argumento que más pesa frente a la compra local |
| Si hay algo concreto y explicable que decir sobre la zona franca | Si hay ventaja real, es un argumento fuerte; si no, se omite |
| Si existe lista de precios segmentada por línea | Los correos dependen de poder enviar un segmento, no el archivo completo |

### De datos y alcance

| Pendiente | Por qué importa |
|---|---|
| ¿Qué pasó con la pauta entre agosto y septiembre? (0 leads nuevos) | Define si el flujo nuevo de la Ola 2 existe |
| ¿Está EBL dentro del alcance o es otro contrato? | Cambia qué se mide y qué se cobra |
| ¿Cómo se registran las cotizaciones si `quotes` está vacía? | Sin esto no hay KPI auditable del contrato |
| ¿Los 21.479 `GANADO` de Jivo Chat son autocierres de conversación? | Confirmar la hipótesis del falso positivo |
| Meta de ventas en USD/mes | EBC no tiene meta definida. Sin meta no hay forma de evaluar el sistema |

---

## 10. Qué se puede pedir con este contexto, y qué no

**Se puede:** analizar, comparar, resumir, proponer, diseñar secuencias y mensajes, redactar borradores, construir consultas SQL, armar reportes internos, criticar la estrategia vigente.

**Requiere autorización humana explícita** (política del proyecto, no preferencia):

- Publicar o enviar mensajes, campañas, correos o piezas.
- Crear, activar, pausar o modificar campañas y presupuestos de pauta.
- Escribir en el CRM o en cualquier sistema de producción.
- Compartir archivos, datos o enlaces con terceros.
- **Aprobar precios, tasas, beneficios, promesas, descuentos, cupos o disponibilidad.**
- Borrar, sobrescribir o migrar datos.

**Nunca:** leer ni mostrar archivos `.env`, claves, tokens, contraseñas o credenciales. Incluir datos personales en entregables públicos o compartidos. Commitear dumps o exportes al repositorio: viven solo en `tmp/` y `.local/`, que están gitignored.

---

## Anexo — resumen de una página para pegar

```
Eléctricas BC Corp. (EBC) distribuye material eléctrico industrial de automatización
y control —contactores, relés, variadores; marcas ancla Relpol e Invertek— desde
Miami, Florida (zona franca), constituida en EE. UU. desde 2001, con más de 5.000
referencias en inventario para entrega inmediata. Vende a tableristas, integradores,
importadores, distribuidores y almacenes eléctricos de Centroamérica y Sudamérica,
más mercado doméstico en EE. UU. Ticket promedio USD 3.000; ventas ~USD 300K al año.
Despacha desde Miami, así que el prospecto tiene que poder importar: ese es el filtro
comercial principal.

MySEO opera un contrato de 90 días (1 oct → 31 dic 2026) para reactivar el sistema
comercial digital. El diagnóstico es que el problema no es de adquisición sino de
capacidad de gestión: la pauta ya entregó 1.113 leads de Meta Ads, de los cuales 778
(70%) están vivos pero sin gestionar —565 nunca recibieron un solo contacto— con 0
cotizaciones y 0 ventas digitales en el mes previo, más 6.527 contactos históricos de
Google Maps sin tocar. La tesis: primero procesar lo que ya hay, después optimizar lo
que entra. Tres olas: procesar inventario (1–28 oct), calificar adquisición (29 oct
–25 nov), sostener y escalar (26 nov–31 dic). Recurso crítico: un SDR dedicado, aún
sin contratar en firme. Fee de agencia $3.5M COP/mes; pauta ~USD 400/mes.

Último corte verificado (7–14 oct): 156 contactados de un plan de 195, 5 handoffs al
cierre, 5 cotizaciones autoreportadas sin registro trazable, 0 ventas confirmadas.
Solo 20 de los 156 contactos pertenecen al alcance de la Ola 1.

Tres trampas en los datos: (1) el estado GANADO del CRM no significa venta —21.479 de
21.638 vienen de una integración de chat que cierra conversaciones automáticamente;
(2) la tabla de cotizaciones está vacía, así que no hay KPI auditable; (3) el dump
local llega hasta el 22 de septiembre y el conector de producción está caído, por lo
que no existe corte de octubre con dato verificado. Cuando falta el dato, se dice que
falta: no se estima.
```
