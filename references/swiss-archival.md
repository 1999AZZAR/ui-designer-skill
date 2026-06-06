# Swiss-Archival (Museum-Grade Digital Archive)

A design language born from the intersection of Swiss International Typographic Style and physical archive aesthetics. Every decision — color, type, spacing, motion — serves the goal of making digital content feel like a curated physical artifact. The UI should feel like a well-designed exhibition catalog, not a generic web app.

---

## Recommended Usage

- Best for: digital archives, editorial portfolios, museum sites, content-heavy research tools, academic platforms, typography-led publications
- Avoid for: playful consumer apps, dense enterprise dashboards (unless brand demands it)
- Strong hybrid partner with: `minimal`, `swiss`, `neo-m3`

## Core Principles

1. **Grid as Foundation** — A visible 1px vertical boundary system (Blueprint Grid) anchors all content within an 80rem (1280px) container. Elements feel "drafted" onto a technical canvas.
2. **Tactility & Materiality** — A fixed SVG fractal noise filter (`feTurbulence`, `baseFrequency="0.65"`, `opacity="0.04"`) creates persistent organic grain mimicking 300gsm matte-printed archival paper.
3. **State-Driven Motion** — All animations communicate state or intent. A global 0.75x motion ratio reduces standard durations by 25% for a snappy, liquid feel.
4. **Structural Honesty** — No ornament for ornament's sake. Borders, spacing, and typography do the structural work. Shadows are reserved for overlays only.
5. **Museum Label Aesthetic** — Technical metadata (labels, nav, timestamps) uses a monospace layer with uppercase and wide tracking, clearly distinguishing data from narrative.

---

## Visual DNA

| Property | Value |
|---|---|
| **Border Radius** | 4px (sm), 6px (md), 12px (lg). Subtle, never playful. Max on primary surfaces is 6px. |
| **Borders** | 1px solid `#CBC3B7` (Dust Grey — Muted). Cards, inputs, dividers. Blueprint grid uses RGBA(191,182,166,0.2). |
| **Shadows** | Minimal. Depth via borders and background contrast. Only for overlays: dropdowns (0 1px 3px), modals (0 4px 12px), command palette (0 8px 24px). |
| **Typography** | Dual-layer: Plus Jakarta Sans (narrative) + JetBrains Mono (technical/metadata). |
| **Font Weight** | 700 for headings, 400/500 for body, 600 for labels/metadata. |
| **Line Height** | 1.05 (display), 1.1 (H1), 1.2 (H2), 1.6 (body). |
| **Letter Spacing** | -0.03em (headings), 0 (body), 0.1em (technical labels). |
| **Grid** | 12-column, 80rem max-width. 4-col mobile, 8-col tablet, 12-col desktop. |
| **Colors** | Warm archival palette: cream bg, coffee fg, burgundy accent. Muted earth tones for structure. |

---

## Color System

Source palette: `assets/palettes/swiss-archival/` (Coolors export + Tailscale 50–950 ramps). Use `assets/palettes/swiss-archival/README.md` as the loader index.

| Token | Hex | Source | Role |
|---|---|---|---|
| Background | `#EFE9DC` | soft-linen 100 | Warm Linen — primary canvas |
| Surface | `#EEE8DB` | soft-linen-2 | Soft Pearl — card elevation |
| Foreground | `#2A2520` | carbon-black | Deep Coffee — core content |
| Accent | `#9C3D3B` | brown-red 500 | Burgundy — focus & action |
| Accent Hover | `#943A38` | brown-red 600 (Tailscale) | +1 step |
| Accent Active | `#6F2B2A` | brown-red 700 (Tailscale) | +2 step |
| Muted | `#CBC3B7` | dust-grey 100 | Earthy Neutral — borders, dividers |
| Muted FG | `#A49C92` | grey-olive 100 | Ash Olive — metadata, labels |
| Muted FG Strong | `#6F675D` | grey-olive 600 (Tailscale) | use when muted-fg needs AA on small text |
| Success | `#3A6B3A` | — | Muted green (state, not in core palette) |
| Warning | `#8B6B1A` | — | Earthy amber (state, not in core palette) |

**Contrast Ratios (WCAG 2.1 AA):**
- Foreground `#2A2520` on Background `#EFE9DC`: ~9.5:1 (AAA)
- Accent `#9C3D3B` on Background `#EFE9DC`: ~5.2:1 (AA normal text)
- Muted FG `#A49C92` on Background `#EFE9DC`: ~2.1:1 — use **only** for text ≥ 18px (or 14px @ 600 weight), or switch to `Muted FG Strong` `#6F675D` (~4.4:1, AA normal) for small UI labels.
- Muted `#CBC3B7` on Background `#EFE9DC`: ~1.5:1 — non-text only (borders, dividers, decorative strokes).

**Tailscale ramps.** The full 50–950 stops for each base color live in `assets/palettes/swiss-archival/tailscale.txt`. Use them for hover, active, focus-ring, and elevation states instead of ad-hoc lighten/darken. Recommended stop choices:

