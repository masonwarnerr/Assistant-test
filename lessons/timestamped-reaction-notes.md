# Preserve the marked source frame in timestamped reaction notes

Status: verified local worker procedure, 2026-10-08.

- Scope: interview feedback that names a spoken word and a visible reaction at a review timestamp.
- Source: three completed reaction-timing corrections in one local Resolve pass, verified by source arithmetic, rendered evidence, and preservation checks.

A review timestamp identifies an output frame, but adding earlier dialogue changes output time. Map the marked frame back to its original source frame before editing. Extend only the continuous opening picture/audio needed to place the named word tail one or two frames before that same source frame. Keep later approved cuts intact. Re-stabilize only an opening whose source range changed.

Constrain waveform-tail refinement with the next word boundary so a broad energy window does not absorb following speech. Extend genuinely quiet room tone without moving or clipping the named word. Preserve grade, crop, later motion, captions, and answer source ranges.

Check the original-to-new source-frame mapping, measured word-tail-to-reaction gap, and annotated frames on both sides of the reaction. Then verify later picture/audio/caption inventories and fully decode the render. Do not claim human listening from automated waveform, ASR, or visual QA.

Evidence: three marked reactions retained their original source frames with measured gaps of about one frame after the named word; the complete 13-movie pass decoded 9,191 frames with no black frames and preserved the later answer sequence.
