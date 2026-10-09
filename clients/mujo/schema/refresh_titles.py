"""Rebuild titles.json for all Mujo textbooks from the live site.

Reusable: run  python -I refresh_titles.py  whenever prices, ISBNs or variants change in
WooCommerce, then  python -I build_schema.py  to regenerate the JSON-LD.

Sources:
- Live Rank Math ProductGroup JSON-LD on each product page (SKUs, GTIN/ISBNs, prices,
  variant URLs and images).
- ../authors-sheet/authors-final.json (authors confirmed by Brittni, 2026-10-09).
- BOOKS below: official book titles (VitalSource where listed), editions and clean
  descriptions (sales lines like "Order now!" removed; site copy is US English).
"""
import html
import json
import re
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
AUTHORS = HERE.parent / "authors-sheet" / "authors-final.json"

HE_CAT = "Higher Ed Textbooks, eBooks and Courseware for Universities & Colleges"
HS_CAT = "High School CTE Textbooks & Courseware"

# product_id: (book title, edition or None, description)
BOOKS = {
    # Higher ed
    30219: ("AI Literacy for Healthcare", "1st edition", "Mujo's AI Literacy for Healthcare textbook prepares higher education students to use, evaluate, and govern AI tools in clinical and administrative healthcare settings. Covers AI fundamentals, platform use, ethics, HIPAA compliance, health data interpretation, and prompting."),
    27293: ("Artificial Intelligence Business Analytics", "1st edition", "Mujo's AI Business Analytics textbook introduces higher education students to big data and AI technologies for collecting, managing, and analyzing business data. Turn data into actionable insights."),
    27289: ("Artificial Intelligence Accounting Principles", "1st edition", "Mujo's AI Accounting Principles textbook teaches higher education students how artificial intelligence is transforming accounting practices. Covers AI-powered auditing, automation, data analysis, and ethical considerations."),
    27286: ("Artificial Intelligence Sales Fundamentals", "1st edition", "Mujo's AI Sales Fundamentals textbook teaches higher education students to leverage artificial intelligence across the full sales cycle. Covers AI-powered prospecting, CRM automation, and predictive analytics."),
    27283: ("Artificial Intelligence Project Management", "1st edition", "In this AI Project Management textbook, students will learn strategies and tactics that leverage AI-powered tools and platforms to more effectively manage projects."),
    27278: ("Artificial Intelligence Literacy", "1st edition", "Build AI literacy with Mujo's higher education AI textbook. Covers prompt engineering, machine learning, LLM providers, data privacy, and real-world applications of AI tools for content creation and analysis."),
    27275: ("Artificial Intelligence and Human Resource Management", "1st edition", "Discover how AI is transforming HR management with Mujo's higher education textbook. Covers AI-powered recruitment, talent management, workforce analytics, and employee engagement strategies."),
    27271: ("Artificial Intelligence for Entrepreneurs", "1st edition", "Mujo's AI for Entrepreneurs textbook equips higher education students with skills to leverage artificial intelligence in launching and scaling new ventures. Covers AI tools, strategy, and implementation."),
    27268: ("Artificial Intelligence Business Administration", "1st edition", "Explore how AI is reshaping business administration with Mujo's higher education textbook. Covers AI-driven decision making, operations management, strategic planning, and organizational leadership."),
    27265: ("Artificial Intelligence Business Writing", "1st edition", "Mujo's AI Business Writing textbook for university and college students offers a hands-on introduction to business writing using AI-powered tools."),
    27262: ("Generative AI for Business", "1st edition", "Explore generative AI's business applications with Mujo's Gen AI higher education textbook. Covers prompt engineering, AI system implementation, demand forecasting, market research, and ethical AI considerations."),
    27258: ("Artificial Intelligence Marketing", "1st edition", "Explore Mujo's AI Marketing Textbook for higher education students. Learn AI technologies, machine learning, and data analytics for impactful marketing strategies."),
    27254: ("User Interface/User Experience Design", "1st edition", "Equip students with essential UI/UX design skills using Mujo's User Interface/User Experience Design textbook. Learn to create and optimize compelling customer experiences."),
    27250: ("Pay-Per-Click Advertising", "1st edition", "Equip students with essential PPC skills using Mujo's advertising textbook. Learn keyword research, platform selection, and optimization."),
    27246: ("Strategic Web Design & e-Commerce", "1st edition", "Equip students with web design and e-commerce skills using Mujo's comprehensive textbook. Learn HTML5, WordPress, and more to build functional websites."),
    27242: ("Public Relations Strategy and Communications", "1st edition", "Equip students with essential PR skills using Mujo's Public Relations Strategy and Communications textbook. Learn media relations, crisis management, and more."),
    27238: ("Big Data Analytics and Reporting", "1st edition", "Mujo's Big Data Analytics and Reporting textbook for higher education equips students with skills to interpret data, create reports, and develop actionable plans."),
    27234: ("Writing Digital Media Content", "1st edition", "Mujo's Writing Digital Media Content textbook teaches higher education students writing strategies for websites, PPC ads, email marketing, social media, and more."),
    27229: ("Customer Relationship Management Marketing Automation", "1st edition", "Mujo's CRM Marketing Automation textbook gives higher education students a deep dive into customer relationship management and marketing automation strategies."),
    27226: ("Influencer Marketing Fundamentals", "1st edition", "Mujo's Influencer Marketing Fundamentals textbook teaches higher education students effective influencer strategies for digital marketing."),
    27221: ("Search Engine Optimization", "4th edition", "Mujo's Search Engine Optimization textbook equips higher education students with essential SEO and GEO skills. Covers on-page and off-page techniques and industry best practices."),
    27217: ("Social Media Marketing Strategies", "7th edition", "Mujo's Social Media Marketing Strategies textbook teaches higher education students to leverage the major social platforms for marketing results."),
    27212: ("Principles of Marketing", "1st edition", "Mujo's Principles of Marketing textbook gives higher education students in-depth marketing knowledge, covering ethics, branding, strategy, and more."),
    27207: ("Digital Marketing Fundamentals", "3rd edition", "Mujo's Digital Marketing Fundamentals textbook covers branding, SEO, PPC, email marketing, and more, available in student and instructor editions for higher education."),
    30070: ("Prompt Engineering and LLMs", "1st edition", "Mujo's Prompt Engineering and LLMs textbook gives higher education students a comprehensive, practical guide to prompt engineering and working with large language models (LLMs)."),
    # High school CTE
    27200: ("Website & E-commerce Strategy", None, None),
    27193: ("Online Marketing Fundamentals", None, None),
    27185: ("Foundations of Marketing", None, None),
    27178: ("Social Media Marketing", None, None),
    27171: ("Creating Digital Media Content", None, None),
    27164: ("Sports & Entertainment Marketing", None, None),
    27155: ("Fashion Marketing", None, None),
    27146: ("AI Marketing Fundamentals", None, None),
    27139: ("Influencer Marketing", None, None),
    27132: ("Foundations of Artificial Intelligence", None, None),
    27125: ("Entrepreneurship Fundamentals: In An AI World", None, None),
    27118: ("Principles of Business: In An AI World", None, None),
    27093: ("AI for Business", None, "Prepare high school students for an AI-driven workforce. Mujo's AI for Business textbook and courseware includes ready-to-teach lessons, tests, and CTE alignment."),
}
HS_DESC = ("Mujo's {book} textbook and courseware for high school CTE programs. Available as a student "
           "e-book (1-, 3- or 6-year license), a print student textbook, and a teacher resource cloud and manual.")

