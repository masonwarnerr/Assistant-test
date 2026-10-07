# Per-machine replication and acceptance checklist

Use this checklist on **each computer**, including computers that appear identical. This public repository distributes instructions, not a live agent image. Copying a configuration or discovering tools is not acceptance. Keep the completed machine record private and share only a sanitized status summary.

For application-specific commands and known traps, see [creative apps](creative-apps.md). For Slack authorization and Socket Mode prerequisites, see [Slack](slack.md). Use [operations](operations.md) for incident handling. Do not assume older specialist-machine templates require remote execution; the reference creative integrations run locally.

## What is shared versus machine-local

| Safe to distribute after review | Re-create privately on each computer |
|---|---|
| This repository's documentation, generic helper code, non-secret skill instructions, placeholder templates | Model/provider authorization; Slack app/bot credentials; Figma OAuth consent and tokens |
| Required application/package names and observed version notes | Installed executable paths, OS permission grants, local addon directories/listeners |
| Generic operator prompts and acceptance criteria | Private work-asset registries, file/node IDs, project/media locations, user/channel allowlists |
| Sanitized gate results and blockers | `.env`, OAuth stores, browser profiles, logs, screenshots, sessions, memories, live config |

Do not export/import a whole Hermes home or profile as the fleet bootstrap. Such archives can contain authorization and private state. Do not delete old profiles, overwrite their auth, or consolidate accounts without an explicit operator decision. Install the reviewed skills needed for this computer; a skill file is knowledge, not an installed application or authenticated integration.

## Operator contract

- One **work-only `default` profile** per reference-style computer, shared by its local Hermes Desktop and Slack gateway. A named profile is optional when genuinely needed, not an automatic specialist-install step.
- One distinct Slack app/bot identity and credential set per computer. Do not run multiple computers against the same Socket Mode app credentials and assume events route to the intended host.
- Work-only account authorization, approved local workspace, and minimal relevant toolsets. Personal accounts, private browser tabs, and unrelated profile state are out of scope.
- Native/local application tools first; GUI control is a local fallback. No public bridge ports, unrequested SSH, or assumed remote computer use.
- Humans complete consent, permission, password, and verification prompts through supported secure UI. Agents must never request secrets in chat or commit credentials.
- No production scene, design, timeline, or file editing just to pass readiness. Creative-task acceptance uses explicitly authorized scratch/duplicate assets.

## Gate A — scope, inventory, and private record

- [ ] Operator identifies this computer's role, OS, intended work account/domain, selected profile, and allowed local directories.
- [ ] Actual repository checkout is discovered; instructions do not assume a container path or another operator's home directory.
- [ ] Installed Hermes and application versions and executable paths are recorded locally, without publishing user paths or device/network identifiers.
- [ ] Existing profiles, addon layout, integrations, and running jobs are inspected before changes. Preserve unrelated state.
- [ ] Required skills are available to this profile. Read them before using an integration; distinguish skill installation from application/server installation.

Read-only starting commands (run in the intended profile):

```sh
hermes --version
hermes --help
hermes profile list
hermes config path
hermes doctor
hermes mcp list
hermes computer-use status
```

For a named profile, prefix commands using the installed `hermes -p <profile> ...` selector. Confirm Desktop's selected profile separately. Use `$HERMES_HOME` when it is set, or discover resolved paths through the CLI; do not hardcode `$HOME/.hermes` for a named profile. These commands can display private metadata: inspect locally and sanitize before sharing.

**Pass:** scope and existing state are known; operator authorizes only the needed changes. **Stop:** profile identity, work-account ownership, or existing-job safety is ambiguous.

## Gate B — model actually runs

- [ ] Complete approved model/provider setup privately with the installed `hermes setup` / `hermes model` flow as needed.
- [ ] Run a real model request, not just a credential-presence check:

```sh
hermes chat -q "Reply exactly: MODEL_OK. Do not call tools or change anything."
```

- [ ] Request succeeds in the intended profile; retain actual model/provider identity and sanitized result privately.
- [ ] Desktop uses that same work profile and can complete a separate harmless request.

