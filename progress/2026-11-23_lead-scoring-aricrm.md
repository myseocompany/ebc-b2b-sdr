# Lead scoring de EBC en AriCRM — configuración y extracción de criterios

**Fecha:** 23 de noviembre de 2026. **Sistema:** AriCRM `app.aricrm.co`, tenant EBC (`019d0099-a43a-703d-b1d0-264d667dc148`, slug `ebcorp`). **Método:** lecturas por `ssh waterfall`; escrituras por `php artisan tinker` descritas abajo.

Este documento no contiene datos personales (el repo es público). Los archivos con nombres, teléfonos y citas textuales están en `tmp/lead-scoring-2026-11-23/`, ignorado por git.

## 1. Qué quedó en producción

### 1.1 Perfil (grado A–D), activo

Configuración creada en `lead_scoring_configs` y recalculada sobre los 10.579 contactos. Se recalcula cada hora. No hay automatizaciones de "cambio de lead score" en el tenant, así que no dispara mensajes.

| Propiedad | Peso | Fuente | Notas |
|---|---:|---|---|
| Calificación humana | 45 | Etiquetas | "Calificado · mes 2" e "Interés calificado" 10 · Propuesta / Negociación / Cierre 9 · Ganado / Asistirá 8 · Seguimiento / Nueva conversión 6 · Nuevo / Intento de contacto 4 · No contesta 3 · Perdido 2 · Sin interés / Mal calificado / Datos incorrectos 1 |
| País | 20 | País del teléfono | US 10 · PR 9 · PA, PE, CL, EC 8 · BO, NI, AR, GT, CR, DO, JM 7 · MX, UY, PY 6 · CO 4 · ES 3 |
| Origen | 20 | Etiquetas | LP Variadores, LP Importador Eléctrico 10 · GetResponse Invertek, Meta Ads Relpol 9 · Meta Ads EBC, Multimarca, Google Ads 8 · LP Teltonika 7 · Feria ESS 6 · Meta Ads EBL, Meta Ads, Import Facebook 5 · Base Google Maps 4 |
| Tipo de negocio | 15 | `gmb_category` (contiene) | Tableros, automatización, tienda o suministro eléctrico, motores 10 · suministros industriales, importadores 9 · instalación e ingeniería eléctrica, solar 7 · maquinaria, HVAC, bombas 6 · electricista, ferretería 4 |

Resultado del primer recálculo:

| Grado | Contactos |
|---|---:|
| A | 40 |
| B | 440 |
| C | 5.013 |
| D | 5.086 |

La tabla y la distribución de arriba son la versión inicial, de cuatro propiedades; la sección 3 trae las dos que se agregaron después y la distribución vigente.

Limitación del motor: una propiedad sin coincidencia vale 0 y no existe nota negativa. Un contacto frío de Google Maps llega como máximo a C, y un descarte no puede bajar el grado.

### 1.2 Interés (temperatura), sin configurar

Las bandas Frío 0 / Templado 25 / Caliente 50 existen, pero no hay grupos de actividad: todos los contactos aparecen en Frío. Propuesta pendiente de aprobación: leyó campaña +5, respondió campaña +15, escribió por WhatsApp +10, negocio creado +20, negocio calificado +20, cita agendada o asistida +25, propuesta / negociación / ganado +40, envío fallido −10, negocio perdido −15, baja −50.

### 1.3 Intents de IA, creados e inactivos

Seis intents en modo "Declara un dato": `ya_importa`, `nunca_ha_importado`, `tiene_agente_carga`, `implementa_proyectos`, `comercializa`, `usuario_final_planta`.

No detectan nada todavía. Para que funcionen hay que encender el flag `intent_classifier_enabled` del tenant (panel de superadmin) y activar los intents. EBC sería el primer tenant en usar el clasificador en producción. Los intents activos entran al prompt del agente de IA, así que conviene pasar `/test_agent` antes.

Prueba de solo lectura sobre 65 conversaciones reales: 4 detecciones, sin falsos positivos por el texto del anuncio ni por el botón "Importar". El clasificador solo ve los mensajes del cliente, no la pregunta del asesor, así que rinde poco mientras el agente no pregunte los criterios.

### 1.4 Campos de calificación escritos en los contactos

Escritos en `contacts.custom_fields` de 358 contactos, conservando sus campos previos. Solo datos con confianza media o alta.

| Campo | Valores | Contactos |
|---|---|---:|
| `ha_importado` | `si`, `tercero`, `dispuesto`, `no` | 72 |
| `agente_carga` | `si`, `no` | 20 |
| `uso` | `proyecto`, `comercializa`, `ambos`, `planta` | 89 (11 `ambos`) |
| `horizonte_compra` | `0-2m`, `2-6m` | 36 |
| `decide` | `si`, `no` | 60 |
| `producto_interes` | texto corto | 154 |
| `motivo_descarte` | texto corto | 170 |
| `calificacion_lote` | `expedientes_2026_11_23` | 358 |

Para revertir: quitar esas ocho claves a los contactos con `calificacion_lote = expedientes_2026_11_23`, o restaurar desde `tmp/lead-scoring-2026-11-23/backup_custom_fields_previos.json`.

## 2. Cómo se extrajeron los criterios

Fuente: los tres criterios del guion de llamada v6 (¿ha importado?, ¿tiene agente de carga?, ¿implementa proyectos o comercializa?) más horizonte de compra, participación en la decisión, producto y motivo de descarte.

Se armó un expediente por contacto con el texto disponible en AriCRM y seis agentes los leyeron completos, marcando solo lo dicho explícitamente y guardando la cita textual de cada dato.

