# SOP-CREA-01 — Piezas de producto para Meta Ads (Relpol / EBC)

Cómo producir una pieza de anuncio de producto sin repetir las 7 rondas que tomó la de "Más relés en el mismo riel DIN" (9–10 nov 2026). Resume lo que se aprendió en esas sesiones y lo que midió el CRM después.

---

## 1. Por qué este formato

La pieza de Relpol 6,2 mm fue la que funcionó. Datos del 10 al 19 de noviembre de 2026, cruzando Meta con AriCRM (`conversations.referral_metadata.source_id` = id del anuncio):

| Anuncio | Gasto | Conversaciones | MQL | Costo por MQL |
|---|---|---|---|---|
| **Relpol 6,2 mm** (esta pieza) | $53 | 91 | **9** | **~$6** |
| Multimarca "Cotiza material eléctrico hoy" | $69 | 162 | 1 | ~$69 |

**Patrón ganador:** un solo producto + un beneficio técnico concreto + público que se filtra solo. Las piezas de catálogo ("muro de productos", "Precisión y rendimiento") atraen gente fuera del perfil de cliente ideal (ICP).

**Mídelo siempre por costo por MQL en el CRM, nunca por costo por conversación de Meta.** El Multimarca tenía la conversación más barata y fue el peor.

---

## 2. Reglas no negociables

1. **El producto NO se genera con IA.** No se redibuja, no se retoca, no se deforma, no se repinta. Solo se permite: recorte del fondo blanco, escala uniforme y sombra de contacto. La v5 se rechazó porque el generador inventó rótulos ("PI6-1P-12VDC", "MADE IN POLAND"), diagramas y combinaciones que no existen.
2. **La IA (Codex) solo genera el fondo**, sin texto, logos, personas, productos ni relés.
3. **Fotos oficiales de relpol.pl** en alta resolución. Las del cliente (560 px) solo sirven como referencia de ángulo y color.
4. **Solo reducir, nunca ampliar** la foto del producto. Si hay que ampliar, máximo ~1,2–1,6× con Lanczos, y es mejor un producto más chico y nítido.
5. **Nada de combinaciones inventadas**: ni un riel DIN dibujado ni un SSR "encima" de un módulo si la foto no lo muestra así.
6. **Sellos CE/UL no protagonistas.** Si se leen grandes, parecen una afirmación de certificación.
7. **"Imagen ilustrativa"** al pie, siempre que haya una escena generada.
8. **robots.txt de relpol.pl:** `Disallow: /content/download/` (fichas PDF, catálogos). No descargar de ahí; solo anotar la URL. Las imágenes en `/var/relpol/storage/images/` sí están permitidas.

---

## 3. Formato y estilo aprobados

- **1080×1350 (4:5)** PNG, mobile-first. Para Stories y Reels se necesita además una versión 9:16 (1080×1920) con la franja inferior libre (unos 250 px), porque ahí van los botones de Reels.
- **Tipografía:** Comfortaa (`~/Library/Fonts/Comfortaa-VariableFont_wght.ttf`). Titular ~94 px, subtítulo ~50 px, pie ~26 px.
- **Acento naranja `#FC5000`** solo en el dato clave (p. ej. "6,2 mm").
- **Texto mínimo:** titular de beneficio + subtítulo con el dato técnico. Sin logos, chips ni listas de credenciales (en v3 se descartaron por ilegibles en el celular).
- **Fondo:** pasillo de almacén/tienda de material eléctrico desenfocado, luces cálidas, tercio superior izquierdo oscuro para el titular y zona central inferior despejada para el producto. La idea es que el distribuidor "se reconozca" (v3), no ver una fábrica ajena.
- **Vocabulario LATAM:** "relé" (no "relevo", que es colombiano).

---

## 4. Proceso paso a paso

Carpeta de trabajo: `tmp/piezas_<marca>_<AAAA_MM_DD>/`. Para la de 6,2 mm es `tmp/piezas_relpol_2026_11_09/`.

### Paso 1 — Elegir producto y beneficio (Claude)
Una sola línea de producto y una frase de beneficio verificable en la página oficial. Escribir `copy_NN_<producto>.md` con: título, descripción, cuerpo, CTA (`WHATSAPP_MESSAGE`) y la lista de **pendientes antes de pautar** (ver §6).