**Pass:** real inference succeeded on both intended local surfaces. **Stop:** configured model name or stored credentials exist but requests fail. Do not require a particular vendor/model merely because the reference machine used it. Do not upload unredacted diagnostics to get help.

## Gate C — Slack identity, authorization, and incoming reply

- [ ] Set up a distinct Slack app and tokens for this computer using the [Slack runbook](slack.md) and current installed help.
- [ ] Store credentials only in this profile's private secret store/`.env`. Use `hermes config set` for non-secret settings; verify resolved profile paths before writes.
- [ ] Confirm bot/workspace identity privately, Socket Mode connected, app installed, required channel membership, operator allowlist, and intended bot-message policy.
- [ ] In an authorized private test channel, a **real authorized human** sends a unique message or @mention to this machine's bot and receives the matching reply from that bot.
- [ ] A denied/unapproved sender remains denied under the intended access policy; do not loosen allowlists globally to pass a test.
- [ ] Record the actual incoming-message/reply test separately from Slack authentication and socket connectivity.

Example human-origin test message:

> `<BOT_MENTION>` Reply with `SLACK_OK <OPERATOR_CHOSEN_NONCE>` and your non-sensitive machine role. Do not call application tools or change anything.

Choose a non-secret unique nonce and substitute the actual bot mention privately. Read back the exact reply in the same target conversation; an outbound `hermes send` or connected-socket log is not proof of incoming event handling or model response.

**Pass:** an actual authorized inbound message gets the expected bot reply. **Reference limit:** Slack reconnect/auth/socket status was observed, but the full human-origin incoming-message/reply test was not demonstrated in the reference setup session. It remains a per-machine gate, not an already-passed claim.

## Gate D — tool policy matches the surface

- [ ] Review installed `hermes tools` behavior and enable only the needed toolsets for CLI/Desktop and Slack.
- [ ] Verify relevant native/MCP tools are available in fresh sessions on each intended surface; do not assume CLI discovery proves gateway availability.
- [ ] After approved MCP changes, `/reload-mcp` in the applicable session or start a fresh session. Keep reload out of an active creative turn.
- [ ] If identity/provider/profile changes need a gateway restart, wait for jobs to finish and verify no active runs before restarting.
- [ ] From Slack, perform the authorized read-only app checks below, not merely ask the model whether it has tools.

**Pass:** live read-only tool execution works from every required surface under the correct work identity. **Stop:** one surface has stale tools, different authorization, or a different profile. A model saying “I can use Blender” without tool output is not evidence.

## Gate E — application layers, individually

Apply only the app rows needed by this computer. Mark an unused app `NOT REQUIRED`, not `PASS`.

| Integration | Required read-only proof | Failure that must not be counted as pass |
|---|---|---|
| Blender | Actual app running; correct addon module loaded; local loopback listener; live `get_addon_status`; protocol match; prompt/scene telemetry off; non-destructive scene read | Client/tool discovery while port refuses; stale shadowing addon package; saving a production scene to make auto-start work |
| Figma | Official OAuth registration; `whoami` verifies work identity privately; `get_metadata` succeeds on specifically authorized file/node | Tools listed without account proof; login to personal account; read success interpreted as edit permission |
| Resolve | Actual installed native executable; persisted Hermes registration; live `get_resolve_status` returns running status/version | Guessed bundle path; non-TTY confirmation canceled; tool list without live app check |
| Computer use | Doctor checks on this host; app-scoped capture verifies correct PID/window; separately approved reversible input with read-back when input is required | Permissions alone called full GUI success; browser CDP image called native window proof; local Mac check called remote-PC access |

Reference observations: Blender 5.2.1 LTS/addon 1.8/protocol 13; Figma 41 discovered tools plus live identity/metadata read; Resolve 21.1 with 14 discovered tools plus live status; macOS Accessibility and Screen Recording passed. Counts/versions are diagnostic context, not acceptance thresholds. Do not downgrade or upgrade solely to match them.

**Pass:** every required row has its own actual live proof and read-only scope. Keep returned private account/design/scene data out of public evidence.

## Gate F — persistence and local availability

