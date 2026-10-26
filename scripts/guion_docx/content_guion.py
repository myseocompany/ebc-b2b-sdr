#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contenido del Guion de llamada SDR — Eléctricas BC Corp. v2.0"""

import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_guion import *  # noqa
import gen_guion as G

W = G.WIDTH

# =============================================================== PORTADA
banner("GUION DE LLAMADA SDR",
       "Material eléctrico industrial · Automatización y control",
       "Eléctricas BC Corp.  —  Miami, FL (Zona Franca)",
       "Versión 2.0  ·  14 de octubre de 2026  ·  Uso interno SDR",
       md_title=False)

G.md.append("")
rich([("Reemplaza a: ", {"bold": True, "color": G.NAVY, "size": 21}),
      ("Guion de ventas SPIN — Variadores de frecuencia Invertek (v1.0, Eléctricas Bogotá Ltda.)",
       {"size": 21, "italic": True})])
rich([("Fuentes: ", {"bold": True, "color": G.NAVY, "size": 21}),
      ("«Script Comercial con Ajustes Luis Niño» (lineamientos de llamada EBC) · «spin_ebc.md» "
       "(estructura SPIN) · PROPUESTA.md (ICP, olas, SLA)", {"size": 21})])

# =============================================================== 1. CÓMO USAR
h1("Cómo usar este guion")

para("Este documento es la guía de conversación del SDR de Eléctricas BC Corp. (EBC). Unifica dos "
     "cosas que antes estaban separadas: los lineamientos de llamada aprobados por EBC y la "
     "estructura de calificación SPIN.")

para("La diferencia central frente a la versión anterior es que aquí se separan dos tipos de "
     "llamada que no se pueden hacer igual: la llamada a alguien que dejó sus datos por pauta y "
     "la llamada en frío a alguien que nunca nos ha oído nombrar.")

h2("Qué cambió frente a la v1.0")

table([
    ["Dimensión", "v1.0 — Guion SPIN Invertek", "v2.0 — Guion de llamada EBC"],
    ["Empresa que habla",
     "Eléctricas Bogotá Ltda., con stock en Bogotá.",
     "Eléctricas BC Corp., constituida en Miami (EE. UU.) desde 2001, +5.000 referencias "
     "disponibles para entrega inmediata."],
    ["Producto del que se habla",
     "Variadores de frecuencia Invertek, como producto único.",
     "Material eléctrico industrial de automatización y control: contactores, relés "
     "bimetálicos, variadores y el resto del portafolio. Anclas: Relpol y Invertek."],
    ["Tipos de llamada",
     "Uno solo: lead de Meta Ads.",
     "Dos vías separadas: Vía A (dejó sus datos por pauta) y Vía B (contacto en frío)."],
    ["Cierre de la llamada",
     "Propuesta con precio enviada el mismo día.",
     "Reunión virtual con el consultor comercial. La cotización la arma el cierre, no el SDR."],
    ["Calificación",
     "Dolor técnico del producto.",
     "Dolor técnico + los tres criterios de importación de EBC (importa, agencia de carga, rol)."],
    ["Tratamiento", "Mezcla de tú y vos.", "Usted, en todo el guion."],
], [1700, 3700, 3960])

pin("Lo que aparece en cursiva con barra azul se dice casi literal: es la redacción aprobada o la "
    "formulación que mejor funciona. El resto del documento es criterio, no libreto. Un guion leído "
    "se oye leído.")

box(["Antes de marcar, el SDR debe saber tres cosas: por qué vía va la llamada "
     "(A o B), de dónde salió el contacto, y qué resultado cuenta como éxito en esa vía.",
     "El objetivo del SDR nunca es vender. Es calificar y entregar la conversación al cierre "
     "comercial con información útil registrada en el CRM.",
     "El SDR no aprueba precios, descuentos, mínimos de compra, plazos de entrega, "
     "disponibilidad ni condiciones de crédito. Eso lo define EBC."],
    title="Regla de oro", color=G.NAVY)

# =============================================================== 2. LAS DOS VÍAS
pagebreak()
h1("Las dos vías de llamada")

para("La misma persona, el mismo portafolio y el mismo SPIN, pero dos conversaciones distintas. "
     "Lo que cambia es el permiso con el que se abre la llamada.")

table([
    ["", "VÍA A — Dejó sus datos por pauta", "VÍA B — Contacto en frío"],
    [{"text": "De dónde sale el contacto", "bold": True, "color": G.NAVY},
     "Formulario de Meta Ads o Google Ads. En el CRM: estados Nuevo, Seguimiento, "
     "Intento de contacto, No contesta.",
     "Base histórica de Google Maps (6.527 contactos), listados de directorio, referidos, "
     "respondedores del bot de WhatsApp."],
    [{"text": "Qué sabe de EBC", "bold": True, "color": G.NAVY},
     "Vio un anuncio y pidió información. Puede haber pasado meses: es probable que no lo "
     "recuerde.",
     "Nada. No conoce la empresa, no pidió la llamada y no esperaba el contacto."],
    [{"text": "Permiso para hablar", "bold": True, "color": G.NAVY},
     "Existe, pero está vencido. Se reactiva recordándole que él dejó sus datos.",
     "No existe. Hay que pedirlo de forma explícita en los primeros 15 segundos."],
    [{"text": "Objetivo de la llamada", "bold": True, "color": G.NAVY},
     "Confirmar si sigue comprando material, calificar con los tres criterios y agendar "
     "reunión con el consultor comercial.",
     "Ganar permiso, confirmar que compra material de automatización y conseguir una "
     "segunda conversación con fecha."],
    [{"text": "Duración objetivo", "bold": True, "color": G.NAVY},
     "4 a 7 minutos.",
     "60 a 120 segundos. Si se extiende porque el prospecto quiere, mejor."],
    [{"text": "Profundidad SPIN", "bold": True, "color": G.NAVY},
     "S + P + I + N completo cuando hay apertura.",
     "S y una sola P. La I y la N quedan para la segunda llamada."],
    [{"text": "Qué cuenta como éxito", "bold": True, "color": G.NAVY},
     "Reunión agendada con fecha y hora, o lista de material solicitada con fecha de "
     "seguimiento.",
     "Permiso + dos datos (qué compra, si importa) + próxima acción con fecha."],
    [{"text": "Error típico", "bold": True, "color": G.NAVY},
     "Hablar de catálogo y precios antes de confirmar que sigue comprando.",
     "Soltar un discurso de dos minutos sin haber pedido permiso."],
], [1500, 3930, 3930])

