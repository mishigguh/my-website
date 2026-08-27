from pathlib import Path
import re

p = Path('bodywork.html')
t = p.read_text()

def sub_once(pattern, repl, label, flags=re.S):
    global t
    t2, n = re.subn(pattern, repl, t, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 match, got {n}')
    t = t2

# Nav: one primary sales path.
sub_once(
    r'<nav aria-label="Primary navigation">.*?</nav>',
    '''<nav aria-label="Primary navigation"><a class="nav-mark" href="/">Misha Bodywork &amp; Movement</a><ul class="nav-links"><li><a href="#approach">Approach</a></li><li><a href="#fit">Good Fit</a></li><li><a href="#starter">Series</a></li><li><a href="#reviews">Reviews</a></li><li><a href="#location">Location</a></li><li><a href="#faq">FAQ</a></li><li><a class="book" href="#booking">Start →</a></li></ul></nav>''',
    'nav'
)

hero = '''<header class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">Therapeutic Bodywork · Downtown Golden, Colorado</span><h1>For pain that keeps returning, and bodies that want more options.</h1><p class="lead">Thoughtful, hands-on work for injuries, chronic tension, and movement patterns that have stopped changing. Each session is collaborative, unhurried, and built around attention.</p><div class="actions"><a class="btn btn-primary" href="#booking">Start the 4-Session Series</a><a class="btn btn-secondary" href="#starter">See What’s Included</a></div></div></div></header>'''
sub_once(r'<header class="hero">.*?</header>', hero, 'hero')

# Capture and remove existing experience section, then move it directly after hero.
experience_pat = r'<section class="section-line"><div class="wrap split reveal"><div><span class="section-heading">Experience</span>.*?</section>'
m = re.search(experience_pat, t, re.S)
if not m:
    raise SystemExit('experience section not found')
experience = m.group(0)
t = t[:m.start()] + t[m.end():]
idx = t.find('</header>') + len('</header>')
t = t[:idx] + experience + t[idx:]

# Replace starter offer with package-first language and fit guarantee.
starter = '''<section class="section-line" id="starter"><div class="wrap reveal"><span class="section-heading">Start Here</span><h2 class="section-title">The way I recommend beginning.</h2><p class="section-note">A single session can change how you feel. Four sessions give us enough time to see what actually changes, what returns, and how hands-on work, self-release, and movement fit together for your specific case.</p><article class="starter-card"><div class="session-label">4-Session Bodywork + Movement Series</div><div class="price">$435</div><span class="price-note">Three bodywork sessions · one individualized movement session</span><ul class="starter-list"><li><strong>01 · Understand &amp; begin.</strong> A 75-minute bodywork session to understand your history, work hands-on, and reassess what changes.</li><li><strong>02 · Follow the pattern.</strong> A second bodywork session based on what changed and what returned. This is often where I teach you a simple therapy-ball self-release practice to use between visits.</li><li><strong>03 · Go deeper.</strong> A third bodywork session that continues from what we have learned rather than starting over each time.</li><li><strong>04 · Put it into movement.</strong> An individualized movement-practice session focused on patterns relevant to you—closer to personal training than a group class or generic workout.</li></ul><p style="margin-top:1rem">The exact order can change based on what we learn. The point is continuity: enough contact to see a pattern, work with it from more than one angle, and leave you with more useful options than you had after the first appointment.</p><div class="section-cta" style="margin-top:1.2rem"><div><strong style="color:var(--ink)">You’re only committed to the first session.</strong><p style="margin-top:.35rem">If after the first visit either of us feels the series is not the right fit, I’ll refund the unused $290. Your first 75-minute session remains at its normal $145 rate.</p></div></div><div class="actions"><a class="btn btn-primary" href="#booking">Start the 4-Session Series</a></div></article></div></section>'''
sub_once(r'<section class="section-line" id="starter">.*?</section>', starter, 'starter')

# Move starter before reviews.
m = re.search(r'<section class="section-line" id="starter">.*?</section>', t, re.S)
if not m:
    raise SystemExit('new starter section not found')
starter_block = m.group(0)
t = t[:m.start()] + t[m.end():]
reviews_pos = t.find('<section class="section-line" id="reviews">')
if reviews_pos < 0:
    raise SystemExit('reviews position not found')
t = t[:reviews_pos] + starter_block + t[reviews_pos:]

# Reframe first-session section as how the series begins, then place it after reviews.
first = '''<section class="section-line" id="first-session"><div class="wrap reveal"><span class="section-heading">How the Series Begins</span><h2 class="section-title">A conversation, careful work, and time to notice what changes.</h2><p class="section-note">The series starts with a 75-minute bodywork session. You do not need to know in advance exactly what the remaining sessions should look like; we use the first visit to learn what is most useful.</p><div class="first-session-grid"><div class="first-session-step"><div class="step-label">01 · Talk</div><h3>We begin with your history.</h3><p>I review your intake, ask what matters most today, and learn what you have already tried.</p></div><div class="first-session-step"><div class="step-label">02 · Work</div><h3>We choose a place to start.</h3><p>The session may include sustained pressure, long holds, movement, breath, traction, or guided awareness.</p></div><div class="first-session-step"><div class="step-label">03 · Reassess</div><h3>We check what changed.</h3><p>We may move, compare sides, or retest the original concern before deciding what deserves attention next.</p></div></div><div class="section-cta"><p>Your feedback is part of the work. After this first visit, we either continue into the rest of the series or, if it is not the right fit, I refund the unused $290.</p><div class="actions" style="margin-top:0"><a class="btn btn-primary" href="#booking">Start the 4-Session Series</a></div></div></div></section>'''
sub_once(r'<section class="section-line" id="first-session">.*?</section>', first, 'first session')
m = re.search(r'<section class="section-line" id="first-session">.*?</section>', t, re.S)
first_block = m.group(0)
t = t[:m.start()] + t[m.end():]
reviews_match = re.search(r'<section class="section-line" id="reviews">.*?</section>', t, re.S)
if not reviews_match:
    raise SystemExit('reviews block not found')
insert = reviews_match.end()
t = t[:insert] + first_block + t[insert:]

# Replace generic embedded-booking block with package-first checkout card.
booking = '''<section class="section-line" id="booking"><div class="wrap reveal"><span class="section-heading">Start the Series</span><h2 class="section-title">Purchase the four-session series and choose your first appointment.</h2><p class="section-note">The series is $435 and begins with a 75-minute bodywork session. Once the dedicated Acuity series appointment is created, this button will take you directly to that checkout and first-session calendar.</p><div class="starter-card"><div class="session-label">4-Session Bodywork + Movement Series</div><div class="price">$435</div><span class="price-note">Pay once · choose session one · arrange the remaining sessions together</span><p>After the first visit, we schedule the remaining two bodywork sessions and individualized movement-practice session based on what we learn.</p><div class="section-cta" style="margin-top:1.2rem"><div><strong style="color:var(--ink)">First-session fit policy</strong><p style="margin-top:.35rem">If after the first visit either of us feels the series is not the right fit, I’ll refund $290 and keep only the normal $145 cost of that first 75-minute session.</p></div></div><div class="actions"><a class="btn btn-primary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Start the 4-Session Series — $435</a></div><p class="microcopy" style="margin-top:1rem">The current button opens my secure Acuity scheduler. A direct series checkout link will replace it once that appointment type is created.</p></div><div style="margin-top:1.5rem"><p style="font-size:.86rem">Prefer to book a single session instead? <a href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank" style="text-decoration:underline;text-underline-offset:3px">Individual bodywork appointments are still available here.</a></p></div></div></section>'''
sub_once(r'<section class="section-line" id="booking">.*?</section>', booking, 'booking')

# Add microcopy class if absent.
if '.microcopy{' not in t:
    t = t.replace('</style>', ".microcopy{font-family:'DM Mono',monospace;font-size:.53rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);line-height:1.6}</style>")

# Final CTA: same purchase decision.
final_cta = '''<section class="final-cta"><div class="wrap"><span class="eyebrow">Begin</span><h2>Relief is useful. Better understanding lasts longer.</h2><p style="max-width:620px">If you want thoughtful, collaborative bodywork—and enough continuity to see what actually changes—start with the four-session Bodywork + Movement Series.</p><div class="actions"><a class="btn btn-clay" href="#booking">Start the 4-Session Series →</a></div></div></section>'''
sub_once(r'<section class="final-cta">.*?</section>', final_cta, 'final CTA')

# Mobile bar follows the same primary offer.
t = re.sub(r'<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#booking">.*?</a></div>', '<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#booking">Start the 4-Session Series</a></div>', t, count=1)

p.write_text(t)
