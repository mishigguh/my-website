"""Build the static practice page from the reviewed content file. No packages required."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT/'content/environmental-movement-practice.json').read_text(encoding='utf-8'))
e = lambda value: escape(str(value), quote=True)

def bullets(items):
    return '<ul>' + ''.join(f'<li>{e(item)}</li>' for item in items) + '</ul>'

def practice(p):
    videos = ''
    if p['videos']:
        videos = '<div class="emp-videos"><h4>Demonstrations</h4><ul>' + ''.join(f'<li><a href="{e(v["url"])}" target="_blank" rel="noopener noreferrer">{e(v["label"])} <span aria-hidden="true">↗</span><span class="emp-sr"> (opens in a new tab)</span></a></li>' for v in p['videos']) + '</ul></div>'
    return f'''<details class="emp-practice" id="practice-{e(p['id'])}">
      <summary><span><span class="emp-label">Phase {e(p['phase'])}</span><span class="emp-practice-title">{e(p['name'])}</span><span class="emp-practice-description">{e(p['description'])}</span></span><span class="emp-expand" aria-hidden="true"></span></summary>
      <div class="emp-practice-body"><p class="emp-purpose">{e(p['purpose'])}</p><div class="emp-prescription"><strong>Example prescription</strong><span>{e(p['prescription'])}</span></div>
      <div class="emp-practice-columns"><div><h4>Practice</h4>{bullets(p['instructions'])}</div><div><h4>Coaching cues</h4>{bullets(p['cues'])}<h4>Progression or adjustment</h4><p>{e(p['progression'])}</p></div></div>{videos}</div>
    </details>'''

domains = []
sections = []
for i, g in enumerate(DATA['groups'], 1):
    examples = [p for p in DATA['practices'] if p['group']==g['id']]
    if examples:
        domains.append(f'<a class="emp-domain" href="#group-{e(g["id"])}"><span class="emp-domain-number">{i:02d}</span><h3>{e(g["title"])}</h3><p>{e(g["description"])}</p><span class="emp-domain-link">Explore the practices <span aria-hidden="true">↗</span></span></a>')
        sections.append(f'<section class="emp-practice-group" id="group-{e(g["id"])}" aria-labelledby="group-title-{e(g["id"])}"><div class="emp-group-heading"><h3 id="group-title-{e(g["id"])}">{e(g["title"])}</h3><span>{len(examples)} practice example{"s" if len(examples)!=1 else ""}</span></div>' + ''.join(practice(p) for p in examples) + '</section>')
    else:
        domains.append(f'<article class="emp-domain"><span class="emp-domain-number">{i:02d}</span><h3>{e(g["title"])}</h3><p>{e(g["description"])}</p></article>')

if not DATA['practices']:
    sections.append('<div class="emp-placeholder"><p class="emp-label">Draft section</p><h3>Practice examples are being prepared.</h3><p>Selected exercises, coaching cues, and demonstrations will be added here.</p></div>')

url = 'https://mishalantsov.com/environmental-movement-practice'
schema = {'@context':'https://schema.org','@graph':[
    {'@type':'WebPage','@id':url+'#page','url':url,'name':DATA['title'],'description':'Individualized movement education with Misha Lantsov and Ian, illustrated through practices in environmental parkour, jumping, acrobatics, coordination, and physical preparation.','inLanguage':'en','about':{'@id':url+'#practice'},'author':[{'@id':'https://mishalantsov.com/#misha-lantsov'},{'@id':url+'#ian'}]},
    {'@type':'Service','@id':url+'#practice','name':DATA['title'],'serviceType':'Individualized remote movement coaching','url':url,'provider':[{'@id':'https://mishalantsov.com/#misha-lantsov'},{'@id':url+'#ian'}]},
    {'@type':'Person','@id':'https://mishalantsov.com/#misha-lantsov','name':'Misha Lantsov','url':'https://mishalantsov.com/'},
    {'@type':'Person','@id':url+'#ian','name':'Ian'},
    {'@type':'ItemList','name':'Practice examples','itemListElement':[{'@type':'ListItem','position':i,'name':p['name'],'url':url+'#practice-'+p['id']} for i,p in enumerate(DATA['practices'],1)]}
]}
if not DATA['practices']:
    schema['@graph'] = [item for item in schema['@graph'] if item['@type']!='ItemList']

template = (ROOT/'templates/environmental-movement-practice.html').read_text(encoding='utf-8')
html = template.replace('{{domains}}','\n'.join(domains)).replace('{{practice_groups}}','\n'.join(sections)).replace('{{schema}}',json.dumps(schema,ensure_ascii=False,indent=2).replace('<','\\u003c'))
(ROOT/'environmental-movement-practice.html').write_text(html,encoding='utf-8')
print(f'Built {len(DATA["practices"])} practice examples into environmental-movement-practice.html')