pin("Si el SDR no sabe por qué vía va la llamada, la llamada no está lista. En el CRM esto se "
    "resuelve filtrando por origen del lead antes de empezar la jornada: origen del lead y "
    "segmento del lead son cosas distintas.")

# =============================================================== 3. FILTRO
h1("Filtro transversal — los tres criterios de EBC")

para("EBC despacha desde Miami. Eso significa que cualquier prospecto, por interesado que esté, "
     "tiene que poder recibir carga desde Estados Unidos. Estos tres criterios aplican en las dos "
     "vías y son los que deciden si el contacto avanza o no.")

table([
    ["#", "Pregunta de calificación", "Qué está midiendo", "Señal de descarte"],
    ["1", "«¿Ya ha realizado importaciones desde otro país?»",
     "Fricción logística y aduanera. Quien ya importó sabe de tiempos, nacionalización y pagos "
     "internacionales.",
     "Nunca ha importado y no está dispuesto a hacerlo."],
    ["2", "«¿Cuenta ya con una agencia de transporte o un agente de carga?»",
     "Quién mueve la carga. Si ya tiene agencia, el proceso es inmediato.",
     "No tiene agencia y no quiere contratar ni evaluar una."],
    ["3", "«¿Usted implementa proyectos o comercializa material?»",
     "Define el perfil y por lo tanto el SPIN que se usa a continuación.",
     "Ni implementa ni comercializa: compra suelta de consumo final."],
], [500, 2900, 3600, 2360])

pin("Estas tres preguntas no son un interrogatorio. Se intercalan en la conversación, nunca "
    "seguidas. La fórmula que funciona es confirmar interés → preguntar producto → colar el "
    "criterio de importación como consecuencia natural.")

h2("Semáforo de calificación y entrega al cierre")

table([
    ["Nivel", "Qué tiene que cumplirse", "Qué hace el SDR", "SLA"],
    [{"text": "A — Caliente", "bold": True, "color": G.GREEN},
     "Producto o referencia concreta + necesidad en 2 meses o menos + es quien decide + puede "
     "importar.",
     "Entrega inmediata al consultor comercial. Reunión agendada en la misma llamada.",
     "Mismo día"],
    [{"text": "B — Tibio", "bold": True, "color": G.AMBER},
     "Compra este tipo de material, hay interés real, horizonte de 2 a 6 meses o falta confirmar "
     "logística.",
     "Entrega al consultor con contexto escrito. Reunión propuesta con dos opciones de horario.",
     "24 horas"],
    [{"text": "C — Frío", "bold": True, "color": G.GRAY},
     "Interés general, sin proyecto, sin referencia y sin fecha.",
     "Queda en seguimiento. Se envía material de referencia y se re-contacta.",
     "15 días"],
    [{"text": "D — Descarta", "bold": True, "color": "9a3412"},
     "No compra este material, o no puede ni quiere importar, o los datos están errados.",
     "Se tipifica el motivo en el CRM y se cierra. No se insiste.",
     "—"],
], [1400, 3300, 3360, 1300])

pin("Tres intentos de contacto sin respuesta y el lead pasa a «No contesta». No se insiste un "
    "cuarto día sobre el mismo número sin cambiar de canal.")

# =============================================================== 4. VÍA A
pagebreak()
section_banner("VÍA A", "Lead que dejó sus datos por pauta",
               "Reactivación de leads de Meta Ads y Google Ads. El prospecto levantó la mano "
               "alguna vez, pero puede haber pasado mucho tiempo. No hay que convencerlo de que "
               "el material existe: hay que confirmar si todavía compra y calificar.",
               G.BLUE, G.BLUEBG)

h2("A.1  Verificación de identidad", G.BLUE)
quote("«Buen día, ¿hablo con [Nombre del prospecto]?»")
pin("Si contesta otra persona: «¿Me podría comunicar con [Nombre], por favor? Le llamo de "
    "Eléctricas BC Corp., él dejó sus datos con nosotros.» Nunca dejar el motivo completo con un "
    "tercero.")

h2("A.2  Presentación y motivo de la llamada", G.BLUE)
quote("«[Nombre], mucho gusto. Le habla [Nombre del SDR], de Eléctricas BC Corp. en Miami.»")
quote("«Le llamo porque hace un tiempo, aproximadamente hace unos meses, dejó sus datos a través "
      "de una de nuestras campañas por información sobre el material eléctrico industrial de "
      "automatización y control que manejamos.»")

h2("A.3  Pregunta puente", G.BLUE)
para("Es la bisagra de toda la Vía A. Reconoce el tiempo transcurrido, baja la guardia y pide una "
     "sola respuesta corta.")
quote("«Sé que ya ha pasado algún tiempo, por eso quería preguntarle algo muy puntual: "
      "¿actualmente sigue manejando o comprando este tipo de material?»")

h2("A.4  Las cuatro respuestas posibles", G.BLUE)

h3("Si responde SÍ", G.GREEN)
quote("«Perfecto. Justamente quería retomar el contacto porque estamos reactivando campaña y "
      "quería saber si actualmente tiene alguna necesidad o algún proyecto donde podamos "
      "apoyarle.»")
quote("«¿Qué referencia o tipo de material está manejando actualmente de automatización?»")
para("Con la respuesta en mano, se entra al SPIN del perfil correspondiente y se intercalan los "
     "tres criterios de calificación:")
