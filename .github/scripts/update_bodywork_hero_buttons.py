from pathlib import Path

p = Path('bodywork.html')
t = p.read_text()
old = '<div class="actions"><a class="btn btn-primary" href="#booking">Book the 4-Session Series</a><a class="btn btn-secondary" href="#starter">See What’s Included</a></div>'
new = '<div class="actions"><a class="btn btn-primary" href="#starter">Explore the 4-Session Intensive</a><a class="btn btn-secondary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Book Single Session</a></div>'
if t.count(old) != 1:
    raise SystemExit(f'Expected one hero button block, found {t.count(old)}')
p.write_text(t.replace(old, new, 1))
