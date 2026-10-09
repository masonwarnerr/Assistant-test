# Preserve approved reel state before overlaying it

Status: verified worker procedure from the DaVinci Mac, 2026-10-08.

- Scope: moving approved B-roll reel selects into finished overview timelines and stabilizing eligible picture in Resolve.
- Source: worker execution in `Ads restored 20261008`, verified by structural readback and per-item receipts.

Before deleting or moving any approved reel TimelineItem, snapshot its media ID, source and record bounds, duration, `GetSpeed()`, enabled state, complete transform/crop/Scaling properties, and grade data. Copying grades and transforms does not preserve speed. Append picture with `mediaType=1` so source audio is never introduced.

Treat mixed-rate append math as a readback problem. Resolve can report the requested timeline duration while clamping the source endpoint and freezing the tail. Read source and record bounds independently; delete only the failed new probe and adjust the source endpoint one frame at a time until the result is exact. Restore the approved speed explicitly and verify it again.

Move unused selects to a compact tail while their originals still exist, prove grade/transform/speed parity, then delete originals non-ripple. Do not delete media-pool items or dependency timelines. Audit combined old and new overlay intervals for overlaps, repeated adjacent shots, and face flashes under 12 frames. Keep cold opens and final syllables uncovered.

Stabilize enabled and disabled camera picture plus real-world overlays. Skip UI, end cards, generators, and unused tail selects. Journal each TimelineItem ID, return value, bounds, enabled state, and error, save in bounded batches, and resume only missing IDs. A true return is not completion proof without coverage readback.

Use the native Resolve viewer for visual QA. ffmpeg may autorotate footage that remains sideways in Resolve, and Color-page clip thumbnails are not proof of the current composite. If a scoped capture shows only a toolbar strip, rediscover the exact Resolve PID/window ID before capturing.

Check: every planned overlay has a structural receipt; combined-track QA is clean; stabilization receipts cover every eligible ID; audio identity/timing/gain and camera source ranges/enabled states are unchanged; the authorized project is saved on the requested timeline/page with no render in progress.
