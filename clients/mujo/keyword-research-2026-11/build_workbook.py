"""Build the Mujo AI + business tracked-keyword proposal workbook (2026-11-21).

Inputs (same folder): kp-volume-us.json, kp-volume-ca.json (Google Ads Keyword Planner),
gsc-ai-business-queries.csv (GSC, sc-domain:mujo.com, 2025-07-20 to 2026-11-18).
SERP observations and the current Semrush tracked set are typed in below, with their sources.
Reusable: edit PROPOSED / EXCLUDED and re-run to regenerate the workbook.
"""
import csv, json, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'mujo-ai-business-tracked-keywords-2026-11.xlsx')

us = {r['keyword']: r for r in json.load(open(os.path.join(HERE, 'kp-volume-us.json')))['results']}
ca = {r['keyword']: r for r in json.load(open(os.path.join(HERE, 'kp-volume-ca.json')))['results']}
gsc = {r['query']: r for r in csv.DictReader(open(os.path.join(HERE, 'gsc-ai-business-queries.csv'), encoding='utf-8'))}

# ---------------- Pages (canonical URLs, checked live 2026-11-21) ----------------
PAGES = {
    'HE-AI': ('/higher-education/ai-textbooks/', 'AI Textbooks For Higher Education | Mujo Learning Systems'),
    'HE-BIZ': ('/higher-education/business-textbooks/', 'Business Textbooks & Curriculum | Higher Education | Mujo'),
    'APPLIED': ('/higher-education/applied-ai-for-business-curriculum/', 'Applied AI for Business Curriculum for Higher Education | Mujo Learning Sys...'),
    'LIT': ('/higher-education/ai-textbooks/artificial-intelligence-literacy/', 'AI Literacy Textbook & Curriculum | Artificial Intelligence Course Curricul...'),
    'HEALTH': ('/higher-education/ai-textbooks/ai-literacy-healthcare/', 'AI Literacy Healthcare Curriculum for University & College'),
    'ACCT': ('/higher-education/business-textbooks/artificial-intelligence-accounting-principles/', 'AI Accounting Principles Textbook for University & College'),
    'HR': ('/higher-education/business-textbooks/artificial-intelligence-and-human-resource-management/', 'Artificial Intelligence and Human Resource Management Curriculum | Mujo Lea...'),
    'PM': ('/higher-education/business-textbooks/artificial-intelligence-project-management/', 'Artificial Intelligence Project Management | Mujo Learning Systems'),
    'SALES': ('/higher-education/business-textbooks/artificial-intelligence-sales-fundamentals/', 'Artificial Intelligence Sales Fundamentals | Mujo Learning Systems'),
    'ENTRE-HE': ('/higher-education/business-textbooks/artificial-intelligence-for-entrepreneurs/', 'Artificial Intelligence for Entrepreneurs | Mujo Learning Systems'),
    'BIZADMIN': ('/higher-education/business-textbooks/artificial-intelligence-business-administration/', 'Artificial Intelligence Business Administration | Mujo Learning Systems'),
    'WRITING': ('/higher-education/business-textbooks/artificial-intelligence-business-writing/', 'Artificial Intelligence Business Writing | Mujo Learning Systems'),
    'GENAI': ('/higher-education/ai-textbooks/generative-ai-for-business/', 'Generative AI for Business Curriculum | Mujo Learning Systems'),
    'PROMPT': ('/higher-education/ai-textbooks/prompt-engineering-curriculum/', "Prompt Engineering and LLM's Curriculum for Higher Education | Mujo Learnin..."),
    'ANALYTICS': ('/higher-education/business-textbooks/business-analytics-fundamentals/', 'Business Analytics Fundamentals | Mujo Learning Systems'),
    'AIMKT-HE': ('/higher-education/ai-textbooks/artificial-intelligence-marketing/', 'Artificial Intelligence Marketing | Mujo Learning Systems'),
    'HS-AI': ('/high-school/ai-textbooks/', 'High School Artificial Intelligence (AI) Textbooks | Mujo Learning Systems'),
    'FOAI': ('/high-school/ai-textbooks/foundations-artificial-intelligence/', 'Foundations of Artificial Intelligence | Mujo Learning Systems'),
    'HS-AIBIZ': ('/high-school/business-textbooks/ai-for-business/', 'AI For Business High School Curriculum | Mujo Learning'),
    'HS-AIMKT': ('/high-school/digital-marketing-textbooks/ai-marketing-fundamentals/', 'AI Marketing Fundamentals Curriculum | Mujo Learning Systems'),
    'ENTRE-HS': ('/high-school/business-textbooks/entrepreneurship-fundamentals/', 'High School Entrepreneurship Fundamentals: In An AI World | Mujo Learning S...'),
    'POB': ('/high-school/business-textbooks/principles-of-business/', 'Principles of Business: In An AI World | Mujo Learning Systems'),
    'HS-BIZ': ('/high-school/business-textbooks/', 'High School Business Textbooks | Mujo Learning Systems'),
}

