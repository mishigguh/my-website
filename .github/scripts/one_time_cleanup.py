from pathlib import Path

bodywork = Path('bodywork.html')
text = bodywork.read_text(encoding='utf-8')

canonical = '<link rel="canonical" href="https://mishalantsov.com/bodywork" />'
if canonical not in text:
    anchor = '<meta name="description" content="Therapeutic bodywork in Golden, Colorado for chronic pain, tension, injuries, and recurring movement patterns. Hands-on body education at the intersection of massage, manual therapy, and movement practice." />'
    metadata = '''
<link rel="canonical" href="https://mishalantsov.com/bodywork" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://mishalantsov.com/bodywork" />
<meta property="og:title" content="Misha Bodywork & Movement — Golden, Colorado" />
<meta property="og:description" content="Therapeutic bodywork in Golden, Colorado for pain, tension, injuries, and recurring movement patterns." />
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "@id": "https://mishalantsov.com/bodywork#business",
      "name": "Misha Bodywork and Movement",
      "url": "https://mishalantsov.com/bodywork",
      "telephone": "+1-720-577-5964",
      "priceRange": "$125-$165",
      "description": "Therapeutic bodywork in Golden, Colorado for pain, tension, injuries, stress, and recurring movement patterns.",
      "founder": {"@id": "https://mishalantsov.com/#misha-lantsov"},
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "1300 Jackson St, Suite B200, Room 6",
        "addressLocality": "Golden",
        "addressRegion": "CO",
        "postalCode": "80401",
        "addressCountry": "US"
      },
      "openingHoursSpecification": [
        {"@type":"OpeningHoursSpecification","dayOfWeek":"https://schema.org/Sunday","opens":"08:30","closes":"13:30"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"https://schema.org/Monday","opens":"15:30","closes":"20:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"https://schema.org/Tuesday","opens":"13:30","closes":"17:00"},
        {"@type":"OpeningHoursSpecification","dayOfWeek":"https://schema.org/Thursday","opens":"15:30","closes":"20:00"}
      ],
      "makesOffer": [
        {"@type":"Offer","price":"125","priceCurrency":"USD","itemOffered":{"@type":"Service","name":"60-minute bodywork session"}},
        {"@type":"Offer","price":"145","priceCurrency":"USD","itemOffered":{"@type":"Service","name":"75-minute bodywork session"}},
        {"@type":"Offer","price":"165","priceCurrency":"USD","itemOffered":{"@type":"Service","name":"90-minute bodywork session"}}
      ]
    },
    {
      "@type": "Person",
      "@id": "https://mishalantsov.com/#misha-lantsov",
      "name": "Misha Lantsov",
      "url": "https://mishalantsov.com/",
      "jobTitle": "Bodyworker and movement teacher"
    }
  ]
}
</script>'''
    if anchor in text:
        text = text.replace(anchor, anchor + metadata, 1)
    else:
        text = text.replace('</title>', '</title>\n' + metadata, 1)

text = text.replace('in my third year of a five-year international movement program', 'in my fourth year of a five-year Human Movement Studies program with Marcello Palozzo')
text = text.replace('https://denvermovement.school', 'https://mishalantsov.com/denver-movement-school')
bodywork.write_text(text, encoding='utf-8')

dms = Path('denver-movement-school.html')
dtext = dms.read_text(encoding='utf-8')
dcanonical = '<link rel="canonical" href="https://mishalantsov.com/denver-movement-school" />'
if dcanonical not in dtext:
    dmeta = '''
<link rel="canonical" href="https://mishalantsov.com/denver-movement-school" />
<meta name="description" content="Denver Movement School is a weekly adult movement practice led by Misha Lantsov at Wiggelruhm in Denver, Tuesdays from 5:30–6:50pm." />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://mishalantsov.com/denver-movement-school" />
<meta property="og:title" content="Denver Movement School | Adult Movement Practice in Denver" />
<meta property="og:description" content="Weekly adult movement practice in Denver: strength, coordination, athleticism, partner work, play, and movement learning. Tuesdays 5:30–6:50pm at Wiggelruhm." />
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "EducationalOrganization",
      "@id": "https://mishalantsov.com/denver-movement-school#organization",
      "name": "Denver Movement School",
      "url": "https://mishalantsov.com/denver-movement-school",
      "description": "Adult movement education in Denver through structured practice in strength, coordination, athleticism, adaptability, partner work, play, and movement learning.",
      "founder": {"@id": "https://mishalantsov.com/#misha-lantsov"},
      "location": {
        "@type": "Place",
        "name": "Wiggelruhm",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "125 S Sherman St",
          "addressLocality": "Denver",
          "addressRegion": "CO",
          "postalCode": "80209",
          "addressCountry": "US"
        }
      }
    },
    {
      "@type": "Person",
      "@id": "https://mishalantsov.com/#misha-lantsov",
      "name": "Misha Lantsov",
      "url": "https://mishalantsov.com/"
    }
  ]
}
</script>
'''
    if '</head>' in dtext:
        dtext = dtext.replace('</head>', dmeta + '</head>', 1)
    else:
        dtext = dtext.replace('<body', dmeta + '<body', 1)
dms.write_text(dtext, encoding='utf-8')
