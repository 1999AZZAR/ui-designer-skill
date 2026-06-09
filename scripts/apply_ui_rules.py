#!/usr/bin/env python3
"""
UI Design Rules Generator

Generates structured AI design rules for .cursorrules or other config files.
Supports single systems, hybrid patterns, and cross-cutting rules.

Usage:
    python3 apply_ui_rules.py --style ant --palette dark
    python3 apply_ui_rules.py --style polaris --hybrid swiss --palette mono
    python3 apply_ui_rules.py --list
    python3 apply_ui_rules.py --dry-run --style material --archetype dashboard
"""

import argparse
import os
import sys
from typing import Optional

# ─── Style Definitions ─────────────────────────────────────────────────────────

STYLE_CHOICES = [
    "fluent",
    "ant",
    "carbon",
    "atlassian",
    "apple-hig",
    "polaris",
    "material",
    "minimal",
    "glass",
    "neumorphism",
    "neo-brutalism",
    "claymorphism",
    "skeuomorphism",
    "swiss",
    "swiss-archival",
    "m3-pastel",
    "neo-m3",
]

PALETTE_CHOICES = ["pastel", "dark", "vibrant", "mono"]

ARCHETYPE_CHOICES = [
    "dashboard",
    "settings",
    "table-detail",
    "marketing-hero",
    "editorial-landing",
]

HYBRID_SECONDARY = [
    "swiss",
    "swiss-archival",
    "glass",
    "neo-m3",
    "m3-pastel",
    "minimal",
]

# ─── Base Rules ────────────────────────────────────────────────────────────────

BASE_RULES = """# AI Design Rules

## Core Philosophy
- Choose the design system from product context first, not visual taste first.
- Prefer one primary design language unless a hybrid has explicit ownership boundaries.
- Avoid generic AI aesthetics: no default purple gradients, no glossy filler, no emoji in functional UI.
- Keep interfaces production-ready, accessible, and structurally coherent.
"""

# ─── Cross-Cutting Rules ──────────────────────────────────────────────────────

ICON_RULES = [
    "NEVER use icons from unapproved sources.",
    "Only these 6 icon libraries are allowed: Phosphor, Font Awesome, Google Material Symbols, Tabler, Lucide, Heroicons.",
    "Use icons from the approved set only — reject all others.",
    "Match icon style (outline/filled/duotone) to the chosen design system.",
]

ACCESSIBILITY_RULES = [
    "All text must meet WCAG AA contrast (4.5:1 normal, 3:1 large).",
    "Every interactive element must have visible focus indicators.",
    "All form inputs must have visible labels (not placeholder-only).",
    "Use semantic HTML: landmarks (header, nav, main, footer), headings in order, lists for repeated items.",
    "Never use color alone to convey information — add icon, text, or pattern.",
    "Icon-only buttons must have aria-label.",
    "Respect prefers-reduced-motion for all animations.",
    "Minimum touch target: 44x44px.",
]

MOTION_RULES = [
    "Use motion as feedback, not decoration.",
    "Standard transitions: 150-250ms with ease-out for entering, ease-in for exiting.",
    "No animation longer than 500ms without a progress indicator.",
    "No flashing content (max 3 flashes per second).",
    "Always respect prefers-reduced-motion.",
]

RESPONSIVE_RULES = [
    "Design mobile-first, enhance for larger screens.",
    "Use 12-column grid with consistent gutters.",
    "Stack elements vertically on mobile, use columns on tablet+.",
    "Tables become card layouts on mobile.",
    "Navigation: bottom tabs (mobile) → sidebar (desktop).",
]

TOKEN_RULES = [
    "Use consistent spacing scale based on 4px increments.",
    "Typography: max 4-5 size steps per system.",
    "Border radius: pick 2-3 values max (sm, md, lg) and reuse.",
    "Shadows: use sparingly, prefer surface elevation via color shift.",
    "Z-index: use a scale, not ad-hoc values.",
]