# ---------------- Live SERP check (google.com, gl=us, hl=en, pws=0; 2026-11-21) ----------------
# value: (Mujo organic rank in top 10, 0 = not in top 10; who leads / what intent the page shows)
SERP = {
    'ai textbooks': (0, 'AI Overview; Amazon best sellers, Tableau and Russell & Norvig (AIMA) lists, Reddit. Trade-book intent dominates.'),
    'ai textbook for college': (0, 'AI Overview recommends AIMA, Routledge and Bookshop titles; university library guides. No publisher curriculum pages.'),
    'artificial intelligence textbook': (0, 'AIMA (Berkeley), Amazon, Wikipedia, Cengage Intro to AI. Computer-science intent.'),
    'generative ai textbooks': (0, 'Reddit, Amazon, Manning, SAGE "Generative AI for Students", O\'Reilly.'),
    'ai textbook for business students': (0, 'Reddit, MyEducator reader, Bookshop "Intro to AI in Business", Goodreads, bkstr. Weak field.'),
    'ai in business textbook': (5, 'McGraw Hill "AI in Business: Creating Value Responsibly" #1 and #3, UMD Smith, then Mujo (Generative AI for Business page).'),
    'applied ai for business curriculum': (1, 'Mujo #1, then U Delaware Lerner, Coursera, MIT Professional, HBS Online.'),
    'ai literacy curriculum': (0, 'AI Overview; Day of AI, Jisc, Common Sense, AI Literacy Day, Stanford Teaching Commons. Free K-12 / faculty resources.'),
    'ai literacy textbook': (5, 'SAGE/Corwin "Teaching AI Literacy Across the Curriculum", UMN open text, UVA Pressbooks, then Mujo.'),
    'ai in accounting textbook': (1, 'Mujo #1, Routledge, Amazon, UMD Smith, McGraw Hill "AI and the Future of Accounting".'),
    'ai in accounting course': (0, 'Becker, Coursera, AICPA-CIMA, Surgent CPE, LinkedIn Learning. CPA continuing-education intent: wrong audience.'),
    'ai in human resource management textbook': (8, 'Amazon, Harvard Business Publishing, Springer, Elgar, IGI, ILO, Routledge, then Mujo.'),
    'ai project management textbook': (0, 'Amazon, PM World Journal, O\'Reilly, Routledge, PMI, Harvard Business Publishing. Mujo absent.'),
    'business communication textbook with ai': (2, 'TX Wesleyan Pressbooks #1, Mujo #2, CMU, Business Communication Network videos.'),
    'ai business writing textbook': (1, 'Mujo #1 and #6, Purdue, VitalSource (Mujo title), "Business Writing with AI For Dummies".'),
    'prompt engineering textbook': (0, 'AI Overview; Manning, Amazon, Reddit, GitHub DAIR guide, O\'Reilly, IBM. Practitioner intent.'),
    'business analytics textbook': (0, 'AI Overview; McGraw Hill, Cengage, Amazon, SAGE. Big publishers own it.'),
    'ai business analytics textbook': (1, 'Mujo #1, Routledge, Harvard Business Publishing, Amazon, McGraw Hill.'),
    'ai sales textbook': (4, 'Jeb Blount "The AI Edge" (#1 and #2), Reddit, then Mujo.'),
    'ai for entrepreneurs textbook': (4, 'Amazon, Strategic Coach, Cambridge "The AI Entrepreneur", then Mujo.'),
    'ai business administration textbook': (2, 'McGraw Hill AI in Business #1, Mujo #2, Routledge, U Delaware guide.'),
    'ai in healthcare textbook for students': (4, 'Squarespace course site, ScienceDirect, PCOM library guide, then Mujo, Routledge, Elsevier.'),
    'ai in nursing education textbook': (0, 'Cognella "AI for Nursing Education", Springer, NLN, AACN. Mujo absent.'),
    'ai marketing textbook': (4, 'Routledge, Amazon, Stanford UP "AI Marketing Canvas", then Mujo.'),
    'generative ai for business textbook': (1, 'Mujo #1, AI Mode answer, GenAI4All, O\'Reilly, HBR, Columbia.'),
    'ai curriculum for high school': (0, 'AI Overview; Reddit, Day of AI, Common Sense, CodeHS, Stanford, Code.org (free), HelloWorldCS.'),
    'ai textbook for high school': (1, 'Mujo #1 and #4, Amazon, McGraw Hill "Foundations of AI", AIClub, MIT, CodeHS.'),
    'ai lesson plans for high school': (0, 'Eduaide, MagicSchool, Flint, Brisk, Canva: AI lesson-plan GENERATORS. Wrong intent.'),
    'foundations of artificial intelligence': (0, 'AI Overview; Georgia Tech course, Scribd, McGraw Hill "Foundations of AI", Code.org AI Foundations. Mujo absent.'),
    'introduction to artificial intelligence course high school cte': (0, 'Savvas, CodeHS, Accelerate Education, district CTE pages, CTE Resource Center (VA).'),
    'ai cte curriculum': (0, 'AI Overview; Regional CTE, CTE Learning, NCBCE, Tech & Learning. Informational.'),
    'ai for business high school curriculum': (1, 'Mujo #1, Reddit, Inspirit AI, AACSB, Wharton Global Youth.'),
    'high school entrepreneurship curriculum': (0, 'Ramsey, Reddit, VentureLab, NGPF (free), JA, K12. Mujo absent.'),
    'entrepreneurship textbook high school': (1, 'Mujo #1 and #5, McGraw Hill Entrepreneurship Fundamentals, Amazon, OpenStax, G-W.'),
    'principles of business textbook': (0, 'AI Overview; Cengage 9th ed, Scribd and OUP CSEC (Caribbean exam) titles, G-W "Principles of Business, Marketing, and Finance".'),
    'principles of business marketing and finance curriculum': (0, 'UT High School, G-W (2 results), Edmentum, iCEV, Texas district pages. Texas course name.'),
    'high school business curriculum': (9, 'District curriculum pages, Reddit, JA, iCEV, then Mujo HS hub.'),
    'introduction to business textbook': (0, 'AI Overview; OpenStax (free), McGraw Hill, Amazon, UMN open text, SAGE.'),
}

