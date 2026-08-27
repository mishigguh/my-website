from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly 1 match, found {count}")
    return text.replace(old, new, 1)


bodywork_path = Path("bodywork.html")
bodywork = bodywork_path.read_text(encoding="utf-8")

replacements = [
    (
        'Start with a four-session bodywork and movement process or book an individual session.',
        'Start with the 4-Session Intensive or book an individual session.',
        'meta description offer name',
    ),
    (
        '"name":"Four-session bodywork and movement starter process"',
        '"name":"4-Session Intensive"',
        'schema offer name',
    ),
    (
        '<li><a href="#starter">Series</a></li>',
        '<li><a href="#starter">4-Session Intensive</a></li>',
        'nav offer name',
    ),
    (
        'movement patterns that have stopped changing.',
        'movement patterns that feel stuck.',
        'hero clarity edit',
    ),
    (
        'Most pain and tension is not a single problem in a single place. It is often part of a larger pattern: how you brace, breathe, move, recover, and adapt to old injuries or repeated stress.',
        'Recurring pain and tension are often part of a larger pattern: how you brace, breathe, move, recover, and adapt to old injuries or repeated stress.',
        'approach claim edit',
    ),
    (
        '<div class="session-label">4-Session Bodywork + Movement Series</div>',
        '<div class="session-label">4-Session Intensive</div>',
        'offer card name',
    ),
    (
        '<strong>03 · Go deeper.</strong>',
        '<strong>03 · Build on what changed.</strong>',
        'step three label',
    ),
    (
        '<strong style="color:var(--ink)">You’re only committed to the first session.</strong><p style="margin-top:.35rem">If after the first visit either of us feels the series is not the right fit, I’ll refund the unused $415. Your first 75-minute session remains at its normal $145 rate.</p>',
        '<strong style="color:var(--ink)">Not the right fit after the first session? I’ll refund the remaining $415.</strong><p style="margin-top:.35rem">You’ll purchase the 4-Session Intensive up front. If after the first visit either of us feels it isn’t the right fit, I’ll refund $415 and you’ll only pay the normal $145 cost of that first session.</p>',
        'refund statement',
    ),
    (
        '<h3>Start the 4-Session Series</h3>',
        '<h3>Start the 4-Session Intensive</h3>',
        'booking heading name',
    ),
    (
        'What to Expect on Your First Session',
        'What to Expect at Your First Session',
        'first-session heading',
    ),
    (
        '<summary>Do I have to buy the four-session series?</summary><p>No. Single sessions remain available. The four-session series is simply the starting point I recommend when you want more than temporary relief and would benefit from both bodywork and individualized movement practice.</p>',
        '<summary>Do I have to buy the 4-Session Intensive?</summary><p>No. Single sessions remain available. The 4-Session Intensive is simply the starting point I recommend when you want more than temporary relief and would benefit from both bodywork and individualized movement practice.</p>',
        'FAQ offer name',
    ),
    (
        'start with the four-session Bodywork + Movement Series.',
        'start with the 4-Session Intensive.',
        'final CTA copy name',
    ),
    (
        '<a class="btn btn-clay" href="#starter">Start the 4-Session Series →</a>',
        '<a class="btn btn-clay" href="#booking">Start the 4-Session Intensive →</a>',
        'final CTA link and name',
    ),
    (
        '>Book a Session</a><a class="footer-note" href="/denver-movement-school">',
        '>Book Single Session</a><a class="footer-note" href="/denver-movement-school">',
        'footer single-session label',
    ),
    (
        '<div class="testimonial-text" id="testimonial-text">Best massage therapist in Golden! I have been a loyal client for 5 years now. Misha is great at listening to what you need and also finding the spots you did not even realize needed bodywork. He incorporates stretching and breath work into the massage. The space is nice and he is very professional. Highly recommend!</div><div class="testimonial-author" id="testimonial-author">Lisa Carropen · Google Review</div>',
        '<div class="testimonial-text" id="testimonial-text">Misha is the best massage therapist I have encountered. I had a persistent knee issue after a ski fall with frequent pain flare ups. My pain dramatically decreased after our first session. He worked slowly and steadily, and he also taught me how to do my own myofascial work with massage balls so I could take care of my body.</div><div class="testimonial-author" id="testimonial-author">Kathleen Shea · Google Review</div>',
        'initial testimonial',
    ),
    (
        'const testimonials=[{text:"Best massage therapist in Golden! I have been a loyal client for 5 years now. Misha is great at listening to what you need and also finding the spots you did not even realize needed bodywork. He incorporates stretching and breath work into the massage. The space is nice and he is very professional. Highly recommend!",author:"Lisa Carropen · Google Review",stars:"★★★★★"},{text:"Misha is the best massage therapist I have encountered. I had a persistent knee issue after a ski fall with frequent pain flare ups. My pain dramatically decreased after our first session. He worked slowly and steadily, and he also taught me how to do my own myofascial work with massage balls so I could take care of my body.",author:"Kathleen Shea · Google Review",stars:"★★★★★"}',
        'const testimonials=[{text:"Misha is the best massage therapist I have encountered. I had a persistent knee issue after a ski fall with frequent pain flare ups. My pain dramatically decreased after our first session. He worked slowly and steadily, and he also taught me how to do my own myofascial work with massage balls so I could take care of my body.",author:"Kathleen Shea · Google Review",stars:"★★★★★"},{text:"Best massage therapist in Golden! I have been a loyal client for 5 years now. Misha is great at listening to what you need and also finding the spots you did not even realize needed bodywork. He incorporates stretching and breath work into the massage. The space is nice and he is very professional. Highly recommend!",author:"Lisa Carropen · Google Review",stars:"★★★★★"}',
        'testimonial ordering',
    ),
]

for old, new, label in replacements:
    bodywork = replace_once(bodywork, old, new, label)

bodywork_path.write_text(bodywork, encoding="utf-8")

index_path = Path("index.html")
index = index_path.read_text(encoding="utf-8")

index_replacements = [
    ('"priceRange": "$125-$165"', '"priceRange": "$125-$560"', 'homepage schema price range'),
    ('<a class="nav-mark" href="index.html">Misha Lantsov</a>', '<a class="nav-mark" href="/">Misha Lantsov</a>', 'homepage nav home link'),
    ('<a href="writing.html">Writing</a>', '<a href="/writing">Writing</a>', 'homepage nav writing link'),
    ('<a class="home-portal portal-bodywork" href="bodywork.html"', '<a class="home-portal portal-bodywork" href="/bodywork"', 'homepage bodywork portal link'),
    ('<a class="home-portal portal-dms" href="denver-movement-school.html"', '<a class="home-portal portal-dms" href="/denver-movement-school"', 'homepage DMS portal link'),
]

for old, new, label in index_replacements:
    if label == 'homepage nav writing link':
        count = index.count(old)
        if count != 2:
            raise RuntimeError(f"{label}: expected exactly 2 matches, found {count}")
        index = index.replace(old, new)
    else:
        index = replace_once(index, old, new, label)

index_path.write_text(index, encoding="utf-8")

print("Applied only the requested final-pass edits to bodywork.html and index.html")