TAILWIND_RULES = [
    "When using Tailwind CSS, follow utility-first patterns.",
    "Use @apply sparingly — prefer utilities in markup.",
    "Dark mode: use class-based dark: prefix.",
    "Custom colors go in tailwind.config.js extend section.",
    "Responsive: mobile-first with sm:, md:, lg:, xl: prefixes.",
]

CROSS_CUTTING_SECTIONS = {
    "icons": {"label": "Icon Standards", "rules": ICON_RULES},
    "accessibility": {"label": "Accessibility (WCAG AA)", "rules": ACCESSIBILITY_RULES},
    "motion": {"label": "Motion & Animation", "rules": MOTION_RULES},
    "responsive": {"label": "Responsive Layout", "rules": RESPONSIVE_RULES},
    "tokens": {"label": "Design Tokens", "rules": TOKEN_RULES},
}

# ─── Style Rules ───────────────────────────────────────────────────────────────

STYLE_RULES = {
    "fluent": {
        "label": "Fluent Design",
        "use_for": "Windows-like software, Microsoft-adjacent enterprise products, layered productivity UI",
        "rules": [
            "Use light, depth, motion, material, and scale as the main interaction vocabulary.",
            "Prefer Segoe UI or system-like Microsoft typography.",
            "Use acrylic or layered surfaces sparingly and intentionally.",
            "Structure pages with command bars, modular cards, and panels.",
        ],
    },
    "ant": {
        "label": "Ant Design",
        "use_for": "Admin panels, dashboards, CMS, internal tools, workflow-heavy products",
        "rules": [
            "Apply Natural, Certain, Meaningful, and Growing as operating checks.",
            "Use familiar enterprise patterns: forms, tables, tags, drawers, modals, inline validation, empty/loading/error states.",
            "Prefer page scaffolding with header, actions or filters row, main content region, and secondary detail region.",
            "Keep motion functional feedback, not decoration.",
        ],
    },
    "carbon": {
        "label": "Carbon Design",
        "use_for": "Enterprise software, analytical tools, dense data interfaces",
        "rules": [
            "Prioritize clarity, efficiency, consistency, and inclusive interaction behavior.",
            "Use IBM Plex Sans and IBM Plex Mono where appropriate.",
            "Keep structure grid-driven and tightly aligned.",
            "Favor dense but highly legible layout over decorative flourish.",
        ],
    },
    "atlassian": {
        "label": "Atlassian Design",
        "use_for": "Collaboration products, project management, teamwork-heavy tools",
        "rules": [
            "Design for shared task context and highly visible action hierarchy.",
            "Use clear status language, approachable feedback, and practical structure.",
            "Favor boards, lists, sidebars, task detail surfaces, and collaboration context.",
            "Keep patterns trustworthy and discoverable.",
        ],
    },
    "apple-hig": {
        "label": "Apple Human Interface Guidelines",
        "use_for": "iOS apps, macOS apps, Apple-adjacent premium interfaces",
        "rules": [
            "Apply clarity, deference, and depth.",
            "Use SF Pro or an Apple-platform-aligned sans.",
            "Respect generous touch targets, calm hierarchy, and platform-native navigation patterns.",
            "Use blur and vibrancy only when they support depth and legibility.",
        ],
    },
    "polaris": {
        "label": "Shopify Polaris",
        "use_for": "Merchant tools, commerce operations, inventory and order management",
        "rules": [
            "Optimize for merchant productivity and reassuring task flow.",
            "Use clean cards, resource lists, tables, and direct helper/error copy.",
            "Keep merchant state visible: draft, active, paid, unavailable, etc.",
            "Balance operational clarity with a friendly product tone.",
        ],
    },
    "material": {
        "label": "Material You",
        "use_for": "Adaptive modern apps, expressive product UI, Android-aligned products",
        "rules": [
            "Use tonal surfaces, adaptive hierarchy, and rounded geometry.",
            "Prefer material-style app bars, cards, chips, tabs, FABs, and sheets.",
            "Keep layouts responsive and fluid across breakpoints.",
            "Use expressive but disciplined motion.",
        ],
    },
    "minimal": {
        "label": "Minimalism",
        "use_for": "Editorial sites, portfolios, clean product pages, content-first SaaS",
        "rules": [
            "Let typography and whitespace carry hierarchy.",
            "Remove decorative structure that does not improve comprehension.",
            "Use borders rarely and shadows only if they are nearly invisible.",
            "Favor calm, content-first composition over component clutter.",
        ],
    },
    "glass": {
        "label": "Glassmorphism",
        "use_for": "Hero sections, premium overlays, modern branded dashboards",
        "rules": [
            "Use transparency and blur against rich backgrounds only.",
            "Keep glass surfaces readable with controlled opacity and contrast.",
            "Do not use glass as the sole logic system for dense workflows.",
            "Use it as a surface treatment, not as a substitute for structure.",
        ],
    },
    "neumorphism": {
        "label": "Neumorphism",
        "use_for": "Tactile niche controls, wellness or ambient experimental UI",
        "rules": [
            "Use monochrome or near-monochrome palettes and dual shadow depth.",
            "Keep surfaces simple, spacious, and limited in number.",
            "Offset low-contrast surfaces with very clear typography and focus treatment.",
            "Do not use for dense enterprise workflows.",
        ],
    },
    "neo-brutalism": {
        "label": "Neo-Brutalism",
        "use_for": "Loud digital brands, campaign surfaces, creative launches",
        "rules": [
            "Use thick borders, hard shadows, bold type, and unapologetic contrast.",
            "Keep hierarchy obvious through scale and graphic separation.",
            "Avoid soft gradients, blurred shadows, and timid edge treatment.",
            "Use for strong brand expression, not dense workflow scaffolding.",
        ],
    },
    "claymorphism": {
        "label": "Claymorphism",
        "use_for": "Playful consumer interfaces and soft friendly product surfaces",
        "rules": [
            "Use inflated shapes, large radii, and soft dimensional depth.",
            "Keep layouts simple and spacious so the 3D treatment can breathe.",
            "Use soft or pastel colors with readable contrast.",
            "Avoid dense or highly analytical layouts.",
        ],
    },
    "skeuomorphism": {
        "label": "Skeuomorphism",
        "use_for": "Luxury, nostalgic, tactile, or retro control surfaces",
        "rules": [
            "Use realistic materials, layered shadows, reflections, and tactile cues.",
            "Commit to one dominant material story such as leather, metal, or wood.",
            "Use sparingly and intentionally to avoid visual overload.",
            "Keep readability and interaction clarity ahead of realism.",
        ],
    },
    "swiss": {
        "label": "Swiss Design",
        "use_for": "Typography-first editorial systems, professional modernist pages",
        "rules": [
            "Treat the grid as law.",
            "Use type, spacing, and asymmetry as the main compositional tools.",
            "Avoid shadows, gradients, and decorative effects.",
            "Keep the palette highly restrained.",
        ],
    },
    "swiss-archival": {
        "label": "Swiss-Archival Design",
        "use_for": "Digital archives, museum sites, academic platforms, research tools, heritage brands",
        "rules": [
            "Follow the geometry ruleset: seed, superformula paths, layers, orbits, captions.",
            "Use the dual-font system: display + body with strict hierarchy.",
            "Apply noise texture and tactile surface treatment.",
            "Use keyboard-first interaction patterns.",
            "Source color tokens from the Swiss-Archival palette (Tailscale ramps).",
        ],
    },
    "m3-pastel": {
        "label": "M3 Pastel",
        "use_for": "Soft modern SaaS, creative dashboards, gentler material-style products",
        "rules": [
            "Keep Material-style structure but soften it with pastel tonal surfaces.",
            "Use large rounded geometry and controlled surface layering.",
            "Protect contrast when using pale colors.",
            "Let color soften the tone without reducing clarity.",
        ],
    },
    "neo-m3": {
        "label": "Neo-M3",
        "use_for": "Editorial tech products, bold SaaS, structured brand-forward product UI",
        "rules": [
            "Mix strong product structure with bolder editorial energy.",
            "Use bold borders, strong geometry, and controlled hard-shadow accents.",
            "Reserve monospace for metadata and technical emphasis.",
            "Do not let expressive surfaces break overall layout discipline.",
        ],
    },
}

