# Ant Components

Use these patterns for operational products where clarity, predictability, and dense workflows matter more than visual novelty.

## Page Scaffold

- Header with title, context, and top-right primary action
- Filters/search row before the main data region
- Main content in cards, tables, forms, or lists
- Secondary detail in drawer, side panel, tabs, or expandable row

## Component Priorities

- Primary: button, form, table, tabs, tag, alert, drawer, modal
- Supporting: empty state, pagination, dropdown, tooltip, toast/message

## Behavior Rules

- Use inline validation before modal interruption
- Keep action hierarchy explicit: primary, secondary, tertiary, dangerous
- Prefer status tags and alerts over decorative badges
- Design empty, loading, success, and error states as first-class states

## Tailwind Notes

- Spacing rhythm: 8px base
- Radius: 6px to 8px
- Primary: `#1677FF`
- Borders: light neutral strokes
- Shadows: subtle and functional

## Example Pattern

- Resource table page
  - header with title and create button
  - filter bar with search, status filter, date range
  - table with status tags and row actions
  - drawer for inline editing
