# Neo-Brutalism (Digital Rawness)

A bold, high-contrast evolution of traditional brutalism, optimized for high visibility and playful digital experiences. It rejects the "softness" of modern web design in favor of raw energy and mathematical honesty.

---

## 🎨 Design DNA

| Property | Value |
|---|---|
| **Border Radius** | Mixed: `0px` (sharp) or `8px`-`12px` (rounded-but-thick) |
| **Borders** | Mandatory: `2px` – `4px` Solid Black (`#000000`) |
| **Shadows** | **Hard Offset** only. No blur. `shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]` |
| **Typography** | `Lexend`, `Space Grotesk`, or `Archivo Black`. Font-black (900). |
| **Colors** | High-saturation primaries: `#FFD600` (Yellow), `#FF006B` (Pink), `#00F0FF` (Cyan). |

---

## 🎨 The "Loud" Palette

| Name | Hex Code | Tailwind Class |
|---|---|---|
| **Electric Yellow** | `#FFD600` | `bg-yellow-400` |
| **Cyber Blue** | `#3D5A80` | `bg-blue-600` |
| **Hot Pink** | `#FF006B` | `bg-pink-500` |
| **Vibrant Lime** | `#A3FF00` | `bg-lime-400` |
| **Deep Ink** | `#000000` | `bg-black` |

---

## 🧩 Components

### 1. The "Tactile" Button
Neo-brutalist buttons should feel like real-world physical switches.
```html
<button class="bg-[#A3FF00] border-2 border-black px-6 py-3 font-black uppercase tracking-widest shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:shadow-none active:translate-x-[4px] active:translate-y-[4px] transition-all">
    Push Me
</button>
```

### 2. The "Overlapped" Card
```css
.brutal-card {
    background: #fff;
    border: 3px solid #000;
    padding: 2rem;
    box-shadow: 12px 12px 0px 0px #000;
    transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.brutal-card:hover {
    transform: translate(-4px, -4px);
    box-shadow: 16px 16px 0px 0px #000;
}
```

### 3. All-Caps Navigation
```html
<nav class="flex border-b-4 border-black">
    <a href="#" class="flex-1 text-center py-4 font-black text-xl hover:bg-yellow-400 border-r-4 border-black transition-colors">WORK</a>
    <a href="#" class="flex-1 text-center py-4 font-black text-xl hover:bg-pink-500 border-r-4 border-black transition-colors">SHOP</a>
    <a href="#" class="flex-1 text-center py-4 font-black text-xl hover:bg-lime-400 transition-colors">ABOUT</a>
</nav>
```

---

## interaksi (Motion)

- **Snappy Transitions** — Use `cubic-bezier(0.175, 0.885, 0.32, 1.275)` for that "springy" feel.
- **No Fades** — Prefer instant color swaps or hard-edged slides.
- **Micro-Hover** — Elements should "jump" toward the user on hover.

---

## 🚫 Anti-Patterns

- ❌ **Gradients**: Gradients are for soft designs. Neo-brutalism is flat.
- ❌ **Blurred Shadows**: If it's not hard-edged, it's not brutal.
- ❌ **Subtle Borders**: `1px` borders will get lost. Use `2px` or `4px`.
- ❌ **Muted Colors**: Avoid pastels unless they are used as high-contrast background against black.

---

## 💡 Pro-Tip
Combine Neo-Brutalism with large ASCII art or simple SVG patterns (dots, stripes) in the background to emphasize the "digital raw" aesthetic.
