"""Replay the Make test blueprint's regex chain locally against the real Doc export.

Reads patterns straight from spiedr-test-blueprint.json so the check uses exactly what Make runs.
JS -> Python differences handled: (?<name>) -> (?P<name>), $1 -> \\1, {{emptystring}} -> "".
"""
import base64, json, re, sys

src, bp_path, out_path = sys.argv[1:4]
raw = json.load(open(src, encoding="utf-8"))["content"]
html = base64.b64decode(raw).decode("utf-8")
flow = json.load(open(bp_path, encoding="utf-8"))["flow"]

text = html
parsed = {}
for m in flow[1:]:
    mp = m.get("mapper", {})
    if m["module"] == "regexp:Replace":
        if m["id"] == 24:
            text = parsed["faq"]
        flags = re.S | (0 if mp["sensitive"] else re.I)
        value = mp["value"].replace("{{emptystring}}", "")
        value = re.sub(r"\$(\d)", r"\\\1", value)
        text = re.sub(mp["pattern"], value, text, count=0 if mp["global"] else 1, flags=flags)
        if m["id"] == 24:
            parsed["faq_out"] = text
    elif m["module"] == "regexp:Parser":
        p = m["parameters"]["pattern"].replace("(?<", "(?P<")
        mm = re.match(p, text, re.S | re.I)
        if not mm:
            sys.exit("FAQ parser found no match (Make would stop here)")
        parsed = {k: (v or "") for k, v in mm.groupdict().items()}
    elif m["module"] == "util:ComposeTransformer":
        text = parsed["before"] + '<section class="blog-faq">' + parsed["heading"] + parsed["faq_out"] + "</section>" + parsed["after"]

open(out_path, "w", encoding="utf-8").write(text)
print("google.com/url left:", text.count("google.com/url"))
print("empty anchors left:", len(re.findall(r"<a[^>]*>(?:\s|&nbsp;|\xa0)*</a>", text)))
print("empty headings left:", len(re.findall(r"<h([1-6])>(?:\s|&nbsp;|\xa0)*</h\1>", text)))
print("%23 left:", text.count("%23"))
print("links:", len(re.findall(r"<a href=", text)))
for h in re.findall(r'href="([^"]*)"', text):
    print("  ", h)
print("quick answer:", text[:text.find("</table>") + 8] if "<table>" in text else "NOT CONVERTED")
print("FAQ details:", text.count("<details"))
