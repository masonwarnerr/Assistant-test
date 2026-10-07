# Coordinator machine brief

Role: intake, routing, approvals, report review, Git maintenance, and final verification.

Setup: install Hermes, run `hermes setup` and `hermes doctor`, create/use a `coordinator` profile, then connect Slack only after local acceptance. Keep the coordinator workspace free of specialist caches and raw media.

Routing: use the direct DaVinci path when the Resolve Mac is available; use Lloyd as the local Slack-connected Flex worker for work assigned to that machine. Git is the only shared durable layer for the pilot. No Notion queue or HTTP relay is required.

Standing rules: assign a stable task ID and acceptance criteria; require the worker execution-report contract; verify artifacts and exact observations; promote only verified lessons into Git procedures/skills; never expose secrets; keep Slack bot-to-bot mode off unless explicitly needed.
