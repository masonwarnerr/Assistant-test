# First-device pilot

Run this on the coordinator device. The pilot uses Git as its only shared durable layer. It does not require a Notion queue or an HTTP relay.

## 1. Install and verify

Windows native install (official docs):

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Then start the setup flow and health check:

```powershell
hermes setup
hermes doctor
hermes
```

If using the Nous Portal, the official quick path is `hermes setup --portal`. Choose a provider/model with at least 64K context. Do not paste credentials into this repository.

## 2. Establish a profile boundary

Use the default profile for the pilot. Create specialist profiles only when the first task is verified:

```powershell
hermes profile list
hermes profile create coordinator
hermes -p coordinator chat
```

If the installed version's profile subcommand differs, run `hermes profile --help`; do not guess flags.

## 3. Configure non-secrets safely

Use the CLI, not hand-edits to YAML:

```powershell
hermes config set terminal.backend local
hermes config set display.interface tui
```

Behavioral settings belong in `config.yaml`. Secrets belong in the active Hermes home `.env` or OAuth flow. Never create a repo copy of either.

## 4. Choose the execution path

- Use the **direct DaVinci path** when the Resolve Mac is available. Keep the project, source media, cache, and exports on that Mac; return paths or approved artifact links in the report.
- Use **Lloyd's local path** for work assigned to the local Slack-connected Flex worker. Slack is the worker's local trigger/return surface, not a replacement for the reviewed Git record.
- Do not introduce a Notion queue or HTTP relay for the pilot. If either is evaluated later, document the result and security boundary first.

## 5. Pilot acceptance test

Ask Hermes to:

- read this repository;
- assign a stable task ID and acceptance criteria;
- execute a small, harmless task through one of the two paths;
- run the relevant verification;
- complete `templates/reports/worker-execution-report.md`;
- have the coordinator review the report and commit only the redacted, useful result.

The pilot passes only if the report is reproducible, exact observations are distinguished from interpretation, the artifact is verified, and no secret or private state entered Git. Keep scratch notes and raw logs local or ignored.

## 6. Optional integrations later

Add Slack or other integrations only when needed and after the local loop passes. The existing Slack setup remains available in `docs/slack.md`. The Notion design is retained as a deferred option in `docs/notion-task-board.md`; it is not part of the pilot.
