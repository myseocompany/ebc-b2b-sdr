# Generador — Guion de llamada SDR (EBC)

Reconstruye `tmp/scripts/Guion_Llamada_SDR_EBC_v2.docx` y `progress/guion_llamada_sdr_ebc_v2.md`
a partir de un único contenido fuente.

- `gen_guion.py` — componentes de maquetación (portada, franjas de sección, tablas, citas,
  notas 📌, cajas, checklists). Hereda estilos, tema y numeración del docx de EBL
  (`tmp/Guion_SPIN_Variadores_EBL.docx`), que se desempaca solo la primera vez.
- `content_guion.py` — el contenido del guion. Es el archivo que se edita.

```bash
python3 scripts/guion_docx/content_guion.py \
  tmp/scripts/Guion_Llamada_SDR_EBC_v2.docx \
  progress/guion_llamada_sdr_ebc_v2.md
```

El `.md` queda versionado en el repo; el `.docx` vive en `tmp/` (gitignored) porque es el
entregable que se comparte con EBC.
