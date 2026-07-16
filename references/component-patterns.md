# Component Patterns

Universal component patterns applicable across all design systems. Adapt to the chosen system's tokens and spacing.

## 8-State Discipline

Every interactive component MUST ship code for all 8 states. This is mandatory, not advisory.

| # | State | Trigger | Implementation |
|---|-------|---------|----------------|
| 1 | **default** | Initial render | Resting visual |
| 2 | **hover** | Mouse over | `:hover` pseudo-class |
| 3 | **focus** | Keyboard focus | `:focus-visible` with visible ring |
| 4 | **active** | Pressed | `:active` pseudo-class |
| 5 | **disabled** | `disabled` attribute | `opacity: 0.5; cursor: not-allowed; pointer-events: none` |
| 6 | **loading** | Processing | `data-state="loading"`, replace label with spinner/ellipsis, disable interaction |
| 7 | **error** | Validation/request failure | `data-state="error"`, red accent, error message |
| 8 | **success** | Completed | `data-state="success"`, green accent, checkmark |

**State demo**: Use `generate_8state_component` (the-designer MCP) to produce a standalone preview page with all 8 states rendered simultaneously.

**State CSS pattern**:
```css
.btn:hover, .btn.is-hover { background: var(--color-paper-3); }
.btn:focus-visible, .btn.is-focus { outline: 2px solid var(--color-focus); outline-offset: 2px; }
.btn:active, .btn.is-active { transform: translateY(1px); }
.btn:disabled { opacity: 0.5; cursor: not-allowed; pointer-events: none; }
.btn[data-state="loading"] { cursor: wait; }
.btn[data-state="error"] { border-color: var(--color-accent); }
.btn[data-state="success"] { border-color: var(--color-accent-2); }
```

## Forms

### Input Field Structure
```
Label
[ Input field                    ]
Helper text / Error message
```

**States**: default, hover, focus-visible, active, disabled, loading, error, success

**Required patterns**:
- Label above input, not placeholder-only (placeholder-only is an anti-pattern)
- Error message below input with color and icon
- Helper text for complex fields
- Required fields: `*` after label
- Max-width: 480px for single-column

### Input heights
| Size | Height |
|------|--------|
| Small | 32px |
| Medium | 40px |
| Large | 48px |

### Form Layout
```
Single Column (preferred):
[ Full-width field              ]
[ Full-width field              ]

Two Column (dense admin):
[ Label ] [ Input              ]
[ Label ] [ Input              ]
```

**Spacing**: 16-24px between field groups, 8px between label and input

### Validation
- Inline validation on blur, not on every keystroke
- Error state: red accent + message below
- Never rely on color alone — always include text
- Focus ring must appear instantly (no animation)

## Tables

### Structure
```
[ Search/Filter bar                    ]
[ Action bar (bulk actions)            ]
+---+----------+----------+----------+
| # | Column A | Column B | Column C |  ← Header (sticky)
+---+----------+----------+----------+
| 1 | Data     | Data     | Data     |  ← Row
| 2 | Data     | Data     | Data     |
+---+----------+----------+----------+
[ Pagination                    Page X ]
```

**Column types**:
- Text: left-aligned
- Numbers: right-aligned
- Dates: center or left-aligned
- Actions: right-aligned, icon buttons

**Empty state**: Illustration + message + action button
**Loading state**: Skeleton rows, never empty page during load

## Navigation

### Sidebar (Admin/Dashboard)
```
Logo
──────────
Section Header
  Nav Item (icon + label)
  Nav Item
──────────
User/Settings (bottom)
```

**Width**: 240px (expanded), 64px (collapsed icon-only)
**States**: default, hover, active, focus-visible

### Top Navigation (Marketing/SaaS)
```
[ Logo ] [ Nav ] [ Nav ] [ Nav ]   [ CTA ]
```

**Height**: 56-72px
**Mobile**: Hamburger menu, slide-out drawer

### Tab Navigation
```
[ Tab 1 | Tab 2 | Tab 3 ]
────────────────────────
Content area
```

**Active**: Underline or filled background. **Disabled**: Muted text.

