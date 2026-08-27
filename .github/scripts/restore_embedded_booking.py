from pathlib import Path
import re

p = Path('bodywork.html')
t = p.read_text()

def replace_once(old, new, label):
    global t
    n = t.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 exact match, got {n}')
    t = t.replace(old, new, 1)

# Route primary CTAs to the embedded booking section.
t = t.replace('<li><a class="book" href="#starter">Start →</a></li>', '<li><a class="book" href="#booking">Book →</a></li>', 1)
t = t.replace('<a class="btn btn-primary" href="#starter">Start the 4-Session Series</a>', '<a class="btn btn-primary" href="#booking">Book the 4-Session Series</a>', 1)

# The offer section should explain the offer, then send people to booking below.
replace_once(
    '<div class="actions"><a class="btn btn-primary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Start the 4-Session Series — $560</a></div>',
    '<div class="actions"><a class="btn btn-primary" href="#booking">Book the 4-Session Series</a></div>',
    'starter CTA'
)

# Restore the embedded Acuity booking block without repeating pricing or series explanation.
if 'id="booking"' in t:
    raise SystemExit('booking section already exists')

booking = '''<section class="section-line" id="booking"><div class="wrap reveal"><span class="section-heading">Booking</span><h2 class="section-title">Choose your appointment.</h2><p class="section-note">Use the secure scheduler below to choose a time that works for you.</p><div class="embedded-booking-shell"><div class="booking-intro"><div><h3>Book online</h3><p>The four-session Bodywork + Movement Series is the recommended starting point. Individual sessions are also available.</p></div><div class="booking-meta">Secure booking through Acuity</div></div><div class="scheduler-frame-wrap"><iframe allow="payment" frameborder="0" height="900" id="acuity-scheduler" loading="lazy" src="https://movementandbodywork.as.me/bodywork" title="Book bodywork and movement" width="100%"></iframe></div><div class="scheduler-fallback"><p>If the scheduler does not load in your browser, open the secure booking page directly.</p><a class="btn btn-secondary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Open Secure Booking</a></div></div></div></section>'''

marker = '<section class="crossover">'
idx = t.find(marker)
if idx < 0:
    raise SystemExit('crossover section not found')
t = t[:idx] + booking + '\n' + t[idx:]

# Mobile booking bar should jump to the embedded scheduler.
t = re.sub(
    r'<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#[^"]+">.*?</a></div>',
    '<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#booking">Book</a></div>',
    t,
    count=1,
)

p.write_text(t)
