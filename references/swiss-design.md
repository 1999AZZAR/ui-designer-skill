# Swiss Design (International Typographic Style)

A design philosophy born in 1950s Switzerland that prioritizes clarity, objectivity, and mathematical precision. It treats design as a system, not decoration.

---

## Core Principles

1. **Grid is Law** — All layout decisions are governed by a strict modular grid system. Content aligns to invisible columns and baselines.
2. **Typography as Architecture** — Type is the primary design element. Use sans-serif typefaces (Helvetica, Neue Haas Grotesk, Univers, Aktiv Grotesk, Inter). Hierarchy is built through weight, size, and spacing — never decoration.
3. **Objective Communication** — Design serves content. Remove anything that doesn't communicate. No ornament, no gratuitous imagery.
4. **Asymmetric Balance** — Compositions favor asymmetry over centered layouts, creating dynamic visual tension within the grid.
5. **Whitespace as Structure** — Negative space is an active design element, not leftover emptiness. It creates rhythm and breathing room.
6. **Photography over Illustration** — When imagery is needed, use objective photography. Avoid stylized or illustrative graphics.

---

## Visual DNA

| Property | Value |
|---|---|
| **Border Radius** | `0px` – `4px` (sharp, geometric) |
| **Borders** | Thin rules (`1px solid`) used as grid dividers, not decoration |
| **Shadows** | None. Depth is achieved through layering and contrast |
| **Typography** | Sans-serif only. Large display type (48–120px), strict size scale |
| **Font Weight** | Bold (700–900) for headlines, Regular (400) for body |
| **Line Height** | Tight: `1.1` – `1.2` for headlines, `1.5` – `1.6` for body |
| **Letter Spacing** | Tight (`-0.02em` to `-0.04em`) for headlines |
| **Grid** | 12-column modular grid, strict alignment |
| **Colors** | Limited palette: 1–2 accent colors + black/white |
| **Imagery** | Full-bleed photography, duotone treatments |

---

## Color Palette

Swiss Design uses restrained, high-contrast palettes. Color is functional — used to highlight, categorize, or create hierarchy.

### Classic Swiss

```css
--swiss-black: #000000;
--swiss-white: #FFFFFF;
--swiss-red: #FF0000;        /* Signal red — the classic Swiss accent */
--swiss-gray-100: #F5F5F5;
--swiss-gray-300: #D4D4D4;
--swiss-gray-600: #737373;
--swiss-gray-900: #1A1A1A;
```

### Modern Swiss (Softer)

```css
--swiss-ink: #111111;
--swiss-paper: #FAFAFA;
--swiss-accent: #0055FF;     /* International Klein Blue */
--swiss-warm: #FF4D00;       /* Warm signal orange */
--swiss-muted: #A0A0A0;
```

### Swiss Dark Mode

```css
--swiss-bg: #0A0A0A;
--swiss-surface: #161616;
--swiss-text: #E5E5E5;
--swiss-accent: #FF3333;
--swiss-divider: #2A2A2A;
```

---

## Tailwind CSS Implementation

### `tailwind.config.js` Extension

```javascript
module.exports = {
  theme: {
    extend: {
      fontFamily: {
        swiss: ['"Inter"', '"Helvetica Neue"', '"Arial"', 'sans-serif'],
        display: ['"Space Grotesk"', '"Inter"', 'sans-serif'],
      },
      fontSize: {
        'display-xl': ['7.5rem', { lineHeight: '1.05', letterSpacing: '-0.04em' }],
        'display-lg': ['4.5rem', { lineHeight: '1.1', letterSpacing: '-0.03em' }],
        'display-md': ['3rem', { lineHeight: '1.15', letterSpacing: '-0.02em' }],
        'heading':    ['1.5rem', { lineHeight: '1.2', letterSpacing: '-0.01em' }],
        'body':       ['1rem', { lineHeight: '1.6' }],
        'caption':    ['0.75rem', { lineHeight: '1.4', letterSpacing: '0.05em' }],
      },
      colors: {
        swiss: {
          black: '#000000',
          white: '#FFFFFF',
          red: '#FF0000',
          blue: '#0055FF',
          gray: {
            100: '#F5F5F5',
            300: '#D4D4D4',
            600: '#737373',
            900: '#1A1A1A',
          },
        },
      },
      borderRadius: {
        swiss: '2px',
      },
      spacing: {
        grid: '1.5rem',    /* Base grid unit */
      },
    },
  },
};
```

