# Independent agents and shared local surfaces

## Default topology

```text
Computer A                         Computer B
work-only default profile          work-only default profile
  desktop / CLI / Slack app A         desktop / CLI / Slack app B
  local skills + memory               local skills + memory
  local application MCPs              local application MCPs
  own provider/OAuth credentials      own provider/OAuth credentials
```

The desktop agent and its Slack identity share one local profile. Each computer remains independent: its own state, unique Slack app/token pair, and OAuth grants. No SSH, shared live memory, or central PC dispatcher is required for local control.

A local profile is not a filesystem sandbox. A shared bot with terminal and desktop tools can exercise the OS account's permissions. Cleaning personal skills removes context, not access to personal files or signed-in browser sessions.

## When additional profiles make sense

Use a named profile for a genuinely independent role or state boundary on the same computer—not merely a different chat surface. Preserve an existing specialist profile if it still owns needed authentication or sessions; do not blindly delete it in a consolidation.

The tested installed Hermes CLI uses one host gateway to serve profiles and refuses ordinary per-profile gateway installation. Use `hermes gateway --help` and `hermes gateway migrate --help` to check the installed version. Historical standalone overrides are compatibility shims, not the new-computer recipe. [Operations](operations.md) describes careful same-machine consolidation.

## Roles are optional specialization

| Role | Work scope | Boundary |
|---|---|---|
| General local work agent | Local intake, creative tools, verification, delivery | Does not inherit another computer's persona or private accounts |
| Coordinator | Prioritization, optional board, approvals and handoff | Does not assume it can reach a remote workstation |
| Resolve specialist | Local projects, media and exports | No unapproved source overwrite or publishing |
| Blender specialist | Local scenes, simulations and renders | No unapproved changes to accepted assets |
| Browser/design specialist | Authorized work design and research | No private account or browser-tab access |

Use [machine briefs](../templates/machines/) to select a role; keep the profile choice separate from the role label.

## What travels between computers

Travel: source-controlled instructions, reviewed portable skills, templates, and explicit task briefs/artifact links.

Stay local: `.env`, provider and OAuth stores, memory, sessions, logs, browser profiles, personal preferences, machine caches, and private exports. This repository is not a live state synchronizer. Copying a skill does not connect its service.

Optional collaboration uses [documented peer connections](second-device-rollout.md) over private networking with explicit authorization. Do not auto-connect a PC because an old skill mentions it. An optional [Notion board](notion-task-board.md) tracks durable work but is not necessary for a local agent to answer Slack.

## Completion contract

Every work task has scope and acceptance criteria. Return the actual artifact path, tool/command results, verification, and remaining blockers. A model reply, a running process, discovered tools, and a finished deliverable are different levels of evidence. Verify the level requested.
