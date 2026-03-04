# Skeuomorphism

Skeuomorphism is a design approach that mimics real-world objects using realistic textures, shadows, reflections, and dimensional details to make digital interfaces feel familiar and tangible.

## Core Principles

### 1. Real-World Mimicry
Digital elements imitate physical counterparts.
- Realistic textures (leather, wood, metal)
- Physical affordances and constraints
- Familiar metaphors from real life
- Tactile visual cues

### 2. Rich Detail
Abundant visual information creates authenticity.
- Complex gradients and lighting
- Multiple shadow layers
- Reflective surfaces
- Textured backgrounds

### 3. Depth & Dimension
Layered elements create tangible 3D space.
- Inner shadows for insets
- Outer shadows for elevation
- Highlights for reflections
- Embossed/debossed effects

### 4. Material Authenticity
Surfaces look and feel like real materials.
- Stitched leather textures
- Brushed metal effects
- Glossy glass surfaces
- Wood grain patterns

## Color System

Skeuomorphism uses realistic, material-based colors:

### Leather Tones
```
Dark Brown: #3E2723
Medium Brown: #5D4037
Tan: #8D6E63
Cream: #D7CCC8
```

### Wood Tones
```
Dark Walnut: #4E342E
Oak: #795548
Maple: #A1887F
Pine: #BCAAA4
```

### Metal Tones
```
Dark Steel: #37474F
Brushed Steel: #546E7A
Chrome: #90A4AE
Aluminum: #B0BEC5
```

### Fabric & Felt
```
Deep Green: #1B5E20
Navy Felt: #0D47A1
Charcoal: #212121
Burgundy: #880E4F
```

### Accent Colors
```
Gold: #FFB300
Copper: #BF360C
Bronze: #6D4C41
Silver: #BDBDBD
```

## Typography

### Font Recommendations
Fonts that complement skeuomorphic designs:
```css
/* Elegant Serif */
font-family: 'Playfair Display', 'Georgia', serif;

/* Classic Sans */
font-family: 'Futura', 'Avenir', 'Helvetica Neue', sans-serif;

/* Vintage */
font-family: 'Abril Fatface', 'Bodoni', serif;
```

### Type Scale
```
Display: 48px / 56px, Bold (700)
Heading Large: 36px / 44px, Semi-bold (600)
Heading: 28px / 36px, Semi-bold (600)
Subheading: 20px / 28px, Medium (500)
Body: 16px / 24px, Regular (400)
Small: 14px / 20px, Regular (400)
Caption: 12px / 16px, Regular (400)
```

## Spacing System

Traditional spacing based on content hierarchy:
```
4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px
```

## Border Radius

Realistic curves matching physical objects:
```
Tight: 2px (modern devices)
Subtle: 4px (paper edges)
Medium: 8px (buttons, cards)
Rounded: 12px (rounded corners)
Pill: 9999px (fully rounded)
```

## Shadow & Lighting System

Complex multi-layered shadows create realism:

### Raised Elements
```css
/* Leather Button */
box-shadow: 0 1px 0 rgba(255,255,255,0.4) inset,
            0 -1px 0 rgba(0,0,0,0.2) inset,
            0 4px 8px rgba(0,0,0,0.3),
            0 1px 2px rgba(0,0,0,0.2);

/* Glossy Button */
box-shadow: 0 1px 3px rgba(0,0,0,0.12),
            0 1px 2px rgba(0,0,0,0.24),
            inset 0 1px 0 rgba(255,255,255,0.5),
            inset 0 -1px 0 rgba(0,0,0,0.1);

/* Wood Panel */
box-shadow: 0 2px 4px rgba(0,0,0,0.3),
            inset 0 1px 0 rgba(255,255,255,0.1),
            inset 0 -1px 1px rgba(0,0,0,0.3);
```

### Inset/Pressed Elements
```css
/* Recessed Display */
box-shadow: inset 0 2px 4px rgba(0,0,0,0.6),
            inset 0 1px 2px rgba(0,0,0,0.4),
            0 1px 0 rgba(255,255,255,0.1);

/* Pressed Button */
box-shadow: inset 0 2px 4px rgba(0,0,0,0.3),
            inset 0 1px 2px rgba(0,0,0,0.2);
```

## Texture & Material Effects

### Leather Texture
```css
.leather-texture {
  background: linear-gradient(135deg, #5D4037 0%, #3E2723 100%);
  background-image: 
    repeating-linear-gradient(45deg, transparent, transparent 2px, rgba(0,0,0,.05) 2px, rgba(0,0,0,.05) 4px),
    linear-gradient(135deg, #5D4037 0%, #3E2723 100%);
  box-shadow: 0 2px 4px rgba(0,0,0,0.3),
              inset 0 1px 0 rgba(255,255,255,0.1),
              inset 0 -1px 1px rgba(0,0,0,0.3);
}
```

