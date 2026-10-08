---
name: agent-learning-sync
description: "Use when syncing agent learnings to GitHub."
version: 0.1.0
author: Mason Warner, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [learning, github, edit, fleet]
---

# Agent learning sync

Shared creative learnings live in `https://github.com/masonwarnerr/Assistant-test.git`. Full contract: `docs/recursive-learning.md` in that repo.

## When to Use

- The overnight learning cron
- Mason asks to record a reusable edit/design/animation correction for other agents
- Another agent needs the same loop installed

Don't use for: one-off chat answers, secrets, personal admin, or dispatching a Resolve/AE job.

## Procedure

1. Identify this computer's agent id. masonpc is taken. Read `agents/*.md` for the slot table. Done when the id is unique.
2. `git pull --rebase` in the clone. Done when local main matches origin or the rebase is clean.
3. Read `lessons/` and every `inbox/*/INDEX.md`. Done when you can name what is already stored.
4. Scan the last working day in the local profile skills and sessions. Done when each candidate is either kept or dropped in writing.
5. If nothing new qualifies, stop. No commit. Done when the reply is `no change`.
6. Write only `inbox/<agent-id>/YYYY-MM-DD.md` and that agent's `INDEX.md`. Promote a **new** `lessons/<slug>.md` only for a repeated correction or a procedure already proven in a local skill. Done when no other agent's path is staged.
7. Commit `learn: <agent-id> <date>`, `git pull --rebase`, `git push`. One rebase retry. No force-push. Done when `git status` is clean and the commit is on origin.

## Hard stops

- No Astra. Soul (`gpt-5.6-sol`) if openai-api is logged in, else Grok.
- No tokens, addresses, Tailscale IPs, or raw transcripts in the repo.
- Do not edit another agent's inbox to "clean it up."
- A clone is not a skill install. Copy this skill into the active profile.

## Verification

`git log -1` and `git status` after push. The new files exist under this agent's inbox only.
