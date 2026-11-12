# Keep audio continuous across chunked Resolve renders

Status: verified worker procedure from the DaVinci Mac, 2026-11-11.

- Scope: long Resolve timelines whose picture must be rendered in bounded chunks because a full single-job render is unstable.
- Prerequisites: exact timeline frame bounds, lossless or stream-copy-compatible picture chunks, and a way to render or reconstruct the full timeline audio as one continuous stream.
- Source: two same-machine episode deliveries completed from six and eleven picture chunks, with full audio decode, join-window checks, packet-timestamp checks, and video-payload preservation proof.

Do not treat concatenated AAC chunk audio as continuous program audio. Independent AAC chunks can carry encoder priming or padding at every boundary even when their H.264 picture concatenates correctly.

Render bounded picture chunks from exact, non-overlapping timeline ranges. Concatenate the completed video with stream copy. Separately render the timeline audio once across the entire program to PCM/WAV, fully decode that source, then mux it with the concatenated picture and encode AAC exactly once. Make no editorial, level, or timing changes during this recovery.

For every chunk boundary, decode a window spanning both sides of the join. Require continuous video PTS from zero, strictly increasing audio DTS, the expected full-program frame and audio-sample inventories, and a complete final decode. Prove that the corrective mux did not re-encode or replace the accepted concatenated picture by comparing the video packet payload before and after the mux.