bullet("¿Ya ha realizado importaciones desde otro país?")
bullet("¿Cuenta ya con una agencia de transporte?")
bullet("¿Implementa proyectos o comercializa?")

h3("Si dice «no recuerdo» o «¿de qué empresa?»", G.AMBER)
quote("«Claro, no hay problema. Le cuento rápidamente: somos Eléctricas BC Corp., manejamos "
      "material eléctrico e industrial y estamos constituidos en Miami, Estados Unidos, desde el "
      "2001. Contamos con un portafolio de más de 5.000 referencias que podrían ser de su interés, "
      "disponibles para entrega inmediata.»")
quote("«No quiero quitarle tiempo; simplemente quería confirmar si actualmente ese tipo de "
      "material sigue siendo de su interés.»")
pin("«No quiero quitarle tiempo» es la frase que recupera la llamada. Devuelve el control al "
    "prospecto y casi siempre produce una respuesta honesta en lugar de una evasiva.")

h3("Si dice que ya no está interesado", G.AMBER)
quote("«Perfecto, no hay problema. Le agradezco la confirmación. ¿Actualmente está trabajando con "
      "algún otro tipo de material eléctrico o industrial que pueda serle útil? Por ejemplo "
      "contactores o relés bimetálicos. Quizás podamos apoyarle en otra necesidad.»")
pin("Una sola repregunta, no dos. Si vuelve a decir que no, se agradece, se tipifica «Sin interés» "
    "con el motivo y se cierra bien. Un cierre cordial deja la puerta abierta para la próxima ola.")

h3("Si dice «mándeme la información»", G.NAVY)
para("Es la objeción más frecuente y la más fácil de perder. No se manda catálogo completo: se "
     "cambia información por un dato de calificación.")
quote("«Claro. Para no enviarle información que no necesita, ¿qué producto o materiales está "
      "manejando actualmente?»")
quote("«Perfecto. Le envío las opciones y precios que tengamos disponibles. ¿Se las envío por "
      "WhatsApp o por correo?»")
pin("Enviar la información sin acordar fecha de seguimiento no es un cierre. Siempre: «Le llega "
    "hoy. ¿Le marco el [día] para revisarla juntos?»")

h2("A.5  Puente a la reunión", G.BLUE)
quote("«¿Qué le parece si coordinamos una reunión virtual con el consultor comercial? Con eso "
      "afinan los detalles del método de trabajo, los tiempos y las condiciones.»")

h2("A.6  Bifurcación de perfil", G.BLUE)
para("Antes de entrar al SPIN hay que saber con qué perfil se está hablando. Una sola pregunta lo "
     "resuelve:")
quote("«¿Para qué lo está necesitando: para un proyecto que usted implementa, para su propio "
      "inventario o para un equipo de su planta?»")

table([
    [{"text": "Para un proyecto que implementa", "fill": G.TEAL, "color": "ffffff",
      "bold": True, "jc": "center"},
     {"text": "Para su inventario o para revender", "fill": G.PURPLE, "color": "ffffff",
      "bold": True, "jc": "center"},
     {"text": "Para un equipo propio de su planta", "fill": G.MAGENTA, "color": "ffffff",
      "bold": True, "jc": "center"}],
    [{"text": "→ Perfil 1: Tablerista / Integrador", "fill": G.TEALBG, "color": G.TEAL,
      "jc": "center"},
     {"text": "→ Perfil 2: Distribuidor / Importador", "fill": G.PURPLEBG, "color": G.PURPLE,
      "jc": "center"},
     {"text": "→ Perfil 3: Usuario final industrial", "fill": G.MAGENTABG, "color": G.MAGENTA,
      "jc": "center"}],
], [3120, 3120, 3120], header=False)

# =============================================================== 5. VÍA B
pagebreak()
section_banner("VÍA B", "Llamada en frío",
               "Base histórica de Google Maps, directorios y referidos. El prospecto no pidió la "
               "llamada, no conoce EBC y no tiene ninguna razón para darnos tiempo. Todo el peso "
               "de la llamada está en los primeros 15 segundos.",
               G.AMBER, G.AMBERBG)

h2("B.1  Qué cambia respecto a la Vía A", G.AMBER)
box(["No se puede decir «usted dejó sus datos». Es falso y se nota de inmediato.",
     "Hay que pedir permiso explícitamente, antes de contar nada del portafolio.",
     "No se califica todo en la primera llamada: se gana el derecho a la segunda.",
     "El SPIN se recorta a Situación más una sola pregunta de Problema.",
     "La tasa de contacto efectivo es mucho más baja. El volumen es parte del método, no una "
     "señal de que algo está mal."],
    title="Reglas de la llamada en frío", color=G.AMBER, fill=G.AMBERBG)

h2("B.2  Apertura en frío", G.AMBER)
quote("«Buen día, ¿hablo con [Nombre] / con el área de compras de [Empresa]?»")
quote("«[Nombre], le habla [Nombre del SDR], de Eléctricas BC Corp. Somos distribuidores de "
      "material eléctrico industrial en Miami, Estados Unidos.»")
quote("«Le voy a ser honesto: es la primera vez que lo llamo. ¿Me da treinta segundos para "
      "decirle por qué, y usted me dice si tiene sentido seguir?»")
pin("Declarar la llamada en frío de entrada desarma la resistencia. Pedir treinta segundos y "
    "cumplirlos es lo que compra el resto de la conversación.")

h2("B.3  La razón de la llamada, en veinte segundos", G.AMBER)
quote("«Trabajamos con empresas como la suya que compran material de automatización y control: "
      "contactores, relés bimetálicos, variadores. Tenemos más de 5.000 referencias disponibles "
      "para entrega inmediata y estamos constituidos en Estados Unidos desde el 2001.»")
quote("«Lo llamo por una sola razón: saber si usted hoy compra este tipo de material y si le "
      "interesaría comparar condiciones de importación directa. ¿Hoy compra material de "
      "automatización?»")
pin("Una sola pregunta al final, cerrada y fácil de responder. Si la apertura termina en dos "
    "preguntas, el prospecto no responde ninguna.")