# ---------------- Proposed keywords ----------------
# (keyword, audience, title cluster, page key, tier, add_to_CA, intent, serp_key or None, why)
T1, T2 = 'Tier 1: core', 'Tier 2: watch'
PROPOSED = [
    # ---- Higher ed: AI hub + programme
    ('ai textbooks', 'HE', 'AI hub', 'HE-AI', T1, True, 'Commercial / mixed', 'ai textbooks',
     'Biggest AI term with buyer potential (~590/mo US, grouped with "artificial intelligence textbook"). Already tracked; keep as the AI headline term.'),
    ('ai textbook', 'HE', 'AI hub', 'HE-AI', T1, True, 'Commercial / mixed', 'ai textbooks',
     'Singular form gets as many GSC impressions as the plural (642 vs 632, US) and ranks differently. Track both.'),
    ('ai textbook for college', 'HE', 'AI hub', 'HE-AI', T1, True, 'Commercial', 'ai textbook for college',
     'Adds the higher-ed qualifier (Andrew\'s 2026-06-24 rule). The SERP is library guides and trade books: a gap Mujo can fill.'),
    ('ai textbook for business students', 'HE', 'AI hub', 'HE-BIZ', T1, True, 'Commercial', 'ai textbook for business students',
     'Describes Mujo\'s exact niche. Weak SERP (Reddit, MyEducator, Bookshop).'),
    ('ai in business textbook', 'HE', 'AI hub', 'HE-BIZ', T1, True, 'Commercial', 'ai in business textbook',
     'McGraw Hill\'s flagship term ("AI in Business"). Mujo is #5 already: the main head-to-head benchmark.'),
    ('artificial intelligence textbook', 'HE', 'AI hub', 'HE-AI', T2, False, 'Mixed (CS)', 'artificial intelligence textbook',
     'Same Keyword Planner group as "ai textbooks". The SERP is computer-science (AIMA). Watch only.'),
    ('applied ai for business curriculum', 'HE', 'Applied AI for Business programme', 'APPLIED', T1, True, 'Commercial', 'applied ai for business curriculum',
     'Mujo #1. Defend it. "applied ai for business" is already tracked (US); add both to Canada (NACC Canadian colleges programme).'),
    ('applied ai for business', 'HE', 'Applied AI for Business programme', 'APPLIED', T1, True, 'Mixed', None,
     'Already in the US campaign (pos 51). 971 US impressions in GSC at avg pos 21. Add to Canada.'),
    ('turnkey ai curriculum', 'HE', 'Applied AI for Business programme', 'APPLIED', T2, True, 'Commercial', None,
     'Canada-only signal: 709 GSC impressions, all from Canada, avg pos 12.4. Canada campaign only.'),
    ('ai literacy textbook', 'HE', 'AI Literacy', 'LIT', T1, True, 'Commercial', 'ai literacy textbook',
     'Mujo #5. "AI literacy" is the dominant buyer phrase across Pearson, Cengage, iCEV and K-12 (competitor scan).'),
    ('ai literacy curriculum', 'HE', 'AI Literacy', 'LIT', T2, True, 'Mixed', 'ai literacy curriculum',
     'GSC 125 US impressions at pos 19. The SERP is free K-12 and faculty resources: track for visibility, not quick wins.'),
    ('generative ai textbooks', 'HE', 'Generative AI for Business', 'GENAI', T2, False, 'Mixed', 'generative ai textbooks',
     'Already tracked (US). Keep. GSC 144 impressions at pos 9.4.'),
    # ---- Higher ed: AI business titles
    ('ai in accounting textbook', 'HE', 'AI Accounting Principles', 'ACCT', T1, True, 'Commercial', 'ai in accounting textbook',
     'Mujo #1. No major publisher has a dedicated title (competitor scan). Defend it.'),
    ('ai accounting principles textbook', 'HE', 'AI Accounting Principles', 'ACCT', T1, True, 'Commercial', None,
     'Exact title phrase. Benchmarks the product page itself.'),
    ('ai in human resource management textbook', 'HE', 'AI for HR Management', 'HR', T1, True, 'Commercial', 'ai in human resource management textbook',
     'Mujo #8. GSC shows 623 + 372 impressions on "artificial intelligence human resource management for (higher) education" at pos 6-8.'),
    ('artificial intelligence human resource management for higher education', 'HE', 'AI for HR Management', 'HR', T2, False, 'Commercial', None,
     'Real query: 623 US GSC impressions, avg pos 6.2. Long, but the exact buyer phrasing.'),
    ('ai project management textbook', 'HE', 'AI Project Management', 'PM', T1, True, 'Commercial', 'ai project management textbook',
     'Mujo absent from the top 10, but no big publisher owns it (Amazon, O\'Reilly, Routledge, PMI). Good gap.'),
    ('ai in project management book', 'HE', 'AI Project Management', 'PM', T2, False, 'Commercial', None,
     'GSC 51 US impressions at pos 10.2.'),
    ('ai sales textbook', 'HE', 'AI Sales Fundamentals', 'SALES', T1, True, 'Commercial', 'ai sales textbook',
     'Mujo #4, behind trade books only.'),
    ('ai for entrepreneurs textbook', 'HE', 'AI for Entrepreneurs', 'ENTRE-HE', T1, True, 'Commercial', 'ai for entrepreneurs textbook',
     'Mujo #4. "ai for entrepreneurs/entrepreneurship" is 140/mo US (mostly founders, so watch the textbook variant).'),
    ('artificial intelligence for entrepreneurs', 'HE', 'AI for Entrepreneurs', 'ENTRE-HE', T2, False, 'Mixed', None,
     'Exact title. GSC 31 US impressions at pos 4.8.'),
    ('ai business administration textbook', 'HE', 'AI Business Administration', 'BIZADMIN', T1, True, 'Commercial', 'ai business administration textbook',
     'Mujo #2, right behind McGraw Hill. Matches Humber\'s "AI for Business Administration" credential (Canada).'),
    ('ai in business administration', 'HE', 'AI Business Administration', 'BIZADMIN', T2, True, 'Mixed', None,
     'GSC 74 US impressions at pos 3.8.'),
    ('ai business writing textbook', 'HE', 'AI Business Writing', 'WRITING', T1, True, 'Commercial', 'ai business writing textbook',
     'Mujo #1 and #6. Defend it.'),
    ('business communication textbook with ai', 'HE', 'AI Business Writing', 'WRITING', T1, True, 'Commercial', 'business communication textbook with ai',
     'Mujo #2. "Business communication" is what college courses are called. GSC also shows AI-assistant-style questions on this topic.'),
    ('business communication textbook', 'HE', 'AI Business Writing', 'WRITING', T2, True, 'Commercial', None,
     'Stretch: 260/mo US, 70 CA, high competition. Shows whether Mujo can break into the generic course term.'),
    ('generative ai for business textbook', 'HE', 'Generative AI for Business', 'GENAI', T1, True, 'Commercial', 'generative ai for business textbook',
     'Mujo #1. Defend it.'),
    ('generative ai for business book', 'HE', 'Generative AI for Business', 'GENAI', T2, False, 'Commercial', None,
     'GSC 130 US impressions at pos 5.1, plus 582 on the quoted variant.'),
    ('generative ai for business', 'HE', 'Generative AI for Business', 'GENAI', T2, True, 'Mixed', None,
     '260/mo US. Mixed intent (courses, books). GSC pos 31.'),
    ('prompt engineering textbook', 'HE', 'Prompt Engineering and LLMs', 'PROMPT', T1, True, 'Commercial', 'prompt engineering textbook',
     'Mujo absent. Practitioner books lead. The only textbook-intent phrase in a big topic (the "prompt engineering course" group is 2,400/mo but learner intent).'),
    ('prompt engineering curriculum', 'HE', 'Prompt Engineering and LLMs', 'PROMPT', T2, False, 'Commercial', None,
     'Matches the page H1. GSC pos 6.0 on low impressions.'),
    ('ai business analytics textbook', 'HE', 'AI Business Analytics', 'ANALYTICS', T1, True, 'Commercial', 'ai business analytics textbook',
     'Mujo #1. Defend it.'),
    ('business analytics fundamentals', 'HE', 'AI Business Analytics', 'ANALYTICS', T2, True, 'Mixed', None,
     'Title name. GSC 133 US impressions at pos 17; "fundamentals of business analytics" adds 401 US + 100 CA at pos 19-23.'),
    ('business analytics textbook', 'HE', 'AI Business Analytics', 'ANALYTICS', T2, False, 'Commercial', 'business analytics textbook',
     'Stretch: McGraw Hill and Cengage own it. GSC 72 impressions at pos 8.4.'),
    ('ai in healthcare textbook', 'HE', 'AI Literacy for Healthcare', 'HEALTH', T1, True, 'Commercial', 'ai in healthcare textbook for students',
     'Mujo #4 on the "for students" form. New title (Shawn asked for homepage placement, 2026-04-29).'),
    ('ai literacy for healthcare', 'HE', 'AI Literacy for Healthcare', 'HEALTH', T2, True, 'Commercial', None,
     'Exact title. No data yet: a new-title baseline.'),
    ('ai in nursing education textbook', 'HE', 'AI Literacy for Healthcare', 'HEALTH', T2, False, 'Commercial', 'ai in nursing education textbook',
     'The page mentions nursing 4 times; "ai in nursing education" is 110/mo US. Mujo absent. Confirm nursing programmes are a target before optimising for it.'),
    ('ai marketing textbook', 'HE', 'AI Marketing (HE)', 'AIMKT-HE', T1, True, 'Commercial', 'ai marketing textbook',
     'Mujo #4. The page has the highest impressions of all the AI pages (9.8K, mostly off-target martech queries).'),
    ('ai marketing book', 'HE', 'AI Marketing (HE)', 'AIMKT-HE', T2, False, 'Commercial', None,
     'GSC 95 US impressions at pos 7.9.'),
    # ---- High school (USA campaign only)
    ('ai curriculum for high school', 'HS', 'HS AI hub', 'HS-AI', T1, False, 'Commercial', 'ai curriculum for high school',
     'The head HS term. GSC pos 16.8, but absent from the live top 10 (Code.org free, Day of AI, CodeHS). Hard, but it is the market term.'),
    ('ai textbook for high school', 'HS', 'HS AI hub', 'HS-AI', T1, False, 'Commercial', 'ai textbook for high school',
     'Mujo #1 and #4, ahead of McGraw Hill. Defend it.'),
    ('ai books for high school students', 'HS', 'HS AI hub', 'HS-AI', T2, False, 'Mixed', None,
     'GSC 76 US impressions at pos 8.'),
    ('ai school textbook', 'HS', 'HS AI hub', 'HS-AI', T2, False, 'Commercial', None,
     'GSC 136 US impressions at pos 3.5, 0 clicks: a CTR test candidate.'),
    ('foundations of artificial intelligence', 'HS', 'Foundations of Artificial Intelligence', 'FOAI', T1, False, 'Mixed', 'foundations of artificial intelligence',
     'Already tracked. 170/mo US. Exact Georgia CTE course name (11.44300). McGraw Hill and Code.org compete; Mujo absent.'),
    ('foundations of artificial intelligence textbook', 'HS', 'Foundations of Artificial Intelligence', 'FOAI', T1, False, 'Commercial', None,
     'Buyer form of the title. The page title lacks "High School" and "Textbook".'),
    ('foundations of artificial intelligence curriculum', 'HS', 'Foundations of Artificial Intelligence', 'FOAI', T1, False, 'Commercial', None,
     'Matches the page H1 and how Georgia CTE teachers search.'),
    ('introduction to artificial intelligence course high school', 'HS', 'Foundations of Artificial Intelligence', 'FOAI', T2, False, 'Commercial', 'introduction to artificial intelligence course high school cte',
     'Savvas and iCEV course naming (also South Carolina\'s course name). Competitive benchmark.'),
    ('ai cte curriculum', 'HS', 'HS AI hub', 'HS-AI', T2, False, 'Mixed', 'ai cte curriculum',
     'Informational now, but CTE buyers use it. Low cost to watch.'),
    ('ai for business high school curriculum', 'HS', 'AI for Business (HS)', 'HS-AIBIZ', T1, False, 'Commercial', 'ai for business high school curriculum',
     'Mujo #1. Defend it.'),
    ('ai marketing curriculum high school', 'HS', 'AI Marketing Fundamentals (HS)', 'HS-AIMKT', T2, False, 'Commercial', None,
     'No data yet. Baseline for the HS AI Marketing title.'),
    ('high school entrepreneurship curriculum', 'HS', 'Entrepreneurship Fundamentals', 'ENTRE-HS', T1, False, 'Commercial', 'high school entrepreneurship curriculum',
     'GSC 69 US impressions at pos 25; absent from the live top 10 (Ramsey, VentureLab, NGPF). Brittni said the title does well organically (2026-01-22).'),
    ('entrepreneurship curriculum', 'HS', 'Entrepreneurship Fundamentals', 'ENTRE-HS', T1, False, 'Commercial', None,
     '90/mo US. GSC pos 38.7. The head term for the title.'),
    ('entrepreneurship textbook high school', 'HS', 'Entrepreneurship Fundamentals', 'ENTRE-HS', T1, False, 'Commercial', 'entrepreneurship textbook high school',
     'Mujo #1 and #5, ahead of McGraw Hill. GSC 196 US impressions. Defend it.'),
    ('entrepreneurship textbook', 'HS', 'Entrepreneurship Fundamentals', 'ENTRE-HS', T2, False, 'Commercial', None,
     '110/mo US. Mixed HS/college audience. GSC pos 12.'),
    ('principles of business textbook', 'HS', 'Principles of Business', 'POB', T1, False, 'Commercial', 'principles of business textbook',
     'Mujo absent. Cengage leads, plus Caribbean CSEC titles; G-W ranks with its Texas title. Worth winning for the HS title.'),
    ('principles of business curriculum', 'HS', 'Principles of Business', 'POB', T1, False, 'Commercial', None,
     'Matches the page H1 ("Principles of Business Curriculum For High School Students").'),
    ('principles of business marketing and finance', 'HS', 'Principles of Business', 'POB', T2, False, 'Commercial', 'principles of business marketing and finance curriculum',
     '320/mo US: the Texas course name (PEIMS 13011200). G-W, Edmentum, iCEV and UT rank. Track only; don\'t claim TEKS alignment in copy unless Mujo confirms it.'),
    ('high school business curriculum', 'HS', 'HS business hub', 'HS-BIZ', T1, False, 'Commercial', 'high school business curriculum',
     'Mujo #9 (HS hub). GSC 36 impressions at pos 25.'),
]