| State | Linen | Dust | Olive | Carbon | Brown-Red |
|---|---|---|---|---|---|
| Surface | 100 | — | — | — | — |
| Hover surface | 2 (`#eee8db`) | — | — | — | — |
| Border | — | 100 | — | — | — |
| Muted FG (small) | — | — | 600 | — | — |
| Body text | — | — | — | 100 | — |
| Accent base | — | — | — | — | 500 |
| Accent hover | — | — | — | — | 600 |
| Accent active | — | — | — | — | 700 |

---

## Type Scale

| Level | Font | Size | Weight | Tracking | Leading | Usage |
|---|---|---|---|---|---|---|
| Display | Plus Jakarta Sans | 3rem | 700 | -0.03em | 1.05 | Hero titles |
| H1 | Plus Jakarta Sans | 2.25rem | 700 | -0.03em | 1.1 | Page titles |
| H2 | Plus Jakarta Sans | 1.5rem | 700 | -0.02em | 1.2 | Section headers |
| H3 | Plus Jakarta Sans | 1.25rem | 600 | -0.01em | 1.3 | Subsections |
| Body | Plus Jakarta Sans | 1rem | 400 | 0 | 1.6 | Long-form content |
| Body Small | Plus Jakarta Sans | 0.875rem | 400 | 0 | 1.5 | Captions |
| Label | JetBrains Mono | 0.75rem | 600 | 0.1em | 1 | Metadata, nav, UI |
| Micro | JetBrains Mono | 0.625rem | 600 | 0.1em | 1 | Tags, badges |

---

## Spacing System (4px base)

| Token | Value | Usage |
|---|---|---|
| space-1 | 0.25rem (4px) | Micro gaps, icon padding |
| space-2 | 0.5rem (8px) | Inline spacing, tight padding |
| space-3 | 0.75rem (12px) | Small component padding |
| space-4 | 1rem (16px) | Default padding, card inner |
| space-6 | 1.5rem (24px) | Section padding, card gaps |
| space-8 | 2rem (32px) | Component separation |
| space-12 | 3rem (48px) | Section breaks |
| space-16 | 4rem (64px) | Major dividers |
| space-24 | 6rem (96px) | Page-level rhythm |

---

## Animation System

**Easing Curves:**
- `cubic-bezier(0.22, 1, 0.36, 1)` — entrances, reveals
- `cubic-bezier(0.65, 0, 0.35, 1)` — transitions, state changes
- `cubic-bezier(0.34, 1.56, 0.64, 1)` — playful micro-interactions (sparingly)

**Duration Scale (0.75x applied):**
- Fast: 150ms — hover, focus
- Normal: 225ms — component transitions
- Slow: 375ms — page transitions, overlays
- Glacial: 600ms — hero animations

**Rules:**
- Animate `transform` and `opacity` only (hardware-accelerated)
- Every animation must communicate state change or intent
- Respect `prefers-reduced-motion` — degrade all motion to 0.01ms

---

## Glassmorphic Overlays

```css
background: rgba(239, 233, 220, 0.85);
backdrop-filter: blur(12px);
border: 1px solid #CBC3B7;
border-radius: 12px;
box-shadow: 0 4px 12px rgba(42, 37, 32, 0.12);
```

Used for: modals, search overlays, command palette, citation tools.

---

## Keyboard Interaction Layer

All shortcuts disabled in input/textarea contexts.

| Trigger | Action |
|---|---|
| `?` | Open command index |
| `Ctrl+K` | Focus search |
| `Shift+H` | Return home |
| `Esc` | Close all overlays |
| `J/K` | Scroll 150px |
| `[/]` | Prev/Next page or entry |
| `W/S` | Move focus in grid/sidebar |
| `Enter` | Open focused entry |
| `C` | Citation modal (single view) |

---

## Parametric specimen decorator

When the interface needs a **Swiss-Archival-aligned ornament** (generative specimen, technical IDs, glass vitrine, exportable SVG) without breaking museum-label discipline, the **specimen element** is defined by the geometry ruleset in:

`assets/decorators/swiss-archival-specimen-decorator.md`

That document extracts the logic: deterministic seed from a string, Gielis superformula sampling, layered primary and interference paths, orbital satellites, construction guides, and SVG captions (`SPEC_ID`, `MORPH_DNA`). Implement in any stack; tune constants and palette while keeping the ruleset coherent. Use it as a **decorator** for heroes, vault intros, or branded empty states—not as the sole layout system for operational screens.

---

## Anti-Patterns

- Border radius > 12px on primary surfaces
- Drop shadows on cards or content elements (overlays only)
- Generic sans-serif fonts (Inter, Roboto, Arial)
- Gradient backgrounds
- Emoji in functional UI
- Decorative illustrations (use objective photography or generative shapes locked to palette)
- Centered text for multi-line content
- Animating `width`, `height`, `top`, `left`

---

## Print Styles

- A4 size, 2cm margins
- Remove all digital UI (nav, buttons, cursor, overlays)
- Add `[ ARCHIVAL_PRINT_SPECIMEN ]` footer to every page

---

## Reference

**Palette source files:** `assets/palettes/swiss-archival/` — `SWISS-ARCHIVAL.png`, `palette.svg`, `palette.ase`, `palette.scss`, `palette.txt`, `tailscale.txt`. See `assets/palettes/swiss-archival/README.md` for the loader index and token mapping.

**Components:** `assets/components/swiss-archival-components.md`

**Decorators:** `assets/decorators/swiss-archival-specimen-decorator.md`
