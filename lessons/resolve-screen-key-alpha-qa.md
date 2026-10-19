# Verify Resolve screen keys with decoded alpha

Status: verified local worker procedure, 2026-10-18.

- Scope: keyed screen recordings or UI plates assembled over camera footage in Resolve/Fusion.
- Prerequisites: an authorized screen plate, an editable native comp, and an alpha-capable technical render.
- Source: same-machine native Fusion test renders and decoded RGBA inspection.

A green-free RGB still does not prove the key is clean. The default key in the verified case removed visible green but left a colored border at roughly 20% opacity.

Build a short native technical test and render it with alpha. Decode RGBA and inspect representative border, corner, and UI-interior pixels. Tune matte thresholds from the current plate. When the border is fixed and the UI interior must remain fully opaque, protect that interior with a correctly sized solid matte derived from the current plate rather than reusing another plate’s rectangle.

Keep camera grades, CST, and picture-only effects off the screen recording. Export the corrected editable comp, then instantiate fresh source-timed nodes on production cuts instead of blindly importing timing from the QA clip.

The acceptance check is zero alpha on the intended border/background and full alpha on the real UI interior, followed by a rendered composite inspection. If an alpha-capable render is unavailable, report that the key has only RGB evidence and is not fully verified.