- [ ] Reopen each required application at an operator-approved idle time and repeat the live app checks. Do not terminate jobs or reopen production files merely to test.
- [ ] Verify enabled Blender addon/preferences and actual bridge behavior after reopening; do not assume in-memory scene flags were persisted by saving user preferences.
- [ ] Verify the gateway background service is installed for the intended work profile and remains connected after an approved restart.
- [ ] Verify service behavior after the next normal login, if unattended availability is required. Distinguish “configured start on login” from “observed after login.”
- [ ] Record power/network limitations. Sleep, closed lid, logout, shutdown, or loss of network can make the computer unavailable; start-on-login does not solve these conditions.

The reference macOS launchd installation used:

```sh
# State-changing: operator approval and idle-machine check first.
hermes gateway install --start-now --start-on-login
hermes gateway status
```

These flags were present in the installed CLI and the reference service install/reconnect succeeded. Check `hermes gateway install --help` on the target OS/version. Do not copy macOS launchd assumptions to Windows or Linux, run duplicate gateways, or change sleep-prevention settings without approval. No lid-closed availability or sleep-prevention hardware was tested in the reference setup.

**Pass:** required lifecycle behavior is observed on this computer. **Partial:** service is installed but post-login/app-reopen behavior is not yet tested; document the pending test rather than calling it complete.

## Gate G — one real bounded task and usable artifact

Setup is not task readiness. Choose a single small task in an authorized scratch directory/duplicate project and run it from the surface operators will use.

- [ ] Brief names exact allowed inputs/targets, output directory, dimensions/duration/format as applicable, and forbidden side effects.
- [ ] Agent uses actual application tools, not synthesized status or fabricated assets.
- [ ] Output files exist, have usable content, and can be reopened with the relevant application.
- [ ] Render/image/video is visually inspected; duration/audio/format are checked when applicable. Exit zero alone is not QA.
- [ ] Any application write is verified by reading back the exact target; no production file was changed outside scope.
- [ ] If Slack is the operating surface, the task is initiated by a real authorized Slack message and the final result appears in that same task conversation.
- [ ] Operator can receive/open the artifact through an approved delivery route. A local file path that exists only on another computer is not delivery.
- [ ] No automatic posting/publishing, extra paid generation, or external sharing occurs without explicit approval.

Candidate tasks (choose only after operator authorizes the scratch asset):

- **Blender:** create a simple original object in a disposable scene, save `.blend`, render a small still, reopen the file and inspect the still.
- **Resolve:** in a named disposable project, use authorized non-sensitive media, export a short clip, then inspect playback and format. Retrieve current scripting API information before scripting.
- **Figma:** read an authorized test frame and produce an approved local implementation/reference artifact, or perform a narrowly approved scratch-file edit only if current tools and account permissions support it. Do not assume remote MCP read access implies editing support.
- **GUI:** perform one reversible action in an operator-approved test window and verify exact window state; do not use account/permission dialogs as test targets.

**Pass:** operator accepts a usable artifact from the actual intended surface. **Reference limit:** the earlier app connectivity tests did not demonstrate this full creative-task/Slack-delivery gate.

## Gate H — sanitized handoff and recovery

- [ ] Machine record names passed, failed, pending, and not-required gates individually.
- [ ] Recovery notes identify a safe backup location privately, exact redacted failure, and next bounded verification step.
- [ ] Public changes contain only generic docs/code/placeholders; inspect the diff for home paths, emails, device IPs, Slack identifiers, Figma IDs, tokens, private screenshots, and logs.
- [ ] Preserve unrelated profiles and work-asset registries. Revoke/rotate exposed authorization instead of pretending Git deletion erases exposure.
- [ ] Independent agent receives this repository and approved private inputs, not a copy of the first machine's live state.

A private per-machine worksheet:

```text
Machine role: <ROLE>
OS / Hermes version: <OBSERVED>
Active work profile: <PROFILE>
CLI / Desktop / gateway profile alignment: <PASS|FAIL|PENDING>
Model real request: <PASS|FAIL|PENDING>
Slack auth/socket: <PASS|FAIL|PENDING>
Slack authorized human incoming + matching reply: <PASS|FAIL|PENDING>
Tools CLI/Desktop / Slack live execution: <STATUS EACH>
Blender / Figma / Resolve / GUI required: <YES|NO EACH>
Each required app live-read gate: <STATUS + SANITIZED OBSERVATION>
App reopen / gateway restart / next login: <STATUS EACH>
Bounded task and usable artifact / delivery: <STATUS EACH>
Private evidence location: <LOCAL PRIVATE LOCATION; DO NOT COMMIT>
Known blocker / next operator action: <REDACTED>
```