### Brushed Metal
```css
.brushed-metal {
  background: linear-gradient(180deg, #546E7A 0%, #37474F 100%);
  background-image: 
    repeating-linear-gradient(0deg, 
      rgba(255,255,255,0) 0px,
      rgba(255,255,255,0.03) 1px,
      rgba(0,0,0,0.03) 2px,
      rgba(255,255,255,0) 3px
    );
  box-shadow: inset 0 1px 0 rgba(255,255,255,0.2),
              inset 0 -1px 0 rgba(0,0,0,0.3),
              0 2px 4px rgba(0,0,0,0.4);
}
```

### Wood Grain
```css
.wood-grain {
  background: linear-gradient(90deg, #795548 0%, #5D4037 50%, #795548 100%);
  background-size: 200% 100%;
  box-shadow: inset 0 1px 0 rgba(0,0,0,0.3),
              inset 0 -1px 0 rgba(255,255,255,0.1),
              0 2px 8px rgba(0,0,0,0.4);
}
```

### Glass/Glossy
```css
.glossy {
  background: linear-gradient(180deg, 
    rgba(255,255,255,0.3) 0%,
    rgba(255,255,255,0) 50%,
    rgba(0,0,0,0.1) 100%
  );
  box-shadow: 0 4px 8px rgba(0,0,0,0.2),
              inset 0 1px 0 rgba(255,255,255,0.5),
              inset 0 -1px 0 rgba(0,0,0,0.2);
}
```

## Component Examples

### Leather Button (Tailwind + Custom CSS)
```html
<button class="
  px-6 py-3 rounded-lg
  relative overflow-hidden
  text-white font-semibold text-sm
  transition-all duration-200
  active:translate-y-0.5
  leather-button
">
  <span class="relative z-10">Leather Button</span>
</button>

<style>
.leather-button {
  background: linear-gradient(135deg, #5D4037 0%, #3E2723 100%);
  background-image: 
    repeating-linear-gradient(45deg, transparent, transparent 2px, rgba(0,0,0,.05) 2px, rgba(0,0,0,.05) 4px),
    linear-gradient(135deg, #5D4037 0%, #3E2723 100%);
  box-shadow: 0 1px 0 rgba(255,255,255,0.2) inset,
              0 -1px 0 rgba(0,0,0,0.3) inset,
              0 4px 8px rgba(0,0,0,0.4),
              0 2px 4px rgba(0,0,0,0.3);
}
.leather-button:hover {
  background: linear-gradient(135deg, #6D4C41 0%, #4E342E 100%);
}
.leather-button:active {
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.4),
              0 1px 2px rgba(0,0,0,0.2);
}
</style>
```

### Glossy Button
```html
<button class="
  px-6 py-3 rounded-full
  relative overflow-hidden
  glossy-button
  text-white font-semibold text-sm
  transition-all duration-200
  active:scale-95
">
  <span class="relative z-10">Glossy Button</span>
</button>

<style>
.glossy-button {
  background: linear-gradient(180deg, #4CAF50 0%, #2E7D32 100%);
  box-shadow: 0 4px 8px rgba(0,0,0,0.3),
              0 2px 4px rgba(0,0,0,0.2),
              inset 0 1px 0 rgba(255,255,255,0.4),
              inset 0 -1px 0 rgba(0,0,0,0.2);
}
.glossy-button::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 50%;
  background: linear-gradient(180deg, rgba(255,255,255,0.4), transparent);
  border-radius: 9999px 9999px 0 0;
}
.glossy-button:active {
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.3),
              0 1px 2px rgba(0,0,0,0.2);
}
</style>
```

### Recessed Display/Input
```html
<div class="
  p-4 rounded-lg
  recessed-display
  bg-[#263238] text-[#4CAF50]
  font-mono text-sm
">
  System Status: Online
</div>

<style>
.recessed-display {
  box-shadow: inset 0 3px 6px rgba(0,0,0,0.6),
              inset 0 1px 3px rgba(0,0,0,0.5),
              0 1px 0 rgba(255,255,255,0.1);
}
</style>
```

