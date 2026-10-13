# Verify mounted media through file handles and exact presentation timestamps

Status: verified local worker procedure, 2026-10-12.

- Scope: source-media decode checks and frame-accurate QA when mounted-path access or random seeking behaves inconsistently.
- Prerequisites: the source is authorized, its size is stable, and it is not an incomplete download or partial file.
- Source: local worker execution, complete source decode, independent render decode, and requested-frame inspection.

When Python can read a mounted original but FFmpeg reports that the path does not exist, test PyAV with a seekable handle opened from the path before declaring the media unavailable. Enumerate only streams with codec contexts; mounted camera files can include data streams that are not decodable audio or video. Treat complete original-media decode and proxy decode as separate evidence.

After a PyAV seek, decode forward until the requested presentation timestamp. The first decoded frame can be an earlier keyframe, so saving it under the requested frame number creates false timing or shot evidence. Use an enumerated all-frame scan when exact sequential coverage is required.

Check stable source size, complete original AV decode, independent full FFmpeg decode when available, exact requested PTS for sampled stills, and the expected frame/audio inventory. If the original still cannot be fully read, report that boundary instead of substituting successful proxy decode as proof.