### Paso 2 — Fotos oficiales (Claude o subagente)
- Descargar de `https://www.relpol.pl/var/relpol/storage/images/produkty/...` con curl, User-Agent de navegador y pocas requests.
- Guardar en `referencias_oficiales_hd/oficial_relpol_pl/` con nombre `<alias>_<modelo>_<detalle>_<WxH>.jpg`.
- Escribir `referencias_oficiales_hd/ORIGEN.md`: URL exacta, página donde se vio, resolución y producto real en la foto.
- **Verificar la etiqueta impresa en la foto contra el modelo de la página.** Relpol reutiliza una foto por familia: la página de RSR30-D12-A1-24-020-1 muestra un RSR30-D24-D1-02-040-1, y la de NEED-230AC muestra "12DC". Si el anuncio nombra un modelo, la foto tiene que coincidir o no se muestra el código grande.

### Paso 3 — Fondo (Codex, con generador de imágenes)
Usar el prompt de §5.1. Pedir 2 variantes (a: neutra/gris, b: más cálida/dorada) a 1080×1350 exacto. Revisar a ojo que no haya texto ni logos legibles.

### Paso 4 — Recorte del producto (script Python)
Base: `_v6_scripts/06_extraer_hd.py`.
- Flood-fill BFS desde los 4 bordes con **`WHITE_THRESH = 242`** (el gris del módulo ronda RGB 214, con bordes de hasta ~239).
- `alpha = where(bg_mask, blur*0.2, max(blur, 200))`, suavizado de **1 px**, no 3.
- Sombra de contacto en un PNG aparte (`*_sombra.png`).
- Verificar el borde con zoom al 300% en NEAREST sobre fondo oscuro **y** claro: sin halo blanco, sin dentado ni muescas.

### Paso 5 — Composición (script Python)
Base: `_v6_scripts/09_composicion_hd_r4.py` (fondos Codex) y `10_fondoB_y_verificacion_r4.py`.
- **Posicionar por el bounding box real del producto (alpha > 30), no por el lienzo del PNG con sombra.** El margen real de la sombra es ~210 px, no el radio del blur; ese error dejó 200 px de hueco entre módulos en la ronda 1.
- Hilera recta, base común, escala uniforme y separación visual de 8–20 px.
- Spotlight sutil detrás del producto si el fondo es oscuro.

### Paso 6 — Verificación (antes de mostrar)
Generar `comparacion_*.png` (referencia | recorte en pieza | zoom) y `notas_fidelidad_*.md` con origen de cada producto, factor de escala, gaps reales y dudas. Revisar con la checklist de §7.

### Paso 7 — Subir y medir
- Crear el anuncio **en PAUSED** en `act_1908878762587039` con `META_APP_TOKEN_SELLER_EBC` (ver `myseo-env/context/meta-ads-access.md`).
- Agregarlo al mismo conjunto solo los lunes, para no reiniciar el aprendizaje varias veces en la semana.
- A los 7 días, cruzar con el CRM: conversaciones con `referral_metadata->>'source_id' = <ad_id>` → `contacts.prospecting_status = 'calificado'` o `pipeline_deals.stage` en `qualified+`. Comparar contra los ~$6/MQL de la pieza 6,2 mm.

---

## 5. Prompts reutilizables

### 5.1 Fondo (Codex)
> TAREA ACOTADA: generar SOLO un fondo de imagen (sin producto, sin texto) para una pieza publicitaria móvil. Escribe únicamente en `<carpeta>` y solo los archivos indicados; no modifiques nada más, no hagas commit, no subas nada. REFERENCIA DE ESTILO: `<pieza previa>.png` (pasillo de almacén/tienda de material industrial desenfocado); NO copies su texto ni sus productos. GENERA con tu generador de imágenes, vertical 4:5 (1080x1350 PNG), DOS variantes: `fondo_<x>_a.png` (más neutra/gris) y `fondo_<x>_b.png` (más cálida/dorada, pasillo algo más cerrado). Requisitos: pasillo visto de frente con punto de fuga centrado; profundidad de campo muy corta (bokeh fotográfico real, no ilustración); estanterías metálicas con cajas y rollos de cable genéricos SIN etiquetas legibles; luces cálidas arriba; piso de concreto pulido en el tercio inferior con reflejo suave; zona central inferior despejada y algo más clara para apoyar un producto; tercio superior izquierdo calmado y oscuro para un titular blanco grande. Prohibido: texto, letras, números, logos, marcas, personas, productos de cualquier marca, relés. EVIDENCIA: los dos PNG existen a 1080x1350 exactos (verifica con sips o Pillow), los abriste y confirmas que no hay texto/logos/productos legibles.

