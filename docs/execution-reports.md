# Worker execution reports

A worker report is a compact, human-reviewable record of what happened—not a transcript. Use the template at `templates/reports/worker-execution-report.md`.

## Required contract

Every report must identify:

- **Task ID** — stable ID assigned by the coordinator.
- **Request** — the request as understood, including acceptance criteria.
- **Actions** — commands, tools, route used (direct DaVinci or Lloyd local worker), and meaningful steps.
- **Files/artifacts** — files changed, artifact paths or approved links, and checksums where useful; never include private media or secrets.
- **Decisions** — choices made, assumptions, and approvals needed.
- **Errors** — failures, retries, blockers, and unresolved risk; write `None` when none occurred.
- **Exact execution observations** — factual outputs and environment observations, separated from interpretation. Include versions, timings, exit codes, or UI state when relevant.
- **Reusable lessons** — a candidate lesson, or `None` if nothing generalizes.
- **Review status** — `Draft`, `Needs revision`, `Verified`, or `Rejected`, with coordinator, date, and verification evidence.

Workers should fill the report while the evidence is available. The coordinator verifies artifact existence/content and checks the exact observations before accepting it. A report is not proof merely because a command returned zero.

## Review and promotion

The coordinator reviews the report against the request and artifact, redacts sensitive/noisy material, and commits a concise report under `reports/<task-id>.md` when durable history is useful. Candidate lessons go under `lessons/<slug>.md` only after verification. Stable, repeatable lessons can then be promoted into a skill or procedure as described in `docs/shared-learning.md`; one-off observations remain in the report.
