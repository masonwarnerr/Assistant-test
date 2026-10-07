# Hermes Agent Fleet Bootstrap

A source-controlled, secret-free runbook for a small Hermes fleet across Mason's machines. It is written to be pasted into a fresh Hermes install as a setup brief.

## What this repository contains

- [Architecture](docs/architecture.md): machine roles and the simplified pilot communication paths.
- [Pilot setup](docs/first-device-pilot.md): establish the coordinator, direct DaVinci path, and local Lloyd worker.
- [Execution reports](docs/execution-reports.md): worker reporting contract and review flow.
- [Shared learning](docs/shared-learning.md): how verified observations become reusable Git procedures and skills.
- [Second-device rollout](docs/second-device-rollout.md): add Resolve, Blender, or Midjourney workstations safely.
- [Slack](docs/slack.md): verified Socket Mode setup using current Hermes commands.
- [Notion task board](docs/notion-task-board.md): deferred option; not required for the pilot.
- [Operations](docs/operations.md): Git conventions, lifecycle, security, and troubleshooting.
- [Machine templates](templates/machines/): coordinator and specialist-machine briefs.
- [Worker report template](templates/reports/worker-execution-report.md): copy for a reviewed task report.
- [Skill manifest](SKILL-MANIFEST.md): what is included and what is intentionally excluded.

## Pilot architecture

Git is the only shared durable layer. The coordinator uses the direct DaVinci path when a Resolve Mac is available. Lloyd is the local Slack-connected Flex worker for tasks that should run on the Lloyd machine. The pilot requires neither a Notion queue nor an HTTP relay; use local workspaces, Slack where already configured, and committed Git documentation/reports.

## Non-negotiables

1. Never commit tokens, `.env`, OAuth stores, sessions, raw logs, memory, or private exports.
2. Put secrets in the active Hermes home `.env`; put non-secret behavior in `config.yaml` via `hermes config set`.
3. Start with one coordinator and one real task. Add integrations and specialist machines only after the local loop works.
4. Treat this repository as instructions, reviewed reports, and reusable procedures—not as a synchronization store for live agent state.
5. Reports must be concise, redacted, and reviewable; do not turn the repository into a transcript or secret-bearing log archive.

## Official sources used

- Hermes docs: https://hermes-agent.nousresearch.com/docs/
- Docs index: https://hermes-agent.nousresearch.com/docs/llms.txt
- Hermes source: https://github.com/NousResearch/hermes-agent
- Slack setup: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack
- MCP integration: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- MCP config/OAuth reference: https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
- Bot mode and profiles: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode

Commands in this repository are limited to commands verified in those sources or the Hermes source tree at publication time. Re-check the linked docs after upgrading Hermes.
