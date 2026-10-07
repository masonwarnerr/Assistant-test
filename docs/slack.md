# Slack: one local work agent per computer

This is a replication playbook for the tested local setup, not a promise that every Hermes release has identical wizard screens. Check the installed CLI help and the [official Slack guide](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack) before adapting commands. The tested path uses Slack Bolt Socket Mode: outbound WebSockets, no public HTTP endpoint, one bot token and one app-level token per computer.

## 1. Choose the topology before creating credentials

- Run **one work-only default Hermes profile per physical computer**. On that computer, desktop, CLI, and Slack target the same Hermes home. Creating a separate coordinator profile just for Slack is unnecessary.
- Sharing a Hermes home means sharing its configured skills, memory, credentials, and persistent state. It does **not** mean every surface shares one live conversation or transcript.
- Give each computer its **own Slack app and its own token pair**. Multiple apps may be installed in the same Slack workspace. Do not run two computer gateways using the same app's tokens; this is not the tested replication model and can cause competing Socket Mode delivery.
- Keep machine state independent. Do not copy another computer's `.env`, OAuth stores, sessions, memories, or user assets to bootstrap the next computer.
- Use neutral app names such as `<Agent name>` and `<Agent name - device role>`. Record the computer-to-app mapping in a private operations inventory, not a public document containing real workspace identifiers.

The tested CLI uses a per-host gateway multiplexer. A separate named-profile gateway installation was refused. A temporary `gateway.standalone` / `--force` workaround was later removed during consolidation; **it is not the recommended recipe**. Start with the default profile and inspect existing host gateway ownership instead of adding another service.

Before opening Slack to other users, complete [privacy and separation](privacy-and-separation.md). An open Slack bot with terminal/desktop tools grants access to a capable local agent; it is not just a chat interface.

## 2. Confirm the active home and installed commands

Use a real local Terminal for interactive setup. Confirm the intended default profile, shell launch environment, and desktop's selected local home. An explicit `HERMES_HOME` override can change the target even when a command looks unqualified. Resolve the actual home before any file edit; `~/.hermes` is the normal default, not a universal path.

Read-only command discovery:

```bash
hermes --help
hermes profile list
hermes slack manifest --help
hermes gateway --help
hermes gateway install --help
hermes gateway list
hermes gateway status
```

Do not dump `.env`, `auth.json`, token files, or credential-bearing service definitions into chat to prove the path. Check locations and selected nonsecret settings locally. If the installed commands differ, consult the matching official documentation rather than guessing flags.

## 3. Generate and apply the complete manifest

For a **new** Slack app:

```bash
hermes slack manifest --agent-view --write --name "<Agent name>"
```

Replace the name placeholder before running. With no path supplied to `--write`, this writes `slack-manifest.json` in the active Hermes home. Read the generated file locally and paste its complete JSON into Slack's manifest editor. Do not publish a manifest without reviewing any locally customized descriptions, URLs, or identifiers.

