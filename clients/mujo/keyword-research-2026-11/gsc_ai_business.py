"""Aggregate GSC query x page x country rows for Mujo's AI and business pages.
Input: raw GSC export JSON files (args). Output: gsc-ai-business-queries.csv next to this script.
Reusable: change PAGE_PAT / BRAND to re-run for another product family."""
import json, re, sys, csv, collections, os
PAGE_PAT = re.compile(r'(ai-|artificial|business|prompt|generative|entrepreneur|healthcare|accounting|large-language|/ai/)')
BLOG = '/teacher-blog/'
BRAND = re.compile(r'mujo|mojo')
rows = []
for f in sys.argv[1:]:
    rows += json.loads(json.load(open(f, encoding='utf-8'))['result'])['rows']
print('rows', len(rows))
agg = collections.defaultdict(lambda: {'clk':0,'imp':0,'possum':0.0,'usa_imp':0,'usa_clk':0,'usa_pos':0.0,'can_imp':0,'can_clk':0,'can_pos':0.0,'pages':collections.Counter()})
for x in rows:
    p = x['page'].split('?')[0]
    if not PAGE_PAT.search(p) or BLOG in p: continue
    q = x['query'].strip().lower()
    if BRAND.search(q): continue
    a = agg[q]
    a['clk'] += x['clicks']; a['imp'] += x['impressions']; a['possum'] += x['position']*x['impressions']
    c = x['country']
    if c in ('usa','can'):
        a[c+'_imp'] += x['impressions']; a[c+'_clk'] += x['clicks']; a[c+'_pos'] += x['position']*x['impressions']
    a['pages'][p.replace('https://www.mujo.com','')] += x['impressions']
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gsc-ai-business-queries.csv')
with open(out, 'w', newline='', encoding='utf-8') as fh:
    w = csv.writer(fh)
    w.writerow(['query','clicks','impressions','avg_pos','usa_clicks','usa_impr','usa_pos','can_clicks','can_impr','can_pos','top_page','n_pages'])
    for q,a in sorted(agg.items(), key=lambda kv: -kv[1]['imp']):
        f = lambda s,i: round(s/i,1) if i else ''
        w.writerow([q,a['clk'],a['imp'],f(a['possum'],a['imp']),a['usa_clk'],a['usa_imp'],f(a['usa_pos'],a['usa_imp']),a['can_clk'],a['can_imp'],f(a['can_pos'],a['can_imp']),a['pages'].most_common(1)[0][0],len(a['pages'])])
print('queries', len(agg), '->', out)
