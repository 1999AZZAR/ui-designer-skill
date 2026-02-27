# M3 Pastel Glass (Hybrid Design System)

A premium design system combining Material You (M3) geometry, Glassmorphism depth, and soft Pastel tones. Perfect for high-end dashboards and studio management tools.

---

## 🎨 Design DNA

| Property | Value |
|---|---|
| **Border Radius** | Normal: `28px` (M3 Large), Interactive: `12px` – `16px` |
| **Backdrop Blur** | `12px` to `20px` for glass surfaces |
| **Border** | `1px solid rgba(255, 255, 255, 0.15)` (inner glow effect) |
| **Typography** | `Plus Jakarta Sans` or `Outfit`. Medium weight for clarity. |
| **Color Base** | Soft Pastels with low saturation and high value. |

---

## 🎨 Color Palettes (The Pastel Spectrum)

### Pastel Blue (The "Studio" Theme)
```css
:root {
    --m3-blue-primary: #D1E4FF;
    --m3-blue-on-primary: #003258;
    --m3-blue-container: rgba(209, 228, 255, 0.1);
    --m3-blue-glass: rgba(209, 228, 255, 0.05);
}
```

### Pastel Purple (The "Creative" Theme)
```css
:root {
    --m3-purple-primary: #F7D8FF;
    --m3-purple-on-primary: #550066;
    --m3-purple-container: rgba(247, 216, 255, 0.1);
    --m3-purple-glass: rgba(247, 216, 255, 0.05);
}
```

### Pastel Mint (The "Success" Theme)
```css
:root {
    --m3-mint-primary: #C4EED0;
    --m3-mint-on-primary: #00210E;
    --m3-mint-container: rgba(196, 238, 208, 0.1);
}
```

---

## 🧩 Components

### 1. The Glass Sidebar
```css
.sidebar-glass {
    background: rgba(255, 255, 255, 0.02);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(255, 255, 255, 0.05);
    padding: 2rem;
}

.nav-item-m3 {
    border-radius: 100px; /* Full pill shape for nav */
    transition: all 0.3s cubic-bezier(0.2, 0, 0, 1);
}
.nav-item-m3.active {
    background: var(--m3-blue-primary);
    color: var(--m3-blue-on-primary);
}
```

### 2. The Morphing M3 Tile
```css
.m3-tile {
    transition: all 0.4s cubic-bezier(0.2, 0, 0, 1);
    border-radius: 28px;
    background: rgba(255, 255, 255, 0.03);
    border: 1px solid rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(16px);
    overflow: hidden;
}

.m3-tile:hover {
    border-radius: 16px; /* Corner morphing */
    transform: translateY(-6px) scale(1.01);
    background: rgba(255, 255, 255, 0.06);
    border-color: rgba(255, 255, 255, 0.2);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
}
```

### 3. Glass Input
```css
.input-glass {
    background: rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 16px;
    color: #fff;
    padding: 1rem 1.5rem;
    backdrop-filter: blur(8px);
}
.input-glass:focus {
    border-color: var(--m3-blue-primary);
    box-shadow: 0 0 0 4px rgba(209, 228, 255, 0.1);
}
```

---

## 📐 Implementation (Tailwind Classes)

```html
<!-- Example of a M3 Pastel Glass Card -->
<div class="m3-tile p-8 flex flex-col gap-4 group">
    <div class="w-12 h-12 rounded-2xl bg-blue-100 flex items-center justify-center text-blue-600 transition-all group-hover:rounded-xl">
        <i class="fa-solid fa-chart-line"></i>
    </div>
    <div>
        <h3 class="text-xs font-bold text-gray-400 uppercase tracking-widest">Revenue</h3>
        <p class="text-2xl font-bold text-white">$12,450.00</p>
    </div>
</div>
```

---

## 🚫 Anti-Patterns

- ❌ **Hard Blacks**: Avoid `#000000`. Use deep navy or charcoal (`#0A0B0E`) for dark modes.
- ❌ **High Saturation**: Avoid neon colors. Keep everything "dusty" or "creamy".
- ❌ **Sharp Corners in Idle**: M3 is fundamentally round. Sharp corners should only appear on interaction or in small nested elements.
- ❌ **Stacking Blurs**: Too many layers of `backdrop-filter` will kill performance on low-end devices.

---

## 💡 Pro-Tip
Use `mix-blend-mode: overlay` for subtle textures (like noise or gradients) inside glass tiles to give them a "physical" material feel.
