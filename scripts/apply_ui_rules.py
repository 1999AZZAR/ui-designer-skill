import argparse
import os


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


BASE_RULES = """# AI Design Rules

## Core Philosophy
- Choose the design system from product context first, not visual taste first.
- Prefer one primary design language unless a hybrid has explicit ownership boundaries.
- Avoid generic AI aesthetics: no default purple gradients, no glossy filler, no emoji in functional UI.
- Keep interfaces production-ready, accessible, and structurally coherent.
"""


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


def format_section(title, items):
    lines = [f"## {title}"]
    lines.extend(f"- {item}" for item in items)
    return "\n".join(lines)


def build_rules(style, palette, archetype):
    style_data = STYLE_RULES[style]
    sections = [BASE_RULES.rstrip()]

    sections.append(
        format_section(
            f"Selected System: {style_data['label']}",
            [f"Use for: {style_data['use_for']}"] + style_data["rules"],
        )
    )

    sections.append(
        format_section(
            f"Palette Direction: {palette.upper()}",
            PALETTE_RULES[palette],
        )
    )

    if archetype:
        archetype_data = ARCHETYPE_RULES[archetype]
        sections.append(
            format_section(
                f"Page Archetype: {archetype_data['label']}",
                archetype_data["rules"],
            )
        )

    sections.append(
        format_section(
            "Implementation Standards",
            [
                "Use Tailwind CSS or the project's existing token system consistently.",
                "Use Font Awesome 6 only when the project does not already define a stronger icon system.",
                "Keep components readable, reusable, and structurally self-documenting.",
                "Design empty, loading, success, and error states intentionally.",
                "Use motion as feedback, not decoration.",
            ],
        )
    )

    return "\n\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Append structured UI design rules to .cursorrules"
    )
    parser.add_argument(
        "--style",
        choices=STYLE_CHOICES,
        default="minimal",
        help="Primary design system to apply.",
    )
    parser.add_argument(
        "--palette",
        choices=PALETTE_CHOICES,
        default="pastel",
        help="Palette direction to apply.",
    )
    parser.add_argument(
        "--archetype",
        choices=ARCHETYPE_CHOICES,
        default=None,
        help="Optional page archetype to bias the rules toward.",
    )
    args = parser.parse_args()

    rules_to_add = build_rules(args.style, args.palette, args.archetype)
    rules_file = ".cursorrules"
    mode = "a" if os.path.exists(rules_file) else "w"

    with open(rules_file, mode, encoding="utf-8") as handle:
        if mode == "a":
            handle.write("\n\n--- UI Rule Update ---\n")
        handle.write(rules_to_add)

    archetype_suffix = f" with archetype '{args.archetype}'" if args.archetype else ""
    print(
        f"Applied design rules for style '{args.style}' with palette '{args.palette}'{archetype_suffix} into {rules_file}"
    )


if __name__ == "__main__":
    main()