h2("B.4  Ramas de la llamada en frío", G.AMBER)

table([
    ["Lo que pasa", "Qué decir", "Qué no hacer"],
    ["Contesta recepción o conmutador",
     "«Le llamo de Eléctricas BC Corp., en Miami. Es sobre material eléctrico de automatización. "
     "¿Me comunica con la persona que maneja las compras técnicas, por favor?»",
     "Dar el pitch completo a quien no decide ni compra."],
    ["«¿Cómo consiguió mi número?»",
     "«Su empresa aparece en directorios públicos de proveedores eléctricos y por eso llegamos a "
     "usted. Si prefiere que no volvamos a llamar, lo marco así de inmediato y no vuelve a "
     "recibir llamadas nuestras.»",
     "Inventar un formulario, una recomendación o un referido que no existe."],
    ["«Estoy ocupado»",
     "«Lo entiendo, no lo entretengo. ¿Le marco mañana a esta misma hora, o prefiere que le deje "
     "la información por WhatsApp y usted me dice?»",
     "Seguir hablando. Insistir aquí quema el contacto."],
    ["«Ya tengo proveedor»",
     "«Me imaginaba, es lo normal. No lo llamo para que lo cambie. Lo llamo para que tenga una "
     "segunda opción cuando su proveedor no tenga una referencia o se demore. ¿Le ha pasado?»",
     "Atacar al proveedor actual o prometer que somos más baratos."],
    ["«No me interesa»",
     "«Entendido. Solo por curiosidad, para no volver a molestarlo: ¿es porque no compran este "
     "tipo de material, o porque ya lo tienen cubierto?»",
     "Repreguntar dos veces. Una sola, y se cierra cordial."],
    ["«Mándeme información al correo»",
     "«Con gusto. Para mandarle algo que le sirva y no un catálogo de 5.000 referencias: ¿qué "
     "material es el que más le rota?»",
     "Pedir el correo antes de tener un dato de calificación."],
    ["«¿Ustedes están en Miami? Yo no importo»",
     "«Es justo lo que quería confirmar. ¿Nunca ha importado, o lo ha hecho a través de un "
     "tercero? Porque muchos de nuestros clientes empezaron sin saber nada de importación.»",
     "Insistir si confirma que no importa ni piensa hacerlo. Es un descarte legítimo."],
], [2000, 4400, 2960])

h2("B.5  Cierre de la llamada en frío", G.AMBER)
para("El cierre no es una cotización. Es una segunda conversación con fecha.")
quote("«Le propongo algo concreto: coordinamos quince minutos con nuestro consultor comercial, "
      "usted le dice qué material maneja y él le muestra cómo quedarían las condiciones desde "
      "Miami. ¿Le sirve mañana en la mañana o el jueves?»")
quote("«Si prefiere, le escribo primero por WhatsApp con el detalle y nos hablamos el [día]. "
      "¿Le confirmo a este mismo número?»")
pin("Siempre dos opciones de horario, nunca «¿cuándo le queda bien?». La pregunta abierta devuelve "
    "la decisión al prospecto y la reunión se pierde.")

# =============================================================== 6. SPIN
pagebreak()
h1("SPIN por perfil")

para("A partir de aquí el guion es común a las dos vías. Lo que cambia es la profundidad: en la "
     "Vía A hay permiso para indagar; en la Vía B, apenas para abrir.")

table([
    ["Etapa", "Vía A — Lead de pauta", "Vía B — Frío (1.ª llamada)"],
    [{"text": "S — Situación", "bold": True}, "2 preguntas", "1 pregunta"],
    [{"text": "P — Problema", "bold": True}, "2 preguntas", "1 pregunta"],
    [{"text": "I — Implicación", "bold": True}, "1 o 2 preguntas, solo si el dolor apareció",
     "No se hace. Queda para la 2.ª llamada"],
    [{"text": "N — Necesidad", "bold": True}, "1 pregunta de cierre",
     "No se hace. Queda para la 2.ª llamada"],
], [2200, 3700, 3460])

pin("No es un cuestionario. Se para de preguntar cuando ya hay suficiente contexto para que el "
    "consultor comercial pueda armar una propuesta.")

# ---------------------------------------------------------------- PERFIL 1
section_banner("PERFIL 1", "Tablerista / Integrador",
               "Arma tableros, diseña e integra sistemas para terceros. Compra para incluir en "
               "proyectos. Le importa el margen, el cumplimiento de fechas y no quedar mal con su "
               "cliente final. Es el perfil más frecuente en el ICP de EBC. Tono: técnico, de "
               "igual a igual.",
               G.TEAL, G.TEALBG)

h2("S — Situación", G.TEAL)
quote("«¿Está evaluando para un proyecto puntual o está buscando un proveedor para incluirlo en "
      "su línea de trabajo?»")
quote("«¿Qué marcas está especificando hoy en sus tableros?»")
quote("«¿Qué referencias le rotan más: contactores, relés térmicos, variadores?»")
quote("«Ese material, ¿lo compra local o ya importa?»")

h2("P — Problema", G.AMBER)
quote("«¿Le ha pasado que un tablero se frena porque falta una sola referencia?»")
quote("«¿Cuánto se demora su proveedor local cuando la referencia no está en stock?»")
quote("«¿El precio local le deja margen, o está apretado para seguir siendo competitivo en "
      "licitaciones?»")
pin("Si dice que no tiene problemas: «¿Y cuando se le juntan dos o tres proyectos al mismo "
    "tiempo?»")

h2("I — Implicación", G.AMBER)
quote("«Cuando el tablero se atrasa por una referencia, ¿qué pasa con su cliente?»")
quote("«¿Cuántas veces le ha pasado este año?»")
quote("«Si pudiera comprar ese material a precio de importación directa, ¿cuánto cambiaría su "
      "cotización frente a la competencia?»")
pin("El objetivo es que el prospecto haga la cuenta en su cabeza, no que el SDR la haga por él.")

