from pathlib import Path
import re

p = Path('bodywork.html')
t = p.read_text()

old_offer_booking = '''<div class="actions"><a class="btn btn-primary" href="#booking">Book the 4-Session Series</a></div><p style="font-size:.86rem;margin-top:1.25rem">If you would rather start with one appointment, <a href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank" style="text-decoration:underline;text-underline-offset:3px">individual sessions are still available.</a></p><!-- TODO before merge: replace the current scheduler href with the dedicated Acuity series appointment URL once that appointment type exists. -->'''

embedded = '''<div class="embedded-booking-shell" id="booking">
  <div class="booking-intro">
    <div>
      <h3>Start the 4-Session Series</h3>
      <p>Choose a time for your first 75-minute bodywork session. Scheduling, intake, and payment happen here without leaving the page.</p>
    </div>
    <div class="booking-meta">4 sessions · $560</div>
  </div>
  <div class="scheduler-frame-wrap">
    <iframe allow="payment" frameborder="0" height="900" id="acuity-scheduler" loading="lazy" src="https://movementandbodywork.as.me/bodywork" title="Book bodywork and movement" width="100%"></iframe>
  </div>
  <div class="scheduler-fallback">
    <p>If the scheduler does not load in your browser, open the secure booking page directly.</p>
    <a class="btn btn-secondary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Open Secure Booking</a>
  </div>
</div>
<p style="font-size:.86rem;margin-top:1.25rem">If you would rather start with one appointment, <a href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank" style="text-decoration:underline;text-underline-offset:3px">individual sessions are still available.</a></p>'''

if old_offer_booking not in t:
    raise SystemExit('Could not find current starter CTA/fallback block')
t = t.replace(old_offer_booking, embedded, 1)

# Remove the later separate Booking section now that the uploaded Acuity embed lives directly under the offer.
t2, n = re.subn(r'\n*<section class="section-line" id="booking">.*?</section>\n*', '\n', t, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'Expected one later booking section, found {n}')
t = t2

# Point direct booking navigation to the embedded scheduler under the offer.
t = t.replace('<a class="book" href="#starter">Start →</a>', '<a class="book" href="#booking">Book →</a>', 1)
t = t.replace('<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#starter">Start the 4-Session Series</a></div>', '<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#booking">Start the 4-Session Series</a></div>', 1)

p.write_text(t)
