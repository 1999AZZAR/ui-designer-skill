# Swiss-Archival: Specimen decorator (geometry ruleset)

The **specimen decorator** is a Swiss-Archival ornamental block: technical chrome (labels, optional input, glass frame) plus a **single inline SVG** whose marks are generated only by the rules below. Use it for vault intros, heroes, empty states, loaders—not for dense operational layout.

This file is the **ruleset** for that SVG geometry. Implementations may use any language or DOM structure; they must follow these rules if the output is to be called a Swiss-Archival specimen decorator. A full HTML page was used to validate the math; you do not need to copy that page—only this logic.

---

## 1. Decorator element

| Rule | Requirement |
|------|-------------|
| 1.1 | One root `<svg>` with `viewBox="0 0 100 100"` and a square aspect in layout. |
| 1.2 | All parametric marks are **closed paths** from the superformula sampler (Rule 5–6); **fill `none`**, **stroke** only. |
| 1.3 | Construction guides and captions sit in separate groups/text; guides are low-contrast and under the curve group. |

---

## 2. Determinism and seed

| Rule | Requirement |
|------|-------------|
| 2.1 | **Input string** `S` (title, accession id, etc.) drives the whole figure. |
| 2.2 | **Seed** is a non-negative integer: start `hash = 0`; for each character `c` in `S` in order, `hash = codePoint(c) + ((hash << 5) - hash)`; then `seed = abs(hash)`. |
| 2.3 | Same `S` must yield the same seed, same DNA, same layer choices, same orbit count, and same stroke color indices. |

**Default string** when the field is empty: implementers may use a fixed default `S0` (reference: `"Multishape Synthesis v1"`).

---

## 3. Public identifiers (bind to seed)

| Rule | Requirement |
|------|-------------|
| 3.1 | **SID** (specimen id): alphabet exactly `ABCDEFGHJKLMNPQRSTUVWXYZ23456789` (32 characters). Prefix: `(seed % 90) + 10` as decimal text. Suffix: 6 characters; let `t = seed`, for `k = 0..5`: take `alphabet[t % 32]`, then `t = floor(t / 32)`. Concatenate prefix, hyphen, suffix → e.g. `42-A3F9K2`. |
| 3.2 | **UI hash line** (outside or beside SVG): expose seed as uppercase hex, e.g. `HASH_PTR: 0x{seed.toString(16).toUpperCase()}`. |
| 3.3 | **SVG captions** (Rule 8): include `SPEC_ID: {SID}` and `MORPH_DNA: {m1}.{m2}` using integers `m1`, `m2` from Rule 4. |

---

## 4. DNA parameters (shape coefficients from seed)

Superformula call shape: `(m, n1, n2, n3)` with default radii `a = 1`, `b = 1`.

| Rule | Symbol | Definition |
|------|--------|------------|
| 4.1 | `m1` | `(seed % 10) + 3` |
| 4.2 | `n1` | `(seed % 50) / 10 + 0.5` |
| 4.3 | `n2` | `(seed % 100) / 10` |
| 4.4 | `n3` | `((seed >> 2) % 100) / 10` |
| 4.5 | Primary tuple | `P_primary = (m1, n1, n2, n3)` |
| 4.6 | `m2` | `((seed >> 4) % 8) + 2` |
| 4.7 | Secondary tuple (interference / mini-shapes) | `P_secondary = (m2, 2, 1, 1)` unless you extend the ruleset explicitly |

---

## 5. Superformula radius

For angle `theta`, parameters `(m, n1, n2, n3, a, b)`:

```
r(theta) = ( |cos(m * theta / 4) / a|^n2 + |sin(m * theta / 4) / b|^n3 )^(-1/n1)
```

Use the real powers as in a reference implementation; guard edge cases if `n1` or exponents produce invalid values in your runtime.

---

## 6. Path from DNA (closed polyline)

| Rule | Requirement |
|------|-------------|
| 6.1 | Center `(cx, cy)` in user units; reference primary center is `(50, 50)`. |
| 6.2 | Sample `theta` from `0` to `2π` inclusive in `N` equal steps (reference `N = 200`). |
| 6.3 | For each sample: `r = r(theta)` from Rule 5 with the chosen tuple; `x = cx + r * scale * cos(theta)`; `y = cy + r * scale * sin(theta)`. |
| 6.4 | Build `d = "M " + points.join(" L ") + " Z"` with 2-decimal coordinates (or sufficient precision for smooth curves). |

---

## 7. Layer stack (main interference figure)