h2("N — Necesidad", G.GREEN)
quote("«Si tiene acceso a más de 5.000 referencias con entrega inmediata desde Miami y a precio "
      "de importación directa, ¿vale la pena revisar cómo se vería eso en su próximo proyecto?»")
quote("«¿Le sirve que el consultor comercial le arme el ejercicio con su propia lista de "
      "materiales?»")

h2("Cierre — Perfil 1", G.TEAL)
quote("«Le propongo esto: me cuenta el proyecto más cercano que tiene en puerta, coordinamos "
      "quince minutos con el consultor comercial y él le muestra cómo quedaría ese material desde "
      "Miami. Si la aritmética funciona una vez, construimos la relación desde ahí. ¿Cuál es el "
      "proyecto que tiene más cerca?»")

h2("Objeciones — Perfil 1", G.NAVY)
table([
    ["Objeción", "Respuesta"],
    ["«Mi cliente no conoce esas marcas»",
     "«Eso juega a su favor: el que especifica es usted. Nosotros le damos el respaldo técnico y "
     "la ficha de producto para que usted sustente la propuesta.»"],
    ["«Importar me demora el proyecto»",
     "«Al contrario: la idea es que el material esté disponible para entrega inmediata desde "
     "Miami. Lo que le quiero mostrar es el tiempo real puerta a puerta con su propia agencia.»"],
    ["«¿Y si me falla una referencia en obra?»",
     "«Para eso coordinamos la reunión con el consultor: él le confirma disponibilidad por "
     "referencia antes de que usted se comprometa con su cliente.»"],
    ["«No tengo tiempo de aprender a importar»",
     "«¿Ya trabaja con alguna agencia de transporte? Si ya la tiene, el proceso es más simple de "
     "lo que parece. Si no, es justo uno de los puntos de la reunión.»"],
], [2700, 6660])

h2("Señales de compra — Perfil 1", G.GREEN)
checklist([
    "Menciona un proyecto, una licitación o una fecha de entrega",
    "Menciona una referencia, una marca o un rango de potencia específico",
    "Pregunta por disponibilidad o por tiempos de entrega",
    "Pide ficha técnica o lista de referencias",
    "Dice que ya ha importado o que tiene agente de carga",
])
pin("Con el integrador la venta real es la relación, no el pedido puntual. El objetivo de la "
    "primera llamada es conseguir un proyecto piloto.")

# ---------------------------------------------------------------- PERFIL 2
pagebreak()
section_banner("PERFIL 2", "Distribuidor / Importador / Almacén eléctrico",
               "Compra para revender o para inventario: almacenes de material eléctrico, "
               "ferreterías industriales, importadores, fabricantes de maquinaria. Le importa el "
               "precio, el margen, la rotación y la disponibilidad.",
               G.PURPLE, G.PURPLEBG)

h2("S — Situación", G.PURPLE)
quote("«¿Qué marcas de material de automatización está manejando hoy?»")
quote("«¿Importa directo o le compra a un importador local?»")
quote("«¿Qué referencias le rotan más y con qué frecuencia hace pedidos?»")
quote("«¿Ya trabaja con una agencia de transporte propia?»")

h2("P — Problema", G.AMBER)
quote("«El margen que tiene hoy con su proveedor, ¿le deja cómodo o está apretado?»")
quote("«¿Ha perdido ventas por no tener stock cuando el cliente lo necesitaba ya?»")
quote("«¿Sus clientes le piden referencias que no consigue fácil o que le llegan muy demoradas?»")

h2("I — Implicación", G.AMBER)
quote("«¿Cuántas ventas calcula que ha perdido este año por precio o por demora?»")
quote("«¿Eso le ha afectado la relación con algún cliente importante?»")
quote("«¿Cuánto margen le está dejando al intermediario que le vende hoy?»")

h2("N — Necesidad", G.GREEN)
quote("«Si le damos precio de importación directa, más de 5.000 referencias consolidadas en un "
      "solo despacho desde Miami y entrega inmediata, ¿eso le da ventaja frente a su oferta "
      "actual?»")
quote("«¿Qué volumen manejaría al mes si las condiciones son competitivas?»")

h2("Cierre — Perfil 2", G.PURPLE)
quote("«Hagamos algo concreto: me pasa las referencias que más le rotan, coordinamos quince "
      "minutos con el consultor comercial y él le muestra condiciones y tiempos sobre esas "
      "referencias puntuales. ¿Le sirve mañana o el jueves?»")

h2("Objeciones — Perfil 2", G.NAVY)
table([
    ["Objeción", "Respuesta"],
    ["«Ya tengo un proveedor con el que trabajo bien»",
     "«Perfecto, no le pido que lo cambie. Le pido que compare condiciones en una sola "
     "referencia. Si no somos mejores, se lo digo yo mismo.»"],
    ["«¿Cuál es el mínimo de compra?»",
     "«Depende de la línea y del despacho. Es exactamente uno de los puntos que le confirma el "
     "consultor comercial en la reunión, con las referencias que usted maneja.»"],
    ["«¿Cuánto me sale el flete?»",
     "«El flete depende del peso, del volumen y de su agencia. Si ya tiene agente de carga, él "
     "le cotiza sobre el despacho real. Nosotros le damos el peso y las dimensiones.»"],
    ["«Mis clientes piden marcas conocidas»",
     "«Entiendo. Trabajamos marcas con respaldo internacional y el argumento de venta lo "
     "construimos con usted. Pero primero veamos si el precio le da margen.»"],
], [2700, 6660])

h2("Señales de compra — Perfil 2", G.GREEN)
checklist([
    "Pregunta por lista de precios o por descuento por volumen",
    "Pregunta por mínimos de compra o por condiciones de pago",
    "Menciona referencias o cantidades concretas",
    "Pregunta por tiempos de despacho desde Miami",
    "Menciona un cliente final que está esperando material",
])

