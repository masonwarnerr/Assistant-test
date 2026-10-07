# Fleet architecture

## Roles

| Role | Owns | Does not own |
|---|---|---|
| Coordinator | intake, prioritization, routing, approvals, report review, final delivery | heavy media renders or unattended destructive actions |
| DaVinci Mac | Resolve projects, edits, exports, and media cache through the direct path | coordinator credentials or copied shared state |
| Lloyd worker | local Slack-connected Flex work that is best executed on Lloyd's machine | coordinator OAuth stores, final approval, or publishing without approval |
| Blender workstation | Blender scenes, renders, simulations | production publishing without coordinator approval |
| Midjourney bridge | prompt/image research and approved downloads through the available browser surface | unattended account changes or bulk publishing |

A role is a Hermes profile on a machine. Keep each profile's skills, memory, sessions, and OAuth stores local to that machine. Use `hermes -p <profile> chat` for a profile and `hermes profile list` to inspect profiles.

## Pilot communication paths

- **Direct DaVinci path:** the coordinator routes work directly to the available DaVinci Mac and receives the execution report and artifact references through the agreed local/direct access path. Keep Resolve projects and media on that Mac.
- **Local Lloyd path:** Lloyd remains the local Slack-connected Flex worker. Slack is the conversational trigger/return path for work executed on Lloyd; Git is where reviewed durable knowledge and selected reports land.
- **Shared durable layer:** GitHub is the only shared durable layer for the pilot. Commit procedures, templates, reviewed reports, and lessons; do not use the repository for live state, caches, or raw transcripts.

No Notion task queue or HTTP relay is required for this pilot. Do not add either merely to move task metadata between these paths.

## Data flow

1. Coordinator gives a task a stable ID, request, acceptance criteria, and target path.
2. Coordinator executes or routes it through the direct DaVinci path or local Lloyd worker path.
3. Worker performs the task in its local workspace and fills the execution-report contract.
4. Coordinator checks the report against the artifact and exact observations, then marks review status.
5. Coordinator commits only the useful, redacted report and any reusable lesson/procedure to Git.
6. Coordinator delivers the verified artifact or asks for revision.

## Future HTTP feasibility note

Outbound HTTPS or polling may work even when inbound SSH is blocked. That is only a hypothesis until tested from the target Mac. IRU and other network restrictions cannot be assumed away; test the actual target Mac, network, proxy, firewall, DNS, authentication, and polling behavior before designing an HTTP relay. The pilot does not depend on this future path.

## Failure boundaries

A Slack outage must not erase local work: the worker can complete locally and return a report when available. A Git outage must not erase local work: retain a local redacted report and push later. A specialist workstation must not receive coordinator OAuth stores. A bot must not recursively answer other bots without explicit mention gating.
