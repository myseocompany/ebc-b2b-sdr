# Revenue Architecture — Marco de trabajo para AMIA

## Uso y fuentes

Este es el resumen accionable que se debe consultar primero al diseñar una estrategia de crecimiento para AMIA.

- **Fuente primaria:** `revenue-architecture-framework.pdf` (edición completa de *Revenue Architecture*, Jacco van der Kooij).
- **Fuente textual para búsqueda y verificación:** `revenue-architecture-framework-source.txt`.
- **Material complementario anterior:** `revenue_architecture.pdf`.

Si una decisión no queda claramente resuelta aquí, se debe consultar el texto fuente antes de inferir una regla. Este documento adapta conceptos de negocios recurrentes a una clínica; no convierte métricas SaaS como ARR, GRR o NRR en equivalentes clínicos sin definirlas.

## Regla central

No llamar “palancas” indistintamente a los modelos, etapas o métricas. Antes de proponer una iniciativa, identificar con precisión si actúa sobre **adquisición**, **retención** o **expansión**.

## Los tres componentes de crecimiento

El libro separa el crecimiento de ingresos en tres corrientes:

1. **Adquisición:** ingreso de pacientes nuevos.
2. **Retención:** ingreso de pacientes existentes que se mantiene; evita contracción o abandono.
3. **Expansión:** ingreso adicional de pacientes existentes mediante continuidad, cross-sell o upsell.

Para AMIA, en una lectura mensual:

`Facturación neta del período = facturación base + adquisición + expansión − contracción − abandono − notas crédito`

Si se mide solamente el **crecimiento incremental frente a una línea base**, la parte a explicar es:

`Crecimiento neto = adquisición + expansión − contracción − abandono − notas crédito incrementales`

La retención es una condición para sostener la base. No debe sumarse como “ingreso incremental” a una meta de crecimiento sin aclarar primero cuál era el ingreso de base en riesgo.

## Jerarquía correcta de conceptos

| Concepto | Qué es | Uso en AMIA |
|---|---|---|
| 3 componentes de crecimiento | Adquisición, retención y expansión | Clasificar el origen de cada peso de ingreso. |
| Bowtie | Recorrido: awareness → education → priorización → compromiso mutuo → onboarding → retención → expansión | Medir el recorrido completo de paciente. |
| 6 modelos esenciales | Revenue, datos, matemático, operativo, crecimiento y GTM | Diseñar el sistema, no etiquetar una campaña. |
| Métricas | Volumen (VM), conversión (CR) y tiempo (Δt) | Encontrar la restricción y comprobar el impacto. |

## Foco ejecutivo y mejoras simultáneas

El libro no prescribe un número universal de “palancas” o métricas que puedan trabajarse simultáneamente. El ejercicio 7.7 pide escoger las **tres métricas prioritarias** de la tesis de escalabilidad para orientar la atención ejecutiva. En paralelo, el capítulo 10 recomienda mejoras marginales coordinadas en múltiples puntos del customer journey; su ejemplo interviene CR1, CR2, CR3, CR4, CR5, CR7 y CR8 al mismo tiempo.

- Un cambio en una métrica de conversión exige seguimiento riguroso.
- Dos cambios simultáneos multiplican su efecto y requieren vigilancia reforzada.
- Tres cambios simultáneos constituyen un escenario de **"all hands on deck"**: es una advertencia de control y causalidad, no un límite de intervención.

No confundir estas tres métricas con:

- los **tres componentes de crecimiento** (adquisición, retención y expansión), que sirven para clasificar el ingreso;
- las **etapas del Bowtie**, que sirven para localizar dónde ocurre la fricción;
- los **tres procesos concurrentes de expansión** que describe el libro para SaaS (adopción, penetración de cuenta y crecimiento de cuenta). Estos últimos no son tres campañas ni se trasladan literalmente a una clínica.

Para AMIA, mientras se construye la Growth Formula, las tres métricas provisionales de foco ejecutivo son:

1. **Contacto de alta intención → cita asistida.** Mide si WhatsApp, agenda y confirmación convierten la demanda ya generada en atención real.
2. **Valoración asistida → tratamiento/ruta iniciada.** Mide la calidad de la recomendación, la claridad de la ruta y el cierre ético de una indicación clínica.
3. **Tratamiento iniciado → siguiente sesión o control cumplido.** Mide continuidad y protege la retención.

Estas tres métricas no limitan las intervenciones. Procesos, automatización, habilidades, oferta y capacidad pueden mejorarse simultáneamente siempre que cada cambio tenga hipótesis, dueño y medición. El volumen de contactos solo se aumenta si el throughput y la capacidad clínica se sostienen.