# ---------------- Considered and not recommended ----------------
EXCLUDED = [
    ('ai lesson plans / ai lesson plans for high school', 'US 480 (group)', 'Live SERP is all AI lesson-plan GENERATORS (MagicSchool, Brisk, Canva). Teachers want a tool, not curriculum.'),
    ('ai in accounting course', 'US 70', 'Live SERP is CPA continuing education (Becker, AICPA, Surgent). Mujo doesn\'t sell CPA CE (keywords.md section 4).'),
    ('artificial intelligence in accounting', 'US 6,600', 'Informational / practitioner topic. Big number, but it won\'t move adoption.'),
    ('ai in human resource management', 'US 2,900', 'HR practitioner topic. The textbook variant is tracked instead.'),
    ('ai in project management', 'US 2,900', 'PM practitioner topic (PMI, tools). The textbook variant is tracked instead.'),
    ('artificial intelligence marketing', 'US 4,400', 'Martech intent. Mujo sits at pos 32; it inflates impressions without buyers.'),
    ('ai literacy', 'US 2,900', 'Definition intent ("what is AI literacy"). The textbook and curriculum variants are tracked instead.'),
    ('ai literacy course / prompt engineering course / generative ai course', 'US 720 / 2,400 / 880', 'Learner intent (Coursera, Google, IBM). Mujo sells to instructors, not individual learners.'),
    ('ai for business course', 'US 260', 'Professional and executive-education intent (HBS Online, Coursera, MIT). The curriculum term is tracked instead.'),
    ('principles of business', 'US 1,000', 'Generic. The SERP mixes Caribbean CSEC exam material and definitions.'),
    ('introduction to business textbook', 'US 260', 'OpenStax (free) and McGraw Hill own it, and Mujo has no Intro to Business title (AI Business Administration is the closest).'),
    ('ai generated textbook(s)', 'GSC 63 + 44 impr.', 'Conflicts with the "100% Human Authored" brand promise (Shawn, 2026-04-30). Never target.'),
    ('business writing with ai for dummies', 'GSC 142 impr.', 'Another publisher\'s title.'),
    ('applying artificial intelligence in project management / using ai in marketing (Mercury Learning)', 'GSC 300+ impr.', 'Another publisher\'s titles. Mujo ranks by accident.'),
    ('... pdf free download', 'GSC 300+ impr.', 'Piracy intent. Exclude, and add as negatives if PPC relaunches.'),
    ('iaijodojo.com business type and classes offered', 'GSC 9,190 impr.', 'Spam/junk query hitting the HS AI for Business page. Noise; explains that page\'s 0.2% CTR flag in keywords.md.'),
]

