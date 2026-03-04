# Neumorphism (Soft UI)

Neumorphism is a minimalist design trend combining skeuomorphism and flat design, creating soft, extruded shapes that appear to emerge from the background using subtle shadows.

## Core Principles

### 1. Background Unity
Elements appear carved from or extruded out of the background.
- Same color family for background and elements
- Subtle depth without harsh contrasts
- Monochromatic or near-monochromatic palettes

### 2. Dual Shadow System
Two shadows create the soft 3D effect.
- Light shadow (top-left)
- Dark shadow (bottom-right)
- Both shadows work together for depth

### 3. Subtle Contrast
Low contrast maintains the soft, elegant aesthetic.
- Avoid high contrast colors
- Use similar hues with slight variations
- Muted, sophisticated color choices

### 4. Minimalist Forms
Clean, simple shapes work best.
- Rounded corners (large radius)
- Simple geometric forms
- Minimal decorative elements

## Color System

### Light Theme Palette
```
Background: #E0E5EC
Surface Light: #FFFFFF
Surface Dark: #A3B1C6
Text Primary: #4A5568
Text Secondary: #718096
Accent Blue: #667EEA
Accent Pink: #EC4899
Success: #48BB78
Warning: #F6AD55
Error: #F56565
```

### Dark Theme Palette
```
Background: #2D3748
Surface Light: #4A5568
Surface Dark: #1A202C
Text Primary: #E2E8F0
Text Secondary: #A0AEC0
Accent Blue: #667EEA
Accent Pink: #EC4899
```

## Typography

### Font Recommendations
```css
font-family: 'Inter', 'SF Pro', -apple-system, system-ui, sans-serif;
```

### Type Scale
```
Heading Large: 32px / 40px, Semi-bold (600)
Heading: 24px / 32px, Semi-bold (600)
Subheading: 18px / 28px, Medium (500)
Body: 16px / 24px, Regular (400)
Small: 14px / 20px, Regular (400)
Caption: 12px / 16px, Regular (400)
```

## Spacing System

8px base unit for consistent rhythm:
```
4px, 8px, 12px, 16px, 24px, 32px, 40px, 48px, 64px, 80px
```

## Border Radius

Large radii create the soft, organic feel:
```
Small: 8px
Medium: 12px
Large: 16px
X-Large: 24px
Circular: 50%
```

## Shadow System

The signature dual-shadow technique:

### Convex (Raised) Elements
```css
/* Light Theme Raised */
box-shadow: 8px 8px 16px rgba(163, 177, 198, 0.6),
            -8px -8px 16px rgba(255, 255, 255, 0.5);

/* Subtle Raised */
box-shadow: 4px 4px 8px rgba(163, 177, 198, 0.4),
            -4px -4px 8px rgba(255, 255, 255, 0.4);

/* Dark Theme Raised */
box-shadow: 8px 8px 16px rgba(0, 0, 0, 0.4),
            -8px -8px 16px rgba(74, 85, 104, 0.1);
```

### Concave (Pressed) Elements
```css
/* Light Theme Pressed */
box-shadow: inset 4px 4px 8px rgba(163, 177, 198, 0.5),
            inset -4px -4px 8px rgba(255, 255, 255, 0.5);

/* Deep Pressed */
box-shadow: inset 8px 8px 16px rgba(163, 177, 198, 0.6),
            inset -8px -8px 16px rgba(255, 255, 255, 0.5);

/* Dark Theme Pressed */
box-shadow: inset 6px 6px 12px rgba(0, 0, 0, 0.4),
            inset -6px -6px 12px rgba(74, 85, 104, 0.1);
```

### Flat (Barely Raised)
```css
/* Subtle Flat */
box-shadow: 2px 2px 4px rgba(163, 177, 198, 0.3),
            -2px -2px 4px rgba(255, 255, 255, 0.3);
```

## Component Examples

