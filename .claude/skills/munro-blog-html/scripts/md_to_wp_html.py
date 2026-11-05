#!/usr/bin/env python3
"""Convert a Munro & Crawford blog draft (.md) into paste-ready WordPress HTML.

Usage:
    python md_to_wp_html.py <draft.md> [<draft2.md> ...]

Writes <draft>-wp-paste.html next to each draft.

Output follows the pattern of the live munrocrawford.ca posts (July 2026 onward):
  - HTML comment block at the top with title tag, meta, slug, author, hero image
  - Post title as <h2> (WordPress prints the real H1 from the Title field)
  - Hero image placeholder comment, then the Quick Answer <blockquote>
  - Section headings as <h2><strong>..</strong></h2>, subsections <h3><strong>..</strong></h3>
  - FAQ questions as <h3><a href="#">Q</a></h3> + answer paragraph
  - Closing "Contact a Lawyer" link
  - FAQPage schema as microdata (NOT a JSON-LD <script>: the site strips anything
    inside square brackets from post content, which empties every JSON-LD array)

Only the article body is converted (from the "# " H1 up to the first "---" rule
after the FAQ). Editor notes, GBP/social posts and implementation notes are skipped.
Non-ASCII characters and typographic quotes are written as numeric HTML entities
so nothing turns into replacement characters when pasted.
"""
import html
import re
import sys
from pathlib import Path

SITE = "munrocrawford.ca"
AUTHOR = "munro_admin"
CONTACT_URL = "https://munrocrawford.ca/contact/"


# ---------------------------------------------------------------- text helpers
def smart_quotes(text: str) -> str:
    """Curl straight quotes in plain text (no markup inside)."""
    text = re.sub(r'(^|[\s(\[{\u2014-])"', "\\1\u201c", text)
    text = text.replace('"', "\u201d")
    text = re.sub(r"(^|[\s(\[{\u2014-])'", "\\1\u2018", text)
    text = text.replace("'", "\u2019")
    return text


def to_entities(text: str) -> str:
    """Escape &<> and turn every non-ASCII char into &#NNNN;."""
    text = html.escape(text, quote=False)
    return "".join(c if ord(c) < 128 else f"&#{ord(c)};" for c in text)


def attr(text: str) -> str:
    return html.escape(text, quote=True)


def is_external(url: str) -> bool:
    return url.startswith("http") and SITE not in url


def inline(md: str) -> str:
    """Convert inline markdown (links, bold, italic) to HTML."""
    out, pos = [], 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)\s]+)\)", md):
        out.append(("text", md[pos:m.start()]))
        out.append(("link", m.group(1), m.group(2)))
        pos = m.end()
    out.append(("text", md[pos:]))

    def fmt(s: str) -> str:
        s = to_entities(smart_quotes(s))
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
        return s

    html_parts = []
    for part in out:
        if part[0] == "text":
            html_parts.append(fmt(part[1]))
        else:
            _, label, url = part
            extra = ' target="_blank" rel="noopener noreferrer"' if is_external(url) else ""
            html_parts.append(f'<a href="{attr(url)}"{extra}>{fmt(label)}</a>')
    return "".join(html_parts)


def plain(md: str) -> str:
    """Markdown to plain text (for comments)."""
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    md = md.replace("**", "").replace("*", "")
    return md.strip()


# ---------------------------------------------------------------- parsing
def meta_value(lines, label):
    for ln in lines:
        m = re.match(rf"\*\*{re.escape(label)}:\*\*\s*(.+)", ln.strip())
        if m:
            return re.sub(r"\s*\(\d+ characters\)\s*$", "", m.group(1)).strip()
    return ""


def parse_image(line):
    m = re.match(r"\[IMAGE:\s*(.+?)\s*\|\s*alt:\s*(.+?)\s*\|\s*file:\s*(.+?)\s*\]$", line.strip())
    return m.groups() if m else None