## Modals / Dialogs

### Structure
```
+-----------------------------------+
|  Title                     [X]   |
|-----------------------------------|
|  Body content                    |
|-----------------------------------|
|            [ Cancel ] [ Confirm ]|
+-----------------------------------+
```

**Widths**: Small 400px, Medium 560px, Large 720px, Full 90vw

**Behavior**:
- Backdrop: dark overlay, click to dismiss
- Focus trap: Tab cycles within modal only
- ESC key closes (if dismissible)
- Return focus to trigger element on close
- Scroll lock on body when open
- Modal transitions: opacity + translateY, animate transform/opacity only

## Cards

### Standard Card
```
+-----------------------------------+
|  Title                           |
|  Description text                |
|  [ Action ]     [ Action ]       |
+-----------------------------------+
```

**States**: default, hover (subtle lift via translateY), focus-visible within
**Variants**: elevated (shadow), outlined (border), filled (background)
**Spacing**: 16-24px padding internally

## Buttons

### Hierarchy
1. **Primary**: Filled, high contrast — main action per screen
2. **Secondary**: Outlined or ghost — secondary actions
3. **Tertiary/Text**: No border — low-emphasis
4. **Danger**: Red filled — destructive

### Sizes
| Size | Height | Padding | Font Size |
|------|--------|---------|-----------|
| Small | 32px | 8px 12px | 12-13px |
| Medium | 40px | 10px 16px | 14px |
| Large | 48px | 12px 24px | 16px |

### States (mandatory 8)
| State | Visual | Interaction |
|-------|--------|-------------|
| default | Resting fill | — |
| hover | -2px translateY or darker fill | `transition: transform var(--dur-fast) var(--ease-out)` |
| focus-visible | 2px ring at --color-focus | Instant appearance, no animation |
| active | translateY(1px) or scale(0.97) | `transition: transform 0.1s` |
| disabled | 50% opacity | `cursor: not-allowed`, no pointer events |
| loading | Spinner + "Working..." text | `pointer-events: none` |
| error | Red accent border + shake? | Show error message below |
| success | Green accent + checkmark | Brief indication, then revert |

### Icon Buttons
- Square aspect ratio (same height/width)
- Icon-only: must have `aria-label`
- Icon + label: icon on left, 8px gap

## Toasts / Notifications

### Structure
```
[ Icon ]  Title/Message                    [ Close ]
```

**Positions**: Top-right (default)
**Variants**: Success (green), Warning (amber), Error (red), Info (blue)
**Auto-dismiss**: 4-6 seconds for success/info, manual dismiss for errors
**Stacking**: New toasts stack below existing, max 3 visible

**Animate**: transform + opacity only. Slide in from right.
**Never**: bounce or overshoot for toast entrance.

## Dropdowns / Selects

### Single Select
```
[ Selected value              ▼ ]
┌──────────────────────────────┐
│  Option 1                    │
│  Option 2 (selected)  ✓     │
│  Option 3                    │
└──────────────────────────────┘
```

**Behavior**:
- Open on click or Enter/Space
- Arrow keys navigate options
- Close on Escape or click outside
- Max-height: 240-320px with scroll
- Animate: opacity + translateY only

## Breadcrumbs
```
Home / Section / Sub-section / Current Page
```

**Separator**: `/` or chevron icon. **Last item**: Plain text (not a link).

## Pagination
```
[ ← Previous ]  1  2  3  ...  10  [ Next → ]
```

**States**: default, hover, active, disabled (for first/last page bounds)

## Empty States
```
[ Icon ]

Title: "No results found"
Description: "Try adjusting your filters or search terms."
[ Action Button ]
```

**Always include**: Title + description + primary action.

## Loading States

| Pattern | When |
|---------|------|
| Skeleton screen | Content loading (cards, tables, profiles) |
| Spinner | Short operations |
| Progress bar | Known-duration operations |
| Dots | Indeterminate waits |

**Rules**:
- Skeleton mirrors actual content layout
- Never show empty page during load
- Minimum 300ms before showing loading state
- Animate skeleton via CSS `@keyframes shimmer` with `background-position`
