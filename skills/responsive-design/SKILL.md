---
name: responsive-design
description: >
  Refactor UI code to be fully responsive using modern CSS techniques
  like container queries, fluid layouts, and mobile-first design.
---

# Responsive Design

## When to use

Use this skill when:
- UI is not responsive across devices
- Fixed widths (px) are used
- Layout breaks on mobile/tablet
- Too many media queries exist
- Legacy CSS needs modernization

---

## Instructions

When this skill is invoked:

### 1. Analyze
- Identify layout structure (flex, grid, block)
- Detect issues:
  - Fixed widths/heights
  - Overflow problems
  - Poor mobile layout
  - Excessive breakpoints

---

### 2. Refactor Layout
- Convert fixed layouts → flexible layouts
- Use:
  - Flexbox (1D layouts)
  - CSS Grid (2D layouts)
- Apply `auto-fit`, `minmax()` where useful

---

### 3. Improve Responsiveness
- Use mobile-first approach
- Reduce unnecessary media queries
- Prefer container queries for component-level responsiveness

---

### 4. Apply Fluid Design
- Replace static values with:
  - `clamp()` for typography and spacing
  - `%`, `vw`, `cqi` units
- Avoid fixed pixel values unless required

---

### 5. Fix Common Issues
- Prevent horizontal overflow
- Ensure images scale correctly
- Use `aspect-ratio` where needed
- Maintain proper spacing and alignment

---

## Output

- Return only improved code
- Do not include explanation unless asked
- Keep code clean and production-ready
- Preserve original structure where possible

---

## Constraints

- Avoid excessive breakpoints
- Prefer fluid layouts over rigid layouts
- Keep code simple and maintainable

---

## References

Use supporting files:
- fluid-layouts.md
- container-queries.md
- breakpoint-strategies.md