| Fuente | Contactos con texto |
|---|---:|
| Diálogo de WhatsApp (cliente y asesor) | 405 |
| Llamadas transcritas (Channels) | 303 |
| Notas de negocio | 271 |
| Tareas con texto | 180 |
| Notas del contacto | 16 |
| **Total de expedientes** | **775** |

Resultado sobre los 775: 132 contactos con al menos uno de los tres criterios, 52 con dos o más, 13 con los tres. 177 descartados. Algo más de la mitad de los expedientes no tenía nada que extraer (buzón, nadie contesta, transcripción ininteligible, solo la tarea de plantilla).

Quedó por fuera: las 595 llamadas de Retell (sin transcripción en `contact_activities`), unas 1.700 llamadas de Channels sin transcribir y el CRM legacy `eb.aricrm.co`.

Hallazgos de la lectura:

- El agente de carga casi nunca queda registrado: la asesora lo afirma ella misma ("ya cuentan con agencia, ¿cierto?") y la respuesta no se transcribe. El bot además lo pregunta junto con la experiencia importando, en un solo mensaje.
- El horizonte de compra casi no aparece, y buena parte de los valores sale de pedidos en curso, no de una respuesta a la pregunta.
- Muchos clientes comercializan y además implementan proyectos; por eso se agregó el valor `ambos`.
- Mantenimiento de equipos de terceros no encaja en `uso` y quedó vacío.
- Clientes activos que ya importan con EBC quedaron sin `ha_importado` cuando nadie lo dice textualmente.
- Motivos de descarte dominantes: gente ajena al rubro que llegó por el anuncio, números equivocados, y pedidos de una o pocas unidades cerrados por el mínimo de importación.

## 3. Criterios del guion agregados al perfil

Se agregaron `ha_importado` y `uso` como propiedades nuevas del perfil (decisión del 23-nov, después de ver la simulación). Las cuatro propiedades anteriores conservan sus pesos; el total pasa de 100 a 120.

| Propiedad | Peso | Fuente | Notas |
|---|---:|---|---|
| Experiencia importando | 10 | `ha_importado` (exacto) | `si` 10 · `tercero` 7 · `dispuesto` 5 · `no` 1 |
| Uso del material | 10 | `uso` (exacto) | `proyecto`, `comercializa`, `ambos` 10 · `planta` 6 |

Resultado del recálculo, igual al de la simulación previa:

| Grado | Antes | Ahora |
|---|---:|---:|
| A | 40 | 21 |
| B | 440 | 77 |
| C | 5.013 | 4.096 |
| D | 5.086 | 6.387 |

Cambiaron de grado 1.732 contactos; quedaron en el historial como corrida silenciosa, sin despachos. La lista de A y B baja de 480 a 98 porque el peso total crece y una propiedad vacía vale 0: quien no tiene el dato pierde puntaje. A cambio, de los 25 contactos que ya importan y son proyecto o comercializan, 16 quedan en A (antes 9).

La alternativa descartada era llevar los criterios a etiquetas dentro de "Calificación humana", que no movía a nadie más.

`agente_carga` y `horizonte_compra` no se usan para puntuar: tienen 20 y 36 datos.

Para revertir: restaurar `fit_properties` desde `tmp/lead-scoring-2026-11-23/fit_properties_antes_opcion_b.json`.

### 3.1 Descalificación (activa desde el 26-nov)

Para que un descarte baje el grado se agregó al motor de AriCRM una lista de reglas de descalificación (`fit_disqualifiers`, PR aricrm#306, fusionado y desplegado el 26-nov): si el contacto cumple una, su perfil queda en 0 y grado D, y el desglose guarda qué regla aplicó.

EBC tiene una regla, "Descartado": el campo `motivo_descarte` tiene cualquier valor. Resultado del recálculo del 26-nov:

| Grado | Antes de la regla | Con la regla |
|---|---:|---:|
| A | 21 | 21 |
| B | 77 | 73 |
| C | 4.096 | 3.975 |
| D | 6.456 | 6.581 |

Los 170 contactos con `motivo_descarte` quedaron en D (125 cambiaron de grado; 45 ya estaban ahí). Corrida silenciosa, sin despachos. Para revertir: quitar la regla en Ajustes → Lead scoring → Descalificación; el siguiente recálculo restaura los grados.

Para descartar un contacto nuevo basta con escribir `motivo_descarte` en sus campos adicionales.

Seguimiento anotado en el motor, sin implementar: que una propiedad vacía no cuente en la normalización de pesos.

## 4. AriPulse como reporte

No sirve como reporte del lead scoring. Mide conversaciones y negocios desatendidos, no contactos, y su contrato con AriCRM no lee grado, temperatura, etiquetas ni campos del contacto.

Lo más barato es la pestaña Resultados del lead scoring (Ajustes → IA y automatización → Lead scoring), que ya trae la matriz grado × temperatura y los contactos por celda. Le faltan una vista combinada de A y B calientes, el motivo del grado por fila y filtro de fecha en las transiciones. Es solo para rol admin.

## 5. Archivos locales (no versionados)

En `tmp/lead-scoring-2026-11-23/`:

- `consolidado.json` — los 775 resultados con cita textual y confianza.
- `expedientes_fuente.jsonl` — el texto de origen por contacto.
- `backup_custom_fields_previos.json` — `custom_fields` de los 358 contactos antes de la escritura.
- `export_expedientes.php` — consulta con la que se armaron los expedientes.
- `instalar_perfil.php` — script con el que se creó la configuración del perfil.
- `fit_properties_antes_opcion_b.json` — propiedades del perfil antes de agregar `ha_importado` y `uso`.
