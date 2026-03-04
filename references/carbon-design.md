# Carbon Design System (IBM)

Carbon is IBM's open-source design system for products and digital experiences, emphasizing clarity, efficiency, and consistency across enterprise applications.

## Design Principles

### 1. Clarity
Present information and interactions in clear, understandable ways.
- Clear visual hierarchy
- Purposeful typography and spacing
- Meaningful iconography

### 2. Efficiency
Optimize workflows and reduce cognitive load.
- Streamlined user flows
- Predictable patterns
- Keyboard-first interactions

### 3. Consistency
Maintain unified experiences across all touchpoints.
- Reusable components
- Standardized patterns
- Systematic approach

### 4. Inclusive
Design for everyone, regardless of ability or context.
- WCAG 2.1 AA compliance
- Keyboard navigation
- Screen reader support

## Color System

### IBM Core Colors
```
Blue 60 (Primary): #0F62FE
Blue 70 (Hover): #0353E9
Blue 80 (Active): #002D9C

Gray Scale:
Gray 10: #F4F4F4
Gray 20: #E0E0E0
Gray 30: #C6C6C6
Gray 40: #A8A8A8
Gray 50: #8D8D8D
Gray 60: #6F6F6F
Gray 70: #525252
Gray 80: #393939
Gray 90: #262626
Gray 100: #161616
```

### Functional Colors
```
Success (Green 60): #24A148
Warning (Yellow 30): #F1C21B
Error (Red 60): #DA1E28
Info (Blue 60): #0F62FE
```