### 5.2 Composición (Claude o Codex, sin generador)
> TAREA: componer la pieza `<producto>` sobre `fondo_<x>_<a|b>.png`, 1080x1350. Solo puedes escribir en `<carpeta>`. REGLA PRINCIPAL: el producto NO se genera, NO se redibuja, NO se retoca, NO se deforma; solo recorte del fondo blanco (flood-fill desde bordes, umbral 242, feather 1 px), escala uniforme (solo reducir) y sombra de contacto. Fotos: `referencias_oficiales_hd/oficial_relpol_pl/<archivos>`. Posiciona por el bounding box real del producto (alpha>30), no por el lienzo con sombra; hilera recta, base común, gap visual de `<n>` px. Texto: titular "`<titular>`" (Comfortaa ~94 px, blanco), subtítulo "`<subtítulo>`" con "`<dato>`" en #FC5000 (~50 px), pie "Imagen ilustrativa" (~26 px). ENTREGA: PNG final + `comparacion_<n>.png` (referencia | recorte | zoom 300% NEAREST) + `notas_fidelidad_<n>.md` (origen, factor de escala, gaps reales, dudas).

---

## 6. Pendientes antes de pautar (copiar en cada `copy_*.md`)

1. **Permiso de uso de las fotos.** relpol.pl no tiene términos de uso de imágenes ni sección de prensa; que no haya aviso no significa que haya autorización. Pedir permiso escrito a **marketing@relpol.com.pl** (página Marketing Department), o confirmarlo en el contrato de distribución de EBC. *Estado al 19-nov-2026: sin confirmar.*
2. **Declaración de IA en Meta:** el fondo es una imagen generada.
3. **Afirmaciones técnicas** validadas contra la página oficial, y aprobadas por EBC.
4. **Notas de instalación** si la imagen las contradice. Ej.: los PIR6W de 230 V AC/DC requieren ≥5 mm entre relés, así que la hilera compacta es ilustrativa.

---

## 7. Checklist de entrega

- [ ] Un producto, un beneficio, dato clave en naranja.
- [ ] Producto 100% de foto oficial: sin rótulos inventados, sin mezclas que no existen.
- [ ] Etiqueta visible en la foto = modelo que nombra el texto (o el código no se muestra).
- [ ] Solo reducción de escala; borde limpio sobre fondo claro y oscuro.
- [ ] CE/UL no legibles como protagonistas.
- [ ] Sin texto ni logos en el fondo; "Imagen ilustrativa" al pie.
- [ ] 4:5 (1080×1350) y, si va a Stories/Reels, versión 9:16 con la franja inferior libre.
- [ ] "relé", no "relevo"; sin precios, monedas ni promociones de otro país o distribuidor.
- [ ] `copy_*.md` con los pendientes de §6, `ORIGEN.md` y `notas_fidelidad_*.md` al día.
- [ ] Anuncio creado en PAUSED; activación aprobada por el usuario.

---

## 8. Errores ya cometidos (no repetir)

| Ronda | Error | Corrección |
|---|---|---|
| v1–v2 | Producto protagonista gigante, formato 1:1, credenciales en fila ilegibles | 4:5, menos elementos, texto grande |
| v3 | Escena de fábrica ajena | Tienda/almacén eléctrico donde el distribuidor se reconoce |
| v4 | Módulos en ángulos distintos, uno lavado o translúcido (máscara con opacidad parcial), bordes dentados | Escala uniforme, hilera recta, recorte verificado sobre fondo claro y oscuro |
| v4 | Módulos en 3/4: no se ve que miden 6,2 mm | Mostrar el perfil angosto: la imagen tiene que probar el titular |
| v4 | CE/UL grandes en el módulo del frente | Poner adelante el módulo con marcas discretas |
| v5 | **Generador de imágenes redibujó el producto** (rótulos y diagramas falsos) | Regla §2.1: el producto nunca pasa por IA |
| v6 r1 | Posicionado por el lienzo con sombra → 200 px de hueco | Posicionar por el bbox real (alpha>30) |
| v6 r2 | Fotos del cliente de 560 px, ampliadas | Fotos oficiales HD de relpol.pl, solo reducción |
| — | Piezas de catálogo de terceros (precios en COP de EBL, datos de Nova Electro, promos vencidas, URLs de electricasbogota.com) | No reutilizar material de otros distribuidores |

---

## 9. Inventario de fotos oficiales disponibles

| Línea | Carpeta | Contenido |
|---|---|---|
| PI6W / PIR6WB 6,2 mm, RSR30 en zócalo, RM699BV | `tmp/piezas_relpol_2026_11_09/referencias_oficiales_hd/oficial_relpol_pl/` | 10 JPG hasta 1825×1949, fondo blanco; detalle en `ORIGEN.md` |
| PI6W extra + peines ZG20 | por mover desde el scratchpad de la sesión del 19-nov | PIR6WB-1PS 3/4 con bornes de resorte (1214×1260, nueva); peines ZG20-1/2/3 rojo, negro y azul (1239×552 c/u) y foto de grupo (1550×1276); PI6-1P y PI6-1T de la serie anterior (solo referencia, **no son PI6W**) |
| NEED (relé programable) | por mover desde el scratchpad de la sesión del 19-nov | 16E/8S sin y con LCD (2049×1648, 2200×1808), 8E/4S con LCD (1672×1736), cables NEED-PC-15C/15B (2560×1808), memoria NEED-M-4KB (694×547, baja) |
| R15 / R2N / R4N / zócalos | por mover desde el scratchpad de la sesión del 19-nov | R15 3P (1194×1095 y 1014×1486, botón azul o naranja), R2N (1160×1621), R4N (1147×1591), zócalos GZT4/GZT2/GZM2 (~1700×1500), módulo M41G LED/supresor (183×358, baja) |

