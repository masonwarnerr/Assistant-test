# Shared learning workflow

Git is the shared durable layer for verified learning. A worker does not directly change shared skills based on an unreviewed observation.

The overnight loop (what to store, who writes which files, when to pull and push) is [recursive learning](recursive-learning.md). That pass writes `inbox/<agent-id>/` and may add a new `lessons/<slug>.md`. It still does not rewrite shared skills from a single unreviewed note.

## Promotion flow

1. Worker records a candidate in the execution report's **Reusable lessons** field, with the exact observation that supports it.
2. Coordinator reproduces or checks the observation against the artifact, command output, or target-machine state.
3. Coordinator marks the report `Verified` (or records why it needs revision/rejection) and removes secrets, private data, and noisy transcript material.
4. If the lesson is reusable, commit a short entry under `lessons/<slug>.md` or update the relevant procedure/skill. Include scope, prerequisites, tested command/path, expected result, failure boundary, and date/commit.
5. Run the documented verification again, review the diff, and commit the procedure with the report or a link to its task ID.
6. Future workers follow the promoted procedure and report whether it still works. Superseded guidance is updated or removed rather than duplicated.

## Suggested layout

```text
reports/<task-id>.md                 # reviewed, redacted task report
lessons/<slug>.md                    # coordinator-verified reusable lesson
templates/reports/worker-execution-report.md
skills/<name>/SKILL.md               # stable procedure/skill, when warranted
docs/<topic>.md                      # broad architecture or operational guidance
```

Do not commit every run, raw Slack transcript, screenshots, terminal dump, media file, or machine log. Keep those local/ignored and promote only the smallest evidence-backed statement that another worker can use. Never promote secrets, credentials, private URLs, personal data, or unverified network assumptions.