Constants below are **reference defaults**; you may tune `layerCount`, `scaleMax`, `rotStep`, stroke widths, and opacities for product needs while keeping the **structure** of the rules.

| Rule | Requirement |
|------|-------------|
| 7.1 | Let `layerCount` be a fixed integer (reference: `6`). For `i = 1 .. layerCount`: |
| 7.2 | `scale_i = (i / layerCount) * scaleMax` (reference `scaleMax = 35`). |
| 7.3 | `color_i = palette[(seed + i) % palette.length]` for a fixed ordered `palette` array. |
| 7.4 | `rot_i = (seed % 360) + i * rotStep` (reference `rotStep = 10`). |
| 7.5 | **Primary path:** `generatePath(50, 50, scale_i, P_primary)`, rotate `rot_i` degrees about `(50, 50)`, stroke `color_i`, no fill; stroke-width and opacity decrease for deeper layers (reference stroke-width `0.25`, opacity `1.1 - i/layerCount` clamped to valid range). |
| 7.6 | **Interference path:** If `i` is even, append `generatePath(50, 50, scale_i * 0.8, P_secondary)` with rotation **`-rot_i * 1.5`** about `(50, 50)`, same stroke color, lighter stroke (reference width `0.15`, opacity `0.2`), **dashed** stroke (reference dash pattern `1 2`). |

---

## 8. Orbital subsystem

| Rule | Requirement |
|------|-------------|
| 8.1 | `orbitCount = (seed % 4) + 2`. |
| 8.2 | For `j = 0 .. orbitCount - 1`: `angleDeg = j * (360 / orbitCount) + (seed % 90)`. |
| 8.3 | `ox = 50 + R * cos(angleDeg * π/180)`, `oy = 50 + R * sin(angleDeg * π/180)` (reference `R = 38`). |
| 8.4 | Draw small **stroke-only** node circle at `(ox, oy)` (reference `r = 1.5`). |
| 8.5 | Draw **satellite** path `generatePath(ox, oy, s_orbit, (m2, 1, 1, 1))` (reference `s_orbit = 4`), subtle stroke using a catalog color (reference first palette entry). |
| 8.6 | Draw **link** segment from `(50, 50)` to `(ox, oy)`, very faint dashed stroke. |

---

## 9. Construction guides (underlay)

| Rule | Requirement |
|------|-------------|
| 9.1 | Group opacity ~`0.1`: dashed circle centered `(50, 50)`, radius ~`48`; plus vertical and horizontal diameters (crosshair). |
| 9.2 | Hairline stroke; purpose is drafting / archive instrument legibility, not decoration. |

---

## 10. SVG text captions

| Rule | Requirement |
|------|-------------|
| 10.1 | Monospace family; small user-unit size (reference `font-size ~ 1.8`). |
| 10.2 | Lower-left: `SPEC_ID: {SID}` (SID from Rule 3.1). |
| 10.3 | Upper-right: `MORPH_DNA: {m1}.{m2}` with `text-anchor: end`. |
| 10.4 | Fill low contrast against background (reference `rgba(255,255,255,0.3)` on dark shells; remap for light archival surfaces). |

---

## 11. Palette and theming

| Rule | Requirement |
|------|-------------|
| 11.1 | `palette` is an ordered list of stroke colors; indices are **only** from `(seed + i) % length` for layers unless you extend the ruleset. |
| 11.2 | For **warm archival** shells, replace chroma with muted earth, ash, and burgundy accents while keeping Rules 2–10. |

---

## 12. Chrome outside the SVG (optional block)

Not part of the geometry proof, but part of the **decorator pattern**: glass panel around the SVG, optional text field bound to `S`, SID/hash labels in UI, control to copy the SVG markup. Prefer `type="button"` on controls; replace blocking alerts with toasts in apps.

---

## 13. Accessibility and motion

| Rule | Requirement |
|------|-------------|
| 13.1 | If captions duplicate visible UI text, mark the SVG `aria-hidden="true"`; otherwise supply a short `aria-label` describing the specimen id. |
| 13.2 | If `prefers-reduced-motion: reduce`, omit rotations or reduce layer count per product policy. |

---

## Minimal formula reference (implementation)

```text
superformula(theta, m, n1, n2, n3, a=1, b=1):
  part1 = pow(abs(cos(m*theta/4) / a), n2)
  part2 = pow(abs(sin(m*theta/4) / b), n3)
  return pow(part1 + part2, -1/n1)
```

---

## Files

- System tokens and principles: `references/swiss-archival.md`
- Structural components: `assets/components/swiss-archival-components.md`
