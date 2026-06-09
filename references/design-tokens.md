# Design Tokens

Universal token system. Each design system should map these to its own values.

## Color Tokens

### Semantic Colors
| Token | Light Mode | Dark Mode | Usage |
|-------|-----------|-----------|-------|
| `--color-primary` | System primary | System primary | Primary actions, links |
| `--color-primary-hover` | Primary -10% | Primary +10% | Hover state |
| `--color-primary-active` | Primary -20% | Primary +20% | Active/pressed state |
| `--color-secondary` | Gray 500 | Gray 400 | Secondary actions |
| `--color-success` | Green 600 | Green 400 | Success states |
| `--color-warning` | Amber 500 | Amber 400 | Warnings |
| `--color-error` | Red 600 | Red 400 | Errors, destructive |
| `--color-info` | Blue 600 | Blue 400 | Informational |

### Neutral Colors
| Token | Light Mode | Dark Mode |
|-------|-----------|-----------|
| `--color-bg` | White (#FFF) | Gray 900 (#111) |
| `--color-bg-secondary` | Gray 50 | Gray 800 |
| `--color-bg-tertiary` | Gray 100 | Gray 700 |
| `--color-surface` | White | Gray 800 |
| `--color-border` | Gray 200 | Gray 700 |
| `--color-border-strong` | Gray 300 | Gray 600 |
| `--color-text` | Gray 900 | Gray 50 |
| `--color-text-secondary` | Gray 600 | Gray 400 |
| `--color-text-muted` | Gray 400 | Gray 500 |

### Gray Scale (10 steps)
| Step | Hex | Usage |
|------|-----|-------|
| 50 | #F9FAFB | Backgrounds |
| 100 | #F3F4F6 | Secondary backgrounds |
| 200 | #E5E7EB | Borders |
| 300 | #D1D5DB | Borders strong, disabled |
| 400 | #9CA3AF | Muted text, placeholders |
| 500 | #6B7280 | Secondary text |
| 600 | #4B5563 | Body text |
| 700 | #374151 | Headings |
| 800 | #1F2937 | Dark backgrounds |
| 900 | #111827 | Darkest, primary text |

---

## Spacing Scale

Base unit: **4px**

| Token | Value | Usage |
|-------|-------|-------|
| `--space-0` | 0 | Reset |
| `--space-0.5` | 2px | Tight gaps (icon-text) |
| `--space-1` | 4px | Minimal |
| `--space-1.5` | 6px | Compact |
| `--space-2` | 8px | Default small gap |
| `--space-3` | 12px | Default gap |
| `--space-4` | 16px | Standard gap |
| `--space-5` | 20px | Medium gap |
| `--space-6` | 24px | Section gap |
| `--space-8` | 32px | Large section gap |
| `--space-10` | 40px | Page section |
| `--space-12` | 48px | Major section |
| `--space-16` | 64px | Page margins |
| `--space-20` | 80px | Hero spacing |
| `--space-24` | 96px | Large hero |

---

## Typography Scale

### Font Families
| Token | Value | Usage |
|-------|-------|-------|
| `--font-sans` | -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif | Body text |
| `--font-mono` | 'SF Mono', 'Fira Code', 'Fira Mono', Menlo, Consolas, monospace | Code |
| `--font-display` | System or brand font | Hero/headlines (optional) |

### Type Scale
| Token | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| `--text-xs` | 12px | 16px | 400 | Captions, labels |
| `--text-sm` | 14px | 20px | 400 | Helper text, small UI |
| `--text-base` | 16px | 24px | 400 | Body text |
| `--text-lg` | 18px | 28px | 400 | Large body, subheadings |
| `--text-xl` | 20px | 28px | 500 | Section headings |
| `--text-2xl` | 24px | 32px | 600 | Page titles |
| `--text-3xl` | 30px | 36px | 600 | Major headings |
| `--text-4xl` | 36px | 40px | 600 | Display |
| `--text-5xl` | 48px | 48px | 700 | Hero |

### Font Weights
| Token | Value | Usage |
|-------|-------|-------|
| `--font-normal` | 400 | Body |
| `--font-medium` | 500 | Labels, emphasis |
| `--font-semibold` | 600 | Headings, buttons |
| `--font-bold` | 700 | Hero, strong emphasis |

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `--radius-none` | 0 | No rounding |
| `--radius-sm` | 4px | Tags, badges, small elements |
| `--radius-md` | 8px | Inputs, buttons, cards |
| `--radius-lg` | 12px | Cards, dialogs |
| `--radius-xl` | 16px | Large cards, modals |
| `--radius-2xl` | 24px | FABs, large elements |
| `--radius-full` | 9999px | Pills, avatars, circles |

---

## Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `--shadow-xs` | 0 1px 2px rgba(0,0,0,0.05) | Subtle lift |
| `--shadow-sm` | 0 1px 3px rgba(0,0,0,0.1), 0 1px 2px rgba(0,0,0,0.06) | Cards, dropdowns |
| `--shadow-md` | 0 4px 6px rgba(0,0,0,0.1), 0 2px 4px rgba(0,0,0,0.06) | Hover states |
| `--shadow-lg` | 0 10px 15px rgba(0,0,0,0.1), 0 4px 6px rgba(0,0,0,0.05) | Modals, popovers |
| `--shadow-xl` | 0 20px 25px rgba(0,0,0,0.1), 0 10px 10px rgba(0,0,0,0.04) | Floating elements |

### Dark Mode Adjustments
Multiply shadow opacity by 0.3 and increase spread for dark mode:
```css
--shadow-sm-dark: 0 1px 3px rgba(0,0,0,0.3), 0 1px 2px rgba(0,0,0,0.2);
```

---

## Breakpoints

| Token | Value | Target |
|-------|-------|--------|
| `--bp-sm` | 640px | Mobile landscape |
| `--bp-md` | 768px | Tablet |
| `--bp-lg` | 1024px | Desktop |
| `--bp-xl` | 1280px | Large desktop |
| `--bp-2xl` | 1536px | Ultra-wide |

---

## Z-Index Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--z-base` | 0 | Default |
| `--z-dropdown` | 1000 | Dropdowns, selects |
| `--z-sticky` | 1020 | Sticky headers |
| `--z-fixed` | 1030 | Fixed nav, sidebar |
| `--z-overlay` | 1040 | Backdrops, overlays |
| `--z-modal` | 1050 | Modals, dialogs |
| `--z-popover` | 1060 | Popovers, tooltips |
| `--z-toast` | 1070 | Toasts, notifications |

---

## Duration Scale

| Token | Value | Usage |
|-------|-------|-------|
| `--duration-fast` | 100ms | Micro-interactions |
| `--duration-normal` | 200ms | Standard transitions |
| `--duration-slow` | 300ms | Complex animations |
| `--duration-slower` | 500ms | Page transitions |

---

## Easing Curves

| Token | Value | Usage |
|-------|-------|-------|
| `--ease-default` | cubic-bezier(0.4, 0, 0.2, 1) | Standard motion |
| `--ease-in` | cubic-bezier(0.4, 0, 1, 1) | Exiting elements |
| `--ease-out` | cubic-bezier(0, 0, 0.2, 1) | Entering elements |
| `--ease-in-out` | cubic-bezier(0.4, 0, 0.2, 1) | State changes |
| `--ease-spring` | cubic-bezier(0.34, 1.56, 0.64, 1) | Bounce, playful |