NOTES = {
    27254: "Group SKU is UIUX but variant SKUs are UXUI. Harmless, but worth tidying in WooCommerce.",
    27275: "VitalSource title is 'Artificial Intelligence and Human Resource Management'; mujo.com says 'for'. Used the VitalSource title.",
    27200: "VitalSource lists this title as 'Website Design Strategy'.",
    27125: "Student print variant uses the teacher (TM) cover image on the live site.",
    27118: "Student print variant uses the teacher (TM) cover image on the live site.",
    27139: "Teacher print variant uses the student (SM) cover image on the live site.",
}


def variant_label(path, query):
    """Edition label and bookFormat from the WooCommerce attribute query string."""
    q = dict(p.split("=", 1) for p in query.split("&"))
    fmt = "Paperback" if q.get("attribute_pa_book-format") == "soft-copy-printed" else "EBook"
    ed = q.get("attribute_pa_textbook-edition", "")
    lic = q.get("attribute_pa_license", "")
    if path == "higher-ed":
        label = "Instructor Edition" if ed == "for-instructors" else "Student Edition"
        return f"{label} (eBook)", fmt
    who = "Teacher Resource Cloud & Manual" if ed == "for-teachers-resource" else "Student Textbook"
    if fmt == "Paperback":
        return f"{who} (Print)", fmt
    years = lic.split("-")[0]
    return f"{who} (eBook, {years}-year license)", fmt


