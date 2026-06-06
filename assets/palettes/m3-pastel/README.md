# M3 Pastel — Dedicated Assets

Source-of-truth palette and export files for the M3 Pastel Glass design system. The system is shipped as **four candidate Coolors swatches** (one folder per swatch) so the consumer can pick the one whose mood fits the project. All hex tokens in `references/m3-pastel-glass.md` and `assets/components/m3-pastel-components.md` are derived from this folder.

## Layout

```
assets/palettes/m3-pastel/
├── README.md
├── 1/   # Studio Mix    — multicolor neutral-to-pastel
├── 2/   # Warm Blush    — powder blush to peach
├── 3/   # Soft Studio   — lavender, mint, periwinkle, parchment
└── 4/   # Soft Cream    — warm blush + alabaster greys
```

Each numbered folder contains the same four exports. The folder number is the only stable id; treat the palette name as a human-readable summary.

## Files (per swatch `<n>/`)

| File | Format | Purpose |
|------|--------|---------|
| `palette.svg` | SVG | Inline 10-stripe swatch, drop into docs or design briefs |
| `palette.ase` | Adobe Swatch Exchange | Import into Figma, Illustrator, Photoshop, InDesign |
| `palette.scss` | SCSS / CSS custom properties | CSS HEX, HSL, RGB variables + 8-direction gradients + radial |
| `palette.txt` | Plain text | CSV, hex list, JSON array/object, XML — multi-format export |

No PNG companion — the SVG swatch is the visual reference for this system. No Tailscale ramps — M3 Pastel relies on alpha-tinted containers and CSS color-mix for state variation, not on per-hue lightening ramps.

## Candidate Swatches

### `1/` — Studio Mix (multicolor)

| Token | Hex | Coolors Name | Role |
|-------|-----|--------------|------|
| `alabaster-grey` | `#e2e2df` | Alabaster Grey | Neutral surface / dividers |
| `dust-grey` | `#d2d2cf` | Dust Grey | Muted text, low-emphasis surfaces |
| `powder-petal` | `#e2cfc4` | Powder Petal | Warm secondary |
| `powder-petal-2` | `#f7d9c4` | Powder Petal 2 | Warm container |
| `pearl-beige` | `#faedcb` | Pearl Beige | Highlight / decorative |
| `frozen-water` | `#c9e4de` | Frozen Water | Cool secondary / success tint |
| `pale-sky` | `#c6def1` | Pale Sky | Info / primary surface tint |
| `thistle` | `#dbcdf0` | Thistle | Brand / accent |
| `pastel-petal` | `#f2c6de` | Pastel Petal | Soft call-out |
| `cotton-rose` | `#f9c6c9` | Cotton Rose | Soft warning / error tint |

Best for: full-spectrum pastel dashboard where every section can wear a different hue without breaking cohesion. The widest palette of the four.

### `2/` — Warm Blush (warm-only)

| Token | Hex | Coolors Name | Role |
|-------|-----|--------------|------|
| `powder-blush` | `#e8a598` | Powder Blush | Primary brand / strong accent |
| `powder-blush-2` | `#ffb5a7` | Powder Blush 2 | Primary hover / lift |
| `powder-blush-3` | `#fec5bb` | Powder Blush 3 | Primary container |
| `almond-silk` | `#fcd5ce` | Almond Silk | Secondary container |
| `soft-blush` | `#fae1dd` | Soft Blush | Surface tint |
| `seashell` | `#f8edeb` | Seashell | Canvas / background |
| `powder-petal` | `#f9e5d8` | Powder Petal | Warm surface variant |
| `powder-petal-2` | `#f9dcc4` | Powder Petal 2 | Warm surface variant 2 |
| `soft-apricot` | `#fcd2af` | Soft Apricot | Highlight |
| `peach-glow` | `#fec89a` | Peach Glow | Strong decorative accent |

Best for: friendly consumer apps, lifestyle, beauty, wellness, or any product where the warm pink-peach language carries the brand.

### `3/` — Soft Studio (cool + soft)

| Token | Hex | Coolors Name | Role |
|-------|-----|--------------|------|
| `lavender-mist` | `#eae4e9` | Lavender Mist | Neutral surface / dividers |
| `linen` | `#fff1e6` | Linen | Warm surface accent (single warm note) |
| `soft-blush` | `#fde2e4` | Soft Blush | Soft warning / error tint |
| `petal-frost` | `#fad2e1` | Petal Frost | Soft call-out |
| `mint-cream` | `#e2ece9` | Mint Cream | Cool secondary / success tint |
| `light-blue` | `#bee1e6` | Light Blue | Info / cool surface |
| `parchment` | `#f0efeb` | Parchment | Canvas / background |
| `lavender` | `#dfe7fd` | Lavender | Brand / accent |
| `periwinkle` | `#cddafd` | Periwinkle | Strong decorative accent |