### Component Patterns

#### Hero Section
```html
<section class="grid grid-cols-12 gap-0 min-h-screen">
  <div class="col-span-7 flex flex-col justify-end p-12">
    <p class="text-caption uppercase tracking-widest text-swiss-gray-600 mb-6">
      Established 2026
    </p>
    <h1 class="text-display-xl font-bold text-swiss-black leading-none">
      Design<br/>is a<br/>System
    </h1>
  </div>
  <div class="col-span-5 bg-swiss-black">
    <img src="hero.jpg" class="w-full h-full object-cover mix-blend-luminosity" />
  </div>
</section>
```

#### Navigation
```html
<nav class="flex items-center justify-between px-12 py-6 border-b border-swiss-gray-300">
  <span class="text-body font-bold uppercase tracking-widest">Studio</span>
  <div class="flex gap-8">
    <a href="#" class="text-caption uppercase tracking-widest hover:text-swiss-red transition-colors">Work</a>
    <a href="#" class="text-caption uppercase tracking-widest hover:text-swiss-red transition-colors">About</a>
    <a href="#" class="text-caption uppercase tracking-widest hover:text-swiss-red transition-colors">Contact</a>
  </div>
</nav>
```

#### Content Card (Grid-Aligned)
```html
<article class="border-t border-swiss-gray-300 py-8 grid grid-cols-12 gap-6">
  <span class="col-span-1 text-caption text-swiss-gray-600">01</span>
  <h3 class="col-span-4 text-heading font-bold">Project Title</h3>
  <p class="col-span-5 text-body text-swiss-gray-600">
    Brief description maintaining grid alignment across the modular structure.
  </p>
  <span class="col-span-2 text-caption text-swiss-gray-600 text-right">2026</span>
</article>
```

#### Button
```html
<button class="px-8 py-3 bg-swiss-black text-swiss-white text-caption uppercase tracking-widest hover:bg-swiss-red transition-colors duration-200">
  View Project
</button>
```

---

## Layout Rules

1. **Grid First** — Always start with `grid grid-cols-12`. No exceptions.
2. **Horizontal Rules** — Use `border-t` or `border-b` to section content, not cards or boxes.
3. **Numbering** — Index items with small numbers (`01`, `02`) in a dedicated column.
4. **Uppercase Captions** — Small text is always uppercase with wide tracking (`tracking-widest`).
5. **Full-Bleed Images** — Images span full columns, often with `mix-blend-luminosity` or `grayscale`.
6. **No Rounded Corners** — Maximum `rounded-sm` (2px). Prefer `rounded-none`.
7. **No Shadows** — Elevation is communicated through contrast and spacing, never `shadow-*`.
8. **Minimal Color** — One accent color maximum. Let black, white, and gray do the work.

---

## Typography Rules

1. **Display text** — Massive, bold, tight letter-spacing. Can break across lines for dramatic effect.
2. **Body text** — Regular weight, comfortable line-height (1.5–1.6).
3. **Captions/Labels** — Small, uppercase, wide letter-spacing. Used for metadata, categories, dates.
4. **No italic** for emphasis — use weight or color instead.
5. **No underline** for links — use color change on hover.

---

## Motion & Interaction

- **Transitions** — Minimal: `transition-colors duration-200` or `transition-opacity duration-300`.
- **No bouncy animations** — Movement is linear and purposeful.
- **Hover states** — Color shift only (e.g., black → red). No scale, no shadow, no transform.
- **Page transitions** — Simple fade or slide. Nothing playful.

---

## Anti-Patterns (What NOT to Do)

- ❌ Rounded corners > 4px
- ❌ Drop shadows or glows
- ❌ Gradient backgrounds
- ❌ Decorative illustrations or icons
- ❌ Centered text layouts (except single-line captions)
- ❌ More than 2 accent colors
- ❌ Comic Sans, script fonts, or serif fonts
- ❌ Skeuomorphic elements
- ❌ Cluttered layouts without grid discipline

---

## Famous References

- **Josef Müller-Brockmann** — Grid Systems in Graphic Design
- **Max Miedinger** — Creator of Helvetica
- **Armin Hofmann** — Graphic Design Manual
- **Modern Web** — [Stripe](https://stripe.com), [Linear](https://linear.app), [Vercel](https://vercel.com)

---

*"The grid system is an aid, not a guarantee. It permits a number of possible uses and each designer can look for a solution appropriate to his personal style."* — Josef Müller-Brockmann
