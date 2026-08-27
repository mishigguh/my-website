from pathlib import Path
import re

p = Path('bodywork.html')
t = p.read_text()

# Pricing and scope.
t = t.replace('"priceRange":"$125-$435"', '"priceRange":"$125-$560"')
t = t.replace('"price":"435"', '"price":"560"')
t = t.replace('Three 75-minute bodywork sessions, one individualized movement-practice session, and in-person therapy-ball self-release instruction.', 'Three 75-minute bodywork sessions, one 60-minute individualized movement-practice session, and in-person therapy-ball self-release instruction.')
t = t.replace('$435', '$560')
t = t.replace('unused $290', 'unused $415')
t = t.replace('refund $290', 'refund $415')
t = t.replace('refund the unused $290', 'refund the unused $415')
t = t.replace('Three bodywork sessions · one individualized movement session', 'Three 75-minute bodywork sessions · one 60-minute individualized movement session')
t = t.replace('<strong>04 · Put it into movement.</strong> An individualized movement-practice session', '<strong>04 · Put it into movement.</strong> A 60-minute individualized movement-practice session')

# Keep only a quiet single-session fallback; remove any leftover comparison/cards or couples block.
t = re.sub(r'<div class="single-session-row">.*?</div></div></div>', '</div></div>', t, count=1, flags=re.S)
t = re.sub(r'<div class="small-offers">.*?</div></div></section>', '</div></section>', t, count=1, flags=re.S)
t = re.sub(r'<div class="small-offer">\s*<h3>Couples instruction</h3>.*?</div>\s*</div>', '', t, count=1, flags=re.S)

# Normalize the fallback copy near checkout to the requested sentence.
t = re.sub(
    r'<div style="margin-top:1\.5rem"><p style="font-size:\.86rem">Prefer to book a single session instead\? <a href="https://movementandbodywork\.as\.me/bodywork" rel="noopener" target="_blank" style="text-decoration:underline;text-underline-offset:3px">Individual bodywork appointments are still available here\.</a></p></div>',
    '<div style="margin-top:1.5rem"><p style="font-size:.86rem">If you would rather start with one appointment, <a href="https://movementandbodywork.as.me/bodywork" rel="noopener" target="_blank" style="text-decoration:underline;text-underline-offset:3px">individual sessions are still available.</a></p></div>',
    t,
    count=1,
)

# Remove unused styles from deleted comparison/secondary-offer blocks.
t = re.sub(r'\.single-session-row\{.*?\.single-session p\{font-size:\.86rem\}', '', t, count=1, flags=re.S)
t = re.sub(r'\.small-offers\{.*?\.small-offer p\{font-size:\.86rem\}', '', t, count=1, flags=re.S)

# Update mobile grid selector if deleted classes remain there.
t = t.replace(',.single-session-row,.small-offers', '')

# Sanity checks.
assert '$435' not in t
assert '$290' not in t
assert 'Couples instruction' not in t
assert 'Prefer one session?' not in t
assert 'You can book 60, 75, or 90 minutes through the same scheduler' not in t
assert '$560' in t
assert '$415' in t
assert 'one 60-minute individualized movement' in t
assert 'If you would rather start with one appointment' in t

p.write_text(t)
