# Apply the exact project-saved Resolve gallery still

Status: verified local worker procedure, 2026-10-20.

- Scope: a Resolve grade correction where the reviewer identifies a saved gallery frame as the authority.
- Prerequisites: the authorized project is open, the saved still is in that project's gallery, and a new revision can be tested without changing the approved source timeline.
- Source: repeated reviewer correction, same-machine gallery readback, still/DRX export, native grade application, and rendered comparison.

Inspect the current project's gallery albums and stills before considering a timeline clip, historical still index, shared PowerGrade, or older export. Identify the exact saved still by its real gallery metadata and inspect its pixels. If PNG export fails but DPX export succeeds, use the produced DPX and DRX rather than fabricating a reference or declaring the gallery empty from stale UI text.

Duplicate the latest authorized timeline. Apply the exact exported DRX to one intended camera clip, then verify the actual correction and OFX parameters, current sizing, and a decoded pilot render against the saved reference at the same source frame. Only after that check should the grade be applied to the remaining intended camera keeps. Preserve screen recordings, keys, flares, captions, audio, and other non-camera graphs independently.

The acceptance check is exact project-still identity, usable image and DRX evidence, parameter equality on intended camera clips, a rendered reference match, preserved non-camera graphs, and a complete final decode. Node count, a successful grade-apply return, or equality to a previously contaminated revision is not sufficient proof.