# ---------------- Current Semrush tracked set (from the 2026-11-06 monthly report PDF, Oct 1-31 data) ----------------
CUR_US = """social media marketing textbook|marketing automation curriculum|digital marketing lesson plans|digital marketing teacher manual|digital marketing teaching materials|digital marketing teachers manual|digital marketing teacher's manual|what is social media marketing in high school|social media marketing lesson plans for high school students|what is marketing in high school|high school marketing class curriculum|marketing textbooks for high school|high school marketing curriculum|marketing curriculum high school|marketing strategies high school textbook|curriculum seo|marketing books for high school students|marketing textbook high school|college textbook for digital marketing|social media curriculum|seo textbook|teaching digital marketing|pr textbook|social media textbook|social media marketing lesson plans|curriculum digital marketing|how to teach seo|teaching social media marketing|social media marketing teaching materials|digital marketing textbook publisher|how to teach digital marketing|digital marketing textbook publishers|seo teaching materials|web design lesson plans|digital marketing teaching resources|principles of marketing textbook|textbooks on artificial intelligence|communications textbook|foundations of artificial intelligence|user interface design textbook|ai textbooks|generative ai textbooks|applied ai for business|accounting principles textbook|ecommerce textbook|digital marketing high school|high school marketing textbook|social media for educators|social media campaigns textbook|writing for the web book|teaching marketing in high school|digital marketing teacher|e commerce textbook|seo training for higher ed|social media for high school students|seo teacher|social media marketing workbook|big data textbook|social media strategy book|digital marketing course book|online marketing textbook|seo lesson plans|online marketing fundamentals|seo curriculum|digital marketing curriculum|social media lesson plans|web design textbook|digital marketing training materials|best digital marketing textbooks|digital marketing textbook|best digital marketing textbook|marketing automation syllabus|digital marketing essentials textbooks|best digital marketing texbooks|marketing textbook online|internet marketing textbook|digital marketing fundamentals|curriculum web design|seo textbook publisher|web design textbook publisher|web development textbook""".split('|')
CUR_CA = """digital marketing lesson plans|digital marketing textbook publishers|how to teach digital marketing|seo textbook|digital marketing teacher's manual|digital marketing teacher manual|marketing textbook high school|marketing textbooks for high school|high school marketing textbook|digital marketing textbook publisher|seo teacher|social media marketing lesson plans|digital marketing teaching resources|college textbook for digital marketing|marketing books for high school students|high school marketing class curriculum|digital marketing essentials textbooks|seo teaching materials|digital marketing high school|how to teach seo|seo lesson plans|curriculum seo|social media marketing textbook|social media textbook|teaching social media marketing|digital marketing teaching materials|social media marketing lesson plans for high school students|what is marketing in high school|digital marketing teachers manual|digital marketing textbook|marketing strategies high school textbook|curriculum web design|social media marketing teaching materials|marketing curriculum high school|high school marketing curriculum|social media for educators|teaching digital marketing|social media campaigns textbook|what is social media marketing in high school|writing for the web book|teaching marketing in high school|digital marketing teacher|ecommerce textbook|seo training for higher ed|social media for high school students|social media marketing workbook|big data textbook|social media strategy book|digital marketing course book|web development textbook|web design textbook publisher|web design textbook|web design lesson plans|social media lesson plans|social media curriculum|seo textbook publisher|seo curriculum|online marketing textbook|online marketing fundamentals|marketing textbook online|marketing automation syllabus|marketing automation curriculum|internet marketing textbook|digital marketing training materials|digital marketing fundamentals|digital marketing curriculum|curriculum digital marketing|best digital marketing textbooks|best digital marketing textbook|best digital marketing texbooks""".split('|')
AI_FLAG = ('artificial intelligence', 'ai ', 'generative', 'applied ai', 'accounting')
REMOVE = {
    'best digital marketing texbooks': 'Typo duplicate of "best digital marketing textbooks".',
    'best digital marketing textbook': 'Singular duplicate; keep the plural.',
    'social media for educators': 'Teachers using social media, not buying curriculum. Mujo not ranking.',
    'social media for high school students': 'Student intent. Mujo not ranking.',
    'writing for the web book': 'Generic trade-book query. Mujo not in top 20.',
    'digital marketing fundamentals': 'Google certification / learner intent (320 US, 210 CA). Mujo not in top 40.',
}

