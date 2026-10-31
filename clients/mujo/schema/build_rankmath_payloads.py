"""Turn build_schema.py's ProductGroup graphs into Rank Math custom-schema payloads.

Reusable: after refresh_titles.py and build_schema.py, run  python -I build_rankmath_payloads.py.
Writes rankmath-payloads.json: {product_id: body for POST /rankmath/v1/updateSchemas}.
Each body saves one primary custom ProductGroup schema, which replaces Rank Math's default
WooCommerceProduct output on that product. Prices are copied in, so re-run and re-push after
any WooCommerce price or variant change.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
from build_schema import graph  # noqa: E402 (also rebuilds the .html files)

payloads = {}
for t in json.load(open(HERE / "titles.json", encoding="utf-8")):
    node = graph(t)["@graph"][0]
    node["metadata"] = {"title": "ProductGroup", "type": "custom", "isPrimary": True}
    payloads[t["product_id"]] = {"objectType": "post", "objectID": t["product_id"], "schemas": {"new-1": node}}
json.dump(payloads, open(HERE / "rankmath-payloads.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"wrote {len(payloads)} payloads")
