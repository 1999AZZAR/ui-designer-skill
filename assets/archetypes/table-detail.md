# Table Detail Archetype

Use for CRUD-heavy admin tools where users scan a list and inspect or edit a selected record.

## Best System Fits

- `ant`
- `carbon`
- `atlassian`
- `polaris`

## Core Regions

- page header with primary action
- search, filter, sort, and bulk actions
- table or list with strong status visibility
- detail drawer, side panel, expandable row, or split pane

## Behavior Rules

- Keep row actions predictable and discoverable
- Prefer inline status and lightweight editing where safe
- Use drawers or side panels for context-preserving edits
- Design bulk selection and empty states from the start

## Good Hybrids

- `ant` + `neo-m3` for stronger editorial product voice
- `carbon` + `minimal` for calmer enterprise tooling

## Starter Structure

```text
Header
Filter and Bulk Action Row
Primary Table
Detail Drawer or Side Panel
```
