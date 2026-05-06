# Frontend Create And Upload Reference

This repo-development reference records owner-provided screenshots of the
Wondermint create form from 2026-05-06. Use it to improve user-facing skill
guidance. It is not an instruction for installable skill agents to browse the
frontend.

Production user-facing guidance should refer to `https://wondermint.now`.

## Create Page Structure

The page heading is "Create Your Item" with this quality note:

> As a collective, we only want the highest quality items. No spam. No slop.

Main sections and controls:

| Section | Visible controls |
|---|---|
| Upload Files | `Add Media*`; `Thumbnail` upload control |
| About Your Item | beta notice; `Name*`; `Description*`; `Prompt`; `Tags`; `Releases`; `Additional Documents`; `License*`; `Cancel`; `Create` |

Observed field copy:

- Beta notice: "Text or information cannot be edited after you tap create"
- Prompt placeholder: "Write the prompt used to create your item"
- Tags placeholder: "Write a tag and press Enter to add it. Example: CAT HAIRY FUNNY"
- Name counter shown as `5/50` in the screenshot

## License And Submission Copy

The frontend labels the rights choice as `License*`.

| Frontend label | Helper copy | API value |
|---|---|---|
| Non-Exclusive Contract | "Licenses may be used commercially according to the license terms." | `non_exclusive` |
| Public Domain | "I confirm this work is free of all copyright and IP claims." | `public_domain` |

Submission copy:

- "By submitting your content to Wondermint, you acknowledge that you agree to
  Wondermint's Terms of Service."
- "Please be sure not to violate any copyright or privacy rights. Learn more"

## Category-Dependent Fields

The create form changes the `Model*` choices and "Pick 3 that describe your
post *" descriptors after the category is selected. In API terms, the selected
descriptors map to Level 3 `subcategories`.

### Image

Visible model choices:

- Midjourney
- ChatGPT / DALL-E
- Nano Banana
- Adobe Firefly
- Ideogram
- FLUX.1
- Stable Diffusion (SDXL / SD 3.5)
- Other

Visible descriptors:

- Hyper-Detailed
- Cinematic
- Painterly
- Sketch / Line Art
- Flat / Graphic
- Minimal
- Maximal
- Low-poly
- Stylized
- Grainy / Film-grain
- Glossy
- Matte
- Photoreal
- Anime / Manga
- Comic / Cartoon
- Pixel Art
- Vaporwave / Retro
- Classic Fine Art
- Pop Art
- Street Art / Graffiti
- Folk / Traditional
- Sci-Fi / Futuristic
- Everyday / Contemporary
- Historical
- Post-Apocalyptic
- Dystopian
- Utopian
- Surreal / Dreamlike
- Horror / Dark
- Everyday / Dark
- Steampunk
- Cyberpunk
- Fantasy / Mythic
- Playful / Whimsical
- Dark / Moody
- Calm / Peaceful
- Energetic / Intense
- Cold / Stark
- Warm / Cozy

### Video

Visible model choices:

- Midjourney
- OpenAI Sora
- Runway (Gen-3 / Gen-4)
- Luma Dream Machine
- Kling AI
- Synthesia
- HeyGen
- Pika
- LTX-2
- Stable Video Diffusion (SVD)
- Other

If `Other` is selected, the form shows an input with placeholder "Type your
model name".

Visible descriptors:

- Photoreal
- Cinematic
- Painterly
- Flat / Graphic
- Minimal
- Maximal
- Low-poly
- Stylized
- Grainy / Film-grain
- Glossy
- Matte
- Hyper-Detailed
- Sketch / Line Art
- Anime / Manga
- Comic / Cartoon
- Pixel Art
- Vaporwave / Retro
- Classic Fine Art
- Pop Art
- Street Art / Graffiti
- Folk / Traditional
- Cyberpunk
- Sci-Fi / Futuristic
- Fantasy / Mythic
- Steampunk
- Everyday / Dark
- Horror / Dark
- Surreal / Dreamlike
- Utopian
- Dystopian
- Post-Apocalyptic
- Historical
- Everyday / Contemporary
- Warm / Cozy
- Cold / Stark
- Energetic / Intense
- Calm / Peaceful
- Dark / Moody
- Playful / Whimsical

### Audio

Visible model choices:

- Suno AI
- Udio
- Soundraw
- AIVA
- Mubert
- Other

Visible descriptors:

- Minimal
- Maximal
- Raw / Distorted
- Polished / Clean
- Lo-fi
- High-fidelity
- Tight / Dry
- Spacious / Reverb-Heavy
- Textured
- Classical / Orchestral
- Folk / Acoustic
- Jazz
- Ambient / Atmospheric
- Electronic
- Hip-Hop / Beats
- Pop / Vocal
- Rock
- Soundtrack / Score
- Experimental / Noise
- Folk / Traditional
- Energetic / Driving
- Aggressive / Tense
- Epic / Cinematic
- Calm / Peaceful
- Nostalgic / Dreamy
- Melancholic / Sad
- Dark / Ominous
- Ominous
- Uplifting
- Playful / Quirky

## Skill Implications

- Explain the website as asking users to pick exactly 3 descriptors, while the
  REST API accepts approved Level 3 `subcategories`.
- Treat `License*` as rights metadata, separate from private/public visibility.
- For `Other` model selections, capture the custom model name before upload.
- Warn users that the frontend says text and information cannot be edited after
  tapping Create. Do not promise frontend editability.
- Keep full field inventories here; keep installable skill guidance concise.