### Stitched Leather Card
```html
<div class="leather-card p-8 rounded-2xl">
  <h3 class="text-2xl font-serif font-bold text-white mb-3">
    Premium Card
  </h3>
  <p class="text-sm text-white/80 leading-relaxed">
    Luxurious card with stitched leather texture and realistic depth.
  </p>
</div>

<style>
.leather-card {
  background: linear-gradient(135deg, #5D4037 0%, #3E2723 100%);
  box-shadow: 0 8px 16px rgba(0,0,0,0.4),
              0 4px 8px rgba(0,0,0,0.3),
              inset 0 1px 0 rgba(255,255,255,0.1),
              inset 0 -1px 1px rgba(0,0,0,0.3);
  border: 2px solid rgba(0,0,0,0.3);
  position: relative;
}
.leather-card::before {
  content: '';
  position: absolute;
  inset: 12px;
  border: 1px dashed rgba(255,255,255,0.2);
  border-radius: 12px;
  pointer-events: none;
}
</style>
```

### Toggle Switch (Realistic)
```html
<label class="inline-flex items-center cursor-pointer">
  <div class="relative">
    <input type="checkbox" class="sr-only peer" />
    <div class="
      w-14 h-7 rounded-full realistic-toggle-bg
      transition-all duration-300
    "></div>
    <div class="
      absolute top-0.5 left-0.5
      w-6 h-6 rounded-full realistic-toggle-knob
      peer-checked:translate-x-7
      transition-transform duration-300
    "></div>
  </div>
  <span class="ml-3 text-sm font-medium">Enable</span>
</label>

<style>
.realistic-toggle-bg {
  background: linear-gradient(180deg, #37474F 0%, #263238 100%);
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.5),
              inset 0 1px 2px rgba(0,0,0,0.3);
}
.realistic-toggle-knob {
  background: linear-gradient(180deg, #ECEFF1 0%, #B0BEC5 100%);
  box-shadow: 0 2px 4px rgba(0,0,0,0.4),
              0 1px 2px rgba(0,0,0,0.3),
              inset 0 1px 0 rgba(255,255,255,0.6);
}
</style>
```

### Notebook/Paper Texture
```html
<div class="paper-texture p-8 rounded shadow-2xl">
  <h2 class="text-3xl font-serif mb-4 text-[#3E2723]">Notes</h2>
  <div class="space-y-3">
    <div class="border-b border-[#E0E0E0] pb-2">
      <p class="text-[#5D4037]">Task item with ruled lines</p>
    </div>
    <div class="border-b border-[#E0E0E0] pb-2">
      <p class="text-[#5D4037]">Another note entry</p>
    </div>
  </div>
</div>

<style>
.paper-texture {
  background: linear-gradient(180deg, #FAFAFA 0%, #F5F5F5 100%);
  background-image: 
    repeating-linear-gradient(0deg,
      transparent 0px,
      transparent 31px,
      rgba(0,0,0,0.05) 31px,
      rgba(0,0,0,0.05) 32px
    );
  box-shadow: 0 8px 16px rgba(0,0,0,0.2),
              0 4px 8px rgba(0,0,0,0.15),
              inset 0 1px 0 rgba(255,255,255,0.8);
}
</style>
```

## Accessibility Considerations

### High Contrast Challenges
Skeuomorphic designs can have contrast issues:
- Ensure text has 4.5:1 contrast minimum
- Test with grayscale to verify hierarchy
- Provide high-contrast mode option
- Use semantic colors for status

### Focus States
Add clear focus indicators:
```css
.focus-visible:focus-visible {
  outline: 3px solid #FFD700;
  outline-offset: 2px;
}
```

## Best Practices

1. **Use Sparingly**: Skeuomorphism works best for specific UI elements, not entire interfaces
2. **Performance**: Complex gradients and shadows can impact rendering
3. **Context**: Best for creative, artistic, or nostalgic applications
4. **Subtlety**: Modern skeuomorphism is more subtle than early iOS versions
5. **Consistency**: If using skeuomorphism, commit to the aesthetic throughout
6. **Testing**: Always test on various devices and screen sizes

## When to Use Skeuomorphism

Best suited for:
- Creative/artistic applications
- Game interfaces
- Luxury/premium products
- Nostalgic/vintage themes
- Physical product simulators
- Music production software
- Educational apps mimicking real objects

## Tailwind Config Extension

```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        leather: {
          dark: '#3E2723',
          medium: '#5D4037',
          tan: '#8D6E63',
          cream: '#D7CCC8',
        },
        wood: {
          walnut: '#4E342E',
          oak: '#795548',
          maple: '#A1887F',
        },
        metal: {
          steel: '#37474F',
          brushed: '#546E7A',
          chrome: '#90A4AE',
        },
      },
      fontFamily: {
        elegant: ['Playfair Display', 'Georgia', 'serif'],
        vintage: ['Abril Fatface', 'Bodoni', 'serif'],
      },
    },
  },
};
```
