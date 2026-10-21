# Verify Adobe-enhanced program audio before recutting

Status: verified worker procedure from the DaVinci Mac, 2026-10-20.

- Scope: long-form camera speech enhanced in Adobe Podcast, then used as the only program-audio track in Resolve.
- Source: same-machine browser execution, completed download, full decode, multi-window correlation, native Resolve placement, save, and state readback.

Use the browser profile that is already authenticated for the work account. A custom debugging profile that lands on a Google email screen may simply be the wrong empty profile; do not turn that into a new-login request. Drive the already-open authenticated browser with the available desktop interface and complete the native file chooser end to end. Treat `Uploading…` as progress only. Accept the upload when Adobe exposes a real clip duration or enhancement state, and accept the download only when the full stem exists and decodes.

Move the finished stem beside the authorized shoot audio before removing temporary upload/download copies. Verify sample rate, channel count, duration, stable size, and a complete decode. Compare the enhanced stem with the camera source in several windows distributed across the recording. Measure lag and normalized cross-correlation in every window; do not assume a matching duration proves sync. Convert the measured median lag to source frames at the actual timeline rate and record the mapping explicitly.

In Resolve, append the enhanced media to a separate program track using each picture item’s exact source and record bounds plus the measured offset. Disable, but do not silently replace, camera audio. Save, then read back the picture and enhanced source offsets, record starts, durations, and camera-track enabled state.

The acceptance check is a completed Adobe stem, full decode, consistent multi-window lag, explicit frame mapping, exact native placement readback, and muted camera audio. Browser success alone, a downloaded filename, or `AppendToTimeline` returning an item is not sufficient proof.