1. Open [Slack app management](https://api.slack.com/apps).
2. Choose **Create New App → From an app manifest**, select the intended workspace, and paste the generated JSON.
3. Review, create, then reopen the saved **App Manifest** page to verify what actually persisted.

Slack may also offer an **AI agent** creation wizard or a starter/from-scratch app. Those are alternative entry paths, **not** a required “AI agent, then manifest” sequence. If a starter app already exists, open its manifest editor and replace the entire starter manifest with the Hermes-generated manifest. A default “Demo App” JSON with `socket_mode_enabled: false` is not configured just because its display name changed.

New apps use `--agent-view`. Slack's Agent-view migration is irreversible; do not apply it casually to an existing legacy Assistant-view app. For an existing app, inspect its current view and choose the documented migration or legacy-compatible refresh deliberately. Preserve the intended name and view flags when regenerating a manifest after upgrades.

### Saved-manifest verification

Compare the saved manifest to the locally generated one. At minimum, confirm:

| Area | Required checks |
|---|---|
| Socket Mode | `settings.socket_mode_enabled` is `true`; Slack's Socket Mode UI also shows enabled |
| Sending and mentions | Bot scopes include `chat:write` and `app_mentions:read` |
| Public/private history | `channels:history` and `groups:history` are present |
| DMs | `im:history`, `im:read`, `im:write`; group-DM history/read scopes if using group DMs |
| Other features | Keep generated user lookup, file, command, and Agent-view scopes/events; do not reduce the manifest to this abbreviated checklist |
| Bot events | `message.im`, `message.channels`, `message.groups`, `message.mpim`, and `app_mention`, plus the generated Agent-view events |
| App Home | Messages tab permits messages; if Slack reports messaging is turned off, check the App Home toggles |

An editor paste or a Save click is not verification. Reopen the saved page. After scope/event changes, complete any requested reinstall/authorization and test message delivery again.

## 4. Obtain the two different tokens

| Credential | Slack UI path | Expected prefix | Hermes variable |
|---|---|---|---|
| App-level Socket Mode token | **Basic Information → App-Level Tokens → Generate Token and Scopes**; select `connections:write` | `xapp-` | `SLACK_APP_TOKEN` |
| Installed bot OAuth token | **Install App** or **OAuth & Permissions → Install to Workspace**; review consent and click **Allow** | `xoxb-` | `SLACK_BOT_TOKEN` |

Enable Socket Mode if not already enabled. Some Slack screens offer app-level token generation during that step; Basic Information is the route to find it again.

**Client Secret and Signing Secret are neither of these tokens.** A user OAuth token is not the bot token. Prefix checks identify obvious mistakes, but do not prove the tokens belong to the correct app/workspace; validate connectivity and installed identity later.

Human-only checkpoints:

- A human completes login, 2FA, workspace selection, and installation consent. Automation stops at those boundaries rather than guessing credentials or granting permissions unattended.
- Use a secure local prompt/vault workflow to transfer tokens. Never paste them into agent chat, a Git command, a shell command line, an issue, or this repository.
- Never take or publish screenshots of token screens. If DOM inspection is needed, inspect presence/type without returning secret text. Secret redaction is defense in depth, not permission to collect raw secrets.

## 5. Configure Hermes in the same home

Run in the intended default-profile Terminal:

```bash
hermes gateway setup
```

Select Slack and securely enter the bot and app-level tokens in their corresponding prompts. Setup saves credentials in the active home's local `.env`. If a wrong token was entered, rerun setup to replace it; do not keep debugging with the wrong credential class.

Restrict the environment file to the local account (normally mode `600` on Unix-like systems). Do not store real tokens in `config.yaml`, checked-in examples, or public troubleshooting output. Also inspect inherited shell/service variables and any existing Slack OAuth token store privately if credentials appear to come from an unexpected source.

### Choose authorization explicitly

**Restricted access is the recommended starting point.** Obtain each human's Slack Member ID via **profile → more → Copy member ID**. Put the permitted `U…` IDs in `SLACK_ALLOWED_USERS` through the setup flow. Use member IDs, not display names, bot tokens, or app tokens. Test with an authorized human and a second, unauthorized test account; authorization is not proven by the owner's successful message alone.

**Intentional open access:** the tested installed Slack plugin did **not** show a generic open-access question after the allowed-users answer was left blank. Never infer that blank means open. Explicitly save `SLACK_ALLOW_ALL_USERS=true` in the active profile's local environment through the wizard **if that version supports it**, or through a secure local environment editor/helper otherwise. Do not print the rest of `.env` while checking that this nonsecret flag persisted. Restart the actual owning gateway after changes and test the resulting policy. If that version lacks the flag or its behavior differs, stop and consult its implementation/docs; do not claim open access is enabled.

Open access includes guests or other users who can reach the bot. In the tested setup, it was accepted after personal-context cleanup, **not** after creation of an OS sandbox. Read the privacy document before making the same trade-off. Member authorization, bot-message policy, and channel routing are separate controls.

`SLACK_HOME_CHANNEL` is an optional destination for scheduled/proactive messages. It is **not an authorization allowlist**. A chosen home channel does not prevent DMs or requests elsewhere.

## 6. Start the actual host gateway

For initial foreground testing, use the command supported by the installed CLI:

```bash
hermes gateway
```

The inspected CLI also exposes `hermes gateway run`. Do not start a competing foreground instance while a service already owns the connection. Inspect `hermes gateway list` and `hermes gateway status` first.

Once foreground delivery is proven, inspect service options and install the default-profile service if one does not already serve it:

```bash
hermes gateway install --help
hermes gateway install
hermes gateway status
```

Explicitly decide whether the service should start now and on login using the options shown by that release. On macOS, a user service normally follows account login; do not describe it as a guaranteed boot-time system service. Linux has different user/system-service choices. A live process or successful install alone does not establish automatic restart after reboot/login: test the lifecycle you require.

Use `hermes gateway restart` for an existing owning service after configuration changes, then inspect status and send a test message. If installation says the host multiplexer already serves a profile, diagnose existing service ownership. Do not turn on `gateway.standalone`, use `--force`, or create a named coordinator simply to bypass the warning. Consolidation/migration can affect other local profiles: inventory them and obtain approval before changing their services.

## 7. Verify installation, identity, and routing separately

Keep API validation local and nonprinting: load credentials from the active local environment into an SDK/helper, call Slack's `auth.test`, then call `users.info` for **the exact user ID returned by `auth.test`**. Assert success, expected workspace, bot status, `name`, `real_name`, and any display-name field relevant to the desired identity. Report only pass/fail and nonsecret error categories publicly; do not print token values, complete API responses, or real workspace/member IDs.

`bots.info` may report an app-oriented name that differs from the installed bot user's identity. It is useful supplementary evidence, not a substitute for `auth.test` plus `users.info`.

Manual delivery checks:

1. Find the installed bot in Slack; do not assume the developer app name is its searchable username.
2. Send a harmless 1:1 DM, such as “Reply with the device role; do not read files.” Verify the correct computer's gateway handled it.
3. Invite the **actual installed bot** into each intended channel using Slack's invitation UI or `/invite @<installed bot name>`.
4. Start a channel conversation with an explicit @mention. Verify the reply arrives in the intended thread.
5. Reply in the active thread and confirm the expected continuation behavior. By default, human follow-ups in an engaged thread need not repeat the mention; a fresh top-level channel message does.
6. Test authorization with another account under the chosen policy. Group DMs are shared surfaces, not equivalent to private 1:1 DMs; test them separately if used.
7. Confirm CLI and desktop still use the same local home. Do not claim Slack shares the current desktop conversation just because the home matches.

Keep bot-to-bot traffic disabled by default (`allow_bots: none`). If peer collaboration is deliberately enabled, use `platforms.slack.extra.allow_bots: mentions` via the documented configuration interface and require each peer message itself to mention its target. An earlier mention in thread history is insufficient. Avoid `all`, which can create response loops. This is optional coordination, not a prerequisite for independent per-computer bots.

## 8. Correct the installed workspace bot name

Changing developer **App Home** defaults and reinstalling did **not** update the existing installed bot's searchable username or `real_name` in the tested setup. The working correction was in the workspace's installed-app settings:

1. Open **Installed Apps**, select the app, then **App Details → Configuration**.
2. Scroll to **Bot User → Edit**.
3. Set the intended workspace bot identity and click **Save Changes**.
4. Reopen the page and repeat `auth.test` + `users.info` validation for the same installed bot user. Search it in Slack as a separate user-facing check.

Generic navigation URLs, with placeholders only:

```text
https://app.slack.com/apps-manage/<TEAM_ID>/integrations/installed
https://<workspace>.slack.com/marketplace/<APP_ID>-<slug>?tab=settings
```

Navigate from the workspace UI if the slug or route is unknown; do not invent a real app URL. Developer app name, Bot User defaults, installed bot identity, and app icon are distinct state. A stopped gateway does not explain a persisted Slack name mismatch.

### App icon: unresolved

Repeated icon save attempts did not persist in the tested setup: Basic Information still showed **Add App Icon**, and API icon metadata remained at defaults. Do not describe the icon as fixed, or promise that another upload or reinstall is a proven fix. A useful next investigation needs the exact source image, upload/crop UI error, and sanitized network response evidence. Capture only noncredential screens and do not publish an unredacted HAR. Messaging can be verified while branding remains unresolved.

## Acceptance checklist

- [ ] One work-only default home on this computer; desktop/CLI/Slack target it.
- [ ] Unique Slack app and token pair assigned to this computer.
- [ ] Complete generated manifest persisted; Socket Mode, scopes, events, and Messages tab verified.
- [ ] Correct `xapp-` and `xoxb-` credential classes saved locally without publication.
- [ ] Restricted or explicitly open authorization chosen and tested; blank allowlist not treated as consent.
- [ ] Owning gateway identified; DM, channel mention, thread, and service lifecycle tested.
- [ ] Installed workspace bot identity verified, independently of developer defaults.
- [ ] Privacy limitations accepted; no claim of an OS sandbox or uninspected remote isolation.
- [ ] Any icon persistence failure remains explicitly unresolved.

See [troubleshooting](troubleshooting.md) for symptom-based checks and [privacy and separation](privacy-and-separation.md) for cleanup, evidence boundaries, and stronger isolation.