# ---------------------------------------------------------------- PERFIL 3
section_banner("PERFIL 3", "Usuario final industrial",
               "Jefe de mantenimiento, gerente de planta, dueño de empresa industrial. Compra "
               "para usar, no para revender. Sectores: bombeo, minería, alimentos, ladrilleras, "
               "cementeras, textiles, refrigeración.",
               G.MAGENTA, G.MAGENTABG)

pin("Es el perfil menos frecuente en el ICP de EBC. Si es un usuario final pequeño, sin volumen y "
    "sin disposición a importar, lo correcto es clasificarlo como C o descartarlo, no forzarlo.")

h2("S — Situación", G.MAGENTA)
quote("«¿Qué equipos o líneas tiene en la planta: bombas, compresores, bandas?»")
quote("«¿Qué material eléctrico compra con más frecuencia para mantenimiento?»")
quote("«¿El mantenimiento lo hace con personal propio o lo terceriza?»")

h2("P — Problema", G.AMBER)
quote("«¿Han tenido paradas por falta de un repuesto eléctrico?»")
quote("«¿Cuánto se demora conseguir localmente una referencia crítica cuando se daña?»")
quote("«¿Han tenido arranques bruscos que les dañen correas, acoples o rodamientos?»")

h2("I — Implicación", G.AMBER)
quote("«Cuando para ese equipo, ¿cuánto tiempo tarda en volver a producción?»")
quote("«¿Eso ha pasado más de una vez este año?»")
quote("«¿Cuánto le cuesta una hora de planta detenida?»")

h2("N — Necesidad", G.GREEN)
quote("«Si pudiera tener stock de seguridad de sus referencias críticas, a precio de importación "
      "directa y con respaldo técnico, ¿eso justifica revisarlo?»")
quote("«¿Qué tan importante es para ustedes no depender de un solo proveedor local?»")

h2("Cierre — Perfil 3", G.MAGENTA)
quote("«Lo más práctico es esto: me pasa la lista de las referencias que más consume o que le son "
      "críticas, y coordinamos quince minutos con el consultor comercial para que le muestre cómo "
      "quedaría ese material desde Miami. ¿Le sirve esta semana?»")

h2("Objeciones — Perfil 3", G.NAVY)
table([
    ["Objeción", "Respuesta"],
    ["«Yo le compro a mi electricista / a la ferretería»",
     "«Claro, y para urgencias eso funciona. Lo que le propongo es para el material que compra "
     "recurrente, donde el precio y el respaldo sí hacen diferencia.»"],
    ["«Yo no importo nada»",
     "«¿Nunca, o no directamente? Porque en muchos casos la empresa ya importa otras cosas y el "
     "proceso está montado. ¿Tienen agencia de transporte?»"],
    ["«Está muy caro»",
     "«¿Caro comparado con qué? Antes de hablar de precio, dejemos que el consultor le haga el "
     "ejercicio con sus referencias reales.»"],
    ["«¿Quién me lo instala?»",
     "«Nosotros vendemos el material con respaldo técnico. La instalación la hace su equipo o su "
     "contratista, y el consultor le confirma qué soporte técnico incluye.»"],
], [2700, 6660])

h2("Señales de compra — Perfil 3", G.GREEN)
checklist([
    "Pregunta por precio o por tiempo de entrega",
    "Menciona un equipo específico, una potencia o una referencia",
    "Dice que es él quien decide, o menciona a quien decide",
    "Pregunta por garantía o por soporte técnico",
    "Menciona una parada reciente o un equipo crítico",
])

# =============================================================== 7. CIERRES
pagebreak()
h1("Cierres — el cierre es la reunión, no la cotización")

para("En la v1.0 el cierre era enviar una propuesta con precio el mismo día. En EBC no: el SDR "
     "no cotiza. El cierre del SDR es entregar la conversación al consultor comercial con una "
     "fecha puesta.")

table([
    ["Tipo de cierre", "Cuándo se usa", "Qué se dice", "Qué queda registrado"],
    [{"text": "Primario — reunión agendada", "bold": True, "color": G.GREEN},
     "Nivel A o B: hay producto, hay interés y puede importar.",
     "«Coordinamos quince minutos con el consultor comercial. ¿Le sirve mañana en la mañana o el "
     "jueves?»",
     "Fecha y hora de la reunión, producto mencionado, nivel A o B."],
    [{"text": "Secundario — lista solicitada", "bold": True, "color": G.BLUE},
     "Hay interés pero no quiere reunión todavía.",
     "«Le envío las opciones y precios disponibles. ¿Por WhatsApp o por correo? ¿Le marco el "
     "[día] para revisarla juntos?»",
     "Canal elegido, material solicitado y fecha de seguimiento."],
    [{"text": "Nurture — re-contacto", "bold": True, "color": G.GRAY},
     "Nivel C: interés general, sin proyecto ni fecha.",
     "«Le dejo mi contacto y lo busco en unos quince días, cuando tenga más claro el panorama. "
     "¿Le parece?»",
     "Fecha de re-contacto a 15 días y motivo."],
    [{"text": "Cierre cordial — descarte", "bold": True, "color": "9a3412"},
     "No compra el material, o no puede ni quiere importar.",
     "«Le agradezco la confirmación. Si en algún momento necesita material de automatización, "
     "quedo a la orden.»",
     "Motivo de descarte explícito."],
], [1900, 2100, 3300, 2060])

pin("«Le envío la información» sin fecha de seguimiento no es un cierre: es un lead que vuelve a "
    "la pila de los 565 sin gestionar.")

# =============================================================== 8. LÍMITES
h1("Lo que el SDR no hace")

box(["No aprueba ni promete precios, descuentos, mínimos de compra, plazos de entrega, "
     "disponibilidad ni condiciones de crédito. Todo eso lo confirma EBC.",
     "No dice «distribuidor oficial» de ninguna marca sin que EBC lo haya confirmado por escrito.",
     "No menciona stock en Bogotá ni en el país del prospecto: EBC despacha desde Miami.",
     "No inventa el origen del contacto. En frío se dice que es en frío.",
     "No envía catálogo completo: envía lo que corresponde a lo que el prospecto dijo que maneja.",
     "No negocia, no cotiza y no cierra la venta. Califica y entrega.",
     "No insiste más de tres veces sobre el mismo número sin cambiar de canal."],
    title="Límites operativos", color="9a3412", fill="fdf0ef")