# ---------------- Competitors ----------------
COMPETITORS = [
    ('mheducation.com', 'Keep', 'Both', 'Owns "AI in Business" and HS "Foundations of AI". Appears in most AI SERPs checked.'),
    ('pearson.com', 'Keep', 'Both', 'AI Literacy Modules (HE add-on).'),
    ('cengage.com', 'Keep', 'Both', 'Principles of Business 9e; business analytics.'),
    ('stukent.com', 'Keep', 'Both', 'GenAI courseware (HE) and CTE "Principles of GenAI".'),
    ('businessu.org', 'Replace', 'Both', 'Now 301-redirects to cte.stukent.com/business/: a duplicate of Stukent. Slot wasted.'),
    ('g-w.com', 'Add (US)', 'US', 'Goodheart-Willcox ranks for "principles of business marketing and finance", "principles of business textbook" and "entrepreneurship textbook high school".'),
    ('savvas.com', 'Add (US)', 'US', '#1 for "introduction to artificial intelligence course high school cte".'),
    ('icevonline.com', 'Add (US)', 'US', 'Introduction to AI course, PBMF, HS business curriculum SERPs.'),
    ('routledge.com', 'Add (Both)', 'Both', 'In the top 10 for 9 of the AI business textbook SERPs checked (accounting, HR, PM, analytics, marketing, admin).'),
    ('code.org', 'Consider (US)', 'US', 'Free "AI Foundations" curriculum; top 10 on HS AI terms. A visibility benchmark, not a sales competitor.'),
]

# ======================= build =======================
ARIAL = 'Arial'
HFILL = PatternFill('solid', fgColor='1F3864')
HFONT = Font(name=ARIAL, bold=True, color='FFFFFF', size=10)
BODY = Font(name=ARIAL, size=10)
BOLD = Font(name=ARIAL, size=10, bold=True)
WRAP = Alignment(wrap_text=True, vertical='top')
thin = Side(style='thin', color='D9D9D9')
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)


