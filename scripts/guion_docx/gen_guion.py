#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el Guion de llamada SDR EBC v2.0 en .docx (clonando la estetica del
docx de EBL) y en .md (fuente versionable para el repo)."""

import html
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "tpl")
BUILD = os.path.join(HERE, "build")

# La estetica (styles.xml, tema, numeracion) se hereda del docx de EBL. Si la
# plantilla no esta desempacada, se desempaca desde tmp/.
if not os.path.isdir(TPL):
    import zipfile
    cand = os.environ.get("GUION_TPL_DOCX") or os.path.join(
        HERE, "..", "..", "tmp", "Guion_SPIN_Variadores_EBL.docx")
    cand = os.path.abspath(cand)
    if not os.path.exists(cand):
        raise SystemExit("No se encuentra la plantilla docx: %s "
                         "(definir GUION_TPL_DOCX)" % cand)
    os.makedirs(TPL, exist_ok=True)
    with zipfile.ZipFile(cand) as z:
        for n in z.namelist():
            if n.startswith("/") or ".." in n.split("/"):
                continue
            z.extract(n, TPL)

NAVY = "1b3a6b"
BLUE = "2e6db4"
GRAY = "6b7280"
GRAYBG = "f2f4f7"
BORDER = "d1d5db"
AMBER = "b45a00"
GREEN = "166534"
TEAL, TEALBG = "1a7a6e", "e6f4f2"
PURPLE, PURPLEBG = "5b3a8f", "ede6f7"
MAGENTA, MAGENTABG = "8f3a7a", "f7e6f4"
AMBERBG = "fbeedd"
BLUEBG = "eaf1fa"
WIDTH = 9360

body = []   # XML del cuerpo
md = []     # version markdown


def esc(t):
    return html.escape(str(t), quote=False).replace('"', "&quot;")


# ---------------------------------------------------------------- runs / paras
def run(text, bold=False, italic=False, color=None, size=22, font="Arial"):
    rpr = ['<w:rFonts w:ascii="%s" w:cs="%s" w:eastAsia="%s" w:hAnsi="%s"/>' % (font, font, font, font)]
    if bold:
        rpr.append('<w:b w:val="1"/><w:bCs w:val="1"/>')
    if italic:
        rpr.append('<w:i w:val="1"/><w:iCs w:val="1"/>')
    if color:
        rpr.append('<w:color w:val="%s"/>' % color)
    rpr.append('<w:sz w:val="%d"/><w:szCs w:val="%d"/>' % (size, size))
    rpr.append('<w:rtl w:val="0"/>')
    return ('<w:r><w:rPr>%s</w:rPr><w:t xml:space="preserve">%s</w:t></w:r>'
            % ("".join(rpr), esc(text)))


def para_xml(runs, style=None, jc=None, after=80, before=80, ind=None,
             pbdr=None, num=False, keep=False):
    ppr = []
    if style:
        ppr.append('<w:pStyle w:val="%s"/>' % style)
    if keep:
        ppr.append('<w:keepNext w:val="1"/><w:keepLines w:val="1"/>')
    if num:
        ppr.append('<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>')
    if pbdr:
        ppr.append(pbdr)
    ppr.append('<w:spacing w:after="%d" w:before="%d" w:lineRule="auto"/>' % (after, before))
    if ind:
        ppr.append(ind)
    if jc:
        ppr.append('<w:jc w:val="%s"/>' % jc)
    return "<w:p><w:pPr>%s</w:pPr>%s</w:p>" % ("".join(ppr), runs)


# ---------------------------------------------------------------- bloques API
def h1(text, md_too=True):
    body.append(para_xml(run(text, bold=True, color=NAVY, size=36),
                         style="Heading1", after=120, before=360, keep=True))
    if md_too:
        md.append("\n# %s\n" % text)


def h2(text, color=NAVY):
    body.append(para_xml(run(text, bold=True, color=color, size=28),
                         style="Heading2", after=100, before=280, keep=True))
    md.append("\n## %s\n" % text)


def h3(text, color=NAVY):
    body.append(para_xml(run(text, bold=True, color=color, size=24),
                         style="Heading3", after=60, before=200, keep=True))
    md.append("\n### %s\n" % text)


def para(text, size=22, color=None, bold=False, md_prefix=""):
    body.append(para_xml(run(text, size=size, color=color, bold=bold)))
    md.append(md_prefix + text + "\n")


def rich(parts):
    """parts: lista de (texto, dict de formato)"""
    body.append(para_xml("".join(run(t, **k) for t, k in parts)))
    out = []
    for t, k in parts:
        if k.get("bold"):
            core = t.rstrip()
            out.append("**%s**%s" % (core, t[len(core):]))
        else:
            out.append(t)
    md.append("".join(out) + "\n")


QBDR = '<w:pBdr><w:left w:color="%s" w:space="12" w:sz="12" w:val="single"/></w:pBdr>' % BLUE
QIND = '<w:ind w:left="560" w:firstLine="0"/>'


def quote(text):
    """Linea que se dice casi literal."""
    body.append(para_xml(run(text, italic=True, color=NAVY),
                         after=100, before=100, ind=QIND, pbdr=QBDR))
    md.append("\n> *%s*\n" % text)


def pin(text):
    body.append(para_xml(run("\U0001F4CC ", size=20) + run(text, color=GRAY, size=20)))
    md.append("\n\U0001F4CC %s\n" % text)


def bullet(text, bold_head=None):
    runs = ""
    if bold_head:
        runs += run(bold_head, bold=True)
    runs += run(text)
    body.append(para_xml(runs, num=True, after=60, before=60,
                         ind='<w:ind w:left="560" w:right="0" w:hanging="280"/>'))
    md.append("- %s%s" % ("**%s**" % bold_head if bold_head else "", text) + "\n")


def spacer(h=100):
    body.append(para_xml("", after=0, before=h))


def pagebreak():
    body.append('<w:p><w:pPr><w:spacing w:after="0" w:before="0"/></w:pPr>'
                '<w:r><w:br w:type="page"/></w:r></w:p>')
    md.append("\n---\n")


# ---------------------------------------------------------------- tablas
def _cell(spec, width, default_fill=None):
    if not isinstance(spec, dict):
        spec = {"text": spec}
    fill = spec.get("fill", default_fill)
    runs = spec.get("runs")
    if runs is None:
        runs = run(spec.get("text", ""), bold=spec.get("bold", False),
                   italic=spec.get("italic", False),
                   color=spec.get("color"), size=spec.get("size", 21))
    tcpr = ['<w:tcW w:w="%d" w:type="dxa"/>' % width]
    if spec.get("span"):
        tcpr.append('<w:gridSpan w:val="%d"/>' % spec["span"])
    tcpr.append('<w:tcBorders>'
                '<w:top w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
                '<w:left w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
                '<w:bottom w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
                '<w:right w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
                '</w:tcBorders>' % (BORDER, BORDER, BORDER, BORDER))
    if fill:
        tcpr.append('<w:shd w:fill="%s" w:val="clear"/>' % fill)
    tcpr.append('<w:tcMar><w:top w:w="100.0" w:type="dxa"/><w:left w:w="140.0" w:type="dxa"/>'
                '<w:bottom w:w="100.0" w:type="dxa"/><w:right w:w="140.0" w:type="dxa"/></w:tcMar>')
    tcpr.append('<w:vAlign w:val="center"/>')
    jc = spec.get("jc")
    paras = spec.get("paras")
    if paras:
        inner = "".join(para_xml(run(t, size=spec.get("size", 21),
                                     bold=spec.get("bold", False),
                                     italic=spec.get("italic", False),
                                     color=spec.get("color")),
                                 after=40, before=40,
                                 jc=jc) for t in paras)
    else:
        inner = para_xml(runs, after=20, before=20, jc=jc)
    return "<w:tc><w:tcPr>%s</w:tcPr>%s</w:tc>" % ("".join(tcpr), inner)


def table(rows, widths, header=True, md_table=True):
    tot = sum(widths)
    grid = "".join('<w:gridCol w:w="%d"/>' % w for w in widths)
    xml = ['<w:tbl><w:tblPr><w:tblStyle w:val="Table1"/>'
           '<w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="left"/>'
           '<w:tblBorders>'
           '<w:top w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:left w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:bottom w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:right w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:insideH w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:insideV w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '</w:tblBorders><w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr>'
           '<w:tblGrid>%s</w:tblGrid>' % (tot, BORDER, BORDER, BORDER, BORDER,
                                          BORDER, BORDER, grid)]
    for ri, row in enumerate(rows):
        is_head = header and ri == 0
        trpr = '<w:trPr><w:cantSplit w:val="0"/><w:tblHeader w:val="%d"/></w:trPr>' % (1 if is_head else 0)
        cells = []
        wi = 0
        for spec in row:
            span = spec.get("span", 1) if isinstance(spec, dict) else 1
            w = sum(widths[wi:wi + span])
            wi += span
            if is_head:
                if not isinstance(spec, dict):
                    spec = {"text": spec}
                spec = dict(spec)
                spec.setdefault("bold", True)
                spec.setdefault("color", NAVY)
                spec.setdefault("fill", GRAYBG)
            cells.append(_cell(spec, w))
        xml.append("<w:tr>%s%s</w:tr>" % (trpr, "".join(cells)))
    xml.append("</w:tbl>")
    body.append("".join(xml))
    body.append(para_xml("", after=0, before=100))

    if md_table:
        md.append("")
        for ri, row in enumerate(rows):
            vals = []
            for spec in row:
                if isinstance(spec, dict):
                    t = " · ".join(spec.get("paras")) if spec.get("paras") else spec.get("text", "")
                else:
                    t = spec
                vals.append(str(t).replace("|", "/"))
            md.append("| " + " | ".join(vals) + " |")
            if header and ri == 0:
                md.append("|" + "---|" * len(vals))
        md.append("")


def banner(title, sub1=None, sub2=None, tag=None, md_title=True):
    paras = [para_xml(run(title, bold=True, color="ffffff", size=52), jc="center",
                      after=0, before=0)]
    if sub1:
        paras.append(para_xml(run(sub1, color="a8c4e8", size=30), jc="center",
                              after=0, before=120))
    if sub2:
        paras.append(para_xml(run(sub2, color="7aadd4", size=24), jc="center",
                              after=0, before=80))
    if tag:
        paras.append(para_xml(run(tag, color="7aadd4", size=20), jc="center",
                              after=0, before=160))
    tc = ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/><w:tcBorders>'
          '<w:top w:color="000000" w:space="0" w:sz="0" w:val="nil"/>'
          '<w:left w:color="000000" w:space="0" w:sz="0" w:val="nil"/>'
          '<w:bottom w:color="000000" w:space="0" w:sz="0" w:val="nil"/>'
          '<w:right w:color="000000" w:space="0" w:sz="0" w:val="nil"/></w:tcBorders>'
          '<w:shd w:fill="%s" w:val="clear"/>'
          '<w:tcMar><w:top w:w="400.0" w:type="dxa"/><w:left w:w="400.0" w:type="dxa"/>'
          '<w:bottom w:w="400.0" w:type="dxa"/><w:right w:w="400.0" w:type="dxa"/></w:tcMar>'
          '<w:vAlign w:val="center"/></w:tcPr>%s</w:tc>' % (WIDTH, NAVY, "".join(paras)))
    body.append('<w:tbl><w:tblPr><w:tblStyle w:val="Table1"/>'
                '<w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="left"/>'
                '<w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr>'
                '<w:tblGrid><w:gridCol w:w="%d"/></w:tblGrid>'
                '<w:tr><w:trPr><w:cantSplit w:val="0"/></w:trPr>%s</w:tr></w:tbl>'
                % (WIDTH, WIDTH, tc))
    body.append(para_xml("", after=0, before=200))
    if md_title:
        md.append("# %s\n" % title)
    if sub1:
        md.append("*%s*" % sub1)
    if sub2:
        md.append("*%s*" % sub2)
    if tag:
        md.append("\n%s\n" % tag)


def section_banner(label, title, desc, color, fill):
    """Franja de seccion a color (vias y perfiles)."""
    paras = [para_xml(run(label, bold=True, color="ffffff", size=20), after=0, before=0)]
    tc1 = ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/><w:tcBorders>'
           '<w:top w:color="%s" w:space="0" w:sz="0" w:val="nil"/>'
           '<w:left w:color="%s" w:space="0" w:sz="0" w:val="nil"/>'
           '<w:bottom w:color="%s" w:space="0" w:sz="0" w:val="nil"/>'
           '<w:right w:color="%s" w:space="0" w:sz="0" w:val="nil"/></w:tcBorders>'
           '<w:shd w:fill="%s" w:val="clear"/>'
           '<w:tcMar><w:top w:w="140.0" w:type="dxa"/><w:left w:w="200.0" w:type="dxa"/>'
           '<w:bottom w:w="140.0" w:type="dxa"/><w:right w:w="200.0" w:type="dxa"/></w:tcMar>'
           '<w:vAlign w:val="center"/></w:tcPr>%s</w:tc>'
           % (WIDTH, color, color, color, color, color, "".join(paras)))
    inner = [para_xml(run(title, bold=True, color=color, size=30), after=0, before=0)]
    if desc:
        inner.append(para_xml(run(desc, color="333333", size=21), after=0, before=100))
    tc2 = ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/><w:tcBorders>'
           '<w:top w:color="%s" w:space="0" w:sz="0" w:val="nil"/>'
           '<w:left w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:bottom w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
           '<w:right w:color="%s" w:space="0" w:sz="4" w:val="single"/></w:tcBorders>'
           '<w:shd w:fill="%s" w:val="clear"/>'
           '<w:tcMar><w:top w:w="200.0" w:type="dxa"/><w:left w:w="200.0" w:type="dxa"/>'
           '<w:bottom w:w="200.0" w:type="dxa"/><w:right w:w="200.0" w:type="dxa"/></w:tcMar>'
           '</w:tcPr>%s</w:tc>' % (WIDTH, color, BORDER, BORDER, BORDER, fill, "".join(inner)))
    body.append('<w:tbl><w:tblPr><w:tblStyle w:val="Table1"/>'
                '<w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="left"/>'
                '<w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr>'
                '<w:tblGrid><w:gridCol w:w="%d"/></w:tblGrid>'
                '<w:tr><w:trPr><w:cantSplit w:val="1"/></w:trPr>%s</w:tr>'
                '<w:tr><w:trPr><w:cantSplit w:val="0"/></w:trPr>%s</w:tr></w:tbl>'
                % (WIDTH, WIDTH, tc1, tc2))
    body.append(para_xml("", after=0, before=160))
    md.append("\n# %s — %s\n" % (label, title))
    if desc:
        md.append("*%s*\n" % desc)


def box(lines, title=None, fill=GRAYBG, color=NAVY):
    inner = []
    if title:
        inner.append(para_xml(run(title, bold=True, color=color, size=22), after=80, before=0))
    for ln in lines:
        inner.append(para_xml(run("•  ", color=color, size=21) + run(ln, size=21),
                              after=40, before=40,
                              ind='<w:ind w:left="300" w:hanging="300"/>'))
    tc = ('<w:tc><w:tcPr><w:tcW w:w="%d" w:type="dxa"/><w:tcBorders>'
          '<w:top w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
          '<w:left w:color="%s" w:space="0" w:sz="12" w:val="single"/>'
          '<w:bottom w:color="%s" w:space="0" w:sz="4" w:val="single"/>'
          '<w:right w:color="%s" w:space="0" w:sz="4" w:val="single"/></w:tcBorders>'
          '<w:shd w:fill="%s" w:val="clear"/>'
          '<w:tcMar><w:top w:w="200.0" w:type="dxa"/><w:left w:w="240.0" w:type="dxa"/>'
          '<w:bottom w:w="200.0" w:type="dxa"/><w:right w:w="240.0" w:type="dxa"/></w:tcMar>'
          '</w:tcPr>%s</w:tc>' % (WIDTH, BORDER, color, BORDER, BORDER, fill, "".join(inner)))
    body.append('<w:tbl><w:tblPr><w:tblStyle w:val="Table1"/>'
                '<w:tblW w:w="%d" w:type="dxa"/><w:jc w:val="left"/>'
                '<w:tblLayout w:type="fixed"/><w:tblLook w:val="0000"/></w:tblPr>'
                '<w:tblGrid><w:gridCol w:w="%d"/></w:tblGrid>'
                '<w:tr><w:trPr><w:cantSplit w:val="0"/></w:trPr>%s</w:tr></w:tbl>'
                % (WIDTH, WIDTH, tc))
    body.append(para_xml("", after=0, before=120))
    if title:
        md.append("\n**%s**\n" % title)
    for ln in lines:
        md.append("- %s" % ln)
    md.append("")


def checklist(rows, color=GREEN):
    """Filas con check verde."""
    out = []
    for r in rows:
        out.append([{"runs": run("✓  ", bold=True, color=color, size=21) + run(r, size=21)}])
    table(out, [WIDTH], header=False, md_table=False)
    for r in rows:
        md.append("- ✓ %s" % r)
    md.append("")
