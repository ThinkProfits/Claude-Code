"""Build Product + Book JSON-LD for Mujo higher-ed textbooks.

Reusable: add a title to titles.json (from the live Rank Math ProductGroup output and the
VitalSource author lookup), then run:  python -I build_schema.py
Writes one <slug>.html per title (paste into Rich Results Test > Code) and all-titles.html.
Pattern tested in Rich Results Test 2026-10-08 (see memory/mujo-context.md).
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
BASE = "https://www.mujo.com/shop/higher-ed/"
ORG = "https://www.mujo.com/#organization"

EDITIONS = {
    "sm": ("Student Edition", "for-students", "119",
           "Student edition of the {book} textbook. Instant digital access via VitalSource."),
    "tm": ("Instructor Edition", "for-instructors", "0",
           "Instructor edition of the {book} textbook, for adopting faculty. Instant digital access via VitalSource."),
}


def variant(t, key):
    sku, isbn, img = t[key]
    label, edition, price, desc = EDITIONS[key]
    url = BASE + t["slug"] + "/"
    return {
        "@type": ["Product", "Book"],
        "@id": f"{url}#{sku}",
        "name": f"{t['book']}: {label} (eBook)",
        "description": desc.format(book=t["book"]),
        "sku": sku,
        "gtin13": isbn,
        "isbn": isbn,
        "bookFormat": "https://schema.org/EBook",
        "bookEdition": "1st edition",
        "inLanguage": "en-US",
        "author": [{"@type": "Person", "name": a} for a in t["authors"]],
        "publisher": {"@id": ORG},
        "image": img,
        "offers": {
            "@type": "Offer",
            "price": price,
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock",
            "itemCondition": "https://schema.org/NewCondition",
            "priceValidUntil": "2027-12-31",
            "url": f"{url}?attribute_pa_book-format=electronic-vital-source&attribute_pa_textbook-edition={edition}",
        },
    }


def graph(t):
    url = BASE + t["slug"] + "/"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "Organization", "@id": ORG, "name": "Mujo Learning Systems Inc.", "url": "https://www.mujo.com"},
            {
                "@type": "ProductGroup",
                "@id": f"{url}#richSnippet",
                "name": t["name"],
                "description": t["desc"],
                "url": url,
                "sku": t["sku"],
                "productGroupID": t["sku"],
                "brand": {"@type": "Brand", "name": "Mujo Learning Systems"},
                "category": "Higher Ed Textbooks, eBooks and Courseware for Universities & Colleges",
                "image": t["img"],
                "hasVariant": [variant(t, "sm"), variant(t, "tm")],
            },
        ],
    }


def block(t):
    head = f"<!-- {t['book']} | {', '.join(t['authors'])} | {BASE}{t['slug']}/"
    if t["notes"]:
        head += f"\n     Note: {t['notes']}"
    body = json.dumps(graph(t), indent=2, ensure_ascii=False)
    return f"{head} -->\n<script type=\"application/ld+json\">\n{body}\n</script>\n"


titles = json.load(open(HERE / "titles.json", encoding="utf-8"))
for t in titles:
    (HERE / f"{t['slug']}.html").write_text(block(t), encoding="utf-8")
(HERE / "all-titles.html").write_text("\n".join(block(t) for t in titles), encoding="utf-8")
print(f"wrote {len(titles)} titles")
