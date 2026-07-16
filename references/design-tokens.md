# Design Tokens

Universal token system. Tokens are locked — every color and font-family must reference a named CSS custom property. No inline hex/OKLCH values bypassing the token block.

## Color Tokens — OKLCH Primary

Prefer OKLCH over hex for perceptual uniformity. Generate via `generate_tokens` (the-designer MCP) or construct using the paper/accent architecture below.

### Paper + Accent Architecture (Hallmark)

Each theme defines three diversification axes:

| Axis | Values |
|------|--------|
| **Paper band** | dark (L < 30%), mid (30-85%), light (> 85%) |
| **Display style** | high-contrast-serif, roman-serif, classical-serif, geometric-sans, grotesk-sans, rounded-sans, mono, display-condensed, display-heavy |
| **Accent hue** | warm (10-60°), cool (200-300°), neutral, chromatic-other |

Generated token block (via `generate_tokens`):
```css
:root {
  --color-paper: oklch(97% 0.01 85);
  --color-paper-2: oklch(93% 0.02 85);
  --color-paper-3: oklch(88% 0.03 85);
  --color-text: oklch(25% 0.02 85);
  --color-text-2: oklch(45% 0.03 85);
  --color-accent: oklch(50% 0.25 250);
  --color-accent-2: oklch(45% 0.20 130);
  --color-border: oklch(80% 0.02 85);
  --color-focus: oklch(60% 0.30 260);
  --font-display: 'Inter', system-ui, sans-serif;
  --font-body: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

**Locked-token discipline**: Every color and font-family declaration in output CSS must reference these named variables. Lifting a new value into the token block is required before referencing it.

### Semantic Colors (for structural mapping)

| Token | Usage |
|-------|-------|
| `--color-paper` | Page background |
| `--color-paper-2` | Secondary surface (cards, panels) |
| `--color-paper-3` | Interactive hover surface |
| `--color-text` | Primary body text |
| `--color-text-2` | Secondary/muted text |
| `--color-accent` | Primary action color |
| `--color-accent-2` | Success/positive states |
| `--color-border` | Dividers, borders |
| `--color-focus` | Focus ring (:focus-visible) |

## Spacing Scale

Base unit: **4px**

| Token | Value | Usage |
|-------|-------|-------|
| `--space-xs` | 4px | Minimal gap |
| `--space-sm` | 8px | Default small gap |
| `--space-md` | 16px | Standard gap |
| `--space-lg` | 24px | Section gap |
| `--space-xl` | 32px | Large section gap |
| `--space-2xl` | 48px | Major section |
| `--space-3xl` | 64px | Page margins |
| `--space-4xl` | 96px | Hero spacing |

## Typography Scale

### Font Families (via named tokens)
| Token | Usage |
|-------|-------|
| `--font-display` | Hero/headlines |
| `--font-body` | Body text |
| `--font-mono` | Code |

### Type Scale
| Token | Size | Usage |
|-------|------|-------|
| `--text-display` | clamp(2.5rem, 6vw, 4.5rem) | Hero headline (use size-by-length brackets) |
| `--text-display-s` | clamp(2rem, 4vw, 3rem) | Larger headlines |
| `--text-2xl` | 1.75rem | Page titles |
| `--text-xl` | 1.25rem | Section headings |
| `--text-lg` | 1.125rem | Large body |
| `--text-base` | 1rem | Body text |
| `--text-sm` | 0.875rem | Helper, labels |
| `--text-xs` | 0.75rem | Captions |

**Hero headline sizing**: Match font-size to copy length. ≤7 words (≤50 chars): use `--text-display`. 51-90 chars: cap at `--text-display-s`. >90 chars: rewrite shorter or cap at `--text-2xl`.

**Discipline**: No italic headings. Headings are always roman (`font-style: normal`). Italic survives only as body-copy emphasis inside running paragraphs.

## Easings

| Token | Value | Usage |
|-------|-------|-------|
| `--ease-out` | cubic-bezier(0.16, 1, 0.3, 1) | Entering elements |
| `--ease-in` | cubic-bezier(0.4, 0, 0.68, 0.06) | Exiting elements |
| `--ease-in-out` | cubic-bezier(0.65, 0, 0.35, 1) | State changes |

No other easings. No bounce/overshoot on UI state transitions.

## Durations

| Token | Value | Usage |
|-------|-------|-------|
| `--dur-fast` | 150ms | Hover, micro-interactions |
| `--dur-base` | 250ms | Standard transitions |
| `--dur-slow` | 400ms | Complex animations |

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-sm` | 4px | Tags, badges |
| `--radius-md` | 8px | Inputs, buttons, cards |
| `--radius-lg` | 16px | Large cards, modals |

Pick 2-3 values max and reuse.

## Breakpoints

| Name | Value | Target |
|------|-------|--------|
| `--bp-sm` | 640px | Mobile landscape |
| `--bp-md` | 768px | Tablet |
| `--bp-lg` | 1024px | Desktop |
| `--bp-xl` | 1280px | Large desktop |

## Z-Index Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--z-dropdown` | 1000 | Dropdowns |
| `--z-sticky` | 1020 | Sticky headers |
| `--z-overlay` | 1040 | Backdrops |
| `--z-modal` | 1050 | Modals |
| `--z-toast` | 1070 | Toasts |
