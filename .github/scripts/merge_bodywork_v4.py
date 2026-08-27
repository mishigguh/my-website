from pathlib import Path
import re

p = Path('bodywork.html')
t = p.read_text()

# Metadata/schema: preserve the GitHub discovery work while reflecting the fuller starter offer.
t = t.replace(
    '<title>Misha Bodywork & Movement — Golden, Colorado</title>',
    '<title>Misha Bodywork & Movement — Therapeutic Bodywork in Golden, Colorado</title>'
)
t = t.replace(
    '<meta name="description" content="Therapeutic bodywork in Golden, Colorado for chronic pain, tension, injuries, and recurring movement patterns. Hands-on body education at the intersection of massage, manual therapy, and movement practice." />',
    '<meta name="description" content="Thoughtful therapeutic bodywork in Golden, Colorado for recurring pain, injuries, chronic tension, and movement patterns. Start with a four-session bodywork and movement process or book an individual session." />'
)
t = t.replace(
    '<meta property="og:title" content="Misha Bodywork & Movement — Golden, Colorado" />',
    '<meta property="og:title" content="Misha Bodywork & Movement — Therapeutic Bodywork in Golden, Colorado" />'
)
t = t.replace(
    '<meta property="og:description" content="Therapeutic bodywork in Golden, Colorado for pain, tension, injuries, and recurring movement patterns." />',
    '<meta property="og:description" content="Thoughtful therapeutic bodywork for recurring pain, injuries, chronic tension, and movement patterns in Golden, Colorado." />'
)
t = t.replace('"priceRange": "$125-$165"', '"priceRange": "$125-$435"')
t = t.replace(
    '{"@type":"Offer","price":"165","priceCurrency":"USD","itemOffered":{"@type":"Service","name":"90-minute bodywork session"}}',
    '{"@type":"Offer","price":"165","priceCurrency":"USD","itemOffered":{"@type":"Service","name":"90-minute bodywork session"}},\n        {"@type":"Offer","price":"435","priceCurrency":"USD","itemOffered":{"@type":"Service","name":"Four-session bodywork and movement starter process","description":"Three 75-minute bodywork sessions, one individualized movement-practice session, and in-person therapy-ball self-release instruction."}}'
)