### Button (Tailwind)
```html
<!-- Raised Button -->
<button class="
  px-8 py-3 rounded-2xl
  bg-[#E0E5EC]
  text-[#4A5568] font-medium text-sm
  shadow-[8px_8px_16px_rgba(163,177,198,0.6),-8px_-8px_16px_rgba(255,255,255,0.5)]
  hover:shadow-[4px_4px_8px_rgba(163,177,198,0.4),-4px_-4px_8px_rgba(255,255,255,0.4)]
  active:shadow-[inset_4px_4px_8px_rgba(163,177,198,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]
  transition-all duration-300
">
  Neumorphic Button
</button>

<!-- Icon Button (Circular) -->
<button class="
  w-12 h-12 rounded-full
  bg-[#E0E5EC]
  flex items-center justify-center
  text-[#667EEA]
  shadow-[8px_8px_16px_rgba(163,177,198,0.6),-8px_-8px_16px_rgba(255,255,255,0.5)]
  hover:shadow-[4px_4px_8px_rgba(163,177,198,0.4),-4px_-4px_8px_rgba(255,255,255,0.4)]
  active:shadow-[inset_4px_4px_8px_rgba(163,177,198,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]
  transition-all duration-300
">
  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
    <path d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z"/>
  </svg>
</button>
```

### Input Field
```html
<div class="space-y-2">
  <label class="text-sm font-medium text-[#4A5568]">
    Email Address
  </label>
  <input
    type="email"
    placeholder="Enter your email"
    class="
      w-full px-4 py-3 rounded-xl
      bg-[#E0E5EC]
      text-[#4A5568] text-sm
      shadow-[inset_4px_4px_8px_rgba(163,177,198,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]
      focus:shadow-[inset_6px_6px_12px_rgba(163,177,198,0.6),inset_-6px_-6px_12px_rgba(255,255,255,0.5)]
      placeholder:text-[#718096]
      transition-shadow duration-300
      outline-none
    "
  />
</div>
```

### Card
```html
<div class="
  p-8 rounded-3xl
  bg-[#E0E5EC]
  shadow-[8px_8px_16px_rgba(163,177,198,0.6),-8px_-8px_16px_rgba(255,255,255,0.5)]
  hover:shadow-[12px_12px_24px_rgba(163,177,198,0.6),-12px_-12px_24px_rgba(255,255,255,0.5)]
  transition-all duration-300
">
  <h3 class="text-xl font-semibold mb-3 text-[#4A5568]">
    Neumorphic Card
  </h3>
  <p class="text-sm text-[#718096] leading-relaxed">
    This card demonstrates the soft, extruded aesthetic of neumorphism 
    with dual shadows creating subtle depth.
  </p>
</div>
```

### Toggle Switch
```html
<label class="inline-flex items-center cursor-pointer">
  <div class="relative">
    <input type="checkbox" class="sr-only peer" />
    <div class="
      w-14 h-7 rounded-full
      bg-[#E0E5EC]
      shadow-[inset_4px_4px_8px_rgba(163,177,198,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]
      peer-checked:shadow-[inset_4px_4px_8px_rgba(102,126,234,0.3),inset_-4px_-4px_8px_rgba(255,255,255,0.3)]
      transition-all duration-300
    "></div>
    <div class="
      absolute top-0.5 left-0.5
      w-6 h-6 rounded-full
      bg-[#E0E5EC]
      shadow-[4px_4px_8px_rgba(163,177,198,0.6),-4px_-4px_8px_rgba(255,255,255,0.5)]
      peer-checked:translate-x-7 peer-checked:bg-[#667EEA]
      transition-all duration-300
    "></div>
  </div>
  <span class="ml-3 text-sm font-medium text-[#4A5568]">
    Enable Feature
  </span>
</label>
```

### Progress Bar
```html
<div class="space-y-2">
  <div class="flex justify-between text-sm text-[#4A5568]">
    <span>Progress</span>
    <span>65%</span>
  </div>
  <div class="
    h-3 rounded-full
    bg-[#E0E5EC]
    shadow-[inset_4px_4px_8px_rgba(163,177,198,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]
    overflow-hidden
  ">
    <div class="
      h-full w-[65%] rounded-full
      bg-gradient-to-r from-[#667EEA] to-[#EC4899]
      shadow-[2px_2px_4px_rgba(102,126,234,0.4)]
      transition-all duration-500
    "></div>
  </div>
</div>
```

