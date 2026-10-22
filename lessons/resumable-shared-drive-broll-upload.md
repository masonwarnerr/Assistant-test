# Upload selected raw media to a shared drive with resumable verification

Status: verified worker procedure from the DaVinci Mac, 2026-10-21.

- Scope: publishing a reusable set of raw product or case-study B-roll from media already selected during an edit.
- Prerequisites: saved worker-side selection records, authorized source media on the local machine, an approved shared-drive destination, and authenticated Drive API access that remains local.
- Source: same-machine manifest construction, resumable Drive API upload, per-object receipts, and exact manifest-to-receipt reconciliation.

Build the upload manifest from proved edit records rather than copying an entire source tree. Include enabled timeline sources, approved planned hits, and retained unused selects when those selects are part of the accepted review reel. Deduplicate by source identity. Classify each item into the intended product or study subfolder before upload.

Apply explicit exclusions before any network write: interviews, music, standalone audio, rejected or `DONTUSE` media, BTS owned by another workflow, missing files, and unsupported media. Keep credentials and the full private source registry local; neither belongs in the learning repository.

Upload from the machine that owns the source media. Use resumable sessions and enable shared-drive support on list, create, and upload requests. Before starting a new upload, query the exact destination subfolder and skip only a remote file whose name and byte size both match. Record one durable receipt per file with status, destination group, name, returned object identity, and size, but do not publish those private identities.

The acceptance check is an independently counted local manifest of unique destination/name/size tuples, zero excluded-source matches, a receipt for every manifest row, zero failed rows, matching manifest and receipt totals, and a final status record with the same file and byte totals. A completed upload process, a folder that merely opens, or a matching filename without matching size is not sufficient proof.
