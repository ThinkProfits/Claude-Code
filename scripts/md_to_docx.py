"""Convert a blog-draft markdown file into a .docx for client review.

Reusable for any client draft written by the agency-blog-writer skill.
Handles headings (#..####), paragraphs, bullet and numbered lists,
blockquotes, **bold**, *italic*, [links](url) as real hyperlinks,
horizontal rules and simple pipe tables.

Usage: python scripts/md_to_docx.py draft.md [more.md ...]
Writes draft.docx next to each input.
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s][^*]*\*|\[[^\]]+\]\([^)]+\))")


def add_hyperlink(par, text, url):
    part = par.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "005394")
    underline = OxmlElement("w:u")
    underline.set(qn("w:val"), "single")
    rpr.append(color)
    rpr.append(underline)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    par._p.append(link)


def add_inline(par, text):
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**"):
            par.add_run(piece[2:-2]).bold = True
        elif piece.startswith("[") and "](" in piece:
            label, url = re.match(r"\[([^\]]+)\]\(([^)]+)\)", piece).groups()
            add_hyperlink(par, label, url)
        elif piece.startswith("*") and piece.endswith("*") and len(piece) > 2:
            par.add_run(piece[1:-1]).italic = True
        else:
            par.add_run(piece)


def convert(md_path):
    md_path = Path(md_path)
    doc = Document()
    doc.styles["Normal"].font.name = "Arial"
    doc.styles["Normal"].font.size = Pt(11)
    lines = md_path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        s = line.strip()
        if not s:
            i += 1
            continue
        if re.fullmatch(r"-{3,}|\*{3,}|_{3,}", s):
            doc.add_paragraph("_" * 40)
        elif s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-+:?", c) for c in cells):
                    rows.append(cells)
                i += 1
            table = doc.add_table(rows=len(rows), cols=max(len(r) for r in rows))
            table.style = "Table Grid"
            for r, cells in enumerate(rows):
                for c, val in enumerate(cells):
                    p = table.cell(r, c).paragraphs[0]
                    add_inline(p, val)
                    if r == 0:
                        for run in p.runs:
                            run.bold = True
            continue
        elif m := re.match(r"(#{1,4})\s+(.*)", s):
            level = len(m.group(1))
            h = doc.add_heading(level=level)
            add_inline(h, m.group(2))
        elif s.startswith(">"):
            p = doc.add_paragraph(style="Intense Quote")
            add_inline(p, s.lstrip("> ").strip())
        elif m := re.match(r"[-*+]\s+(.*)", s):
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, m.group(1))
        elif m := re.match(r"\d+[.)]\s+(.*)", s):
            p = doc.add_paragraph(style="List Number")
            add_inline(p, m.group(1))
        elif s.startswith("[IMAGE"):
            p = doc.add_paragraph()
            run = p.add_run(s)
            run.italic = True
            run.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
            run.font.highlight_color = WD_COLOR_INDEX.YELLOW
        else:
            p = doc.add_paragraph()
            add_inline(p, s)
        i += 1
    out = md_path.with_suffix(".docx")
    doc.save(out)
    return out


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        print(convert(arg))