Notas de NEED (verificadas en la página oficial, no en la ficha PDF): 16 entradas/8 salidas (relé 10 A/250 V AC o transistor 0,5 A/24 V DC), familia compacta 8E/4S; alimentación 230 V AC, 12/24 V DC y 220 V DC; software gratuito, LAD y STL; montaje en riel DIN; versiones "-D" con LCD y teclado. El cartucho de memoria se llama **NEED-M-4KB** (no "4K8"). No existe "NEED-LCD-A" en el sitio oficial. Las fotos de una misma familia son idénticas entre tensiones: la etiqueta puede no coincidir con el modelo que se nombre.

Notas de PI6W / RSR30 (verificadas en el HTML oficial):
- 6,2 mm de ancho, riel DIN de 35 mm. Zócalo PI6W-1PS más relé RM699BV o RSR30.
- Salida -R: 6 A/250 V AC (AC1). -T (triac): 1 A AC1. RSR30 suelto: de 1 a 4 A según modelo.
- Entradas PIR6WB-1PS: 12/24/36/48 V DC, 24/42/115/230 V AC/DC.
- El peine de puenteo se llama **ZG20** (no "ZGPI6W"): 36 A/250 V AC, en rojo, negro o azul. La página no confirma que sea compatible con el PI6W: verificarlo antes de mostrarlos juntos.
- **No existen fotos oficiales en riel DIN ni en hilera.** Cualquier hilera es una composición ilustrativa.
- **No existe foto del RSR30 suelto con el modelo correcto:** todas las variantes usan la imagen del RSR30-D24-D1-02-040-1.
- **Sin cifras oficiales de vida útil del SSR frente al electromecánico** en el HTML. No usar "dura X veces más"; como mucho, "sin contactos mecánicos".

Notas de R15 / R2N / R4N (verificadas en el HTML oficial):
- Contactos AgNi. R15 3P: 10 A/250 V AC (10 A/277 V AC UL 508), 10 A/24 V DC. R2N: 12 A/250 V AC. R4N: 6 A/250 V AC.
- Bobinas AC 6–240 V y DC 5–220 V.
- R15: "mechanical indicator; test button". R2N: indicador mecánico, LED opcional, botón de prueba.
- Certificados UL, cUL, VDE, CSA (R15) y Lloyd's (R15, R4N, GZT4); bases con UL/cUL.
- −40 a +55 °C (AC) / +70 °C (DC); vida mecánica ≥2×10⁷ ciclos.
- **No prometer "bloqueo" del botón de prueba**: el texto oficial solo dice "test button"; confirmarlo en la ficha PDF.
- La foto del R15 "-WTL" muestra la etiqueta "-WT": no sirve como prueba visual del LED.

---

## 10. Sesiones de referencia

Se encuentran con `orca search "Relpol"` o `orca search "riel DIN"`.

| Qué | Agente | Archivo / resume |
|---|---|---|
| Orquestación de la campaña | Claude | `claude --resume edccdf5e-0511-4821-976c-78b1ff4613fd` (desde `/Volumes/ExternoMS/projects/ebc`) |
| v6 (fotos reales, scripts) | Claude | `claude --resume c269eea5-b5f0-46b0-8cd7-8f5bf9cc1597` |
| v1–v5 | Codex | `~/.codex/sessions/2026/11/09/rollout-2026-11-09T20-*` y `T21-05-*` |
| v6 (intento) y fondos | Codex | `~/.codex/sessions/2026/11/10/rollout-2026-11-10T11-28-*` y `T12-07-*` |
| Análisis Meta × CRM (19-nov) | Claude | `claude --resume 6e37dc5a-0e60-403b-85e3-d2c698f7252b` (desde `velo_wa/EBC`) |

Pieza publicada: anuncio `120249541772780280` ("Relpol 6,2mm - producto"), campaña "MS - [Leads] - Relpol LATAM", composición `concepto_07b_hd_r4.png` (P1a + P2 + P4x sobre `fondo_almacen_codex_b.png`).