h1("Registro en el CRM")

para("Una llamada sin registro no existe. Al terminar cada conversación se tipifica el estado y "
     "se deja la próxima acción con fecha.")

table([
    ["Resultado de la llamada", "Estado en CRM", "Próxima acción", "Plazo"],
    ["Reunión agendada con el consultor", "Cotizado", "Confirmar asistencia del consultor y del prospecto", "Mismo día"],
    ["Interés real, sin reunión aún", "Seguimiento", "Enviar material solicitado y marcar fecha de revisión", "24 horas"],
    ["Interés general, sin proyecto", "Seguimiento", "Programar re-contacto", "15 días"],
    ["No contesta (3 intentos)", "No contesta", "Cambiar de canal: WhatsApp o correo", "—"],
    ["Teléfono errado o empresa cerrada", "Datos incorrectos", "Cerrar. Buscar dato alterno si el perfil es ICP", "—"],
    ["No compra el material / no importa", "Sin interés", "Cerrar con motivo explícito", "—"],
], [2900, 1900, 3360, 1200])

h2("Qué se registra siempre", G.NAVY)
bullet("Vía de la llamada (A o B) y origen del contacto.")
bullet("Producto o referencia que mencionó el prospecto.")
bullet("Cantidad o volumen, si lo dio.")
bullet("Horizonte de compra: ya, menos de 2 meses, 2 a 6 meses, sin fecha.")
bullet("¿Ha importado? Sí / No / A través de un tercero.")
bullet("¿Tiene agencia de transporte? Sí / No.")
bullet("Rol: implementa proyectos / comercializa / usuario final.")
bullet("Nivel asignado: A, B, C o descarte, con el motivo.")
bullet("Próxima acción con fecha.")

# =============================================================== 9. REFERENCIA
pagebreak()
h1("Referencia rápida — una página")

table([
    ["", "VÍA A — Lead de pauta", "VÍA B — Frío"],
    [{"text": "Primera frase", "bold": True, "color": G.NAVY},
     "«Dejó sus datos a través de una de nuestras campañas.»",
     "«Es la primera vez que lo llamo. ¿Me da treinta segundos?»"],
    [{"text": "Pregunta puente", "bold": True, "color": G.NAVY},
     "«¿Actualmente sigue manejando o comprando este tipo de material?»",
     "«¿Hoy compra material de automatización?»"],
    [{"text": "Qué hay que calificar", "bold": True, "color": G.NAVY},
     "Producto + horizonte + importación + agencia + rol.",
     "Que compre el material y que pueda importar. El resto, en la 2.ª llamada."],
    [{"text": "Profundidad SPIN", "bold": True, "color": G.NAVY},
     "S, P, I y N.", "S y una P."],
    [{"text": "Cierre esperado", "bold": True, "color": G.NAVY},
     "Reunión con el consultor comercial, con fecha.",
     "Segunda conversación con fecha, o paso a WhatsApp."],
    [{"text": "Duración", "bold": True, "color": G.NAVY}, "4 a 7 minutos.", "60 a 120 segundos."],
    [{"text": "Si no contesta", "bold": True, "color": G.NAVY},
     "3 intentos en días y horas distintas, luego WhatsApp.",
     "2 intentos, luego WhatsApp o se deja en la base."],
], [1800, 3900, 3660])

h2("Dolor principal por perfil", G.NAVY)
table([
    ["", "Tablerista / Integrador", "Distribuidor / Importador", "Usuario final"],
    [{"text": "Dolor", "bold": True, "color": G.NAVY},
     "Referencia que falta y frena el tablero; margen apretado en licitación.",
     "Margen que se come el intermediario; venta perdida por falta de stock.",
     "Parada de planta por repuesto; precio local del material crítico."],
    [{"text": "Pregunta clave", "bold": True, "color": G.NAVY},
     "«¿Qué pasa con su cliente cuando el tablero se atrasa?»",
     "«¿Cuántas ventas ha perdido por precio o por demora?»",
     "«¿Cuánto le cuesta una hora de planta detenida?»"],
    [{"text": "Lo que más valora", "bold": True, "color": G.NAVY},
     "Disponibilidad por referencia y respaldo técnico.",
     "Precio de importación directa y rotación.",
     "No depender de un solo proveedor local."],
    [{"text": "Cierre", "bold": True, "color": G.NAVY},
     "Ejercicio sobre su lista de materiales del próximo proyecto.",
     "Condiciones sobre sus referencias de mayor rotación.",
     "Ejercicio sobre sus referencias críticas."],
], [1500, 2620, 2620, 2620])

box(["Identificar la vía antes de marcar.",
     "Confirmar que compra el material antes de hablar de portafolio.",
     "Colar los tres criterios de importación dentro de la conversación, no en fila.",
     "Cerrar siempre con una fecha: reunión, envío con revisión o re-contacto.",
     "Registrar la llamada el mismo día, con la próxima acción puesta."],
    title="Checklist de cada llamada", color=G.GREEN, fill="eef7f0")

h1("Pendientes de confirmación con EBC")

para("Estos puntos no están definidos en las fuentes disponibles y el SDR no los puede improvisar "
     "en una llamada. Se deben cerrar con EBC antes de que el guion entre en operación.")

table([
    ["Punto", "Por qué importa", "Quién lo confirma"],
    ["Quién es el consultor comercial al que se agenda la reunión",
     "Todo el cierre del guion depende de que haya un nombre y una agenda disponible.",
     "EBC (Alejandro)"],
    ["Mínimo de compra por línea y por despacho",
     "Es la primera pregunta del perfil distribuidor. Sin respuesta, el SDR queda expuesto.",
     "EBC"],
    ["Condiciones de pago y de crédito",
     "Aparece en todas las conversaciones de canal.",
     "EBC"],
    ["Marcas sobre las que se puede afirmar representación o distribución oficial",
     "Afirmar una representación que no existe es un riesgo comercial y legal.",
     "EBC"],
    ["Tiempos reales de despacho desde Miami",
     "Es el argumento de «entrega inmediata». Debe ser verificable.",
     "EBC"],
], [3200, 4200, 1960])
G.md.append("")

