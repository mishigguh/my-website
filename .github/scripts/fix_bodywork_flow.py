from pathlib import Path
import re

p = Path('bodywork.html')
t = p.read_text()

# Sweep stale pricing references first.
t = t.replace('$435', '$560').replace('"435"', '"560"').replace('$290', '$415')
t = t.replace('one individualized movement-practice session', 'one 60-minute individualized movement-practice session')

# Hero should lead to the offer explanation, not a duplicate booking block.
t = t.replace('href="#booking">Start the 4-Session Series</a><a class="btn btn-secondary" href="#starter">See What’s Included</a>', 'href="#starter">Start the 4-Session Series</a><a class="btn btn-secondary" href="#starter">See What’s Included</a>')

# In the main offer, make the CTA the actual purchase action and keep only the requested single-session fallback.
old_offer_tail = '''<div class="actions"><a class="btn btn-primary" href="#booking">Start the 4-Session Series</a></div></article></div></section>'''
new_offer_tail = '''<div class="actions"><a class="btn btn-primary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Start the 4-Session Series — $560</a></div><p style="font-size:.86rem;margin-top:1.25rem">If you would rather start with one appointment, <a href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank" style="text-decoration:underline;text-underline-offset:3px">individual sessions are still available.</a></p><!-- TODO before merge: replace the current scheduler href with the dedicated Acuity series appointment URL once that appointment type exists. --></article></div></section>'''
if old_offer_tail not in t:
    raise SystemExit('main offer tail not found')
t = t.replace(old_offer_tail, new_offer_tail, 1)

# Rename and simplify the first-session section. It should explain the visit, not resell the series.
pattern = re.compile(r'<section class="section-line" id="first-session">.*?</section>', re.S)
m = pattern.search(t)
if not m:
    raise SystemExit('first-session section not found')
first_session = '''<section class="section-line" id="first-session"><div class="wrap reveal"><span class="section-heading">What to Expect on Your First Session</span><h2 class="section-title">A conversation, careful work, and time to notice what changes.</h2><p class="section-note">For most new clients, 75 minutes gives us enough room to understand the problem and begin working without rushing.</p><div class="first-session-grid"><div class="first-session-step"><div class="step-label">01 · Talk</div><h3>We begin with your history.</h3><p>I review your intake, ask what matters most today, and learn what you have already tried.</p></div><div class="first-session-step"><div class="step-label">02 · Work</div><h3>We choose a place to start.</h3><p>The session may include sustained pressure, long holds, movement, breath, traction, or guided awareness.</p></div><div class="first-session-step"><div class="step-label">03 · Reassess</div><h3>We check what changed.</h3><p>We may move, compare sides, or retest the original concern before deciding what deserves attention next.</p></div></div><div class="section-cta"><p>Your feedback is part of the work. You do not need the right words—only a willingness to notice and respond.</p></div></div></section>'''
t = t[:m.start()] + first_session + t[m.end():]

# Remove the duplicated purchase/booking section entirely.
t, count = re.subn(r'\n<section class="section-line" id="booking">.*?</section>\n', '\n', t, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'duplicate booking section removal count={count}')

# Navigation/mobile CTA targets should point to the main offer now that #booking is gone.
t = t.replace('href="#booking">Start →</a>', 'href="#starter">Start →</a>')
t = t.replace('href="#booking">Start the 4-Session Series</a>', 'href="#starter">Start the 4-Session Series</a>')
t = t.replace('href="#booking">Start the 4-Session Series →</a>', 'href="#starter">Start the 4-Session Series →</a>')

# Make sure no stale pricing remains.
for stale in ['$435', '$290', 'price":"435"']:
    if stale in t:
        raise SystemExit(f'stale price remains: {stale}')

# Make sure duplicate booking heading is gone and new heading is present.
if 'Purchase the four-session series and choose your first appointment.' in t:
    raise SystemExit('duplicate booking language still present')
if 'What to Expect on Your First Session' not in t:
    raise SystemExit('new first-session heading missing')

p.write_text(t)
