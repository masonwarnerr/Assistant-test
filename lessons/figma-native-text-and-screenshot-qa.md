# Verify native Figma text reflow and screenshot evidence

Status: verified local worker procedure, 2026-10-17.

- Scope: native editable Figma collateral with multi-line text and screenshot-based visual QA.
- Prerequisites: the authorized fonts are loaded, the deliverable must remain editable, and full-page plus dense-module inspection is in scope.
- Source: same-machine worker execution, native node readback, complete geometry audit, and inspected PNG evidence.

Set each text node's fixed width before enabling height auto-resize. Resizing after height auto-resize can leave the node at its initial short height and clip multi-line copy. After reflow, read back the actual text and parent-module bounds rather than trusting the requested dimensions.

If a returned screenshot URL downloads as an empty file, capture the native node directly and inspect the resulting image. Transparent section captures may appear black outside Figma; composite only local QA copies onto white for inspection. Do not modify or flatten the native artwork to make evidence easier to view.

Check every visible text node, exact frame dimensions, missing-font state, image nodes, out-of-bounds nodes, parent clipping, pairwise text overlaps, and final hyperlinks. Inspect full pages and the densest modules because a clean geometry audit does not prove the composition is readable.

The acceptance check is successful native readback with no unintended clipping, overlaps, missing fonts, or out-of-bounds nodes, plus usable full-page and dense-module screenshot evidence. If direct node capture also fails, report the evidence boundary instead of claiming visual QA from geometry alone.
