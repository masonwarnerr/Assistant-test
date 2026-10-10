# Preserve native state when revising imported Resolve DRTs

Status: verified local worker procedure, 2026-10-09.

- Scope: feedback revisions built from a copied DaVinci Resolve DRT when the revision includes a ripple trim, Fusion-caption retiming, or a reported black flash.
- Prerequisites: keep the approved source timeline and DRT untouched; create an isolated revision; retain the originally submitted source bounds and exact intended caption expressions for comparison.
- Source: local worker execution, native timeline readback, rendered source-waveform comparison, complete frame decode, and splice-frame inspection.

## Procedure

After a DRT ripple trim, inspect native linked-audio start, end, duration, and source offsets on both sides of every splice. Literal fractional fields in the serialized DRT are not sufficient proof: import can expand one trimmed audio item by a frame and shorten the next while picture timing remains correct. Replace only mismatched items in the new revision using the originally submitted exclusive source bounds. Verify native ends and direct rendered source-waveform correlation, then rerender only the affected deliverable.

When retiming Fusion captions, parse complete Lua quoted strings with escaped quotes. Replace `time` tokens only outside nested text literals. A regex that stops at an escaped quote can transform only part of `StyledText` and create caption drift. Compare every native read-back expression with the intended transformed expression, including text literals, before export.

For a reported black flash, scan the picture region independently of burned-in captions. Bright subtitles can raise the full-frame mean while the underlying picture is black. Inspect the exact reported frame sequence and adjacent footage, then check the replacement shot and caption state on both sides of the splice.

## Verification

The approved source revision still exists unchanged. The imported revision's native audio bounds match the intended exclusive source ranges, every transformed caption expression matches its intended value, and the complete render decodes without a black picture region at the reported frames. Inspect splice contact sheets and compare rendered audio directly with the intended source ranges. Do not claim success from serialized DRT equality, a full-frame luma threshold, or a successful import alone.

## Failure boundary

If native readback disagrees with serialized fields, trust the native timeline and repair only the affected new-revision items. If import returns null, the project handle is lost, or the application becomes unstable, stop mutation, recover the saved application state, and re-read the live project before retrying. Never modify the approved source revision to make the check pass.
