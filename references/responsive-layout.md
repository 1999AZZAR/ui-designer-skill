# Responsive Layout

Mobile-first grid and layout patterns for all screen sizes.

## Grid System

### 12-Column Grid (Default)
```css
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 16px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 24px;
}
```

**Column widths by breakpoint**:
| Breakpoint | Columns | Gutter | Margin |
|------------|---------|--------|--------|
| Mobile (<640px) | 4 | 16px | 16px |
| Tablet (768px) | 8 | 24px | 24px |
| Desktop (1024px) | 12 | 24px | 32px |
| Wide (1280px+) | 12 | 32px | auto |

### Grid Usage Examples
```html
<!-- Full width -->
<div class="col-span-12">...</div>

<!-- Half -->
<div class="col-span-6">...</div>

<!-- Third -->
<div class="col-span-4">...</div>

<!-- Sidebar + Content -->
<div class="col-span-3">Sidebar</div>
<div class="col-span-9">Content</div>

<!-- Card grid: 3 columns -->
<div class="col-span-4">Card 1</div>
<div class="col-span-4">Card 2</div>
<div class="col-span-4">Card 3</div>
```

---

## Breakpoint Behavior

### Mobile (< 640px)
- Single column layout
- Stack all elements vertically
- Full-width inputs and buttons
- Bottom navigation or hamburger menu
- Hide sidebar (use drawer)
- Reduce font sizes 10-15%
- Simplify tables → card layout

### Tablet (640px – 1023px)
- 2-column layouts possible
- Sidebar optional (collapsible)
- Cards: 2 per row
- Forms: 2 columns for related fields
- Tables: horizontal scroll

### Desktop (1024px – 1279px)
- Full 12-column grid
- Sidebar always visible
- Cards: 3-4 per row
- Full table display
- Multi-column forms

### Wide (1280px+)
- Max-width container (1280px)
- More breathing room
- Cards: 4+ per row
- Dense layouts acceptable

---

## Layout Patterns

### Admin Dashboard
```
┌──────────┬────────────────────────────┐
│          │  Header/Breadcrumb          │
│ Sidebar  ├────────────────────────────│
│ (fixed)  │                            │
│          │  Content Area              │
│          │                            │
│          │                            │
│          ├────────────────────────────│
│          │  Footer (optional)         │
└──────────┴────────────────────────────┘
```
- Sidebar: fixed, 240px / 64px collapsed
- Content: scrollable, max-width 1280px

### Marketing Landing
```
┌────────────────────────────────────────┐
│  Top Nav (fixed/sticky)               │
├────────────────────────────────────────┤
│  Hero Section (full-width)            │
├────────────────────────────────────────┤
│  Features (3-col grid)                │
├────────────────────────────────────────┤
│  CTA Section                          │
├────────────────────────────────────────┤
│  Footer                               │
└────────────────────────────────────────┘
```

### Content/App
```
┌────────────────────────────────────────┐
│  Top Bar (64px)                        │
├────────────────────────────────────────┤
│                                        │
│  Main Content (scrollable)             │
│                                        │
└────────────────────────────────────────┘
```
- Mobile: Bottom tab bar
- Desktop: Top navigation

---

## Container Queries (Modern)

Prefer container queries over media queries for component-level responsiveness:

```css
.card-container {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .card {
    display: flex;
    flex-direction: row;
  }
}

@container (min-width: 600px) {
  .card {
    grid-template-columns: 200px 1fr;
  }
}
```

---

## Responsive Utilities

### Show/Hide Classes
| Class | Mobile | Tablet | Desktop |
|-------|--------|--------|---------|
| `.hidden-mobile` | hidden | visible | visible |
| `.hidden-tablet` | visible | hidden | visible |
| `.hidden-desktop` | visible | visible | hidden |
| `.visible-mobile` | visible | hidden | hidden |
| `.visible-tablet` | hidden | visible | hidden |
| `.visible-desktop` | hidden | hidden | visible |

### Responsive Spacing
| Class | Mobile | Tablet | Desktop |
|-------|--------|--------|---------|
| `.p-responsive` | 16px | 24px | 32px |
| `.gap-responsive` | 16px | 24px | 32px |
| `.m-responsive` | 16px | 24px | 32px |

---

## Responsive Typography

| Token | Mobile | Tablet | Desktop |
|-------|--------|--------|---------|
| H1 | 28px | 36px | 48px |
| H2 | 24px | 30px | 36px |
| H3 | 20px | 24px | 30px |
| Body | 14px | 16px | 16px |
| Small | 12px | 14px | 14px |

---

## Touch Targets

Minimum touch target sizes (WCAG 2.5.5):
- **Minimum**: 44x44px
- **Recommended**: 48x48px
- **Spacing between targets**: 8px minimum

```css
.touch-target {
  min-height: 44px;
  min-width: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
}
```

---

## Mobile-Specific Patterns

### Bottom Navigation
```
┌─────────┬─────────┬─────────┬─────────┬─────────┐
│  Home   │ Search  │  Plus   │  Alerts │  Profile │
│   🏠    │   🔍    │    +    │   🔔    │    👤    │
└─────────┴─────────┴─────────┴─────────┴─────────┘
```
- 5 items max
- Active state: filled icon + label
- Safe area padding for notch devices

### Pull to Refresh
- Overscroll reveals spinner
- Release triggers refresh
- Show timestamp of last update

### Swipe Actions
- Swipe left: Delete/archive
- Swipe right: Mark as read/favorite
- Reveal actions gradually, don't hide content

---

## Safe Areas

Account for device-specific safe areas:
```css
.content {
  padding-top: env(safe-area-inset-top);
  padding-bottom: env(safe-area-inset-bottom);
  padding-left: env(safe-area-inset-left);
  padding-right: env(safe-area-inset-right);
}
```

---

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
