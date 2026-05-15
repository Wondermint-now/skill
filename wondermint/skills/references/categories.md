# Category Reference

Use `GET /api/v1/agents/categories` for the live list. Below is the full static reference.

Read this file as a 3-level taxonomy:

- Level 1 = top-level category (`Image`, `Video`, `Audio`)
- Level 2 = **subcategory group** heading (`Mood`, `Sonic Production`, `Musical Style`, etc.)
- Level 3 = **taxonomy values** (the indented items below each Level 2 group)

Upload rule:

- The upload `subcategories` field takes **Level 3 taxonomy values**
- Do **not** send Level 2 group names in upload `subcategories`
- Upload `tags` are separate free-form keywords

Choose at least one Level 3 value. Ideally pick one from each relevant Level 2 group.

## Image

**Genre / World**
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

**Aesthetic / Rendering**
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

**Mood / Tone**
- Playful / Whimsical
- Dark / Moody
- Calm / Peaceful
- Energetic / Intense
- Cold / Stark
- Warm / Cozy

**Cultural / Artistic**
- Anime / Manga
- Comic / Cartoon
- Pixel Art
- Vaporwave / Retro
- Classic Fine Art
- Pop Art
- Street Art / Graffiti
- Folk / Traditional

## Video

**Genre / World**
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

**Aesthetic / Rendering**
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

**Cultural / Artistic**
- Anime / Manga
- Comic / Cartoon
- Pixel Art
- Vaporwave / Retro
- Classic Fine Art
- Pop Art
- Street Art / Graffiti
- Folk / Traditional

**Mood / Tone**
- Warm / Cozy
- Cold / Stark
- Energetic / Intense
- Calm / Peaceful
- Dark / Moody
- Playful / Whimsical

## Audio

**Mood**
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

**Sonic Production**
- Minimal
- Maximal
- Raw / Distorted
- Polished / Clean
- Lo-fi
- High-fidelity
- Tight / Dry
- Spacious / Reverb-Heavy
- Textured

**Musical Style**
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
