# Verify Resolve delivery audio against the approved master

Status: verified local worker procedure, 2026-10-20.

- Scope: Resolve deliveries whose program audio has an approved enhanced or mastered source.
- Prerequisites: the approved audio master, the native render, and packet/decode inspection tools are available.
- Source: same-machine native export, waveform and channel checks, corrective mux, packet comparison, and complete decode.

Track enablement and native render success do not prove that delivered audio matches the approved master. Decode the native output and compare timing, waveform behavior, channel-wise peaks, loudness, and sampled alignment against the actual approved source. Measure decoded stereo channels directly; a power-preserving mono downmix can add apparent level and create a false clipping diagnosis.

If native encoding materially changes the master or produces an unsafe result, preserve the failed intermediate. Create a separately named final delivery that retains the verified native video bitstream while encoding the validated master audio. Prove that picture was not re-encoded by comparing video packet hashes, then repeat full decode, duration, lag, loudness, peak, and delivery-inventory checks.

For a later picture-only or grade-only revision whose prior delivered audio is already approved, render new picture without audio and remux the prior approved audio packets with stream copy. Verify audio packet count and hashes are identical between revisions and verify native/final video packet identity.

The acceptance check is complete AV decode, safe channel-wise peaks, expected loudness and alignment, proved video-packet preservation, and either validated new audio or packet-identical approved audio. Do not claim unchanged audio from enabled tracks, matching duration, or a successful export alone.
