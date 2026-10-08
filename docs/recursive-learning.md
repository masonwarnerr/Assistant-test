# Recursive learning loop

This is the handoff. A fresh agent should follow it without a chat recap.

GitHub repo: `https://github.com/masonwarnerr/Assistant-test.git`
Local checkout on this PC: `C:\Users\mason\Assistant-test-bootstrap`

Git is the only shared durable layer. Profiles, memory, sessions, tokens, and OAuth stay on the machine that owns them. A clone does not install a skill or authenticate an app.

## What this is for

Creative work: video editing, graphic design, animation, and the tools around them (Resolve, Adobe Podcast, After Effects, Blender, Figma). The loop stores corrections that will happen again, plus procedures another agent can run. It does not store one-off taste notes, raw transcripts, or secrets.

## Where things live

```text
agents/<agent-id>.md          who this machine is, and which overnight slot it owns
inbox/<agent-id>/YYYY-MM-DD.md   that agent's nightly candidate pass (only they write here)
lessons/<slug>.md             reusable rule, safe for every agent to follow
skills/<name>/SKILL.md        stable procedure, only after the lesson has held
templates/learnings/          the daily-pass shape and the overnight prompt
```

An agent writes only:

- `agents/<its-own-id>.md`
- `inbox/<its-own-id>/` (new dated files, plus its own `INDEX.md`)
- a **new** `lessons/<slug>.md` when promoting

It does not edit another agent's inbox, and it does not rewrite a shared index. Read every `inbox/*/INDEX.md` and `lessons/` on pull. That is the shared memory.

## Agent id

One id per computer, stable, lowercase, no spaces. This PC is `masonpc`. The other agent picks its own id (hostname is fine) and must not reuse `masonpc`.

## When to push and pull

Overnight, local time `America/Los_Angeles`, between 02:00 and 04:00. Slots are 15 minutes apart so two agents are not pushing the same minute. Claim the first free slot by adding `agents/<id>.md` before enabling the cron.

| Slot (PT) | Owner |
|---|---|
| 02:15 | masonpc |
| 02:30 | next agent |
| 02:45 | next |
| 03:00 | next |
| 03:15 | next |

File isolation is the real lock. The stagger is just politeness. If two pushes still race, `git pull --rebase` and push again. Do not force-push.

Order inside a run:

1. `git pull --rebase origin main` (or the repo default branch).
2. Read `lessons/` and every `inbox/*/INDEX.md`. Do not re-file a lesson that is already there.
3. Scan the local profile's last working day: skills that changed, session corrections, revision notes. Cron sessions do not see the daytime chat, so the prompt has to point at the profile skills and session store.
4. Write `inbox/<agent-id>/YYYY-MM-DD.md` only if there is at least one reusable learning. Update that agent's `INDEX.md`.
5. Promote to a new `lessons/<slug>.md` only when the same correction already showed up more than once, or it is already a proven step in a local skill. One-off notes stay in the inbox file.
6. Commit only those new files. Message: `learn: <agent-id> <YYYY-MM-DD>`.
7. `git pull --rebase`, then `git push`. If push rejects, rebase once and push once more. Then stop.
8. If nothing new qualified, do not commit and do not push.

## What qualifies

Keep it if a future edit would be wrong without it:

- A correction Mason repeated (ums and uhs in Victor's dialogue, grade timing, which project is locked).
- A procedure with a real tool path (Adobe Podcast enhance, Resolve gallery grade, MCP vs clicking).
- A failure mode with the check that proves it worked.

Drop it if it is a single taste call, a file path that will not recur, a secret, a token, a personal address, a Tailscale IP, or a raw log.

## Model

Do not use Astra for this pass. Preferred pin, when that provider is actually logged in on the machine: `openai-api` / `gpt-5.6-sol` (Soul). This PC's mason profile is authenticated for Grok, not Soul, so masonpc's job is pinned to `xai-oauth` / `grok-4.7`. Another agent should pin Soul if `openai-api` works there, otherwise Grok. Never pin `gpt-6-astra`.

## Overnight job (copy this)

Workdir is the clone. Skill to load: `agent-learning-sync`. Schedule for masonpc: `15 2 * * *`. Deliver `local` so a quiet night does not ping Slack. The prompt is `templates/learnings/overnight-prompt.md`.

```bash
hermes cron create "15 2 * * *" --name "recursive-learning" \
  --skill agent-learning-sync \
  --workdir "C:/Users/mason/Assistant-test-bootstrap" \
  --model grok-4.7 --provider xai-oauth \
  --deliver local --continuity \
  --prompt-file templates/learnings/overnight-prompt.md
```

`hermes cron create` takes the prompt as an argument, not `--prompt-file`. Paste the file contents as the prompt. The cron tool inside a chat cannot set `--model`; use the CLI.

Replace the schedule, workdir, agent id, and model when installing on another computer. Write `agents/<id>.md` first.

## What the other agent does on day one

1. Clone the repo. Read this file, `docs/shared-learning.md`, and `AGENTS.md`.
2. Pick an agent id and the next free slot. Commit `agents/<id>.md`.
3. Install `skills/agent-learning-sync` into that machine's active Hermes profile (a clone is not an install).
4. Create the cron with the CLI, pinned off Astra.
5. Do not rewrite masonpc's inbox. Pull, then add your own pass under your id.

## Privacy

Same boundary as the rest of this repo. No `.env`, tokens, OAuth, memories, sessions, personal preferences, or private media. Lessons can name work volumes and tool steps. They cannot name credentials or home addresses.
