# Stick-Man Series: Locked Character Bible

These two characters are **locked**. Every episode uses them unchanged.
Hosts **alternate** by episode: in odd episodes Blu asks and Sunny explains; in even episodes they swap.

## ✅ Clean, original reference files (USE THESE in Flow)
Drawn from scratch as vector art (no stock, no watermark): `characters/`

| File | Use as ingredient for |
|---|---|
| `blu_wave.png` | Blu intro / greeting shots (master reference) |
| `blu_think.png` | Blu wondering / question shots |
| `blu_explain.png` | Blu explaining / pointing shots |
| `sunny_present.png` | Sunny explaining (master reference) |
| `sunny_point.png` | Sunny pointing at visuals |
| `sunny_wave.png` | Sunny intro / outro |
| `*_transparent.png` | Same poses on transparent background (thumbnails, Canva, CapCut overlays) |
| `character_sheet.png` | Overview of all six poses |

Editable source: `*.svg`. Need a new pose? Edit `make.py`, run `python3 make.py <folder>` then `node render.js <folder>`.
**Never** use the original watermarked stock images.

---

## Character 1: BLU (the curious one): crayon-scribble style

| Trait | Locked value |
|---|---|
| Head | Large perfect circle, thick black outline, filled with peach/light-orange (#F9C784) **crayon scribble** that leaves white gaps |
| Face | Two vertical black oval eyes, simple thin black curved smile, no nose, no ears |
| Torso | Small rounded rectangle, thick black outline, filled with light-blue (#7FB2E0) **crayon scribble** with white gaps |
| Limbs | Thick solid black rounded strokes |
| Hands | Solid black mitten hands (thumb only) |
| Feet | Solid black flat oval feet |
| Style | Flat 2D, hand-drawn children's doodle, crayon texture |
| Personality | Curious, asks questions, scratches head, waves |

**Clean reference prompt (Nano Banana / Flow image, 1:1):**
> Character turnaround sheet of a cute stick-man named Blu: large perfect circle head with thick black outline filled with peach crayon scribble leaving white gaps, two vertical black oval eyes, thin black curved smile, no nose; small rounded-rectangle torso with thick black outline filled with light blue crayon scribble; thick solid black rounded limbs, solid black mitten hands, solid black oval feet. Poses: front waving, three-quarter, side, back, thinking with hand on chin. Pure white background, flat even lighting, no shadows. Flat 2D hand-drawn children's doodle style, crisp vector-clean outlines, high resolution.
> Negative: watermark, text, logo, 3D, realistic, fingers, nose, ears, hair, extra limbs, gradients.

---

## Character 2: SUNNY (the explainer): glossy vector style

| Trait | Locked value |
|---|---|
| Head | Large perfect circle, thin black outline, **glossy lemon-yellow (#FFE04D)** with darker golden shading at the bottom and two white shine highlights top-right |
| Face | Two tall black oval eyes, big open D-shaped smile, black mouth with red tongue |
| Torso | Yellow tapered teardrop/bowling-pin shape, thin black outline, golden side shading |
| Limbs | Thin black line arms and legs |
| Hands | Small yellow open palms (mitten shape) with black outline |
| Feet | Small yellow oval shoes with black outline |
| Style | Glossy 2D vector cartoon, clean cel shading |
| Personality | Cheerful, confident, explains with open-hand gestures |

**Clean reference prompt (1:1):**
> Character turnaround sheet of a cheerful stick-man named Sunny: large perfect circle head, glossy lemon-yellow with golden shading at the bottom and two small white shine highlights at top right, thin black outline, two tall black oval eyes, big open smile with red tongue; yellow tapered teardrop-shaped torso with thin black outline; thin black line arms and legs; small yellow open-palm mitten hands; small yellow oval shoes. Poses: front with both palms open presenting, pointing, three-quarter, side, back. Pure white background, flat even lighting. Glossy 2D vector cartoon, clean cel shading, crisp lines, high resolution.
> Negative: watermark, text, logo, 3D render, realistic, fingers, nose, hair, clothes, extra limbs.

---

## Global series style (paste at the end of every video prompt)

> STYLE: 16:9 widescreen, clean 2D animated kids' explainer, soft pastel cream background with simple flat props, bright cheerful lighting, smooth bouncy cartoon motion, characters exactly match the reference images, consistent proportions, 24fps.

## Global negative (paste in every prompt)

> NEGATIVE: watermark, logo, text, subtitles, 3D realistic render, human features, fingers, nose, hair, morphing face, extra limbs, flicker, style change between characters.

## Consistency rules
1. Always attach the reference PNG(s) as ingredients; never rely on text alone.
2. Max **two** characters per shot.
3. Never describe new clothes or colors for them.
4. Keep the two art styles distinct: Blu stays crayon, Sunny stays glossy. That contrast is the series' look.
5. Voices come from ElevenLabs (one fixed voice per character), not Veo, so they sound the same in every episode.
