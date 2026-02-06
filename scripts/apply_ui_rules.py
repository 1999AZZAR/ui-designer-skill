import os
import argparse

def main():
    parser = argparse.ArgumentParser(description="Apply UI design rules to .cursorrules")
    parser.add_argument("--style", choices=["material", "minimal", "glass"], default="minimal", help="The design language to use.")
    parser.add_argument("--palette", choices=["pastel", "dark", "vibrant"], default="pastel", help="The color palette preference.")
    args = parser.parse_args()

    # Base rules that always apply
    base_rules = """
# AI Design Rules (Azzar's UI Designer)

## Core Philosophy
- "Wong edan mah ajaib" (Crazy people are magical).
- Just enough engineering to get it done well. No bloat.
- Mobile-first, accessible, and responsive by default.
"""

    style_rules = {
        "material": "- Use Material You (M3) principles.
- Large rounded corners (rounded-3xl).
- Tonal palettes and subtle elevation.",
        "minimal": "- Focus on typography and whitespace.
- Limit borders and shadows.
- High contrast for readability.",
        "glass": "- Use backdrop-blur-md/lg.
- Semi-transparent backgrounds (bg-white/20).
- Subtle white borders (border-white/10)."
    }

    palette_rules = {
        "pastel": "- Use soft, muted colors. Avoid harsh saturation.
- Backgrounds should be very light or off-white.",
        "dark": "- Use deep grays/zinc for backgrounds.
- High-contrast accents for visibility.",
        "vibrant": "- Use bold, energetic colors for CTAs.
- Strong gradients where appropriate."
    }

    rules_to_add = f"""
{base_rules}
### Style: {args.style.capitalize()}
{style_rules[args.style]}

### Palette: {args.palette.capitalize()}
{palette_rules[args.palette]}

### Technical Stack
- Tailwind CSS
- Font Awesome (fa-duotone/fa-light)
- React / Next.js
"""

    rules_file = ".cursorrules"
    mode = "a" if os.path.exists(rules_file) else "w"
    
    with open(rules_file, mode) as f:
        if mode == "a":
            f.write("

--- Updated by ui-designer ---
")
        f.write(rules_to_add)
    
    print(f"✅ Successfully applied {args.style} style with {args.palette} palette to {rules_file}")

if __name__ == "__main__":
    main()
