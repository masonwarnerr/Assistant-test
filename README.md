# Independent local Hermes agents

A secret-free setup and operations playbook for one local work agent per computer. **Use one work-only Hermes profile for that computer's desktop, CLI, and Slack bot.** Give each computer its own Slack app and token pair. Do not create a second profile merely because you are adding Slack.

## Start here

1. Read [the replication checklist](docs/replication-checklist.md).
2. Follow [the local pilot](docs/first-device-pilot.md): profile, model, work context, and a real read-only test.
3. Configure [Slack](docs/slack.md), including the distinction between app defaults and the installed bot's searchable name.
4. Connect only installed local applications using [the creative-app guide](docs/creative-apps.md): native Resolve MCP, Blender's live addon, and Figma OAuth.
5. Review [privacy and separation](docs/privacy-and-separation.md) before opening access to teammates.
6. Use [operations](docs/operations.md) and the [architecture](docs/architecture.md) for ongoing work. [Notion](docs/notion-task-board.md) and [other-device connections](docs/second-device-rollout.md) are optional, later steps—not prerequisites for a local Slack agent.

## What the tested setup established

A local Mac's desktop and Slack agent were consolidated onto its default profile, keeping cleaned work skills and persistent memory together. Its old setup gateway was uninstalled and its history retired outside active profiles; an existing app-specific profile was preserved rather than discarding its authentication. Another computer's agent was not contacted or modified.

Verified outcomes: model inference; Slack bot authentication and Socket Mode reconnection; native Resolve status reporting version 21.1; Blender 5.2.1 LTS with addon 1.8/protocol 13 and live loopback connectivity; Figma work-account authentication and a read of an authorized work node. Tool counts and versions are observations, not requirements or promises about future releases. A full creative task delivered through Slack remains a separate acceptance gate. The repeated Slack avatar upload problem was **not resolved**; it is not documented as a successful fix.

## Fast troubleshooting rules

- A missing Slack search identity is not a stopped-gateway problem. Check the installed workspace bot user name.
- `connections:write` is the app token's Socket Mode permission; reading messages is governed by separate bot OAuth scopes.
- Blank allowed-user IDs do not mean everyone is allowed, and the home channel is not an access policy.
- MCP tool discovery does not prove Blender's addon is reachable or Figma can read the intended work file.
- Copying skills does not copy connections or OAuth, and a repository checkout is not automatically profile memory.
- Never transplant another machine's Hermes home to create an "independent" agent.
- Open Slack plus local terminal/desktop access is powerful. Cleaning prompts and personal skills is **not** an OS sandbox.

## Included helpers

- [Addon layout repair](scripts/fix_blender_addon_layout.py): dry-run by default; explicit `--apply`; backs up replaced addon code and refuses symlinked paths.
- [Enable Blender bridge](scripts/enable_blender_bridge.py): run inside Blender; enables the addon, disables prompt/scene telemetry consent, starts the loopback bridge, and saves preferences—not project files.

These helpers do not authenticate services, transfer secrets, or create cloud resources. Close Blender before updating addon code. See the creative-app guide for the order of operations.

```bash
python3 -m unittest discover -s tests -v
git diff --check
```

The unit tests use isolated fixtures; they do not substitute for the live application and Slack acceptance checks.

## Repository boundary

Commit instructions, reviewed reusable skills, templates, and safe helper code only. Never commit `.env`, provider keys, Slack tokens, OAuth stores, personal preferences, memories, sessions, logs, browser profiles, generated Slack manifests, or private work asset registries. [SKILL-MANIFEST.md](SKILL-MANIFEST.md) describes the distributed material. The existing copied Hermes hub is not a complete replacement for the locally installed skill and its references.

Authoritative current references: [Hermes docs](https://hermes-agent.nousresearch.com/docs/), [documentation index](https://hermes-agent.nousresearch.com/docs/llms.txt), and the installed `hermes <command> --help`. When they differ, validate the live command instead of following a stale recipe.