def sheet(wb, title, headers, rows, widths, table=True):
    ws = wb.create_sheet(title)
    ws.append(headers)
    for r in rows:
        ws.append(list(r))
    for c in range(1, len(headers) + 1):
        cell = ws.cell(row=1, column=c)
        cell.font, cell.fill, cell.alignment = HFONT, HFILL, Alignment(wrap_text=True, vertical='center')
        ws.column_dimensions[get_column_letter(c)].width = widths[c - 1]
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.font, cell.alignment, cell.border = BODY, WRAP, BORDER
    ws.freeze_panes = 'B2'
    if table and rows:
        ref = f'A1:{get_column_letter(len(headers))}{len(rows) + 1}'
        t = Table(displayName=title.replace(' ', '_').replace('-', '_'), ref=ref)
        t.tableStyleInfo = TableStyleInfo(name='TableStyleLight9', showRowStripes=True)
        ws.add_table(t)
    return ws


# Second Keyword Planner pull (2026-11-21) for phrases added after the first pull; all others returned 0.
EXTRA_US = {'ai textbook': 590}
EXTRA_CA = {'ai textbook': 70}
CA_ONLY = {'turnkey ai curriculum'}  # demand is Canada-only in GSC


def vol(d, k):
    if k in d:
        return d[k].get('avg_monthly_searches', 0)
    return (EXTRA_US if d is us else EXTRA_CA).get(k, 0)


def num(x):
    try:
        return float(x) if '.' in str(x) else int(x)
    except (TypeError, ValueError):
        return None


cur_us, cur_ca = set(CUR_US), set(CUR_CA)
prop_rows = []
for kw, aud, cluster, pk, tier, add_ca, intent, sk, why in PROPOSED:
    g = gsc.get(kw, {})
    rank, serp_note = SERP.get(sk, (None, '')) if sk else (None, '')
    serp_txt = ('not checked' if rank is None else ('not in top 10' if rank == 0 else f'#{rank}'))
    if sk and sk != kw and rank is not None:
        serp_txt += f' (checked as "{sk}")'
    in_us = 'Yes (keep)' if kw in cur_us else ('No (Canada only)' if kw in CA_ONLY else 'Add')
    if aud == 'HE' and add_ca:
        in_ca = 'Yes (keep)' if kw in cur_ca else 'Add'
    else:
        in_ca = 'No (HS is US-only)' if aud == 'HS' else 'No'
    title_gap = ''
    ptitle = PAGES[pk][1]
    if aud == 'HE' and not any(s in ptitle for s in ('Higher Ed', 'University', 'College')):
        title_gap = 'Title lacks "Higher Education"'
    if aud == 'HS' and 'High School' not in ptitle:
        title_gap = 'Title lacks "High School"'
    tags = f'{aud}-{"AI" if ("AI" in cluster or "Artificial" in cluster or "Prompt" in cluster or "Generative" in cluster) else "Business"}; {cluster}; {"T1" if tier == T1 else "T2"}'
    prop_rows.append([kw, aud, cluster, tier, in_us, in_ca, vol(us, kw), vol(ca, kw),
                      num(g.get('usa_impr')), num(g.get('usa_pos')), num(g.get('can_impr')), num(g.get('can_pos')),
                      serp_txt, serp_note, intent, 'https://www.mujo.com' + PAGES[pk][0], ptitle, title_gap, tags, why])

wb = Workbook()
ws0 = wb.active
ws0.title = 'Read me'

# Proposed sheet first so summary formulas can reference it
PH = ['Keyword', 'Audience', 'Title / cluster', 'Tier', 'USA campaign', 'Canada campaign', 'US vol / mo (KP)', 'CA vol / mo (KP)',
      'GSC US impr. (16 mo)', 'GSC US avg pos', 'GSC CA impr. (16 mo)', 'GSC CA avg pos', 'Live SERP: Mujo (US, 2026-11-21)',
      'Who ranks / intent seen', 'Intent', 'Target page (canonical)', 'Current page title', 'Title gap', 'Semrush tags', 'Why track it']
ws1 = sheet(wb, 'Proposed keywords', PH, prop_rows, [34, 9, 24, 13, 12, 14, 10, 10, 10, 9, 10, 9, 18, 46, 13, 46, 40, 20, 34, 60])

us_add = [r[0] for r in prop_rows if r[4] == 'Add']
ca_add = [r[0] for r in prop_rows if r[5] == 'Add']
paste = [[k, '', ''] for k in []]
ws2 = sheet(wb, 'Paste - USA add', ['Keyword (add to USA campaign)', 'Tags'],
            [[r[0], r[18]] for r in prop_rows if r[4] == 'Add'], [52, 50])
ws3 = sheet(wb, 'Paste - Canada add', ['Keyword (add to Canada campaign)', 'Tags'],
            [[r[0], r[18]] for r in prop_rows if r[5] == 'Add'], [52, 50])

cur_rows = []
for k in CUR_US:
    cur_rows.append([k, 'USA', 'AI / business' if any(f in k + ' ' for f in AI_FLAG) else 'Digital marketing', 'Remove' if k in REMOVE else 'Keep', REMOVE.get(k, '')])
for k in CUR_CA:
    cur_rows.append([k, 'Canada', 'AI / business' if any(f in k + ' ' for f in AI_FLAG) else 'Digital marketing', 'Remove' if k in REMOVE else 'Keep', REMOVE.get(k, '')])
ws4 = sheet(wb, 'Current tracked set', ['Keyword', 'Campaign', 'Topic', 'Recommendation', 'Reason'], cur_rows, [52, 10, 18, 15, 60])

ws5 = sheet(wb, 'Not recommended', ['Keyword(s)', 'Demand seen', 'Why not'], EXCLUDED, [60, 22, 90])
ws6 = sheet(wb, 'SERP check', ['Query (google.com, gl=us)', 'Mujo in top 10', 'Who ranks / intent'],
            [[q, ('not in top 10' if r == 0 else f'#{r}'), n] for q, (r, n) in SERP.items()], [52, 16, 100])
ws7 = sheet(wb, 'Competitors', ['Domain', 'Action', 'Campaign', 'Why'], COMPETITORS, [22, 14, 12, 90])