# =============================================================== EMPAQUETADO
NS = ('xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" '
      'xmlns:o="urn:schemas-microsoft-com:office:office" '
      'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
      'xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" '
      'xmlns:v="urn:schemas-microsoft-com:vml" '
      'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
      'xmlns:w10="urn:schemas-microsoft-com:office:word" '
      'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
      'xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" '
      'xmlns:sl="http://schemas.openxmlformats.org/schemaLibrary/2006/main" '
      'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
      'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" '
      'xmlns:c="http://schemas.openxmlformats.org/drawingml/2006/chart" '
      'xmlns:lc="http://schemas.openxmlformats.org/drawingml/2006/lockedCanvas" '
      'xmlns:dgm="http://schemas.openxmlformats.org/drawingml/2006/diagram" '
      'xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" '
      'xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" '
      'xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" '
      'xmlns:w15="http://schemas.microsoft.com/office/word/2012/wordml"')

SECTPR = ('<w:sectPr><w:headerReference r:id="rId7" w:type="default"/>'
          '<w:footerReference r:id="rId8" w:type="default"/>'
          '<w:pgSz w:h="15840" w:w="12240" w:orient="portrait"/>'
          '<w:pgMar w:bottom="1440" w:top="1440" w:left="1440" w:right="1440" '
          'w:header="708" w:footer="708" w:gutter="0"/><w:pgNumType w:start="1"/></w:sectPr>')

document = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document %s><w:body>%s%s</w:body></w:document>'
            % (NS, "".join(G.body), SECTPR))

HDR = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:hdr %s>'
       '<w:p><w:pPr><w:pBdr><w:bottom w:color="%s" w:space="1" w:sz="6" w:val="single"/></w:pBdr>'
       '<w:spacing w:after="200" w:lineRule="auto"/></w:pPr>%s%s</w:p></w:hdr>'
       % (NS, G.BLUE,
          run("Eléctricas BC Corp.", bold=True, color=G.NAVY, size=20),
          run("  |  Guion de llamada SDR — Vía pauta / Vía frío — v2.0", color=G.GRAY, size=20)))

FTR = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr %s>'
       '<w:p><w:pPr><w:pBdr><w:top w:color="%s" w:space="1" w:sz="6" w:val="single"/></w:pBdr>'
       '<w:tabs><w:tab w:val="right" w:leader="none" w:pos="9026"/></w:tabs>'
       '<w:spacing w:before="100" w:lineRule="auto"/></w:pPr>%s'
       '<w:r><w:rPr><w:rFonts w:ascii="Arial" w:cs="Arial" w:hAnsi="Arial"/>'
       '<w:color w:val="%s"/><w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr>'
       '<w:tab/></w:r>'
       '<w:fldSimple w:instr=" PAGE "><w:r><w:rPr>'
       '<w:rFonts w:ascii="Arial" w:cs="Arial" w:hAnsi="Arial"/><w:color w:val="%s"/>'
       '<w:sz w:val="18"/><w:szCs w:val="18"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple>'
       '</w:p></w:ftr>'
       % (NS, G.BLUE,
          run("Uso interno — SDR / Ventas · Eléctricas BC Corp.", color=G.GRAY, size=18),
          G.GRAY, G.GRAY))

if os.path.exists(BUILD):
    shutil.rmtree(BUILD)
shutil.copytree(TPL, BUILD)

with open(os.path.join(BUILD, "word", "document.xml"), "w", encoding="utf-8") as f:
    f.write(document)
with open(os.path.join(BUILD, "word", "header1.xml"), "w", encoding="utf-8") as f:
    f.write(HDR)
with open(os.path.join(BUILD, "word", "footer1.xml"), "w", encoding="utf-8") as f:
    f.write(FTR)

core = os.path.join(BUILD, "docProps", "core.xml")
if os.path.exists(core):
    t = open(core, encoding="utf-8").read()
    t = re.sub(r"<dc:title>.*?</dc:title>",
               "<dc:title>Guion de llamada SDR — Eléctricas BC Corp. v2.0</dc:title>", t)
    open(core, "w", encoding="utf-8").write(t)

OUT_DOCX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BUILD, "..", "out.docx")
OUT_MD = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BUILD, "..", "out.md")
OUT_DOCX = os.path.abspath(OUT_DOCX)
if os.path.exists(OUT_DOCX):
    os.remove(OUT_DOCX)
subprocess.run(["zip", "-Xr", OUT_DOCX, "."], cwd=BUILD, check=True,
               stdout=subprocess.DEVNULL)

header_md = (
    "# Guion de llamada SDR — Eléctricas BC Corp.\n\n"
    "**Versión 2.0 · 14 de octubre de 2026 · Uso interno SDR**\n\n"
    "> Reemplaza a `Guion de ventas SPIN — Variadores de frecuencia Invertek` (v1.0, "
    "Eléctricas Bogotá Ltda.).\n> Fuentes: `tmp/scripts/Script Comercial con Ajustes Luis "
    "Niño.pdf` (lineamientos de llamada EBC), `tmp/scripts/spin_ebc.md` (estructura SPIN), "
    "`PROPUESTA.md` (ICP, olas, SLA).\n> Entregable con formato: "
    "`tmp/scripts/Guion_Llamada_SDR_EBC_v2.docx`.\n\n---\n"
)
with open(os.path.abspath(OUT_MD), "w", encoding="utf-8") as f:
    f.write(header_md + "\n".join(G.md) + "\n")

print("docx:", OUT_DOCX, os.path.getsize(OUT_DOCX), "bytes")
print("md:  ", os.path.abspath(OUT_MD))
