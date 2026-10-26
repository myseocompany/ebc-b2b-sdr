# Brief de investigación — Cómo se está ejecutando el rol de SDR con IA

**Fecha:** 20 de octubre de 2026 · **Para:** investigación externa (ChatGPT Deep Research / claude.ai Research)
**Responsable:** Nicolás · **Destino:** `progress/` + decisiones en `DECISIONS.md`

> La investigación externa es nivel 5 en la jerarquía de `SOURCES.md`. Informa decisiones; no manda sobre el CRM ni sobre el contrato.

---

## 1. Pregunta central

**¿Cómo se está ejecutando hoy el rol de SDR —conseguir, contactar y calificar leads— cuando hay IA y agentes de por medio?**

Pregunta abierta y de punta a punta. Incluye la construcción de la base desde cero, no solo la gestión de leads existentes. No se busca validar un plan: se busca entender qué está funcionando, qué se rompió y cómo quedó repartido el trabajo entre personas y agentes.

📌 El filtro de aplicabilidad a EBC va **al final** (sección 8), después de entender el panorama. No antes, o la respuesta se contamina con lo que ya decidimos.

---

## 2. El rol, descompuesto

El SDR tradicional hace siete cosas. La investigación debe responder, para cada una, **quién la hace hoy en las operaciones que funcionan: un humano, un agente, o un humano asistido.**

| # | Etapa | Lo que hay que averiguar |
|---|---|---|
| 1 | **Definir y encontrar el ICP** | ¿Cómo se construyen hoy las listas de cuentas objetivo? ¿Qué reemplazó al scraping manual? ¿Se usan agentes para descubrir ICP a partir de clientes actuales? |
| 2 | **Sourcing de datos de contacto** | ¿De dónde sale la data? ¿Qué proveedores, qué calidad, qué costo, qué cobertura fuera de Norteamérica? ¿Qué pasó con el scraping tras los cambios de LinkedIn y de los buscadores? |
| 3 | **Señales e intención** | ¿Qué señales se están usando para priorizar (contrataciones, rondas, cambios de tecnología, licitaciones, registros de importación, actividad web)? ¿Funciona el *intent data* o es humo caro? |
| 4 | **Contacto y secuencias** | ¿Qué canales y qué cadencias? ¿Qué tanto se personaliza con IA y hasta dónde antes de que el comprador lo note y lo castigue? |
| 5 | **Calificación conversacional** | ¿Agentes conversando y calificando de verdad, o solo enrutando? ¿Qué tan lejos llegan antes de pasar a humano? |
| 6 | **Agendamiento y handoff** | ¿Qué se automatizó del agendamiento y del traspaso al cerrador? ¿Qué se pierde en ese traspaso? |
| 7 | **Medición y mejora** | ¿Cómo se mide hoy un SDR asistido por IA? ¿Qué métricas quedaron obsoletas cuando el volumen de toques dejó de costar trabajo? |

---

## 3. Preguntas transversales

Estas son las que más importan, porque son las que no aparecen en el material de los proveedores.

1. **¿Qué quedó del rol humano?** ¿El SDR desapareció, se volvió orquestador de agentes, o subió a trabajo de cuenta? ¿Qué pasó con los equipos que lo reemplazaron por completo? ¿Hubo reversiones documentadas?
2. **¿Qué se rompió?** El outbound masivo asistido por IA saturó bandejas y canales. ¿Qué efectos medibles hay sobre tasas de respuesta, entregabilidad y reputación de dominio? ¿Los compradores B2B están castigando el mensaje que huele a IA?
3. **¿Qué arquitecturas se repiten?** Patrones de operación concretos: quién dispara qué, dónde entra el humano, cómo se maneja el fallo. Diagramas de flujo reales, no promesas de plataforma.
4. **Economía del rol.** Costo por reunión agendada, por lead calificado y por cuenta trabajada, antes y después de los agentes. ¿Bajó el costo o se multiplicó el volumen de ruido?
5. **Qué tan autónomos son realmente los agentes.** ¿Dónde está la frontera hoy entre un agente que decide y una secuencia bien configurada con lenguaje natural encima?
6. **Equipos pequeños.** ¿Qué están haciendo las operaciones de una o dos personas, no las de 40 SDR? Es el caso más parecido a la mayoría de PYMEs.
7. **Qué dicen los que compran.** Evidencia desde el lado del comprador B2B: qué formas de contacto todavía abren y cuáles ya no.

---

## 4. Corte geográfico: LatAm y español

El stack dominante en EE. UU. es correo más LinkedIn. En LatAm el canal real suele ser WhatsApp y teléfono. Hay que averiguar explícitamente:

- Cómo se ejecuta el rol de SDR con IA **en mercados de habla hispana**, y qué cambia respecto al manual estadounidense.
- **WhatsApp como canal de prospección:** qué está permitido, qué se castiga, límites de la API, ventana de 24 horas, riesgo de bloqueo de número, y qué prácticas sostienen una operación sin quemar la línea.
- **Disponibilidad de datos B2B fuera de Norteamérica:** qué fuentes existen realmente para empresas latinoamericanas. Incluir registros públicos, cámaras de comercio, directorios locales, datos de comercio exterior y registros aduaneros de importación/exportación.
- Calidad real del español latinoamericano en agentes de texto y de voz.
- Marco legal de contacto comercial no solicitado y de grabación de llamadas en Colombia, México, Perú, Chile y Centroamérica.

---

## 5. Corte sectorial: B2B industrial de ticket medio

La mayoría del material publicado es de SaaS vendiendo a SaaS. Hay que distinguir qué aplica cuando:

- El ticket es de miles de dólares, no de decenas de miles.
- El ciclo es de semanas o meses y el comprador es técnico (ingeniero, jefe de compras, tablerista, distribuidor).
- La compra es recurrente y la relación pesa más que la campaña.
- No hay categoría de software que buscar: hay referencias, marcas y disponibilidad.

**Pregunta concreta:** ¿hay casos documentados de distribución industrial, ferretería industrial, manufactura o comercio exterior usando agentes para prospectar y calificar? ¿Qué les funcionó y qué no?

---

## 6. Qué no quiero en el informe

- Listados de proveedores copiados de sus propias páginas.
- Casos de SaaS de alto volumen presentados como universales.
- Cifras sin fuente, sin fecha o sin tamaño de muestra.
- Predicciones más allá de 2026.
- El marco «reemplace a su SDR con IA» dado por sentado. Si la evidencia lo sostiene, que lo muestre; si no, que lo diga.
- Conclusiones que solo se sostengan con presupuesto de empresa grande.

---

## 7. Formato de salida esperado

1. **Mapa del rol:** las siete etapas de la sección 2, con quién las ejecuta hoy en las operaciones que funcionan y con qué nivel de autonomía.
2. **Dos o tres arquitecturas de referencia** descritas de punta a punta, con el punto exacto donde entra el humano. Una de ellas, para un equipo de una o dos personas.
3. **Tabla de herramientas por etapa**, con costo real, cobertura de datos fuera de EE. UU., idioma, integración vía API y propiedad de los datos.
4. **Lo que la evidencia respalda vs. lo que es marketing de proveedor**, separado explícitamente.
5. **Qué se rompió y qué está en disputa**, incluyendo fracasos y reversiones documentadas.
6. **Lo específico de LatAm, español y WhatsApp**, en sección propia.
7. **Fuentes con fecha.** Prioridad a implementaciones documentadas, estudios con metodología visible y documentación técnica oficial. Nada anterior a 2025 salvo que sea fundacional.

---

## 8. Prompt listo para pegar

