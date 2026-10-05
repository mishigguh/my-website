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

ICONS = {
    'environment': '<path d="M7 48h50M10 40l13-17 10 13 9-12 13 16M43 13v10M39 19h8"/><circle cx="15" cy="13" r="3"/>',
    'design': '<rect x="15" y="11" width="34" height="43" rx="3"/><path d="M25 11v-3h14v3M23 25h18M23 33h18M23 41h11"/>',
    'material': '<path d="M7 16h20l5 5 5-5h20v34H37l-5 5-5-5H7zM32 21v34M14 26h10M14 34h10M40 27l9 6-9 6z"/>',
    'jumping': '<path d="M7 51h13M43 44h14M15 40c6-28 28-29 36-7" stroke-dasharray="2 5"/><circle cx="31" cy="17" r="3"/><path d="M29 24l6 9-9 5-7 10M35 33l8 7M29 24l-9-1M29 24l10-5"/>',
    'review': '<rect x="8" y="13" width="48" height="33" rx="3"/><path d="M29 23l12 7-12 7zM23 54h18M32 46v8"/>',
    'refinement': '<path d="M14 27a19 19 0 0 1 33-10M47 8v9H38M50 37a19 19 0 0 1-33 10M17 56v-9h9M24 32l6 6 11-12"/>',
    'acrobatics': '<path d="M8 54h48M23 52l9-15 9 15M32 37V24M32 24L20 8M32 24L46 10"/><circle cx="32" cy="44" r="3"/>',
    'strength': '<circle cx="35" cy="12" r="4"/><path d="M34 21l-9 13 17 4-8 15M25 34l-11 5 8 14M34 21l12 7M21 53h18M43 8v11M48 6v15M39 13h13"/>',
    'rolling': '<path d="M8 52h48M19 42c-13-18 0-34 16-30 20 5 20 33 1 33-12 0-17-16-7-21 7-4 15 4 10 10M12 42h8V34"/>',
    'climbing': '<path d="M7 12h50M19 12v15M45 12v15M15 52h12V41h13V30h15"/><circle cx="19" cy="31" r="4"/><circle cx="45" cy="31" r="4"/>',
    'creative': '<path d="M13 44c-1-29 38-32 38-7 0 15-27 20-29 0-1-10 11-13 16-8" stroke-dasharray="3 4"/><circle cx="13" cy="47" r="4"/><path d="M34 25l6 4-5 5M49 15l4-5 4 5-4 5z"/>'
}

def icon(name, extra_class=''):
    return f'<svg class="emp-icon {e(extra_class)}" width="64" height="64" viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'

def paragraphs(items):
    return ''.join(f'<p>{e(item)}</p>' for item in items)

domains = [f'<article class="emp-domain"><div class="emp-domain-meta">{icon(g["icon"])}</div><h3>{e(g["title"])}</h3><p>{e(g["description"])}</p></article>' for g in DATA['groups']]
loop = [f'<li>{icon(node["icon"])}<span class="emp-loop-label">{e(node["title"])}</span>' + ('<span class="emp-loop-arrow" aria-hidden="true">→</span>' if i<len(DATA['loop'])-1 else '') + '</li>' for i,node in enumerate(DATA['loop'])]
steps = [f'<li><span class="emp-step-number" aria-hidden="true">{i:02d}</span><div><h3>{e(s["title"])}</h3><p>{e(s["description"])}</p></div></li>' for i,s in enumerate(DATA['steps'],1)]
formats = [f'<article><h3>{e(f["title"])}</h3><p>{e(f["description"])}</p></article>' for f in DATA['formats']]
milestones = [f'<div><dt>{e(m["title"])}</dt><dd>{e(m["criterion"])}</dd></div>' for m in DATA['milestones']]

sections = []
for g in DATA['groups']:
    examples = [p for p in DATA['practices'] if p['group']==g['id']]
    if examples:
        sections.append(f'<section class="emp-practice-group" id="group-{e(g["id"])}" aria-labelledby="group-title-{e(g["id"])}"><div class="emp-group-heading"><h3 id="group-title-{e(g["id"])}">{e(g["title"])}</h3></div>'+''.join(practice(p) for p in examples)+'</section>')

url = 'https://mishalantsov.com/environmental-movement-practice'
schema = {'@context':'https://schema.org','@graph':[
    {'@type':'WebPage','@id':url+'#page','url':url,'name':DATA['title'],'description':DATA['subtitle'],'inLanguage':'en','about':{'@id':url+'#practice'},'author':[{'@id':'https://mishalantsov.com/#misha-lantsov'},{'@id':url+'#ian'}]},
    {'@type':'Service','@id':url+'#practice','name':DATA['title'],'serviceType':'Individualized remote movement coaching','url':url,'provider':[{'@id':'https://mishalantsov.com/#misha-lantsov'},{'@id':url+'#ian'}]},
    {'@type':'Person','@id':'https://mishalantsov.com/#misha-lantsov','name':'Misha Lantsov','url':'https://mishalantsov.com/'},
    {'@type':'Person','@id':url+'#ian','name':'Ian'},
    {'@type':'ItemList','name':'Practice examples','itemListElement':[{'@type':'ListItem','position':i,'name':p['name'],'url':url+'#practice-'+p['id']} for i,p in enumerate(DATA['practices'],1)]}
]}
if not DATA['practices']:
    schema['@graph'] = [item for item in schema['@graph'] if item['@type']!='ItemList']

template = (ROOT/'templates/environmental-movement-practice.html').read_text(encoding='utf-8')
replacements = {
    'domains':'\n'.join(domains), 'loop':'\n'.join(loop), 'steps':'\n'.join(steps),
    'formats':'\n'.join(formats), 'milestones':'\n'.join(milestones), 'practice_examples':'\n'.join(sections),
    'subtitle':e(DATA['subtitle']), 'system_copy':paragraphs(DATA['system']),
    'return_icon':icon('refinement'), 'milestone_intro':e(DATA['milestone_intro']),
    'difference':paragraphs(DATA['difference']), 'cta_heading':e(DATA['cta']['heading']),
    'cta_body':e(DATA['cta']['body']), 'cta_button':e(DATA['cta']['button']),
    'schema':json.dumps(schema,ensure_ascii=False,indent=2).replace('<','\\u003c')
}
html=template
for key,value in replacements.items():
    html=html.replace('{{'+key+'}}',value)
if '{{' in html:
    raise ValueError('Unresolved template placeholder')
html='\n'.join(line.rstrip() for line in html.splitlines())+'\n'
(ROOT/'environmental-movement-practice.html').write_text(html,encoding='utf-8',newline='\n')
print(f'Built methodology page: {len(DATA["groups"])} domains, {len(DATA["steps"])} coaching steps, {len(DATA["milestones"])} milestones.')
