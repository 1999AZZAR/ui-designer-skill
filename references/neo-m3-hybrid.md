# Neo-M3 Hybrid (Industrial Modernism)

A high-density design language blending the raw, high-contrast structure of **Neo-Brutalism** with the fluid geometry and pastel tones of **Material You 3**. Inspired by tech journalism (Wired, The Verge) and high-end engineering interfaces.

---

## 🎨 Design DNA

| Property | Value |
|---|---|
| **Border Radius** | **Large**: `24px` – `32px` (`rounded-3xl`) for primary containers. |
| **Borders** | **Bold**: `3px` – `4px` Solid Black. Use `dashed` for experimental states. |
| **Shadows** | **Hard Offset**: `6px` – `10px` (No blur). Vibe: "Physical items on a grid." |
| **Typography** | `Plus Jakarta Sans` (Headers), `JetBrains Mono` (Metadata/Stats). |
| **Grid** | Modular with visible dividers. High information density. |

---

## 🎨 The "Verge-inspired" Palette

| Name | Hex Code | Usage |
|---|---|---|
| **Canvas** | `#F8FAFC` | Main background. |
| **Ink** | `#000000` | Borders, primary text, and inverted labels. |
| **M3 Lavender** | `#E9D5FF` | Hero cards, primary actions. |
| **M3 Sky** | `#DBEAFE` | Secondary info, data visualization. |
| **M3 Mint** | `#DCFCE7` | Success states, financial data. |
| **M3 Rose** | `#FCE7F3` | Warnings, delete actions, system alerts. |

---

## 🧩 Components

### 1. The "Wired" Article Card
```html
<article class="bg-white border-[3px] border-black rounded-[32px] p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-y-[-4px] transition-all">
    <div class="flex gap-2 mb-6">
        <span class="bg-black text-white text-[10px] font-black uppercase px-3 py-1 rounded-full">Intelligence</span>
        <span class="font-mono text-[10px] text-zinc-400">2026-02-27</span>
    </div>
    <h2 class="text-3xl font-extrabold tracking-tighter leading-none mb-4">Project Prism: The Next Phase of News.</h2>
    <p class="text-zinc-600 mb-8">Engineering the future of information density through Neo-M3 Hybrid architecture.</p>
    <button class="bg-[#E9D5FF] border-2 border-black rounded-full px-6 py-2 font-bold text-sm">Read More</button>
</article>
```

### 2. Experimental "Dashed" Container
Used for placeholders or "Wong Edan" (magical/hidden) features.
```css
.edan-container {
    border: 3px dashed #000;
    background: repeating-linear-gradient(45deg, #f8fafc, #f8fafc 10px, #ffffff 10px, #ffffff 20px);
    border-radius: 24px;
    padding: 2rem;
}
```

### 3. System Status Marquee
```html
<div class="bg-black text-white py-2 overflow-hidden whitespace-nowrap">
    <div class="animate-marquee inline-block font-mono text-xs uppercase tracking-widest">
        System Operational • Project Prism v2.4 Active • Memory Cache Synced • Welcome Master Azzar • 
    </div>
</div>
```

---

## interaksi (Micro-Motion)

- **Snappy Response** — Use `cubic-bezier(0.19, 1, 0.22, 1)` (Expo-out) for all interactions.
- **Elevation Change** — Elements should lower their shadow offset and translate `XY` on click (active state).
- **Hover Scale** — Subtle scaling (`scale(1.02)`) on cards combined with shadow hardening.

---

## 🚫 Anti-Patterns

- ❌ **Subtle Borders**: Anything less than `2px` is too weak for this style.
- ❌ **Low Contrast**: Black on white is mandatory. No dark gray text.
- ❌ **Traditional Icons**: Use geometric/minimal icons. Avoid overly detailed illustrative icons.
- ❌ **Rounded Corners < 16px**: Keep it bold and chunky.

---

## 💡 Pro-Tip
Mix `font-black` (900) sans-serif for main titles with `font-medium` (500) monospace for technical details to create that "Pro-Journalism" aesthetic.
