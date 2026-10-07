# Local agent pilot: one shared profile

## 1. Choose the boundary before creating anything

For one independent agent per computer, use that computer's work-only **default profile** for desktop, CLI, model credentials, skills, memory, MCP connections, and Slack. A Slack bot is a messaging identity, not a reason to create another profile. Conversations are separate threads even when persistent memory and tools are shared.

Use a named profile only for a genuinely different role or security/data boundary. Profiles separate agent state, not filesystem or browser permissions. For strong privacy separation, use a dedicated work OS account and browser profile. Read [privacy and separation](privacy-and-separation.md).

On an existing installation, identify the current home, profile, applications, connections, and background services. Do not overwrite existing credentials or merge private material into a public/shared work bot.

```bash
hermes --version
hermes profile list
hermes gateway status
hermes mcp list
hermes doctor
```

## 2. Install and configure a working model

Follow the [current installation instructions](https://hermes-agent.nousresearch.com/docs/getting-started/installation) for the actual OS. Hermes is already installed when these commands work; do not reinstall reflexively.

```bash
hermes model
```

Enter credentials locally in the wizard. For an ordinary OpenAI API key, use `https://api.openai.com/v1`; choose a model actually available to that key. An attractive picker entry or a working API key does not guarantee access to a particular model. A 404 "model does not exist or you do not have access" is a model/access issue, not a reason to rotate the key.

```bash
hermes chat --oneshot -Q -q "Do not use tools or edit files. Reply exactly: MODEL_OK"
```

Pass only when the real output returns the requested token. Record errors honestly.

## 3. Make the repository usable context

Clone this repository into a permanent local project directory, not an expiring scratch folder. Use `AGENTS.md` as the setup brief. Read the relevant runbook before acting. Do not copy a full Hermes home, another machine's private memory, or OAuth token stores.

Place a reviewed work-only identity in the active home's `SOUL.md` (use [the work template](../templates/SOUL.work.md)). Install curated reusable skills into the active home's `skills/`; a clone alone does not install them. Never overwrite a richer installed `hermes-agent` skill with the repository's partial hub copy. Keep work asset indexes local and access-controlled.

Non-secret settings use the CLI:

```bash
hermes config set terminal.backend local
hermes config set security.redact_secrets true
hermes config set approvals.mode smart
```

Set `terminal.cwd` to the actual authorized project path via `hermes config set`; never assume a copied machine path is valid. Provider and Slack credentials stay in the active profile's `.env`; OAuth uses the profile's token store.

## 4. Local acceptance

Ask the agent to identify its profile, read this repository's README, and inspect an authorized local work file without modifying it. Verify the actual tool results. A harmless model reply is not proof of file or computer-control capability.

For application access, follow [creative apps](creative-apps.md), test the actual live read-only tools, and distinguish installed skills, configured server, discovered tools, live app/account access, and a completed artifact.

## 5. Add Slack to this same profile

Follow [Slack setup](slack.md). Generate the manifest using the final agent name **before installation**. Configure fresh tokens for this computer in this same profile. Start the host gateway, not a second process for the same bot.

Only after model, local tools, Slack transport, and a real human Slack turn pass should the agent be called ready. Keep private logs outside Git. Add the [optional task board](notion-task-board.md) or [other machines](second-device-rollout.md) only after this local loop works.

## 6. Fleet pilot execution paths

Use the direct DaVinci path when the Resolve Mac is available. Otherwise, assign suitable local work to Lloyd's Slack-connected Flex worker. GitHub is the only shared durable layer: no Notion queue or HTTP relay is required for this pilot.

For every routed task, assign a stable task ID and complete the [worker execution-report template](../templates/reports/worker-execution-report.md). The coordinator must verify the artifact and exact observations before committing a concise, redacted report or promoting a lesson.
