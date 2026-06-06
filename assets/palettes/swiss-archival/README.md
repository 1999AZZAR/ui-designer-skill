# Swiss-Archival — Dedicated Assets

Source-of-truth palette and export files for the Swiss-Archival design system. All hex tokens in `references/swiss-archival.md` and `assets/components/swiss-archival-components.md` are derived from this folder.

## Files

| File | Format | Purpose |
|------|--------|---------|
| `SWISS-ARCHIVAL.png` | PNG (export from coolors.co) | Visual swatch reference, 6 stripes with hex labels |
| `palette.svg` | SVG | Inline swatch, drop into docs or design briefs |
| `palette.ase` | Adobe Swatch Exchange | Import into Figma, Illustrator, Photoshop, InDesign |
| `palette.scss` | SCSS / CSS custom properties | CSS HEX, HSL, RGB variables + 8-direction gradients + radial |
| `palette.txt` | Plain text | CSV, hex list, JSON array/object, XML — multi-format export |
| `tailscale.txt` | JSON | Tailscale 11-stop ramps (50–950) per base color |

## Core Palette

| Token | Hex | Coolors Name | Role |
|-------|-----|--------------|------|
| `surface-linen` | `#efe9dc` | Soft Linen | Primary canvas / cards |
| `surface-dust` | `#cbc3b7` | Dust Grey | Hairline borders, draft lines, low-emphasis surfaces |
| `surface-linen-2` | `#eee8db` | Soft Linen 2 | Subtle elevation variant of linen |
| `muted-olive` | `#a49c92` | Grey Olive | Secondary text, captions, structural framing |
| `ink` | `#2a2520` | Carbon Black | Foreground / body / headings |
| `accent` | `#9c3d3b` | Brown Red | Focus, action, accent strokes |

These six colors are the canonical swatch. Use Tailscale ramps for hover, active, and elevation states.

## Tailscale Ramps

The `tailscale.txt` file gives 11 stops (`50`–`950`) for each base color, including Brown Red. Use the ramps instead of ad-hoc lightening/darkening so the warm-archival character is preserved across hover, focus, active, and disabled states.

Quick reference (full table in `tailscale.txt`):

| Step | soft-linen | dust-grey | grey-olive | carbon-black | brown-red |
|------|------------|-----------|------------|--------------|-----------|
| 50   | `#f7f4ee`  | `#f4f3f0` | `#f3f2f1`  | `#f4f2f0`    | `#f8eded` |
| 100  | `#efe9dc`  | `#eae6e1` | `#e8e6e3`  | `#e9e6e2`    | `#f1dada` |
| 500  | `#ad9052`  | `#94846b` | `#8b8174`  | `#91806e`    | `#b94846` |
| 900  | `#231d10`  | `#1e1a15` | `#1c1a17`  | `#1d1a16`    | `#250e0e` |
| 950  | `#18140b`  | `#15120f` | `#131210`  | `#14120f`    | `#1a0a0a` |

> Note: `soft-linen` 200–800 in the Tailscale file drifts into warmer ochre tones — those are *not* part of the warm archival canvas. Use them only for deliberate contrast (e.g. archived-photo background) or omit from the active palette.

## Recommended Token Mapping

When wiring the palette into CSS custom properties:

```css
--color-bg: #efe9dc;          /* soft-linen 100 */
--color-surface: #eee8db;     /* soft-linen 2 — slight elevation */
--color-muted: #cbc3b7;       /* dust-grey 100 — borders, dividers */
--color-muted-fg: #a49c92;    /* grey-olive — labels, captions */
--color-fg: #2a2520;          /* carbon-black — body, headings */
--color-accent: #9c3d3b;      /* brown-red 500 — focus, action */
--color-accent-hover: #b94846;  /* brown-red 600 (Tailscale) */
--color-accent-active: #6f2b2a; /* brown-red 700 (Tailscale) */
```

Success / warning stay on the muted earth-tone family defined in the reference (green `#3A6B3A`, amber `#8B6B1A`) and are not part of this six-color swatch.

## Loading The Palette

**SCSS:**
```scss
@import './assets/palettes/swiss-archival/palette.scss';
```

**CSS variables (paste from `palette.scss`):**
```css
:root {
  --soft-linen: #efe9dcff;
  --dust-grey: #cbc3b7ff;
  --soft-linen-2: #eee8dbff;
  --grey-olive: #a49c92ff;
  --carbon-black: #2a2520ff;
  --brown-red: #9c3d3bff;
}
```

**Tailscale (per-color stops):**
```js
import tailscale from './assets/palettes/swiss-archival/tailscale.txt';
const accentHover = tailscale['brown-red'][600];
```

**Adobe / Figma:** open `palette.ase` and import.

## Cross-Reference

- System principles & tokens: `../../../references/swiss-archival.md`
- Component recipes using these tokens: `../../components/swiss-archival-components.md`
- Specimen decorator geometry: `../../decorators/swiss-archival-specimen-decorator.md`