### Icon Grid
```html
<div class="grid grid-cols-4 gap-4">
  <div class="
    aspect-square rounded-2xl
    bg-[#E0E5EC]
    shadow-[8px_8px_16px_rgba(163,177,198,0.6),-8px_-8px_16px_rgba(255,255,255,0.5)]
    hover:shadow-[4px_4px_8px_rgba(163,177,198,0.4),-4px_-4px_8px_rgba(255,255,255,0.4)]
    flex items-center justify-center
    cursor-pointer
    transition-all duration-300
  ">
    <svg class="w-6 h-6 text-[#667EEA]" fill="currentColor" viewBox="0 0 20 20">
      <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"/>
    </svg>
  </div>
  <!-- Repeat for other icons -->
</div>
```

### Search Bar
```html
<div class="relative">
  <input
    type="search"
    placeholder="Search..."
    class="
      w-full pl-12 pr-4 py-3 rounded-2xl
      bg-[#E0E5EC]
      text-[#4A5568] text-sm
      shadow-[inset_4px_4px_8px_rgba(163,177,198,0.5),inset_-4px_-4px_8px_rgba(255,255,255,0.5)]
      focus:shadow-[inset_6px_6px_12px_rgba(163,177,198,0.6),inset_-6px_-6px_12px_rgba(255,255,255,0.5)]
      placeholder:text-[#718096]
      transition-shadow duration-300
      outline-none
    "
  />
  <svg class="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-[#718096]" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
  </svg>
</div>
```

## Accessibility Considerations

### Focus States
Neumorphism's low contrast can hurt accessibility. Add clear focus indicators:
```css
.focus-visible:focus-visible {
  outline: 2px solid #667EEA;
  outline-offset: 2px;
}
```

### Color Contrast
- Text needs sufficient contrast (minimum 4.5:1)
- Use darker text colors on light neumorphic backgrounds
- Test with accessibility tools
- Consider adding subtle borders for better definition

### Alternative Highlights
For better accessibility, combine neumorphism with:
- Color changes on interaction
- Border highlights
- Icon state changes
- Text label updates

## Best Practices

1. **Monochromatic Palette**: Keep backgrounds and elements in same color family
2. **Large Radius**: Use generous border-radius (12px+) for soft appearance
3. **Subtle Shadows**: Don't overdo shadow intensity
4. **Limited Use**: Best for hero sections, cards, not entire interfaces
5. **Accessibility**: Always ensure sufficient contrast for text
6. **Performance**: Shadow-heavy designs can impact rendering performance
7. **Context**: Works best on clean, minimal interfaces

## Common Pitfalls

- Too many shadowed elements (visual clutter)
- Insufficient text contrast (readability issues)
- Overuse across entire interface (user fatigue)
- Small elements (shadows don't work well at small sizes)
- Busy backgrounds (neumorphism needs calm surfaces)

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        neu: {
          bg: '#E0E5EC',
          light: '#FFFFFF',
          dark: '#A3B1C6',
          text: '#4A5568',
          'text-muted': '#718096',
          blue: '#667EEA',
          pink: '#EC4899',
        },
      },
      boxShadow: {
        'neu-raised': '8px 8px 16px rgba(163, 177, 198, 0.6), -8px -8px 16px rgba(255, 255, 255, 0.5)',
        'neu-raised-sm': '4px 4px 8px rgba(163, 177, 198, 0.4), -4px -4px 8px rgba(255, 255, 255, 0.4)',
        'neu-pressed': 'inset 4px 4px 8px rgba(163, 177, 198, 0.5), inset -4px -4px 8px rgba(255, 255, 255, 0.5)',
        'neu-pressed-lg': 'inset 8px 8px 16px rgba(163, 177, 198, 0.6), inset -8px -8px 16px rgba(255, 255, 255, 0.5)',
        'neu-flat': '2px 2px 4px rgba(163, 177, 198, 0.3), -2px -2px 4px rgba(255, 255, 255, 0.3)',
      },
    },
  },
};
```