# Additional styles required by the uploaded V4 conversion flow. No image-slot/placeholder styles are added.
addon_css = r'''

  /* V4 CONVERSION FLOW — merged from the image-led landing page, without image placeholders */
  .section-heading {
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.17em;
    font-size: 0.7rem;
    color: var(--clay);
    margin-bottom: 0.75rem;
    display: block;
  }

  .section-title {
    font-size: clamp(1.8rem, 4vw, 2.9rem);
    line-height: 1.08;
    letter-spacing: -0.03em;
    font-weight: 400;
    margin-bottom: 1.1rem;
  }

  .compact-copy { max-width: 720px; }
  .compact-copy p { font-size: 0.98rem; }

  .fit-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 1.4rem;
  }

  .fit-card {
    border: 1px solid var(--line);
    border-radius: 18px;
    padding: 1.25rem;
    background: rgba(255,250,243,.55);
  }

  .check-list { list-style: none; display: grid; gap: .7rem; }
  .check-list li {
    position: relative;
    padding-left: 1.35rem;
    color: var(--muted);
    font-size: .9rem;
    line-height: 1.55;
  }
  .check-list li::before { content: '—'; position: absolute; left: 0; color: var(--clay); }

  .first-session-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
    margin-top: 1.4rem;
  }

  .first-session-step { border-top: 1px solid var(--line); padding-top: 1rem; }
  .first-session-step .step-label {
    font-family: 'DM Mono', monospace;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    font-size: 0.54rem;
    color: var(--clay);
    margin-bottom: 0.55rem;
  }

  .starter-card {
    max-width: 760px;
    background: linear-gradient(160deg, #fffaf3, #f7ece2);
    border: 1px solid rgba(155,98,72,0.45);
    border-radius: 20px;
    padding: clamp(1.35rem, 3vw, 2rem);
    margin-top: 1.5rem;
  }

  .starter-list { list-style: none; display: grid; gap: .75rem; margin-top: 1.1rem; }
  .starter-list li {
    color: var(--muted);
    font-size: .9rem;
    line-height: 1.6;
    padding-left: 1.2rem;
    position: relative;
  }
  .starter-list li::before { content: '·'; position: absolute; left: 0; color: var(--clay); }
  .starter-list strong { color: var(--ink); }

  .single-session-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: .85rem;
    margin-top: 1.2rem;
  }
  .single-session {
    border-top: 1px solid var(--line);
    padding-top: .9rem;
  }
  .single-session h3 { font-size: .95rem; }
  .single-session p { font-size: .86rem; }

  .embedded-booking-shell {
    margin-top: 1.5rem;
    border: 1px solid var(--line);
    border-radius: 22px;
    background: var(--white);
    overflow: hidden;
  }

  .booking-intro {
    display: flex;
    justify-content: space-between;
    gap: 1.25rem;
    align-items: end;
    padding: 1.35rem;
    border-bottom: 1px solid var(--line);
  }
  .booking-intro h3 { font-size: 1.05rem; margin-bottom: 0.3rem; }
  .booking-intro p { max-width: 560px; margin: 0; font-size: 0.88rem; }
  .booking-meta {
    flex-shrink: 0;
    font-family: 'DM Mono', monospace;
    font-size: 0.53rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--clay);
  }
  .scheduler-frame-wrap { width: 100%; min-height: 720px; background: var(--paper-soft); }
  .scheduler-frame-wrap iframe { display: block; width: 100%; min-height: 720px; border: 0; background: var(--white); }
  .scheduler-fallback {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    padding: 1rem 1.35rem;
    border-top: 1px solid var(--line);
    background: rgba(245,239,230,0.45);
  }
  .scheduler-fallback p { margin: 0; font-size: 0.82rem; }

  .small-offers {
    margin-top: 1.2rem;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.85rem;
  }
  .small-offer { border-top: 1px solid var(--line); padding-top: 0.9rem; }
  .small-offer h3 { font-size: 0.95rem; }
  .small-offer p { font-size: 0.86rem; }

  .map-fallback {
    margin-top: 0.9rem;
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.9rem;
  }
  .map-fallback p { margin: 0; max-width: 540px; font-size: 0.84rem; }

  .mobile-booking-bar { display: none; }

  @media (max-width: 800px) {
    body { padding-bottom: 68px; }
    .fit-grid, .first-session-grid, .single-session-row, .booking-intro, .small-offers { grid-template-columns: 1fr; }
    .booking-intro, .scheduler-fallback { align-items: flex-start; flex-direction: column; }
    .scheduler-frame-wrap, .scheduler-frame-wrap iframe { min-height: 860px; }
    .mobile-booking-bar {
      display: block;
      position: fixed;
      left: 0;
      right: 0;
      bottom: 0;
      z-index: 100;
      padding: 0.7rem 1rem calc(0.7rem + env(safe-area-inset-bottom));
      background: rgba(39,33,27,0.96);
      backdrop-filter: blur(12px);
      border-top: 1px solid rgba(255,250,243,0.12);
    }
    .mobile-booking-bar a {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 44px;
      border-radius: 999px;
      background: var(--clay);
      color: var(--white);
      font-family: 'DM Mono', monospace;
      font-size: 0.62rem;
      text-transform: uppercase;
      letter-spacing: 0.13em;
    }
  }
'''
if '/* V4 CONVERSION FLOW' not in t:
    t = t.replace('</style>', addon_css + '\n</style>', 1)

