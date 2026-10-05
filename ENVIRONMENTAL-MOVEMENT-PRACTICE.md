# Environmental Movement Practice page draft

The work is isolated on `environmental-movement-practice`, based on main commit `805c6edcfbc885090cad40f238bd64516500322c`. All files in this change are additions. Existing pages, shared styles, navigation, the sitemap, and deployment configuration are unchanged.

The student program export is background for understanding the work. The page introduces the broad practice domains and coaching approach. It does not publish the student's program, prescriptions, personal details, service logistics, or proposed future curriculum. The exercise examples and progression are clearly marked draft sections awaiting the WhatsApp feedback and audio/video material.

## Files and preview

- `environmental-movement-practice.html` is the static page that can be served directly by the existing site.
- `environmental-movement-practice.css` contains page-specific styles.
- `templates/environmental-movement-practice.html` contains the page structure and narrative.
- `content/environmental-movement-practice.json` contains the domains and the exercise records. The practices array is intentionally empty until teaching examples are selected from the forthcoming material.
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

The builder groups records by domain and creates native expandable `details` sections. Text is escaped. Demonstrations are linked rather than loading multiple external players on page load. Only add actual demonstration links with reviewed public access. Include source locators in local working notes; do not upload raw chats or private student records to this public repository.

## Before publishing

The page has a visible draft label and `noindex,follow` metadata while content is provisional. After the content is approved, remove the draft label and noindex metadata from the template, replace the marked draft sections, regenerate HTML, and consider adding the page to the sitemap. Agree on navigation placement at that point; a homepage movement section or footer link would keep the primary navigation concise.

The hero uses an existing site photograph as a general movement-practice image. It is not presented as footage of this remote student or a demonstration for a specific exercise. No surname, qualifications, pricing, or new package details are invented for Ian or the program.

Merge and deployment are separate later steps; this draft has not been merged or deployed.