```
Necesito un informe de investigación sobre cómo se está ejecutando hoy, a
octubre de 2026, el rol de SDR (Sales Development Representative) en B2B
cuando hay IA y agentes de por medio. Me interesa el rol completo: conseguir
los leads, contactarlos y calificarlos. No solo la gestión de bases existentes.

Es una pregunta abierta. No quiero validación de un plan: quiero entender qué
está funcionando de verdad, qué se rompió y cómo quedó repartido el trabajo
entre personas y agentes.

EL ROL, DESCOMPUESTO
Para cada una de estas siete etapas, dime quién la ejecuta hoy en las
operaciones que funcionan —humano, agente, o humano asistido— y con qué nivel
real de autonomía:
1. Definir y encontrar el ICP / construir la lista de cuentas objetivo.
2. Sourcing de datos de contacto: de dónde sale la data, qué calidad, qué
   costo, qué cobertura fuera de Norteamérica, y qué pasó con el scraping.
3. Señales de intención y priorización: contrataciones, licitaciones, cambios
   tecnológicos, registros de importación, actividad web. ¿Funciona el intent
   data o es humo caro?
4. Contacto y secuencias: canales, cadencias, y hasta dónde llega la
   personalización con IA antes de que el comprador la note y la castigue.
5. Calificación conversacional: ¿los agentes califican de verdad o solo
   enrutan? ¿Hasta dónde llegan antes de pasar a humano?
6. Agendamiento y handoff al cerrador: qué se automatizó y qué se pierde ahí.
7. Medición: cómo se mide un SDR asistido por IA, y qué métricas quedaron
   obsoletas cuando generar volumen dejó de costar trabajo.

PREGUNTAS TRANSVERSALES (las más importantes)
- ¿Qué quedó del rol humano? ¿Desapareció, se volvió orquestador de agentes, o
  subió a trabajo de cuenta? ¿Hay reversiones documentadas de equipos que lo
  automatizaron por completo y volvieron atrás?
- ¿Qué se rompió? Efectos medibles del outbound masivo con IA sobre tasas de
  respuesta, entregabilidad y reputación. ¿Los compradores B2B están
  castigando el mensaje que huele a IA?
- ¿Qué arquitecturas de operación se repiten? Descríbelas de punta a punta:
  quién dispara qué, dónde entra el humano, cómo se maneja el fallo.
- Economía: costo por reunión agendada y por lead calificado, antes y después
  de los agentes. ¿Bajó el costo o solo se multiplicó el ruido?
- ¿Qué están haciendo los equipos de una o dos personas, no los de 40 SDR?
- Evidencia desde el lado del comprador: qué formas de contacto todavía abren.

LATAM Y ESPAÑOL (sección propia)
El stack dominante en EE. UU. es correo más LinkedIn. En Latinoamérica el canal
real suele ser WhatsApp y teléfono. Investiga:
- Cómo se ejecuta el rol en mercados hispanohablantes y qué cambia.
- WhatsApp como canal de prospección: qué permite la API, límites, ventana de
  24 horas, riesgo de bloqueo de número, prácticas que sostienen la operación.
- Qué fuentes de datos B2B existen realmente para empresas latinoamericanas:
  registros públicos, cámaras de comercio, directorios, datos de comercio
  exterior y registros aduaneros de importación.
- Calidad real del español latinoamericano en agentes de texto y de voz.
- Marco legal de contacto comercial no solicitado y grabación de llamadas en
  Colombia, México, Perú, Chile y Centroamérica.

B2B INDUSTRIAL DE TICKET MEDIO (sección propia)
La mayoría del material publicado es de SaaS vendiendo a SaaS. Distingue qué
aplica cuando el ticket es de miles de dólares (no decenas de miles), el ciclo
es de semanas o meses, el comprador es técnico (ingeniero, jefe de compras,
distribuidor) y la compra es recurrente. ¿Hay casos documentados en
distribución industrial, manufactura, ferretería industrial o comercio
exterior? ¿Qué les funcionó y qué no?

PARA CADA HERRAMIENTA QUE MENCIONES
Costo mensual real, cobertura de datos fuera de EE. UU., soporte efectivo de
español latinoamericano, integración vía API o webhook con un CRM propio,
propiedad de los datos, esfuerzo de implementación en días-persona, y modo de
fallo con escalamiento a humano.

NO INCLUYAS
- Listados de proveedores copiados de sus propias páginas.
- Casos de SaaS de alto volumen presentados como universales.
- Cifras sin fuente, sin fecha o sin tamaño de muestra.
- Predicciones más allá de 2026.
- El marco "reemplace a su SDR con IA" dado por sentado: si la evidencia lo
  sostiene, muéstrala; si no, dilo.

FORMATO
1) Mapa del rol: las siete etapas con quién las ejecuta y con qué autonomía.
2) Dos o tres arquitecturas de referencia de punta a punta, con el punto exacto
   donde entra el humano. Una de ellas para un equipo de una o dos personas.
3) Tabla de herramientas por etapa con los criterios de arriba.
4) Separación explícita entre evidencia y marketing de proveedor.
5) Qué se rompió y qué está en disputa, con fracasos y reversiones.
6) Sección propia de LatAm, español y WhatsApp.
7) Fuentes con fecha. Prioriza implementaciones documentadas, estudios con
   metodología visible y documentación técnica oficial. Nada anterior a 2025
   salvo que sea fundacional.
```

---

## 9. Filtro de realidad — se aplica después, no antes

Cuando vuelva el informe, se contrasta contra la operación de EBC. **Este filtro no debe ir en el prompt**: si se incluye, el informe deja de ser un panorama y se vuelve una justificación de lo que ya está decidido.

| Restricción real | Para qué sirve el filtro |
|---|---|
| Presupuesto total de la operación digital en cientos de dólares al mes | Descarta stacks de USD 2.000+/mes por mucho que la evidencia los respalde |
| Un SDR humano por prestación de servicios, más dos cerradores | Define cuánta orquestación es sostenible |
| Mercado: Centroamérica y Sudamérica. Canal real: WhatsApp y teléfono | Invalida casi todo el manual de correo más LinkedIn |
| Comprador técnico: tableristas, integradores, distribuidores, importadores | Filtra los casos de SaaS |
| Ticket promedio USD 3.000, ciclo ~2 meses | Define qué costo por reunión es tolerable |
| CRM propio con API | Determina qué integra y qué no |

### Qué pasa después

1. El informe original se guarda en `tmp/` sin editar, como fuente.
2. Se separa en hechos verificables, inferencias y propuestas, según `POLICIES.md`.
3. Se contrasta contra el contrato vigente: qué confirma, qué contradice y qué abre como opción que no estaba sobre la mesa.
4. **Si contradice la estrategia actual, eso es el hallazgo valioso**, no un problema a resolver escribiendo alrededor.
5. Lo que cambie el plan entra como fila en `DECISIONS.md`. Lo que sobreviva, como tarea con criterio de terminado en `TASKS.md`.

📌 Conviene correrlo en los dos motores (ChatGPT y claude.ai) y comparar. Cubren fuentes distintas, y lo que coincida en ambos informes es lo más confiable que va a salir del ejercicio.