# ─── Hybrid Patterns ───────────────────────────────────────────────────────────

HYBRID_PATTERNS = {
    "polaris+swiss": {
        "label": "Polaris + Swiss",
        "use_for": "Commerce platforms wanting editorial polish, luxury e-commerce, design-forward merchant tools",
        "structure_owner": "polaris",
        "brand_owner": "swiss",
        "rules": [
            "Polaris owns: commerce workflows, forms, tables, filters, product management.",
            "Swiss owns: typography system, editorial layout, grid rigor, brand expression.",
            "Use Swiss typography for product storytelling, Polaris components for operations.",
            "Keep grid strict (Swiss) but apply Polaris spacing for interactive density.",
        ],
    },
    "polaris+swiss-archival": {
        "label": "Polaris + Swiss-Archival",
        "use_for": "Heritage brands, artisan marketplaces, curated commerce with provenance focus",
        "structure_owner": "polaris",
        "brand_owner": "swiss-archival",
        "rules": [
            "Polaris owns: commerce operations, order flows, inventory management.",
            "Swiss-Archival owns: brand surface, product storytelling, visual hierarchy, archival catalogs.",
            "Use Swiss-Archival noise texture and dual-font on product pages.",
            "Use Polaris resource lists and tables for admin/merchant views.",
        ],
    },
    "ant+neo-m3": {
        "label": "Ant + Neo-M3",
        "use_for": "Enterprise products needing bold brand expression on marketing surfaces",
        "structure_owner": "ant",
        "brand_owner": "neo-m3",
        "rules": [
            "Ant owns: tables, forms, filters, drawers, notifications.",
            "Neo-M3 owns: hero sections, high-level brand surfaces, special callouts.",
        ],
    },
    "ant+glass": {
        "label": "Ant + Glass",
        "use_for": "Enterprise products with atmospheric landing/dashboard highlights",
        "structure_owner": "ant",
        "brand_owner": "glass",
        "rules": [
            "Ant owns: product workflows.",
            "Glass owns: landing, dashboard highlight cards, atmospheric shells.",
        ],
    },
    "carbon+minimal": {
        "label": "Carbon + Minimal",
        "use_for": "Dense analytical tools with clean outer layout",
        "structure_owner": "carbon",
        "brand_owner": "minimal",
        "rules": [
            "Carbon owns: dense operational components.",
            "Minimal softens: outer layout and marketing surfaces.",
        ],
    },
    "material+m3-pastel": {
        "label": "Material + M3-Pastel",
        "use_for": "Modern apps needing softer visual tone",
        "structure_owner": "material",
        "brand_owner": "m3-pastel",
        "rules": [
            "Material owns: structure and behavior.",
            "M3-Pastel softens: color and surface language.",
        ],
    },
}