## Growth Formula aplicada a AMIA

La estrategia debe modelarse antes de asignar cuotas entre adquisición y expansión:

`Ingreso nuevo = contactos nuevos válidos × CR contacto→cita × CR cita→asistencia × CR asistencia→inicio × ticket neto inicial`

`Ingreso de expansión = pacientes existentes elegibles × CR contacto→valoración × CR valoración→inicio × ticket neto incremental`

`Crecimiento neto = ingreso nuevo + ingreso de expansión − contracción − abandono − notas crédito incrementales`

La meta se considera alcanzada solo cuando el crecimiento neto es igual o superior al objetivo. Mejorar únicamente el input —más contactos— puede deteriorar la calidad y las conversiones posteriores; por eso se deben simular cambios marginales en varias métricas y comprobar la capacidad del sistema.

El libro propone tres mecanismos transversales para mejorar throughput:

1. Simplificar procesos y eliminar pasos innecesarios.
2. Automatizar sistemas con tecnología.
3. Mejorar habilidades mediante entrenamiento y coaching.

## Aplicación prioritaria en AMIA

La evidencia disponible muestra demanda y respuestas sin cierre; por eso, el orden de trabajo no es aumentar volumen primero.

1. **Retención:** recuperar conversaciones, inasistencias, controles y tratamientos interrumpidos. Cada caso debe tener dueño, siguiente paso y desenlace.
2. **Expansión:** crear rutas de paciente para servicios de baja ocupación —estimulación magnética funcional, radiofrecuencia y depilación láser— solo cuando la valoración y el criterio clínico los indiquen.
3. **Adquisición:** captar demanda de alta intención por problema/servicio y escalar Ads o contenido solo cuando la cadena hasta cita asistida e ingreso funcione.

No usar una recomendación clínica como mecanismo de venta. El papel comercial es facilitar una decisión informada, precio claro, agenda y continuidad del tratamiento indicado.

## Cómo estructurar una meta de ingresos

Para una meta de crecimiento, reportar por separado:

| Corriente | Pregunta obligatoria | Métrica de resultado |
|---|---|---|
| Adquisición | ¿Cuántas pacientes nuevas asistidas y con qué ingreso inicial se requieren? | Ingreso nuevo por cohorte/origen. |
| Retención | ¿Cuánto ingreso de la base se preserva frente a la línea base? | Abandono, contracción y controles recuperados. |
| Expansión | ¿Qué pacientes existentes son elegibles y qué valor adicional aceptan? | Ingreso incremental por paciente/cohorte. |

Una cifra como “$40M más” debe descomponerse en adquisición y expansión netas. La retención se informa además como ingreso protegido, sin duplicarla dentro del incremento.

## Datos mínimos antes de escalar

- Al menos ocho períodos comparables de ingresos, clasificados por paciente/cohorte y por las tres corrientes.
- Servicio, ingreso neto, descuento y margen cuando esté disponible.
- Origen de la paciente o campaña.
- Estados del Bowtie: contacto, cita ofrecida, cita agendada, asistencia, tratamiento iniciado, continuidad y expansión.
- Tiempos entre contacto, cita, asistencia e inicio.

## Criterios de decisión

- No escalar adquisición si la atención, la agenda o el seguimiento son la restricción.
- No atribuir una respuesta, lectura o envío a ingreso: la atribución debe llegar a cita asistida e ingreso cobrado.
- Evaluar una campaña por su corriente de crecimiento y por su costo, no solo por volumen de contactos.
- Cuando se proponga una acción, documentar: componente, hipótesis, cohorte, métrica base, meta, capacidad operativa, propietario y fecha de revisión.
- Mantener tres métricas como foco ejecutivo, sin convertirlas en un límite artificial para las mejoras coordinadas del sistema.
- Simular el efecto conjunto de los cambios con la Growth Formula; no sumar impactos aislados como si fueran independientes.

## Referencias dentro del libro completo

- Capítulo 2: adquisición, retención y expansión como los tres componentes de crecimiento.
- Capítulo 4: Bowtie y sus etapas.
- Capítulo 7: adquisición como sistema multiplicativo; retención y expansión como sistema acumulativo en el tiempo; fórmulas GRR/NRR y análisis de escenarios.
- Capítulo 7, ejercicio 7.7: definir las tres métricas prioritarias de la tesis de escalabilidad.
- Capítulo 10, pp. 420–423: ejemplo de mejora simultánea de siete métricas, efecto compuesto, mejora de throughput y necesidad de vigilar cambios en una, dos o tres métricas.