### Theme Support
Carbon provides four default themes:
- White (Background: #FFFFFF)
- Gray 10 (Background: #F4F4F4)
- Gray 90 (Background: #262626)
- Gray 100 (Background: #161616)

## Typography

### Font Family
```css
font-family: 'IBM Plex Sans', 'Helvetica Neue', Arial, sans-serif;
font-family: 'IBM Plex Mono', 'Menlo', 'DejaVu Sans Mono', monospace; /* Code */
```

### Type Scale
```
Heading 01: 14px / 18px, Semi-bold (600)
Heading 02: 16px / 22px, Semi-bold (600)
Heading 03: 20px / 26px, Regular (400)
Heading 04: 28px / 36px, Regular (400)
Heading 05: 32px / 40px, Light (300)
Heading 06: 42px / 50px, Light (300)
Heading 07: 54px / 64px, Light (300)

Body Short 01: 14px / 18px, Regular (400)
Body Short 02: 16px / 22px, Regular (400)
Body Long 01: 14px / 20px, Regular (400)
Body Long 02: 16px / 24px, Regular (400)

Code 01: 12px / 16px, Regular (400) - Mono
Code 02: 14px / 20px, Regular (400) - Mono

Label 01: 12px / 16px, Regular (400)
Label 02: 14px / 18px, Regular (400)
```

## Spacing System

Carbon uses rem-based spacing with 16px base:
```
2px (0.125rem), 4px (0.25rem), 8px (0.5rem), 12px (0.75rem),
16px (1rem), 24px (1.5rem), 32px (2rem), 40px (2.5rem),
48px (3rem), 64px (4rem), 80px (5rem), 96px (6rem),
160px (10rem)
```

Layout spacing tokens:
```
spacing-01: 2px
spacing-02: 4px
spacing-03: 8px
spacing-04: 12px
spacing-05: 16px
spacing-06: 24px
spacing-07: 32px
spacing-08: 40px
spacing-09: 48px
spacing-10: 64px
spacing-11: 80px
spacing-12: 96px
spacing-13: 160px
```

## Layout Grid

16-column responsive grid:
```
Small: < 672px (4 columns)
Medium: 672px - 1056px (8 columns)
Large: 1056px - 1312px (16 columns)
X-Large: 1312px - 1584px (16 columns)
Max: ≥ 1584px (16 columns)
```

Gutter spacing: 32px (default), 16px (small screens)

## Border & Radius

### Border Width
```
1px: Default borders
2px: Focus indicators
```

### Border Radius
```
None: 0px (default)
Small: 2px
Medium: 4px
Large: 8px
```

## Elevation & Shadow

```css
/* No elevation */
box-shadow: none;

/* Elevation 1 (Subtle) */
box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);

/* Elevation 2 (Raised) */
box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);

/* Elevation 3 (Overlay) */
box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);

/* Elevation 4 (Sticky) */
box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);

/* Elevation 5 (Modal) */
box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3);

/* Elevation 6 (Popover) */
box-shadow: 0 16px 32px rgba(0, 0, 0, 0.3);
```

## Component Examples

### Button (Tailwind)
```html
<!-- Primary Button -->
<button class="
  px-4 h-12
  bg-[#0F62FE] hover:bg-[#0353E9]
  text-white text-sm font-normal
  border-2 border-transparent
  focus:border-white focus:outline-none focus:ring-2 focus:ring-[#0F62FE] focus:ring-offset-2 focus:ring-offset-[#161616]
  disabled:bg-[#C6C6C6] disabled:text-[#8D8D8D] disabled:cursor-not-allowed
  transition-colors duration-200
">
  Primary Button
</button>

<!-- Secondary Button -->
<button class="
  px-4 h-12
  bg-[#393939] hover:bg-[#4C4C4C]
  text-white text-sm font-normal
  border-2 border-transparent
  focus:border-white focus:outline-none focus:ring-2 focus:ring-[#0F62FE] focus:ring-offset-2
  transition-colors duration-200
">
  Secondary Button
</button>

<!-- Tertiary Button -->
<button class="
  px-4 h-12
  bg-transparent hover:bg-[#E0E0E0]
  text-[#0F62FE] hover:text-[#0353E9] text-sm font-normal
  border-2 border-[#0F62FE] hover:border-[#0353E9]
  focus:border-[#0F62FE] focus:outline-none focus:ring-2 focus:ring-[#0F62FE]
  transition-colors duration-200
">
  Tertiary Button
</button>

<!-- Ghost Button -->
<button class="
  px-4 h-12
  bg-transparent hover:bg-[#E0E0E0]
  text-[#0F62FE] hover:text-[#0353E9] text-sm font-normal
  border-2 border-transparent
  focus:border-[#0F62FE] focus:outline-none focus:ring-2 focus:ring-[#0F62FE]
  transition-colors duration-200
">
  Ghost Button
</button>

<!-- Danger Button -->
<button class="
  px-4 h-12
  bg-[#DA1E28] hover:bg-[#BA1B23]
  text-white text-sm font-normal
  border-2 border-transparent
  focus:border-white focus:outline-none focus:ring-2 focus:ring-[#DA1E28] focus:ring-offset-2
  transition-colors duration-200
">
  Danger Button
</button>
```

### Text Input
```html
<div class="space-y-2">
  <label class="block text-xs text-[#161616] mb-2">
    Email Address
  </label>
  <div class="relative">
    <input
      type="email"
      placeholder="Enter email"
      class="
        w-full h-10 px-4
        bg-[#F4F4F4] border-b-2 border-[#8D8D8D]
        text-sm text-[#161616]
        hover:bg-[#E0E0E0]
        focus:bg-white focus:border-[#0F62FE] focus:outline-none
        disabled:bg-[#F4F4F4] disabled:border-[#C6C6C6] disabled:cursor-not-allowed
        placeholder:text-[#6F6F6F]
        transition-all duration-200
      "
    />
  </div>
  <div class="text-xs text-[#6F6F6F]">
    Optional helper text for additional guidance
  </div>
</div>
```

### Notification/Toast
```html
<!-- Info Notification -->
<div class="
  flex items-start gap-4 p-4
  bg-[#161616] border-l-4 border-[#0F62FE]
  shadow-[0_2px_6px_rgba(0,0,0,0.3)]
">
  <svg class="w-5 h-5 text-[#0F62FE] flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/>
  </svg>
  <div class="flex-1">
    <div class="text-sm font-semibold text-white mb-1">Notification title</div>
    <div class="text-sm text-[#C6C6C6]">Description or additional context goes here.</div>
  </div>
  <button class="text-[#C6C6C6] hover:text-white transition-colors">
    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"/>
    </svg>
  </button>
</div>

<!-- Success Notification -->
<div class="
  flex items-start gap-4 p-4
  bg-[#161616] border-l-4 border-[#24A148]
">
  <svg class="w-5 h-5 text-[#24A148] flex-shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
    <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"/>
  </svg>
  <div class="flex-1">
    <div class="text-sm font-semibold text-white mb-1">Success</div>
    <div class="text-sm text-[#C6C6C6]">Your action completed successfully.</div>
  </div>
</div>
```

### Data Table
```html
<div class="overflow-x-auto bg-white">
  <table class="w-full text-sm">
    <thead class="bg-[#E0E0E0] border-t border-[#C6C6C6]">
      <tr>
        <th class="px-4 h-12 text-left text-xs font-semibold text-[#161616] border-b border-[#C6C6C6]">
          Name
        </th>
        <th class="px-4 h-12 text-left text-xs font-semibold text-[#161616] border-b border-[#C6C6C6]">
          Status
        </th>
        <th class="px-4 h-12 text-left text-xs font-semibold text-[#161616] border-b border-[#C6C6C6]">
          Role
        </th>
      </tr>
    </thead>
    <tbody class="divide-y divide-[#E0E0E0]">
      <tr class="hover:bg-[#E0E0E0] transition-colors">
        <td class="px-4 h-12 text-[#161616]">John Doe</td>
        <td class="px-4 h-12">
          <span class="inline-flex items-center px-2 py-0.5 rounded bg-[#24A148] text-white text-xs">
            Active
          </span>
        </td>
        <td class="px-4 h-12 text-[#525252]">Administrator</td>
      </tr>
      <tr class="hover:bg-[#E0E0E0] transition-colors">
        <td class="px-4 h-12 text-[#161616]">Jane Smith</td>
        <td class="px-4 h-12">
          <span class="inline-flex items-center px-2 py-0.5 rounded bg-[#0F62FE] text-white text-xs">
            Pending
          </span>
        </td>
        <td class="px-4 h-12 text-[#525252]">Developer</td>
      </tr>
    </tbody>
  </table>
</div>
```

### Card/Tile
```html
<div class="
  p-4 bg-white
  border border-[#E0E0E0]
  hover:shadow-[0_2px_6px_rgba(0,0,0,0.3)]
  transition-shadow duration-200
">
  <h3 class="text-base font-semibold mb-2 text-[#161616]">Card Title</h3>
  <p class="text-sm text-[#525252] mb-4">
    Card content with Carbon Design styling. Clean, efficient, and accessible.
  </p>
  <button class="text-sm text-[#0F62FE] hover:text-[#0353E9] font-normal">
    Learn more →
  </button>
</div>
```

### Toggle Switch
```html
<label class="inline-flex items-center cursor-pointer">
  <input type="checkbox" class="sr-only peer" />
  <div class="
    relative w-12 h-6
    bg-[#8D8D8D] peer-checked:bg-[#0F62FE]
    rounded-full
    peer-focus:ring-2 peer-focus:ring-[#0F62FE] peer-focus:ring-offset-2
    transition-colors duration-200
    after:content-['']
    after:absolute after:top-[2px] after:left-[2px]
    after:w-5 after:h-5
    after:bg-white after:rounded-full
    after:transition-transform after:duration-200
    peer-checked:after:translate-x-6
  "></div>
  <span class="ml-3 text-sm text-[#161616]">Enable feature</span>
</label>
```

## Accessibility

### Focus States
Carbon enforces visible focus indicators:
```css
.focus-visible:focus-visible {
  outline: 2px solid #0F62FE;
  outline-offset: 2px;
}
```

### Color Contrast
- All text meets WCAG 2.1 AA minimum (4.5:1)
- Interactive elements have 3:1 contrast
- Use Carbon tokens for automatic compliance

### Keyboard Navigation
- All components fully keyboard accessible
- Tab order follows logical flow
- Escape/Enter keys work as expected

## Best Practices

1. **Use IBM Plex**: Typography is core to Carbon's identity
2. **16-Column Grid**: Maintain grid structure for consistency
3. **Layer Model**: Use proper layering for depth hierarchy
4. **Spacing Tokens**: Always use Carbon spacing scale
5. **Accessibility First**: Test with keyboard and screen readers
6. **Theme Support**: Design for both light and dark themes

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        carbon: {
          blue: {
            60: '#0F62FE',
            70: '#0353E9',
            80: '#002D9C',
          },
          gray: {
            10: '#F4F4F4',
            20: '#E0E0E0',
            30: '#C6C6C6',
            40: '#A8A8A8',
            50: '#8D8D8D',
            60: '#6F6F6F',
            70: '#525252',
            80: '#393939',
            90: '#262626',
            100: '#161616',
          },
          success: '#24A148',
          warning: '#F1C21B',
          error: '#DA1E28',
        },
      },
      fontFamily: {
        carbon: ['IBM Plex Sans', 'Helvetica Neue', 'Arial', 'sans-serif'],
        'carbon-mono': ['IBM Plex Mono', 'Menlo', 'DejaVu Sans Mono', 'monospace'],
      },
      spacing: {
        '0.5': '0.125rem', // 2px
        '1.5': '0.375rem', // 6px
        '2.5': '0.625rem', // 10px
      },
      boxShadow: {
        'carbon-1': '0 1px 2px rgba(0, 0, 0, 0.3)',
        'carbon-2': '0 2px 6px rgba(0, 0, 0, 0.3)',
        'carbon-3': '0 4px 8px rgba(0, 0, 0, 0.3)',
        'carbon-4': '0 8px 16px rgba(0, 0, 0, 0.3)',
      },
    },
  },
};
```