Best for: productivity tools, creative SaaS, and "Studio" brand surfaces where cool blues and lavenders dominate. The single `linen` token provides a warm balance.

### `4/` — Soft Cream (warm + neutral)

| Token | Hex | Coolors Name | Role |
|-------|-----|--------------|------|
| `powder-blush` | `#fec5bb` | Powder Blush | Soft brand / accent |
| `almond-silk` | `#fcd5ce` | Almond Silk | Primary container |
| `soft-blush` | `#fae1dd` | Soft Blush | Surface tint |
| `seashell` | `#f8edeb` | Seashell | Canvas / background |
| `alabaster-grey` | `#e8e8e4` | Alabaster Grey | Neutral surface / dividers |
| `alabaster-grey-2` | `#d8e2dc` | Alabaster Grey 2 | Cool-leaning divider / hover |
| `linen` | `#ece4db` | Linen | Warm-leaning divider |
| `powder-petal` | `#ffe5d9` | Powder Petal | Warm call-out |
| `peach-fuzz` | `#ffd7ba` | Peach Fuzz | Highlight |
| `peach-glow` | `#fec89a` | Peach Glow | Strong decorative accent |

Best for: editorial-feel SaaS, journaling, note-taking, reading apps. The warmest and most restrained of the four. The two `alabaster-grey` stops are the secret: they let you build a calm neutral grid and let the warm pinks/peaches speak only on call-outs.

## Choosing a Swatch

| If the product needs… | Pick |
|-----------------------|------|
| Full spectrum / many distinct surface tints | `1/` Studio Mix |
| Strong warm pink-peach brand voice | `2/` Warm Blush |
| Cool, calm, productivity feel with one warm note | `3/` Soft Studio |
| Editorial, journaling, restrained warm + neutral | `4/` Soft Cream |

Wire the chosen swatch into the M3 Pastel Glass tokens. The `m3-pastel-glass.md` reference gives the CSS variable layout (`--m3-blue-primary`, etc.); replace the example hex with the tokens from the swatch you selected.

## Recommended Token Mapping (example: `1/` Studio Mix)

```css
:root {
  --m3-primary:    #c6def1;  /* pale-sky       — primary surface tint */
  --m3-on-primary: #003258;  /* (use studio-blue on-primary from pastel-palettes.md) */
  --m3-secondary:  #dbcdf0;  /* thistle        — secondary surface */
  --m3-accent:     #faedcb;  /* pearl-beige    — highlight / decorative */
  --m3-canvas:     #e2e2df;  /* alabaster-grey — neutral canvas from swatch 1 */
  --m3-surface:    rgba(255, 255, 255, 0.72);  /* glass surface from m3-pastel-glass.md */
  --m3-border:     rgba(255, 255, 255, 0.18); /* glass border */
  --m3-text:       #1E293B;                    /* slate from m3-pastel-glass.md */
}
```

Pair this with the glass + M3 tile patterns in `references/m3-pastel-glass.md`. Do not pull a 50–950 ramp from a swatch — M3 Pastel uses **alpha tinting and color-mix**, not stepped ramps, so the swatch's ten flat colors are the full set.

## Loading The Palette

**SCSS** (pick the swatch folder that matches the chosen theme):
```scss
@import './assets/palettes/m3-pastel/1/palette.scss';
```

**CSS variables (paste the `--<token>` block from the matching `palette.scss`):**
```css
:root {
  --alabaster-grey: #e2e2dfff;
  --dust-grey:      #d2d2cfff;
  --powder-petal:   #e2cfc4ff;
  /* ... continue for the chosen swatch */
}
```

**Adobe / Figma:** open the matching `palette.ase` and import.

**JSON / CSV / XML:** the multi-format dump lives in `<n>/palette.txt` (one combined object — pick the format you need).

## Cross-Reference

- System principles & tokens: `../../../references/m3-pastel-glass.md`
- Component recipes: `../../components/m3-pastel-components.md`
- Pastel color theory (On-Container logic, contrast rules): `../../../references/pastel-palettes.md`
- Companion dark variant: `../../../references/dark-pastel.md`
- Aggregate token JSON (system defaults): `../../palettes.json` — `systems.m3_pastel`
