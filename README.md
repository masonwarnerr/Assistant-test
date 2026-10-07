# Hermes Agent Fleet Bootstrap

A source-controlled, secret-free runbook for building a small Hermes fleet across Mason's machines. It is written to be pasted into a fresh Hermes install as its setup brief.

## What this repository contains

- [Architecture](docs/architecture.md): machine roles, boundaries, and communication paths.
- [Pilot setup](docs/first-device-pilot.md): get one coordinator working before adding integrations.
- [Second-device rollout](docs/second-device-rollout.md): add Resolve, Blender, or Midjourney workstations safely.
- [Slack](docs/slack.md): verified Socket Mode setup using current Hermes commands.
- [Notion task board](docs/notion-task-board.md): shared board design and OAuth/MCP rules; no API keys.
- [Operations](docs/operations.md): Git conventions, lifecycle, security, and troubleshooting.
- [Machine templates](templates/machines/): coordinator and specialist-machine briefs.
- [Skill manifest](SKILL-MANIFEST.md): what is included and what is intentionally excluded.

## Non-negotiables

1. Never commit tokens, `.env`, OAuth stores, sessions, logs, memory, or private exports.
2. Put secrets in the active Hermes home `.env`; put non-secret behavior in `config.yaml` via `hermes config set`.
3. Start with one device and one real task. Add Slack, Notion, and specialist machines only after the local loop works.
4. Treat this repository as instructions and templates, not as a synchronization store for live agent state.

## Official sources used

- Hermes docs: https://hermes-agent.nousresearch.com/docs/
- Docs index: https://hermes-agent.nousresearch.com/docs/llms.txt
- Hermes source: https://github.com/NousResearch/hermes-agent
- Slack setup: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack
- MCP integration: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp
- MCP config/OAuth reference: https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
- Bot mode and profiles: https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode

Commands in this repository are limited to commands verified in those sources or the Hermes source tree at publication time. Re-check the linked docs after upgrading Hermes.
