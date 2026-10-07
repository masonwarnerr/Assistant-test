# Fleet architecture

## Roles

| Role | Owns | Does not own |
|---|---|---|
| Coordinator | intake, prioritization, task board updates, routing, approvals, final delivery | heavy media renders or unattended destructive actions |
| Resolve workstation | DaVinci Resolve projects, exports, media cache | credentials or shared state copied from another machine |
| Blender workstation | Blender scenes, renders, simulations | production publishing without coordinator approval |
| Midjourney bridge | prompt/image research and approved downloads through the available browser surface | unattended account changes or bulk publishing |

A role is a Hermes profile on a machine. Keep each profile's skills, memory, sessions, and OAuth stores local to that machine. Use `hermes -p <profile> chat` for a profile and `hermes profile list` to inspect profiles.

## Communication

- Human intake: Coordinator CLI/desktop, then optional Slack gateway.
- Durable work state: one shared Notion database, with a GitHub link and machine/role fields.
- Code/config/template state: this Git repository.
- Cross-machine agent work: prefer Hermes Bot Mode/connected gateways; for always-on peer routing use the documented `hermes peer` flow and protect `API_SERVER_KEY`.
- Large media: local or approved shared storage; store links and checksums in Notion, not binaries in this repo.

## Data flow

1. Coordinator creates or normalizes a Notion task.
2. Coordinator assigns a role and records an explicit acceptance criterion.
3. Specialist agent works only in its assigned workspace and reports artifacts, blockers, and next action.
4. Coordinator verifies the artifact, updates Notion, and publishes or requests revision.
5. Git changes are committed to a branch and reviewed before merge.

## Failure boundaries

A Slack outage must not erase task state. A Notion outage must not block local work: keep a temporary local task note and reconcile later. A specialist workstation must not receive coordinator OAuth stores. A bot must not be allowed to recursively answer other bots without explicit mention gating.
