"""Build ProductGroup + Product/Book JSON-LD for every Mujo textbook (higher ed and high school CTE).

Reusable: run  python -I refresh_titles.py  (pulls live data into titles.json), then
python -I build_schema.py. Writes one <slug>.html per title (paste into Rich Results Test >
Code) plus all-titles.html.

Pattern: ProductGroup with variants typed ["Product", "Book"], tested in Rich Results Test
2026-10-08 (see memory/mujo-context.md). The Organization node is not repeated here: Rank
Math already outputs it on every page, so publisher points at its @id. Fix the org name to
"Mujo Learning Systems" (legalName "... Inc.") as part of the Organization merge task.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
ORG = "https://www.mujo.com/#organization"


def variant(t, v):
    node = {
        "@type": ["Product", "Book"],
        "@id": f"{t['url']}#{v['sku'].replace(' ', '-')}",
        "name": f"{t['book']} - {v['label']}",
        "description": f"{v['label']} of {t['book']}, published by Mujo Learning Systems.",
        "sku": v["sku"],
        "gtin13": v["isbn"],
        "isbn": v["isbn"],
        "bookFormat": f"https://schema.org/{v['format']}",
        "inLanguage": "en-US",
        "author": [{"@type": "Person", "name": a} for a in t["authors"]],
        "publisher": {"@id": ORG},
        "image": v["img"],
        "offers": {
            "@type": "Offer",
            "price": v["price"],
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "itemCondition": "https://schema.org/NewCondition",
            "priceValidUntil": "2027-12-31",
            "url": v["url"],
        },
    }
    if t["edition"]:
        node["bookEdition"] = t["edition"]
    return node


def graph(t):
    return {
        "@context": "https://schema.org",
        "@graph": [{
            "@type": "ProductGroup",
            "@id": f"{t['url']}#richSnippet",
            "name": t["name"],
            "description": t["desc"],
            "url": t["url"],
            "sku": t["sku"],
            "productGroupID": t["sku"],
            "brand": {"@type": "Brand", "name": "Mujo Learning Systems"},
            "category": t["category"],
            "image": t["img"],
            "hasVariant": [variant(t, v) for v in t["variants"]],
        }],
    }


def block(t):
    head = f"<!-- {t['book']} | {', '.join(t['authors'])} | {t['url']}"
    if t["notes"]:
        head += f"\n     Note: {t['notes']}"
    body = json.dumps(graph(t), indent=2, ensure_ascii=False)
    return f"{head} -->\n<script type=\"application/ld+json\">\n{body}\n</script>\n"


def slug(t):
    return t["url"].rstrip("/").split("/")[-1]


titles = json.load(open(HERE / "titles.json", encoding="utf-8"))
for t in titles:
    (HERE / f"{slug(t)}.html").write_text(block(t), encoding="utf-8")
(HERE / "all-titles.html").write_text("\n".join(block(t) for t in titles), encoding="utf-8")
print(f"wrote {len(titles)} titles")