# ---- Read me / summary with live formulas
P = "'Proposed keywords'"
C = "'Current tracked set'"
n = len(prop_rows) + 1
lines = [
    ('Mujo Learning Systems: AI and business keywords for Semrush position tracking', None),
    ('Prepared 2026-11-21 by Francis (ThinkProfits SEO) for Brittni\'s request in #mujo, 2026-11-07: "change the tracked keywords in SemRush to reflect the keywords we want to target ... the current ones don\'t include any of the AI or business titles for either higher ed or hs."', None),
    ('', None),
    ('Summary', 'h'),
    ('Keywords proposed (all tiers)', f'=COUNTA({P}!A2:A{n})'),
    ('Tier 1: core', f'=COUNTIF({P}!D2:D{n},"Tier 1: core")'),
    ('Tier 2: watch', f'=COUNTIF({P}!D2:D{n},"Tier 2: watch")'),
    ('New keywords for the USA campaign', f'=COUNTIF({P}!E2:E{n},"Add")'),
    ('New keywords for the Canada campaign', f'=COUNTIF({P}!F2:F{n},"Add")'),
    ('Proposed keywords already tracked (USA)', f'=COUNTIF({P}!E2:E{n},"Yes (keep)")'),
    ('Mujo already #1-3 on the live SERP (defend)', f'=COUNTIF({P}!M2:M{n},"#1*")+COUNTIF({P}!M2:M{n},"#2*")+COUNTIF({P}!M2:M{n},"#3*")'),
    ('Mujo not in the live top 10 (gap to close)', f'=COUNTIF({P}!M2:M{n},"not in top 10*")'),
    ('Current USA campaign size', f'=COUNTIF({C}!B2:B{len(cur_rows) + 1},"USA")'),
    ('Current Canada campaign size', f'=COUNTIF({C}!B2:B{len(cur_rows) + 1},"Canada")'),
    ('Current keywords on AI / business topics (both campaigns)', f'=COUNTIF({C}!C2:C{len(cur_rows) + 1},"AI / business")'),
    ('Suggested removals (both campaigns, optional)', f'=COUNTIF({C}!D2:D{len(cur_rows) + 1},"Remove")'),
    ('', None),
    ('How to use this workbook', 'h'),
    ('1. Brittni approves the list on "Proposed keywords" (Tier 1 at minimum). Keyword choices are proposals until she signs off (standing rule, 2026-01-22).', None),
    ('2. Add the "Paste - USA add" list to Semrush project 2160205, USA campaign, and "Paste - Canada add" to the Canada campaign. Paste the tags too, so AI/business visibility can be reported on its own.', None),
    ('3. Optional: remove the 6 keywords flagged on "Current tracked set" (typos, duplicates, off-target).', None),
    ('4. Swap businessu.org (now redirects to Stukent) for g-w.com or routledge.com on "Competitors".', None),
    ('', None),
    ('Read before you report on it', 'h'),
    ('Visibility will DROP the month these are added. Many new keywords start outside the top 20, and Semrush visibility is an average across the campaign. That drop is the new baseline, not a ranking loss. Report AI/business tags separately from the legacy digital-marketing set.', None),
    ('Keyword Planner rounds and buckets volumes, and many niche educator phrases show 0 even though GSC records real impressions on them. GSC impressions (16 months) are the better demand signal here. Volumes are US/Canada monthly averages, Nov 2025 to Oct 2026.', None),
    ('SERP positions are a one-off manual check of google.com with gl=us, hl=en and personalisation off, on 2026-11-21, from outside the US. Semrush will report its own, more reliable numbers once tracking starts.', None),
    ('Tracking a keyword makes no claim. But "principles of business marketing and finance" and "foundations of artificial intelligence" are state CTE course names (Texas, Georgia). Don\'t claim TEKS/state alignment in page copy unless Mujo confirms it; the pages make no such claim today.', None),
    ('Never target "AI-generated textbook" style terms: content is 100% human authored (Shawn, 2026-04-30).', None),
    ('', None),
    ('Sources', 'h'),
    ('Google Search Console, sc-domain:mujo.com, query x page x country, 2025-07-20 to 2026-11-18 (37,921 rows); AI/business pages only, brand and blog excluded.', None),
    ('Google Ads Keyword Planner (ThinkProfits account), US (geo 2840) and Canada, 213 candidate keywords plus 3 idea expansions.', None),
    ('Live Google SERPs, 37 queries, 2026-11-21 (see "SERP check").', None),
    ('Semrush monthly report PDF, 2026-11-06 (October data), for the current tracked sets. Semrush API units were at zero on 2026-11-21, so nothing was pulled or changed in Semrush directly.', None),
    ('Competitor and state CTE course scan (web research, 2026-11-21): McGraw Hill, Pearson, Cengage, Stukent, Savvas, iCEV, Code.org, Georgia/Florida/Texas/SC CTE frameworks.', None),
    ('Mujo pages, canonicals and titles fetched live 2026-11-21.', None),
    ('', None),
    ('Reusable: build_workbook.py, candidates.py and gsc_ai_business.py in this folder regenerate everything. Swap the inputs to redo this for another product family.', None),
]
for i, (a, b) in enumerate(lines, start=1):
    ws0.cell(row=i, column=1, value=a)
    if b == 'h':
        ws0.cell(row=i, column=1).font = Font(name=ARIAL, size=12, bold=True, color='1F3864')
    else:
        ws0.cell(row=i, column=1).font = BODY
        if b:
            c = ws0.cell(row=i, column=2, value=b)
            c.font = BOLD
            c.number_format = '0'
    ws0.cell(row=i, column=1).alignment = Alignment(wrap_text=True, vertical='top')
ws0['A1'].font = Font(name=ARIAL, size=14, bold=True, color='1F3864')
ws0.column_dimensions['A'].width = 120
ws0.column_dimensions['B'].width = 12
wb.save(OUT)
print('saved', OUT, 'proposed', len(prop_rows), 'US add', len(us_add), 'CA add', len(ca_add), 'current', len(CUR_US), len(CUR_CA))