# ─── Palette Rules ─────────────────────────────────────────────────────────────

PALETTE_RULES = {
    "pastel": [
        "Use soft, low-saturation, high-value colors.",
        "Prefer light neutral canvases and toned accents.",
        "Protect text contrast on pale surfaces.",
    ],
    "dark": [
        "Use deep but not absolute-black surfaces unless intentionally brutal.",
        "Separate layers through surface value shifts, not only shadows.",
        "Keep accent colors controlled and high legibility.",
    ],
    "vibrant": [
        "Use strong accent colors against calm neutrals or stark black/white contrast.",
        "Limit the number of loud colors so hierarchy stays clear.",
        "Use saturation strategically for priority and emphasis.",
    ],
    "mono": [
        "Use one hue family across multiple tones and values.",
        "Let spacing, typography, and contrast carry structure.",
        "Use accent shifts carefully to avoid flatness.",
    ],
}

# ─── Archetype Rules ───────────────────────────────────────────────────────────

ARCHETYPE_RULES = {
    "dashboard": {
        "label": "Dashboard",
        "rules": [
            "Use a page header, KPI strip, controls row, primary data region, and secondary widget region.",
            "Make the first screen scannable in under 5 seconds.",
            "Do not let every widget fight for equal visual weight.",
        ],
    },
    "settings": {
        "label": "Settings",
        "rules": [
            "Group settings by user mental model, not backend schema.",
            "Use strong labels, helper text, and inline validation.",
            "Separate destructive actions from routine configuration.",
        ],
    },
    "table-detail": {
        "label": "Table Detail",
        "rules": [
            "Use header, filter and bulk action row, primary table, and detail drawer or side panel.",
            "Keep row actions predictable and status visibility high.",
            "Design bulk, empty, loading, and detail-edit flows together.",
        ],
    },
    "marketing-hero": {
        "label": "Marketing Hero",
        "rules": [
            "Establish one clear visual thesis immediately.",
            "Keep headline, proof, and CTA hierarchy obvious.",
            "Avoid generic interchangeable SaaS hero layouts.",
        ],
    },
    "editorial-landing": {
        "label": "Editorial Landing",
        "rules": [
            "Let typography and rhythm drive the page structure.",
            "Use modular story blocks with intentional asymmetry or calm sequencing.",
            "Treat whitespace as an active layout tool.",
        ],
    },
}


