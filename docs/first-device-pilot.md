# First-device pilot

Run this on the coordinator device. Do not add Slack or Notion until the local agent completes a real, harmless task.

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

## 4. Pilot acceptance test

Ask Hermes to:

- read this repository;
- create a task note with acceptance criteria;
- make a small change in a disposable branch;
- run the relevant verification;
- report files, tests, and blockers.

Record the result in `pilot-log.md` locally (ignored or outside the repo). The pilot passes only if the report is reproducible and no secret or private state entered Git.

## 5. Add the shared board

Follow `notion-task-board.md` only after the local pilot passes. Use the connected OAuth/MCP flow; never request or read `NOTION_API_KEY`.
