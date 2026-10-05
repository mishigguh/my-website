# Environmental Movement Practice page draft

The work is isolated on `environmental-movement-practice`, based on main commit `805c6edcfbc885090cad40f238bd64516500322c`. All files in this change are additions. Existing pages, shared styles, navigation, the sitemap, and deployment configuration are unchanged.

The student program export is background for understanding the work. The current methodology copy and milestone examples come from the user's revised brief, described by the user as incorporating WhatsApp context. Three user-supplied graphics from a shared ChatGPT message explain the overview, coaching process, and included/fit section. The raw WhatsApp export and audio/video material have not been reviewed here. No raw student records, private contact details, pricing, or service response deadlines are published.

## Files and preview

- `environmental-movement-practice.html` is the static page that can be served directly by the existing site.
- `environmental-movement-practice.css` contains page-specific styles.
- `templates/environmental-movement-practice.html` contains the page structure and narrative.
- `content/environmental-movement-practice.json` contains the methodology copy, coaching steps, seven domains, six practice formats, and eight example milestones. The practices array remains available for later reviewed teaching examples.
- `images/emp-overview.webp`, `images/emp-process.webp`, and `images/emp-included.webp` are optimized copies of the three supplied graphics, retaining their original 1672 × 941 dimensions. Together they weigh approximately 499 KB, compared with approximately 4.7 MB for the source PNGs. The two lower images are lazy-loaded.
- `scripts/build-environmental-movement-practice.py` generates the static HTML using Python's standard library. There are no new runtime dependencies and no browser JavaScript requirement.

Run `python scripts/build-environmental-movement-practice.py` from the repository to regenerate the page. Commit the generated HTML alongside template and content changes. With a plain static server, use `/environmental-movement-practice.html`. The intended canonical URL follows the existing site's extensionless convention: `https://mishalantsov.com/environmental-movement-practice`.

## Adding a reviewed practice

Each practice record has these fields:

```json
{
  "id": "stable-exercise-slug",
  "group": "jumping",
  "name": "Reviewed practice name",
  "phase": 1,
  "description": "A concise description supported by the source.",
  "purpose": "The purpose, when supported by the source.",
  "prescription": "The actual individualized prescription, if relevant.",
  "instructions": ["Reviewed instruction"],
  "cues": ["Reviewed coaching cue"],
  "progression": "A progression or regression supported by the source.",
  "videos": [{"label": "Demonstration title", "url": "https://example.com/video"}]
}
```

The builder groups optional exercise records by domain and creates native expandable `details` sections. Text is escaped. Each infographic has descriptive alternative text, a full-size link, and an expandable HTML reading version for accessibility and small screens. Transparent links over the coaching buttons in the overview and included graphics use the existing public email inquiry address; the final section also has a normal HTML inquiry button. Demonstrations, when added, are linked rather than loading multiple external players on page load. Only add actual demonstration links with reviewed public access. Include source locators in local working notes; do not upload raw chats or private student records to this public repository.

## Before publishing

The page has a visible draft label and `noindex,follow` metadata while it is being reviewed. After approval, remove the draft label and noindex metadata from the template, regenerate HTML, and consider adding the page to the sitemap. Agree on navigation placement at that point; a homepage movement section or footer link would keep the primary navigation concise.

The supplied overview graphic replaces the earlier handstand hero photograph. The process graphic replaces the earlier SVG process diagram and visible step cards; the HTML steps remain in its expandable reading version. The included/fit graphic replaces the earlier differentiation text; the explanatory copy remains in its reading version. Domain icons and structured milestone text remain as HTML and inline SVG. No surname, qualifications, pricing, or new package details are invented for Ian or the program.

Merge and deployment are separate later steps; this draft has not been merged or deployed.