# ─── Helper Functions ──────────────────────────────────────────────────────────


def format_section(title: str, items: list[str]) -> str:
    """Format a markdown section with title and bullet items."""
    lines = [f"## {title}"]
    lines.extend(f"- {item}" for item in items)
    return "\n".join(lines)


def build_cross_cutting(include: list[str]) -> str:
    """Build cross-cutting rules sections."""
    sections = []
    for key in include:
        if key in CROSS_CUTTING_SECTIONS:
            section = CROSS_CUTTING_SECTIONS[key]
            sections.append(format_section(section["label"], section["rules"]))
    return "\n\n".join(sections)


def build_hybrid_rules(
    primary: str, secondary: str, palette: str, archetype: Optional[str]
) -> str:
    """Build rules for a hybrid system."""
    hybrid_key = f"{primary}+{secondary}"
    if hybrid_key not in HYBRID_PATTERNS:
        print(f"Warning: No hybrid pattern for {hybrid_key}, using primary only.", file=sys.stderr)
        return build_single_rules(primary, palette, archetype)

    hybrid = HYBRID_PATTERNS[hybrid_key]
    primary_data = STYLE_RULES[primary]
    secondary_data = STYLE_RULES[secondary]

    sections = [BASE_RULES.rstrip()]

    # Hybrid overview
    sections.append(
        format_section(
            f"Hybrid System: {hybrid['label']}",
            [f"Use for: {hybrid['use_for']}"]
            + hybrid["rules"],
        )
    )

    # Primary system
    sections.append(
        format_section(
            f"Structure Owner: {primary_data['label']}",
            [f"Use for: {primary_data['use_for']}"] + primary_data["rules"],
        )
    )

    # Secondary system
    sections.append(
        format_section(
            f"Brand Owner: {secondary_data['label']}",
            secondary_data["rules"],
        )
    )

    # Palette
    sections.append(
        format_section(f"Palette Direction: {palette.upper()}", PALETTE_RULES[palette])
    )

    # Archetype
    if archetype:
        archetype_data = ARCHETYPE_RULES[archetype]
        sections.append(
            format_section(
                f"Page Archetype: {archetype_data['label']}", archetype_data["rules"]
            )
        )

    # Cross-cutting
    sections.append(build_cross_cutting(["icons", "accessibility", "motion"]))

    return "\n\n".join(sections) + "\n"


def build_single_rules(
    style: str, palette: str, archetype: Optional[str], include_tailwind: bool = False
) -> str:
    """Build rules for a single system."""
    style_data = STYLE_RULES[style]
    sections = [BASE_RULES.rstrip()]

    sections.append(
        format_section(
            f"Selected System: {style_data['label']}",
            [f"Use for: {style_data['use_for']}"] + style_data["rules"],
        )
    )

    sections.append(
        format_section(f"Palette Direction: {palette.upper()}", PALETTE_RULES[palette])
    )

    if archetype:
        archetype_data = ARCHETYPE_RULES[archetype]
        sections.append(
            format_section(
                f"Page Archetype: {archetype_data['label']}", archetype_data["rules"]
            )
        )

    # Cross-cutting
    cross_cutting_keys = ["icons", "accessibility", "motion", "tokens"]
    if include_tailwind:
        cross_cutting_keys.append("responsive")
    sections.append(build_cross_cutting(cross_cutting_keys))

    if include_tailwind:
        sections.append(format_section("Tailwind CSS", TAILWIND_RULES))

    return "\n\n".join(sections) + "\n"


