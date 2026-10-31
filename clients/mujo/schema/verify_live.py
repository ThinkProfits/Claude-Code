"""Check live JSON-LD on Mujo product pages after a Rank Math schema push.

Usage: python -I verify_live.py <product_id> [...]   (no ids = all titles in titles.json)
Fetches each page with a cache-busting query so WP Rocket serves a fresh render.
"""
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
titles = {str(t["product_id"]): t for t in json.load(open(HERE / "titles.json", encoding="utf-8"))}
ids = sys.argv[1:] or list(titles)

for pid in ids:
    t = titles[pid]
    req = urllib.request.Request(f"{t['url']}?nocache={int(time.time())}", headers={"User-Agent": "Mozilla/5.0 Chrome/120"})
    page = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")
    types, books, isbns, authors, products = [], 0, set(), set(), 0
    for block in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', page, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            types.append("INVALID-JSON")
            continue
        for node in data.get("@graph", [data]):
            ty = node.get("@type")
            types.append(ty if isinstance(ty, str) else "+".join(ty))
            if ty == "Product":
                products += 1
            for v in node.get("hasVariant", []):
                if "Book" in v.get("@type", []):
                    books += 1
                    isbns.add(v.get("isbn"))
                    authors.update(a["name"] for a in v.get("author", []))
    want = len(t["variants"])
    ok = books == want and types.count("ProductGroup") == 1 and products == 0
    print(f"{'OK ' if ok else 'BAD'} {pid} {t['book']}: Book variants {books}/{want}, authors {sorted(authors)}, types {types}")
    time.sleep(1)
