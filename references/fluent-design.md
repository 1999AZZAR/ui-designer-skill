# Fluent Design System (Microsoft)

Fluent Design System is Microsoft's design language emphasizing light, depth, motion, material, and scale to create intuitive, powerful experiences across all platforms.

## Core Principles

### 1. Light
Strategic use of light draws the eye and creates spatial hierarchy.
- Light reveals relationships and depth
- Focused lighting guides user attention
- Subtle illumination on interactive elements

### 2. Depth
Layering establishes spatial relationships and importance.
- Z-depth creates hierarchy
- Parallax effects enhance immersion
- Layering communicates context

### 3. Motion
Purposeful animation connects experiences and provides feedback.
- Motion validates user actions
- Transitions feel natural and fluid
- 300-500ms duration for most interactions

### 4. Material
Surface textures provide tactile feedback and depth.
- Acrylic material for translucent surfaces
- Reveal effect on hover interactions
- Mica material for seamless integration

### 5. Scale
Adaptive layouts respond to screen sizes and contexts.
- Responsive scaling from mobile to desktop
- Touch targets minimum 40x40px
- Adaptive navigation patterns

## Color System

### Primary Colors
```
Blue (Primary): #0078D4
Dark Blue: #005A9E
Light Blue: #50E6FF

Neutrals:
Gray 10: #FAF9F8
Gray 20: #F3F2F1
Gray 30: #EDEBE9
Gray 40: #E1DFDD
Gray 50: #D2D0CE
Gray 60: #C8C6C4
Gray 70: #BEBBB8
Gray 80: #B3B0AD
Gray 90: #A19F9D
Gray 100: #979593
Gray 110: #8A8886
Gray 120: #605E5C
Gray 130: #484644
Gray 140: #3B3A39
Gray 150: #323130
Gray 160: #292827
Gray 170: #201F1E
Gray 180: #11100F
```

### Semantic Colors
```
Success: #107C10
Warning: #FFC83D
Error: #D13438
Info: #0078D4
```

## Typography

### Font Family
```css
font-family: 'Segoe UI Variable', 'Segoe UI', -apple-system, system-ui, sans-serif;
```

### Type Scale
```
Heading Large: 46px / 56px line-height, Semi-bold (600)
Heading: 28px / 36px line-height, Semi-bold (600)
Subheading: 20px / 28px line-height, Semi-bold (600)
Body Large: 18px / 24px line-height, Regular (400)
Body: 14px / 20px line-height, Regular (400)
Caption: 12px / 16px line-height, Regular (400)
```

## Spacing System

Fluent uses 4px base unit with consistent multipliers:
```
4px (1x), 8px (2x), 12px (3x), 16px (4x), 20px (5x),
24px (6x), 28px (7x), 32px (8x), 36px (9x), 40px (10x)
```

## Border Radius
```
Small: 2px
Medium: 4px
Large: 8px
X-Large: 12px
Circular: 9999px
```

## Elevation & Shadow

### Elevation Levels
```css
/* Shadow 2 (Hover) */
box-shadow: 0 0.3px 0.9px rgba(0,0,0,0.1),
            0 1.6px 3.6px rgba(0,0,0,0.13);

/* Shadow 4 (Popover) */
box-shadow: 0 1.2px 3.6px rgba(0,0,0,0.11),
            0 6.4px 14.4px rgba(0,0,0,0.13);

/* Shadow 8 (Dialog) */
box-shadow: 0 3.2px 7.2px rgba(0,0,0,0.13),
            0 12.8px 28.8px rgba(0,0,0,0.11);

/* Shadow 16 (Menu) */
box-shadow: 0 6.4px 14.4px rgba(0,0,0,0.11),
            0 25.6px 57.6px rgba(0,0,0,0.13);

/* Shadow 28 (Flyout) */
box-shadow: 0 11.2px 25.2px rgba(0,0,0,0.13),
            0 44.8px 100.8px rgba(0,0,0,0.11);

/* Shadow 64 (Panel) */
box-shadow: 0 25.6px 57.6px rgba(0,0,0,0.11),
            0 102.4px 230.4px rgba(0,0,0,0.13);
```

## Material Effects

### Acrylic Background
```css
.acrylic {
  background: rgba(252, 252, 252, 0.7);
  backdrop-filter: blur(30px) saturate(125%);
  border: 1px solid rgba(0,0,0,0.05);
}

/* Dark Acrylic */
.acrylic-dark {
  background: rgba(44, 44, 44, 0.6);
  backdrop-filter: blur(30px) saturate(125%);
  border: 1px solid rgba(255,255,255,0.05);
}
```

### Reveal Effect (Hover)
```css
.reveal {
  position: relative;
  overflow: hidden;
}

.reveal::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at var(--x) var(--y), 
    rgba(255,255,255,0.3) 0%, 
    transparent 80%);
  opacity: 0;
  transition: opacity 0.3s;
  pointer-events: none;
}

.reveal:hover::after {
  opacity: 1;
}
```

