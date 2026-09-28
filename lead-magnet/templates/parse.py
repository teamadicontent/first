import re,json,sys
src=open(sys.argv[1]).read()
issues=re.split(r'(?m)^# (Issue #\S+ — [^\n]*)$',src)
out=[]
for i in range(1,len(issues),2):
    head=issues[i]; body=issues[i+1]
    era='KLEO' if '[KLEO]' in head else 'LC'
    date=re.search(r'— (.*?) `',head).group(1)
    for m in re.finditer(r'(?ms)^## (T[\w.-]+) — (.*?)\n(.*?)(?=^## T|^### |\Z)',body):
        tid,title,b=m.groups()
        g=lambda k:(re.search(r'\*\*'+k+r':\*\*\s*(.*)',b) or [None,''])[1].strip()
        sk=re.search(r'```\n(.*?)```',b,re.S)
        sk=sk.group(1).strip() if sk else ''
        lines=[l for l in sk.splitlines() if l.strip()]
        out.append(dict(id=tid,title=title.strip(),era=era,date=date,principle=g('Principle'),best_for=g('Best for'),tier=g('Material Tier')[:1],requires=g('Requires'),note=g('Note'),hook=' / '.join(lines[:2]),skel_lines=len(lines)))
json.dump(out,open('templates.json','w'),indent=1)
print(len(out)); from collections import Counter; print(Counter(t['tier'] for t in out), Counter(t['era'] for t in out))
print([t['id'] for t in out if not t['tier'] or not t['hook']])
