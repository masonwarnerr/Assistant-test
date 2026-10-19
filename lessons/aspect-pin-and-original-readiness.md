# Separate Aspect pin state from original-media readiness

Status: verified local worker procedure, 2026-10-18.

- Scope: ingesting full-resolution originals from an authorized Aspect folder before editing or delivery.
- Prerequisites: a supported local Aspect interface, the exact authorized folder target, and a decoder that can read the final media.
- Source: same-machine pin creation/readback, transfer-state inspection, final-file checks, and complete decodes of four requested originals.

Create the pin with the installed supported interface and read it back by exact target identity. A durable pin is not a completed cache: `downloading_chunks` with partial `syncedBytes` is not `synced`.

Do not accept expected byte size alone as proof of completion. A detached `.part` file can be preallocated to the full remote size. Do not import `.part` files or start a duplicate full download while the pin cache is already transferring the same source. If a duplicate transfer was started, cancel only that transfer and verify its cancellation without removing the durable pin or stopping the storage daemon.

Accept an original only when the transfer has completed, the final non-`.part` filename exists at a stable size, and the full audio/video decode succeeds. Keep pin/cache status, filesystem readiness, and decode readiness as separate checks.

The acceptance check is exact-target pin readback at `synced`, final filenames with no partials, and a complete independent decode of every required original. If only a proxy decodes, label it as proxy progress rather than original-source readiness.
