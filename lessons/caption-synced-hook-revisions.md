# Preserve hook timing and geometry across overlay revisions

Status: verified local worker procedure, 2026-10-08.

- Scope: overlay-only text hooks on finished vertical movies.
- Source: three completed five-movie batches on the local worker, including two successive whole-graphic size revisions.

When the brief says the hook is caption-synced, use the existing rendered caption's ending frame for the final spoken hook word as the title-out boundary. Check adjacent decoded frames and speech. Do not substitute a fixed duration, picture cut, or independently rounded ASR timestamp, and do not alter the existing captions.

For a whole-graphic size revision, rerasterize from the authorized font and composite from the original base movie. Scale type, panel dimensions, padding, line gaps, and corner radius together. Preserve exact copy and the approved title-out frame. If head clearance constrains placement, keep the approved safe edge and enlarge away from the face rather than silently reducing the requested scale.

Check every hook frame for head clearance, especially after shot changes. Verify complete decode, every video PTS/frame count, unchanged duration, and copied audio payload/decoded PCM against the base. Deliver revisions separately and read back the exact remote inventory and upload state.

Evidence: each size-revision batch covered five movies and 7,047 frames; both later batches preserved all five title-out frames, frame timing, duration, and audio while exact-target upload readback passed.