def convert(md_path: Path) -> str:
    lines = md_path.read_text(encoding="utf-8").splitlines()

    title_tag = meta_value(lines, "Title tag")
    meta_desc = meta_value(lines, "Meta description")
    slug = meta_value(lines, "URL slug").strip("/").split("/")[-1]

    start = next(i for i, ln in enumerate(lines) if ln.startswith("# "))
    end = len(lines)
    seen_faq = False
    for i in range(start, len(lines)):
        if re.match(r"^##\s+(Frequently Asked Questions|FAQ)", lines[i], re.I):
            seen_faq = True
        if seen_faq and lines[i].strip() == "---":
            end = i
            break
    body = lines[start:end]

    images = [parse_image(ln) for ln in body if parse_image(ln)]
    hero = images[0] if images else None

    out = []
    comment = [
        f"Title tag: {title_tag}",
        f"Meta description: {meta_desc}",
        f"URL slug: {slug}",
        f"Author (WordPress): {AUTHOR}",
    ]
    if hero:
        comment += [f"Featured / hero image: {hero[2]}", f"Hero alt text: {hero[1]}"]
    comment.append("(Set title/meta/slug/author/featured image in the WordPress and Yoast "
                   "fields. This comment block is not part of the post body.)")
    def safe(s):  # for text inside HTML comments: no &amp;, no "--"
        s = "".join(c if ord(c) < 128 else f"&#{ord(c)};" for c in s)
        return s.replace("--", "&#8211;").replace(">", "&gt;")
    out.append("<!--\n" + "\n".join(safe(c) for c in comment) + "\n-->")

    faq = []            # (question, answer_html_list)
    in_faq = False
    para, list_items, table_rows = [], [], []
    hero_done = False

    def flush_para():
        if para:
            text = " ".join(s.strip() for s in para)
            if in_faq and faq:
                faq[-1][1].append(f"<p>{inline(text)}</p>")
            else:
                out.append(f"<p>{inline(text)}</p>")
            para.clear()

    def flush_list():
        if list_items:
            items = "\n".join(f"<li>{inline(t)}</li>" for t in list_items)
            out.append(f"<ul>\n{items}\n</ul>")
            list_items.clear()

    def flush_table():
        if table_rows:
            rows = [r for r in table_rows if not re.match(r"^\|?\s*:?-{3,}", r)]
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            head, rest = cells[0], cells[1:]
            th = "".join(f"<th>{inline(c)}</th>" for c in head)
            trs = "\n".join(
                "<tr>" + "".join(
                    (f"<td><strong>{inline(c)}</strong></td>" if j == 0 else f"<td>{inline(c)}</td>")
                    for j, c in enumerate(r)) + "</tr>"
                for r in rest)
            out.append(f"<table>\n<thead>\n<tr>{th}</tr>\n</thead>\n<tbody>\n{trs}\n</tbody>\n</table>")
            table_rows.clear()

    def flush_all():
        flush_para(); flush_list(); flush_table()

    for ln in body:
        s = ln.rstrip()
        if not s.strip():
            flush_all()
            continue
        if s.startswith("# "):
            flush_all()
            out.append(f"<h2>{inline(s[2:].strip())}</h2>")
            if hero:
                out.append(f"<p><!-- Insert hero image here: {safe(hero[2])} --></p>")
            continue
        img = parse_image(s)
        if img:
            flush_all()
            if img is hero or (hero and img == hero and not hero_done):
                hero_done = True
                continue
            desc, alt, fname = img
            out.append(f"<p><!-- Insert image here: {safe(fname)} | alt: {safe(alt)} | "
                       f"shows: {safe(desc)} --></p>")
            continue
        if s.startswith("## "):
            flush_all()
            heading = s[3:].strip()
            in_faq = bool(re.match(r"(Frequently Asked Questions|FAQ)", heading, re.I))
            out.append(f"<h2><strong>{inline(heading)}</strong></h2>")
            continue
        if s.startswith("### "):
            flush_all()
            heading = s[4:].strip()
            if in_faq:
                faq.append((heading, []))
                out.append(("FAQ", len(faq) - 1))
            else:
                out.append(f"<h3><strong>{inline(heading)}</strong></h3>")
            continue
        if s.startswith(">"):
            flush_all()
            out.append(f"<blockquote><p>{inline(s.lstrip('> ').strip())}</p></blockquote>")
            continue
        if s.lstrip().startswith("|"):
            flush_para(); flush_list()
            table_rows.append(s.strip())
            continue
        if re.match(r"^\s*[-*]\s+", s):
            flush_para(); flush_table()
            list_items.append(re.sub(r"^\s*[-*]\s+", "", s))
            continue
        para.append(s)
    flush_all()

    # FAQ block with microdata (survives the site's square-bracket stripping)
    final = []
    faq_open = False
    for item in out:
        if isinstance(item, tuple):
            q, answers = faq[item[1]]
            if not faq_open:
                final.append('<div itemscope itemtype="https://schema.org/FAQPage">')
                faq_open = True
            final.append(
                '<div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question">\n'
                f'<h3 itemprop="name"><a href="#">{inline(q)}</a></h3>\n'
                '<div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">\n'
                '<div itemprop="text">\n' + "\n".join(answers) + "\n</div>\n</div>\n</div>")
        else:
            final.append(item)
    if faq_open:
        final.append("</div>")
    final.append(f'<p><a href="{CONTACT_URL}">Contact a Lawyer</a></p>')
    return "\n".join(final) + "\n"


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    for p in argv:
        src = Path(p)
        dst = src.with_name(src.stem + "-wp-paste.html")
        dst.write_text(convert(src), encoding="ascii")
        print(f"wrote {dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