def list_options():
    """Print all available options."""
    print("\n=== Available Styles ===\n")
    for s in STYLE_CHOICES:
        data = STYLE_RULES[s]
        print(f"  {s:20s}  {data['label']} — {data['use_for'][:60]}")

    print("\n=== Available Palettes ===\n")
    for p in PALETTE_CHOICES:
        print(f"  {p}")

    print("\n=== Available Archetypes ===\n")
    for a in ARCHETYPE_CHOICES:
        data = ARCHETYPE_RULES[a]
        print(f"  {a:20s}  {data['label']}")

    print("\n=== Hybrid Patterns ===\n")
    for key, data in HYBRID_PATTERNS.items():
        print(f"  {key:30s}  {data['label']}")
        print(f"  {'':30s}  {data['use_for'][:70]}")

    print()


def write_output(content: str, output_file: str, clean: bool = False):
    """Write rules to output file."""
    if clean and os.path.exists(output_file):
        os.remove(output_file)

    mode = "a" if os.path.exists(output_file) else "w"
    with open(output_file, mode, encoding="utf-8") as f:
        if mode == "a":
            f.write("\n\n--- UI Rule Update ---\n")
        f.write(content)


# ─── CLI ───────────────────────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="Generate structured UI design rules for AI coding assistants.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --style ant --palette dark
  %(prog)s --style polaris --hybrid swiss --palette mono
  %(prog)s --style material --archetype dashboard --tailwind
  %(prog)s --list
  %(prog)s --dry-run --style carbon --palette dark
        """,
    )

    parser.add_argument(
        "--style",
        choices=STYLE_CHOICES,
        default=None,
        help="Primary design system.",
    )
    parser.add_argument(
        "--palette",
        choices=PALETTE_CHOICES,
        default="pastel",
        help="Palette direction (default: pastel).",
    )
    parser.add_argument(
        "--archetype",
        choices=ARCHETYPE_CHOICES,
        default=None,
        help="Optional page archetype.",
    )
    parser.add_argument(
        "--hybrid",
        choices=HYBRID_SECONDARY,
        default=None,
        help="Secondary system for hybrid pattern (use with --style).",
    )
    parser.add_argument(
        "--tailwind",
        action="store_true",
        help="Include Tailwind CSS integration rules.",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=".cursorrules",
        help="Output file path (default: .cursorrules).",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing file before writing (no append).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print rules to stdout without writing to file.",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available styles, palettes, archetypes, and hybrids.",
    )

    args = parser.parse_args()

    if args.list:
        list_options()
        return

    if not args.style:
        parser.error("--style is required (or use --list to see options)")

    if args.hybrid and args.hybrid in STYLE_RULES.get(args.style, {}).get("rules", []):
        pass  # Valid hybrid

    # Build rules
    if args.hybrid:
        content = build_hybrid_rules(args.style, args.hybrid, args.palette, args.archetype)
    else:
        content = build_single_rules(
            args.style, args.palette, args.archetype, args.tailwind
        )

    # Output
    if args.dry_run:
        print(content)
    else:
        write_output(content, args.output, args.clean)
        hybrid_suffix = f" + {args.hybrid}" if args.hybrid else ""
        archetype_suffix = f" / archetype:{args.archetype}" if args.archetype else ""
        tailwind_suffix = " / tailwind" if args.tailwind else ""
        print(
            f"✓ Applied: {args.style}{hybrid_suffix} + {args.palette}{archetype_suffix}{tailwind_suffix} → {args.output}"
        )


if __name__ == "__main__":
    main()
