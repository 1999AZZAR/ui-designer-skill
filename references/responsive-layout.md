# Responsive Layout

Mobile-first grid and layout patterns for all screen sizes.

## Hard Floor — Non-Negotiable

Every output must render flawlessly at all four mobile widths. These are hard requirements, not a wish list:

1. **No horizontal scroll** — `overflow-x: clip` on both `html` and `body`. Never use `overflow-x: hidden`.
2. **No two-line clickable text** — buttons, nav links, CTAs must fit on one line at 320px.
3. **Image-bearing grid tracks** — use `minmax(0, 1fr)`, never bare `1fr`.
4. **Display headers wrap safely** — use `overflow-wrap: anywhere; min-width: 0` on display headings.
5. **Section heads collapse to single column** on mobile across every theme variant.
6. **Minimum touch target**: 44x44px (WCAG 2.5.5).
7. **Spacing between touch targets**: 8px minimum.

## Breakpoints

| Name | Value | Target |
|------|-------|--------|
| Mobile S | 320px | Small phones |
| Mobile M | 375px | iPhone |
| Mobile L | 414px | Large phones |
| Tablet | 768px | iPad / tablet |
| Desktop | 1024px | Desktop |
| Wide | 1280px+ | Large desktop |

## Grid System

### 4-8-12 Column Grid
```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: 24px;
}
```

**Column counts by breakpoint**:
| Breakpoint | Columns | Gutter | Margin |
|------------|---------|--------|--------|
| Mobile (<640px) | 4 | 16px | 16px |
| Tablet (768px) | 8 | 24px | 24px |
| Desktop (1024px) | 12 | 24px | 32px |
| Wide (1280px+) | 12 | 32px | auto |

### Grid Usage
```html
<!-- Full width -->
<div class="col-span-12">...</div>

<!-- Half -->
<div class="col-span-6">...</div>

<!-- Sidebar + Content -->
<div class="col-span-3">Sidebar</div>
<div class="col-span-9">Content</div>

<!-- Card grid -->
<div class="col-span-4">Card</div>
<div class="col-span-4">Card</div>
<div class="col-span-4">Card</div>
```

## Breakpoint Behavior

### Mobile (< 640px)
- Single column layout — all elements stack vertically
- Full-width inputs and buttons
- Bottom tab bar or hamburger menu
- Hide sidebar (use drawer)
- Section heads collapse to single column
- Reduce font sizes: H1 → clamp(1.75rem, 5vw, 2rem)
- Tables become stacked card layouts
- Overflow-wrap: anywhere on all headings

### Tablet (640px — 1023px)
- 2-column layouts possible
- Sidebar: collapsed or overlay
- Cards: 2 per row
- Forms: 2 columns for related fields

### Desktop (1024px — 1279px)
- Full 12-column grid
- Sidebar always visible
- Cards: 3-4 per row
- Full table display
- Multi-column forms

### Wide (1280px+)
- Max-width container (1280px)
- More breathing room
- Cards: 4+ per row

## Layout Patterns

### Admin Dashboard
```
┌──────────┬──────────────────────────────┐
│          │  Header / Breadcrumb         │
│ Sidebar  ├──────────────────────────────│
│ (fixed)  │  Content Area                │
│          │                              │
└──────────┴──────────────────────────────┘
```
- Sidebar: fixed, 240px / 64px collapsed (overlay on mobile)
- Content: scrollable, max-width 1280px

### Marketing Landing
```
┌──────────────────────────────────────────┐
│  Top Nav (sticky)                        │
├──────────────────────────────────────────┤
│  Hero Section (full-width)               │
├──────────────────────────────────────────┤
│  Features (responsive grid)              │
├──────────────────────────────────────────┤
│  CTA Section                             │
├──────────────────────────────────────────┤
│  Footer                                  │
└──────────────────────────────────────────┘
```

### Content / App
```
┌──────────────────────────────────────────┐
│  Top Bar (64px)                          │
├──────────────────────────────────────────┤
│  Main Content (scrollable)               │
└──────────────────────────────────────────┘
```
- Mobile: Bottom tab bar (max 5 items)
- Desktop: Top navigation

## Container Queries

Prefer container queries for component-level responsiveness:
```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card { display: flex; }
}
```

## Responsive Typography

| Token | Mobile | Tablet | Desktop |
|-------|--------|--------|---------|
| H1 | clamp(1.75rem, 5vw, 2.5rem) | 2.5rem | 3rem+ |
| H2 | 1.5rem | 1.75rem | 2rem |
| Body | 0.875rem | 1rem | 1rem |

## Touch Targets

| Rule | Value |
|------|-------|
| Minimum size | 44x44px |
| Recommended | 48x48px |
| Spacing between | 8px minimum |

```css
.touch-target {
  min-height: 44px;
  min-width: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

## Mobile-Specific Patterns

### Bottom Navigation
```
┌────────┬────────┬────────┬────────┬────────┐
│  Home  │ Search │  Plus  │ Alerts │ Profile│
└────────┴────────┴────────┴────────┴────────┘
```
- 5 items max
- Active state: filled icon + label
- Safe area padding for notch devices

### Tables → Card Layout on Mobile
```css
@media (max-width: 640px) {
  table, thead, tbody, th, td, tr {
    display: block;
  }
  thead { display: none; }
  td {
    display: flex;
    justify-content: space-between;
    padding: 12px 16px;
  }
  td::before {
    content: attr(data-label);
    font-weight: 600;
  }
}
```

## Safe Areas

```css
.content {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
```

## Responsive Images

```html
<picture>
  <source media="(min-width: 1024px)" srcset="large.webp">
  <source media="(min-width: 640px)" srcset="medium.webp">
  <img src="small.webp" alt="..." loading="lazy" decoding="async">
</picture>
```

**Rules**:
- Use `loading="lazy"` for below-fold images
- Use `decoding="async"` for non-critical images
- Provide multiple sizes via `srcset`
- Always include `alt` text
