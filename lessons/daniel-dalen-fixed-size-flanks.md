# Keep Daniel Dalen flank captions at one approved size

Status: verified worker procedure from the DaVinci Mac, 2026-11-11.

- Scope: repairing or rebuilding Daniel Dalen split captions after picture reframing changes the available face-side gutters.
- Prerequisites: the approved text size, locked picture framing, per-word onsets, and a protected snapshot of every timeline outside the caption-repair scope.
- Source: same-machine Resolve rebuild of seven 4:3 split-caption timelines, native readback, protected-state comparison, motion-mask checks, and A/B-camera still inspection.

Do not shrink individual Text+ cards to make phrases fit. Read the current locked framing first, measure one flank pair for each recurring camera geometry, and reuse those camera-specific positions across the batch with one baseline and one approved text size. Reflow long phrases only at word boundaries. If a single word still cannot fit a narrow right flank at the locked size, use an explicit left-flank-only overflow card rather than changing picture or silently reducing type.

Preserve the original word order, spoken onsets, caption-nest bounds, and half-character reveal padding. Snapshot all protected timelines before mutation and compare their IDs, source and record bounds, enabled state, picture properties, grade-node counts, audio structure, track state, markers, and unrelated caption inputs after the repair.

Check every Text+ size by native readback. Assert that reveal ranges cover every non-space character. Compare consecutive reveal frames so already visible word pixels do not move when the next word appears. Inspect at least one representative A-camera and B-camera caption frame per deliverable for complete lettering, face/hair clearance, clipping, and visual-size parity with the approved reference.