A public handoff should omit private evidence locations and machine identifiers. Do not publish raw `hermes dump`, `config show`, profile exports, `.env`, OAuth stores, or logs as proof.

## Copy/paste operator prompts

Replace placeholders privately. These prompts authorize bounded work; they do not replace secure consent dialogs or broader approval policies.

### Fresh-computer bootstrap

> Read this repository's README, `docs/creative-apps.md`, and `docs/replication-checklist.md`, plus relevant installed skills. Work only on this computer and the intended work-only profile. First discover the actual checkout, OS, installed commands, existing profiles/apps/addons, and active jobs using read-only checks. Do not copy another computer's authorization or overwrite unrelated profiles. Report the exact missing prerequisites and request approval before installing downloaded code, changing app preferences, or registering servers. Keep secrets and private identifiers out of chat and Git. Then perform each approved setup and live-read gate, reporting actual outputs and unproven gates separately. Do not claim readiness until the bounded real task and intended delivery surface pass.

### Shared local Desktop and Slack profile

> Align this computer's Desktop, CLI, and Slack gateway with the intended work-only profile. Verify resolved config paths and actual selected identities privately. Use this computer's unique Slack app credentials, not another host's tokens. Preserve unrelated profiles and authorization. Verify a real model request, then ask the operator to send a unique authorized Slack message and read back the matching reply. Do not claim Slack-task readiness from authentication or connected-socket status alone; do not restart a gateway with active work.

### Creative connectivity only

> Follow `docs/creative-apps.md` for `<REQUIRED_APPS>`. Discover installed executables and current schemas; review configuration before any approved changes. Prove Blender with live addon/protocol status, Figma with work identity plus authorized metadata read, Resolve with live status, and GUI with local health plus the exact app-window capture as applicable. No production scene/design/timeline edits, startup-scene saves, external sharing, remote workers, or public ports. Return a sanitized gate table with actual read-only results, failures, and unresolved lifecycle/task gates.

### Bounded task acceptance

> On `<INTENDED_SURFACE>`, complete `<SMALL_TASK>` using only `<AUTHORIZED_INPUTS_OR_SCRATCH_TARGET>` and write deliverables to `<APPROVED_LOCAL_OUTPUT_DIR>`. Required output/QA: `<FORMAT_AND_ACCEPTANCE>`. No production edits, paid extras, publishing, external messages, or permissions changes. Inspect live tool schemas and API documentation before coding. Verify exact write targets, reopen the project, and inspect the artifact visually or through playback as relevant. Deliver through `<APPROVED_DELIVERY_ROUTE>` and confirm the operator can open it. Report actual evidence, not a hypothetical result.

### Blocked machine

> Stop state-changing work. Collect installed version, selected profile, failing command/tool, exact redacted error, and last successful gate using read-only checks. Distinguish missing app, missing skill, server not configured, tools not discovered, app/account not connected, and task artifact not produced. Do not repair Hermes's managed Python with pip, delete addon directories, loosen Slack allowlists, copy OAuth stores, or retry speculative GUI coordinates. Propose the smallest reversible fix and its verification, then wait for approval if that fix changes scope.

## Readiness vocabulary

Use these terms precisely:

- **Instructions present:** relevant repository docs/skills are available.
- **Dependencies installed:** required executable/addon exists locally.
- **Configured:** server/profile settings were written and read back.
- **Discovered:** MCP tool schemas were listed.
- **Live-connected:** an actual app/account read-only call succeeded.
- **Surface-verified:** that live call worked from the intended CLI/Desktop/Slack surface.
- **Task-verified:** a bounded real task produced an inspected, reopenable artifact.
- **Operationally accepted:** required lifecycle, access control, delivery, and operator sign-off passed.

Never substitute one level for the next. A skipped test is `PENDING` or `NOT REQUIRED`, not success.
