# Component Patterns

Universal component patterns applicable across all design systems. Adapt to the chosen system's tokens and spacing.

## Forms

### Input Field Structure
```
Label (optional helper text)
[ Input field                    ]
Helper text / Error message
```

**States**: default, hover, focus, disabled, error, success

**Required patterns**:
- Label above input, not placeholder-only
- Error message below input with color and icon
- Helper text for complex fields
- Required fields: `*` after label or "(Required)" text
- Max-width: 480px for single-column, 320px for multi-column

**Input heights**: Small 32px, Medium 40px, Large 48px

### Form Layout
```
Single Column (preferred):
[ Full-width field              ]
[ Full-width field              ]
[ Half field    ] [ Half field  ]

Two Column (dense admin):
[ Label ] [ Input              ]
[ Label ] [ Input              ]
```

**Spacing**: 16–24px between field groups, 8px between label and input

### Validation
- Inline validation on blur, not on every keystroke
- Error state: red border + icon + message below
- Success state: green border or checkmark (optional)
- Never rely on color alone — always include text/icon

---

## Tables

### Structure
```
[ Search/Filter bar                    ]
[ Action bar (bulk actions, export)    ]
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

**Row density**: Compact (40px), Default (48px), Comfortable (56px)

**Empty state**: Illustration + message + action button

**Loading state**: Skeleton rows or spinner overlay

---

## Navigation

### Sidebar (Admin/Dashboard)
```
Logo
──────────
Section Header
  Nav Item (icon + label)
  Nav Item
    Nested Item
    Nested Item
──────────
Section Header
  Nav Item
──────────
User/Settings (bottom)
```

**Width**: 240px (expanded), 64px (collapsed icon-only)

**Active state**: Background highlight + bold text + indicator (left border or dot)

**Hover state**: Subtle background change

### Top Navigation (Marketing/SaaS)
```
[ Logo ] [ Nav Item ] [ Nav Item ] [ Nav Item ]    [ CTA ]
```

**Height**: 56–72px

**Mobile**: Hamburger menu, slide-out drawer

### Tab Navigation
```
[ Tab 1 | Tab 2 | Tab 3 ]
────────────────────────
Content area
```

**Active**: Underline or filled background
**Disabled**: Muted text, no pointer events

---

## Modals / Dialogs

### Structure
```
+-----------------------------------+
|  Title                     [X]   |
|-----------------------------------|
|  Body content                    |
|                                  |
|-----------------------------------|
|            [ Cancel ] [ Confirm ]|
+-----------------------------------+
```

**Widths**: Small 400px, Medium 560px, Large 720px, Full 90vw

**Behavior**:
- Backdrop: dark overlay, click to dismiss (if not critical)
- Focus trap: Tab cycles within modal only
- ESC key closes (if dismissible)
- Return focus to trigger element on close
- Scroll lock on body when open

**Actions placement**: Right-aligned (primary rightmost), or split (cancel left, confirm right)

---

## Cards

### Standard Card
```
+-----------------------------------+
|  [ Optional media/image ]         |
|-----------------------------------|
|  Title                           |
|  Description text                |
|                                   |
|  [ Action 1 ]     [ Action 2 ]   |
+-----------------------------------+
```

**Variants**: elevated (shadow), outlined (border), filled (background)

**Spacing**: 16–24px padding internally

**Border-radius**: Match system (8–16px typical)

---

## Buttons

### Hierarchy
1. **Primary**: Filled, high contrast — main action per screen
2. **Secondary**: Outlined or ghost — secondary actions
3. **Tertiary/Text**: No border — low-emphasis actions
4. **Danger**: Red filled — destructive actions

### Sizes
| Size | Height | Padding | Font Size |
|------|--------|---------|-----------|
| Small | 32px | 8px 12px | 12–13px |
| Medium | 40px | 10px 16px | 14px |
| Large | 48px | 12px 24px | 16px |

### States
- Default → Hover → Active → Focus → Disabled → Loading
- Loading: replace label with spinner, disable interaction
- Disabled: 40% opacity, `not-allowed` cursor

### Icon Buttons
- Square aspect ratio (same height/width as button size)
- Icon-only: must have `aria-label`
- Icon + label: icon on left, 8px gap

---

## Toasts / Notifications

### Structure
```
[ Icon ]  Title/Message                    [ Close ]
```

**Positions**: Top-right (default), bottom-right, top-center

**Variants**: Success (green), Warning (amber), Error (red), Info (blue)

**Auto-dismiss**: 4–6 seconds for success/info, manual dismiss for errors

**Stacking**: New toasts stack below existing, max 3 visible

---

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
- Type-ahead search for long lists
- Close on Escape or click outside
- Max-height: 240–320px with scroll

### Multi-Select
- Checkbox or tag-based selection
- Show selected count in trigger
- Clear all option available

---

## Breadcrumbs

```
Home / Section / Sub-section / Current Page
```

**Separator**: `/` or chevron icon
**Last item**: Bold or plain text (not a link)
**Mobile**: Truncate middle items, show `...`

---

## Pagination

```
[ ← Previous ]  1  2  3  ...  10  [ Next → ]
```

**Variants**: Numbered, simple (prev/next), load-more button

**Active page**: Filled background or bold

---

## Empty States

```
[ Illustration / Icon ]

Title: "No results found"
Description: "Try adjusting your filters or search terms."
[ Action Button ]
```

**Always include**: Title + description + primary action

---

## Loading States

| Pattern | When to Use |
|---------|-------------|
| Skeleton screen | Content loading (cards, tables, profiles) |
| Spinner | Short operations (form submit, file upload) |
| Progress bar | Known-duration operations (upload, install) |
| Dots/wave | Indeterminate waits |

**Rules**:
- Skeleton mirrors actual content layout
- Never show empty page during load
- Minimum 300ms before showing loading state (avoid flash)