## Component Examples

### Button (Tailwind)
```html
<!-- Primary Button -->
<button class="
  px-5 py-2.5 
  bg-[#0078D4] hover:bg-[#005A9E]
  text-white font-semibold text-sm
  rounded
  shadow-[0_0.3px_0.9px_rgba(0,0,0,0.1),0_1.6px_3.6px_rgba(0,0,0,0.13)]
  hover:shadow-[0_1.2px_3.6px_rgba(0,0,0,0.11),0_6.4px_14.4px_rgba(0,0,0,0.13)]
  transition-all duration-300
  active:scale-[0.98]
">
  Primary Action
</button>

<!-- Subtle Button -->
<button class="
  px-5 py-2.5
  bg-transparent hover:bg-[#F3F2F1]
  text-[#323130] font-semibold text-sm
  rounded
  transition-all duration-300
">
  Secondary Action
</button>
```

### Card with Acrylic
```html
<div class="
  p-6 rounded-lg
  bg-white/70 dark:bg-neutral-900/60
  backdrop-blur-[30px] backdrop-saturate-125
  border border-black/5 dark:border-white/5
  shadow-[0_1.2px_3.6px_rgba(0,0,0,0.11),0_6.4px_14.4px_rgba(0,0,0,0.13)]
  hover:shadow-[0_3.2px_7.2px_rgba(0,0,0,0.13),0_12.8px_28.8px_rgba(0,0,0,0.11)]
  transition-all duration-300
">
  <h3 class="text-xl font-semibold mb-2 text-[#323130]">Card Title</h3>
  <p class="text-sm text-[#605E5C]">Card description with acrylic material effect.</p>
</div>
```

### Navigation Bar
```html
<nav class="
  h-14 px-4
  bg-white/70 backdrop-blur-[30px] backdrop-saturate-125
  border-b border-black/5
  flex items-center gap-4
">
  <div class="text-lg font-semibold text-[#323130]">App Title</div>
  <div class="flex-1 flex items-center gap-2">
    <button class="px-4 py-2 text-sm hover:bg-[#F3F2F1] rounded transition-colors">
      Home
    </button>
    <button class="px-4 py-2 text-sm hover:bg-[#F3F2F1] rounded transition-colors">
      Features
    </button>
    <button class="px-4 py-2 text-sm hover:bg-[#F3F2F1] rounded transition-colors">
      About
    </button>
  </div>
</nav>
```

### Input Field
```html
<div class="space-y-2">
  <label class="text-sm font-semibold text-[#323130]">
    Email Address
  </label>
  <input
    type="email"
    placeholder="Enter your email"
    class="
      w-full px-3 py-2
      bg-white border border-[#8A8886]
      rounded text-sm text-[#323130]
      focus:border-[#0078D4] focus:outline-none focus:ring-1 focus:ring-[#0078D4]
      placeholder:text-[#605E5C]
      transition-all duration-200
    "
  />
</div>
```

## Accessibility

### Focus States
```css
/* Visible focus indicator */
.focus-visible:focus-visible {
  outline: 2px solid #0078D4;
  outline-offset: 2px;
}
```

### Color Contrast
- All text meets WCAG 2.1 AA standards (4.5:1 minimum)
- Interactive elements have clear hover/focus states
- Use semantic colors for status indicators

### Motion Preferences
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Best Practices

1. **Consistency**: Use Fluent components across all experiences
2. **Responsiveness**: Design for multiple devices and input methods
3. **Motion**: Keep animations under 500ms for perceived performance
4. **Depth**: Use elevation purposefully to establish hierarchy
5. **Accessibility**: Always meet WCAG 2.1 AA standards minimum
6. **Performance**: Optimize backdrop-blur usage for better performance

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        fluent: {
          blue: '#0078D4',
          'blue-dark': '#005A9E',
          'blue-light': '#50E6FF',
          gray: {
            10: '#FAF9F8',
            20: '#F3F2F1',
            60: '#C8C6C4',
            130: '#484644',
            160: '#292827',
          },
          success: '#107C10',
          warning: '#FFC83D',
          error: '#D13438',
        },
      },
      fontFamily: {
        fluent: ['Segoe UI Variable', 'Segoe UI', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'fluent-2': '0 0.3px 0.9px rgba(0,0,0,0.1), 0 1.6px 3.6px rgba(0,0,0,0.13)',
        'fluent-4': '0 1.2px 3.6px rgba(0,0,0,0.11), 0 6.4px 14.4px rgba(0,0,0,0.13)',
        'fluent-8': '0 3.2px 7.2px rgba(0,0,0,0.13), 0 12.8px 28.8px rgba(0,0,0,0.11)',
        'fluent-16': '0 6.4px 14.4px rgba(0,0,0,0.11), 0 25.6px 57.6px rgba(0,0,0,0.13)',
      },
      backdropBlur: {
        'fluent': '30px',
      },
      backdropSaturate: {
        '125': '125%',
      },
    },
  },
};
```