nav = '''<nav aria-label="Primary navigation">
  <a class="nav-mark" href="/">Misha Bodywork &amp; Movement</a>
  <ul class="nav-links">
    <li><a href="#approach">Approach</a></li>
    <li><a href="#fit">Good Fit</a></li>
    <li><a href="#first-session">First Session</a></li>
    <li><a href="#reviews">Reviews</a></li>
    <li><a href="#starter">Start</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a class="book" href="#booking">Book →</a></li>
  </ul>
</nav>'''
t, n = re.subn(r'<nav aria-label="Primary navigation">.*?</nav>', nav, t, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'nav replacement failed: {n}')

main = '''<main>
  <header class="hero">
    <div class="wrap hero-grid">
      <div>
        <span class="eyebrow">Therapeutic Bodywork · Downtown Golden, Colorado</span>
        <h1>For pain that keeps returning, and bodies that want more options.</h1>
        <p class="lead">Thoughtful, hands-on work for injuries, chronic tension, and movement patterns that have stopped changing. Each session is collaborative, unhurried, and built around attention.</p>
        <div class="actions">
          <a class="btn btn-primary" href="#starter">See the 4-Session Start</a>
          <a class="btn btn-secondary" href="#booking">Book a Single Session</a>
        </div>
      </div>
    </div>
  </header>

  <section class="section-line" id="approach">
    <div class="wrap split reveal">
      <div>
        <span class="section-heading">Approach</span>
        <h2 class="section-title">It all comes down to attention.</h2>
      </div>
      <div class="compact-copy">
        <p>Most pain and tension is not a single problem in a single place. It is often part of a larger pattern: how you brace, breathe, move, recover, and adapt to old injuries or repeated stress.</p>
        <p>This work weaves together massage, manual therapy, movement practice, and careful observation. The aim is not to force change or follow a fixed routine. It is to provide useful input, notice what responds, and help your body find another option.</p>
        <p>I am not trying to fix your body. I am trying to help you understand it well enough that you can work with it more skillfully.</p>
      </div>
    </div>
  </section>

  <section class="section-line" id="fit">
    <div class="wrap reveal">
      <span class="section-heading">A Good Fit</span>
      <h2 class="section-title">This work is most useful when you want relief and understanding.</h2>
      <div class="fit-grid">
        <div class="fit-card">
          <h3>You may be a good fit if...</h3>
          <ul class="check-list">
            <li>You have tried massage, chiropractic, physical therapy, or exercise, but something still feels unresolved.</li>
            <li>Pain improves for a while and then returns.</li>
            <li>You want to move, train, work, or rest with more confidence.</li>
            <li>You are curious about what your body is doing, not only where it hurts.</li>
            <li>You value careful work, useful feedback, and collaboration.</li>
          </ul>
        </div>
        <div class="fit-card">
          <h3>This may not be the right fit if...</h3>
          <ul class="check-list">
            <li>You are looking for the same routine every visit.</li>
            <li>You want someone to fix a problem without your participation.</li>
            <li>You only want very firm, fast, or painful treatment.</li>
            <li>You are looking for a purely passive spa massage as the whole of the work.</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-line" id="first-session">
    <div class="wrap reveal">
      <span class="section-heading">Your First Session</span>
      <h2 class="section-title">A conversation, careful work, and time to notice what changes.</h2>
      <p class="section-note">For most new clients, 75 minutes gives us enough room to understand the problem and begin working without rushing.</p>
      <div class="first-session-grid">
        <div class="first-session-step">
          <div class="step-label">01 · Talk</div>
          <h3>We begin with your history.</h3>
          <p>I review your intake, ask what matters most today, and learn what you have already tried.</p>
        </div>
        <div class="first-session-step">
          <div class="step-label">02 · Work</div>
          <h3>We choose a place to start.</h3>
          <p>The session may include sustained pressure, long holds, movement, breath, traction, or guided awareness.</p>
        </div>
        <div class="first-session-step">
          <div class="step-label">03 · Reassess</div>
          <h3>We check what changed.</h3>
          <p>We may move, compare sides, or retest the original concern before deciding what deserves attention next.</p>
        </div>
      </div>
      <div class="section-cta">
        <p>Your feedback is part of the work. You do not need the right words—only a willingness to notice and respond.</p>
        <div class="actions" style="margin-top:0;">
          <a class="btn btn-primary" href="#booking">Book Your First Bodywork Session</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-line" id="reviews">
    <div class="wrap reveal">
      <span class="section-heading">What People Say</span>
      <h2 class="section-title">Client words from Google reviews.</h2>
      <div aria-live="polite" class="testimonial-carousel">
        <div class="testimonial-viewport">
          <div class="testimonial-slide" id="testimonial-slide">
            <div class="testimonial-stars" id="testimonial-stars">★★★★★</div>
            <div class="testimonial-text" id="testimonial-text">Best massage therapist in Golden! I have been a loyal client for 5 years now. Misha is great at listening to what you need and also finding the spots you did not even realize needed bodywork. He incorporates stretching and breath work into the massage. The space is nice and he is very professional. Highly recommend!</div>
            <div class="testimonial-author" id="testimonial-author">Lisa Carropen · Google Review</div>
          </div>
        </div>
        <div class="testimonial-controls">
          <div class="testimonial-nav">
            <span class="testimonial-more">Read more</span>
            <button aria-label="Previous review" class="arrow-btn" id="testimonial-prev" type="button"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M14.5 5.5L8 12l6.5 6.5"></path></svg></button>
            <button aria-label="Next review" class="arrow-btn" id="testimonial-next" type="button"><svg aria-hidden="true" viewBox="0 0 24 24"><path d="M9.5 5.5L16 12l-6.5 6.5"></path></svg></button>
          </div>
          <span class="testimonial-count" id="testimonial-count">1 / 7</span>
        </div>
      </div>
    </div>
  </section>

  <section class="section-line" id="starter">
    <div class="wrap reveal">
      <span class="section-heading">Recommended Starting Point</span>
      <h2 class="section-title">Start with four sessions, not just one.</h2>
      <p class="section-note">One session can create relief. Four gives us enough contact to learn what changes, what returns, give you something useful to do between visits, and connect the hands-on work to how you actually move.</p>
      <article class="starter-card">
        <div class="session-label">4-Session Starter Process</div>
        <div class="price">$435</div>
        <span class="price-note">Recommended for new clients</span>
        <ul class="starter-list">
          <li><strong>Three 75-minute bodywork sessions.</strong> Enough time to work hands-on, reassess between visits, and follow the patterns that actually matter.</li>
          <li><strong>One individualized movement-practice session.</strong> Think personal training for movement patterns relevant to your case—not a group class or a generic workout.</li>
          <li><strong>A self-release practice you can use yourself.</strong> During the first or second bodywork visit, I will teach you how I use therapy balls and give you a simple routine to practice between sessions. The tools and technique are shown to you in person.</li>
        </ul>
        <p style="margin-top:1rem;">The exact order can change based on what we learn. The point is to have enough continuity to see a pattern, work with it from more than one angle, and leave you with more agency than you had after the first appointment.</p>
        <div class="actions">
          <a class="btn btn-primary" href="#booking">Book the First Session</a>
        </div>
      </article>

      <div style="margin-top:2.5rem;">
        <span class="section-heading">Single Sessions</span>
        <p class="section-note">If you would rather start with one appointment, individual sessions are still available.</p>
        <div class="single-session-row">
          <div class="single-session"><h3>60 minutes · $125</h3><p>Focused work for one primary area or a general reset when you know what needs attention.</p></div>
          <div class="single-session"><h3>75 minutes · $145</h3><p>The best single-session starting point for most new clients.</p></div>
          <div class="single-session"><h3>90 minutes · $165</h3><p>For deeper work, more complex patterns, or a fuller body session with time to go slow.</p></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-line" id="booking">
    <div class="wrap reveal">
      <span class="section-heading">Book</span>
      <h2 class="section-title">Book your first bodywork session.</h2>
      <p class="section-note">The four-session process begins with a 75-minute bodywork session. Book and pay for that first visit here. If continuing makes sense, we arrange the remaining sessions together in person.</p>
      <div class="embedded-booking-shell">
        <div class="booking-intro">
          <div>
            <h3>First Bodywork Session</h3>
            <p>Seventy-five minutes gives us enough time to talk, work without rushing, and check what changes.</p>
          </div>
          <div class="booking-meta">First visit 75 min · $145 · Starter $435 total</div>
        </div>
        <div class="scheduler-frame-wrap">
          <iframe allow="payment" frameborder="0" height="900" id="acuity-scheduler" loading="lazy" src="https://movementandbodywork.as.me/bodywork" title="Book a bodywork session" width="100%"></iframe>
        </div>
        <div class="scheduler-fallback">
          <p>If the scheduler does not load in your browser, open the secure booking page directly.</p>
          <a class="btn btn-secondary" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Open Secure Booking</a>
        </div>
      </div>
      <div class="small-offers">
        <div class="small-offer">
          <h3>Prefer one session?</h3>
          <p>You can book 60, 75, or 90 minutes through the same scheduler without committing to the four-session process.</p>
        </div>
        <div class="small-offer">
          <h3>Couples instruction</h3>
          <p>I also teach couples simple, careful ways to work on each other at home.</p>
          <div class="actions" style="margin-top:0.9rem;"><a class="btn btn-secondary" href="mailto:misha@mishalantsov.com?subject=Couples%20Bodywork%20Instruction">Inquire Further</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section-line">
    <div class="wrap split reveal">
      <div>
        <span class="section-heading">Experience</span>
        <h2 class="section-title">Seven years working with many kinds of bodies.</h2>
      </div>
      <div class="compact-copy">
        <p>I have worked with people navigating injury histories, surgery history, athletic training, chronic neck and shoulder tension, desk work, age-related mobility concerns, stress, running, pilates, strength training, and movement practice.</p>
        <p>This work is informed by thousands of hours of hands-on practice, study, and personal training in acrobatics, strength, mobility, endurance, and dance. I am also in my fourth year of a five-year Human Movement Studies program with Marcello Palozzo. My own education is active, not finished.</p>
        <p>I try to meet every person where they are—different ages, backgrounds, histories, and relationships to movement.</p>
      </div>
    </div>
  </section>

  <section class="crossover">
    <div class="wrap crossover-inner reveal">
      <div>
        <span class="section-heading">Also at Denver Movement School</span>
        <h2 class="section-title">Bodywork and movement practice pair well.</h2>
        <p>Alongside bodywork, I teach a weekly Tuesday movement class in Denver built around strength, coordination, partner practice, movement skills, play, and physical challenge.</p>
        <p>Bodywork can give you better information about what your body holds. Movement practice gives that information somewhere to go.</p>
        <div class="actions"><a class="btn btn-clay" href="/denver-movement-school">Visit Denver Movement School →</a></div>
      </div>
    </div>
  </section>

  <section class="section-line" id="location">
    <div class="wrap split reveal">
      <div>
        <span class="section-heading">Location</span>
        <h2 class="section-title">Bodywork in downtown Golden.</h2>
      </div>
      <div class="location-block">
        <p class="location-address">1300 Jackson St, Suite B200<br>Golden, CO 80401</p>
        <p>Sessions are held in a shared office building in downtown Golden. Any room-specific arrival details are provided when you book.</p>
        <div class="actions">
          <a class="btn btn-primary" href="https://www.google.com/maps/dir/?api=1&amp;destination=1300+Jackson+St+Suite+B200%2C+Golden%2C+CO+80401" rel="noopener" target="_blank">Get Directions</a>
          <a class="btn btn-secondary" href="https://www.google.com/search?q=Misha+Bodywork+and+Movement+Golden+CO" rel="noopener" target="_blank">View Google Listing</a>
        </div>
        <div aria-label="Map to Misha Bodywork and Movement in downtown Golden" class="map-embed">
          <iframe loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=1300+Jackson+St%2C+Suite+B200%2C+Golden%2C+CO+80401&amp;z=16&amp;output=embed" title="Map to Misha Bodywork and Movement"></iframe>
        </div>
        <div class="map-fallback">
          <p>If the map does not load in your browser, open the location directly in Google Maps.</p>
          <a class="btn btn-secondary" href="https://www.google.com/maps/search/?api=1&amp;query=1300+Jackson+St+Suite+B200%2C+Golden%2C+CO+80401" rel="noopener" target="_blank">Open in Google Maps</a>
        </div>
      </div>
    </div>
  </section>

  <section class="section-line" id="faq">
    <div class="wrap split reveal">
      <div>
        <span class="section-heading">FAQ</span>
        <h2 class="section-title">A few common questions.</h2>
      </div>
      <div class="faq">
        <details>
          <summary>Is this massage?</summary>
          <p>It includes massage and manual therapy, but it is not a fixed massage routine. The work may also include movement, breath, sustained holds, guided attention, and testing or retesting how something feels.</p>
        </details>
        <details>
          <summary>Is this physical therapy?</summary>
          <p>No. This is not medical diagnosis or a physical therapy plan. It is therapeutic bodywork informed by manual therapy, movement practice, and years of hands-on experience.</p>
        </details>
        <details>
          <summary>Will the work be painful?</summary>
          <p>It can be intense, but it should not make you brace against the work. I usually stay near a level where you can still breathe, respond, and remain present.</p>
        </details>
        <details>
          <summary>Will one session help?</summary>
          <p>One session can create meaningful relief and useful information. Some concerns respond quickly; others benefit from repeated sessions and changes in movement, training, or recovery.</p>
        </details>
        <details>
          <summary>Why do you recommend four sessions?</summary>
          <p>Four sessions gives us enough continuity to see what changes and what returns, work hands-on more than once, teach you a useful self-release practice, and spend one session explicitly applying what we learn to movement patterns relevant to you.</p>
        </details>
        <details>
          <summary>Do I have to buy the four-session process?</summary>
          <p>No. Single sessions remain available. The four-session process is simply the starting point I recommend when you want more than temporary relief and would benefit from both bodywork and individualized movement practice.</p>
        </details>
        <details>
          <summary>Do you work with injuries or surgery history?</summary>
          <p>Yes, when bodywork is appropriate and your medical team has cleared it. Please include relevant history on your intake form so we can make careful decisions about pressure, positioning, and scope.</p>
        </details>
      </div>
    </div>
  </section>

  <section class="final-cta">
    <div class="wrap">
      <span class="eyebrow">Begin</span>
      <h2>Relief is useful. Better understanding lasts longer.</h2>
      <p style="max-width:620px;">If you want thoughtful, collaborative bodywork—and a clearer sense of what your body is doing—start with the four-session process. The first step is simply booking the first 75-minute bodywork session.</p>
      <div class="actions"><a class="btn btn-clay" href="#booking">Book Your First Bodywork Session →</a></div>
    </div>
  </section>
</main>'''
t, n = re.subn(r'<main>.*?</main>', main, t, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'main replacement failed: {n}')

footer = '''<footer>
  <div class="footer-note">Misha Bodywork &amp; Movement · Golden, Colorado</div>
  <div class="footer-links">
    <a class="footer-note" href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank">Book a Session</a>
    <a class="footer-note" href="/denver-movement-school">Denver Movement School</a>
    <a class="footer-note" href="https://instagram.com/misha.lantsov" rel="noopener" target="_blank">Instagram</a>
  </div>
</footer>'''
t, n = re.subn(r'<footer>.*?</footer>', footer, t, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'footer replacement failed: {n}')

if 'class="mobile-booking-bar"' not in t:
    t = t.replace(
        '</body>',
        '<div aria-label="Quick booking" class="mobile-booking-bar" role="region"><a href="#booking">Book First Session</a></div>\n<script src="https://embed.acuityscheduling.com/js/embed.js" type="text/javascript"></script>\n</body>',
        1,
    )

p.write_text(t)