def fetch_productgroup(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 Chrome/120"})
    page = urllib.request.urlopen(req, timeout=60).read().decode("utf-8")
    for block in re.findall(r'<script[^>]*application/ld\+json[^>]*>(.*?)</script>', page, re.S):
        try:
            data = json.loads(block)
        except ValueError:
            continue
        for node in data.get("@graph", [data]):
            if node.get("@type") == "ProductGroup":
                return node
    raise RuntimeError(f"no ProductGroup on {url}")


_img_cache = {}


def full_size(thumb):
    """Swap a WordPress -150x150 thumbnail for the full-size file when it exists."""
    full = re.sub(r"-150x150(?=\.\w+$)", "", thumb)
    if full == thumb:
        return thumb
    if full not in _img_cache:
        try:
            req = urllib.request.Request(full, method="HEAD", headers={"User-Agent": "Mozilla/5.0 Chrome/120"})
            _img_cache[full] = urllib.request.urlopen(req, timeout=30).status == 200
        except Exception:
            _img_cache[full] = False
    return full if _img_cache[full] else thumb


def clean_name(s):
    s = html.unescape(s).replace("(SEO)Textbook", "(SEO) Textbook")
    return re.sub(r"\bAnd\b", "and", s)


titles = []
for row in json.load(open(AUTHORS, encoding="utf-8")):
    pid, url = row["product_id"], row["url"]
    path = url.rstrip("/").split("/")[-2]
    pg = fetch_productgroup(url)
    time.sleep(1)
    book, edition, desc = BOOKS[pid]
    img = pg["image"][0]["url"] if isinstance(pg["image"], list) else pg["image"]
    variants = []
    for v in pg["hasVariant"]:
        offer_url = html.unescape(v["offers"]["url"])
        label, fmt = variant_label(path, offer_url.split("?", 1)[1])
        variants.append({
            "sku": v["sku"], "isbn": v["gtin"], "label": label, "format": fmt,
            "price": str(v["offers"]["price"]), "url": offer_url, "img": full_size(v.get("image", img)),
        })
    titles.append({
        "product_id": pid,
        "audience": "higher-ed" if path == "higher-ed" else "high-school",
        "url": url,
        "sku": pg["sku"],
        "book": book,
        "edition": edition,
        "authors": row["authors"],
        "name": clean_name(row["title"]),
        "desc": desc or HS_DESC.format(book=book),
        "category": HE_CAT if path == "higher-ed" else HS_CAT,
        "img": img,
        "variants": variants,
        "notes": NOTES.get(pid, ""),
    })
    print(pid, book, len(variants), "variants", flush=True)

json.dump(titles, open(HERE / "titles.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(f"saved {len(titles)} titles")
