# Intercut case-study B-roll and preserve comparison cuts

Status: verified worker procedure from the DaVinci Mac, 2026-10-09.

- Scope: revising case-study overview ads from sparse or blanket B-roll coverage while retaining an earlier coverage option for review.
- Source: worker execution in `Ads restored 20261008`, local Resolve scripts, marker readback, save receipts, and export inventory/full-decode checks.

Treat a 60–70% B-roll request as an intercut rhythm, not permission to cover the whole body. At 24 fps, a useful starting pattern is 32 frames of speaker, a 48-frame B-roll hit, a 16-frame return to the speaker, repeated as room allows, with roughly 36 speaker frames at the close. The percentage is a guide: preserve stronger face moments, the opening, and the final spoken thought even when measured coverage lands lower.

Before rebuilding, park any required grade donor outside the ad region while it still exists. Delete the old in-ad overlays before appending replacements; appending onto occupied ranges can trim a new hit to the old gap. Append picture only with `mediaType=1`. For mixed-rate media, request enough source frames for the desired timeline duration, such as `round(48 * media_fps / 24)` for a 48-frame hit. Advance the next record position from the placed item's `GetEnd()`, not from the requested source span.

When review requires an earlier 35–40% option, append it after the current overview content instead of overwriting the 60–70% cut. Add one section marker and one uniquely named marker per comparison cut. Read existing comparison marker names before mutation and skip matches so reruns are idempotent.

Check the actual union of B-roll intervals inside every marked ad, then inspect the rhythm: speaker and B-roll must trade places through the body, with no blanket middle and no isolated flashes. Confirm both coverage versions and all comparison markers remain in the same overview after save.

Do not use render-queue completion as delivery proof. Enumerate the exact expected output names and full-decode every file. Missing files, an invalid partial MP4, or a lost Resolve project handle while polling means the export set is incomplete even if the log says `render done`.
