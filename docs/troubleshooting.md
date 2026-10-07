# Troubleshooting the local work agent

Use this alongside [Slack setup](slack.md) and [privacy and separation](privacy-and-separation.md). Separate credential, saved Slack configuration, installed identity, local gateway, and privacy problems. Fixing one does not establish the others.

## Safe diagnostic rules

- Read the installed command help before using a flag or changing service topology.
- Identify the actual active home and owning gateway before restarting anything.
- Keep credentials in secure local prompts/environment storage. Do not paste token values or credential-bearing shell commands into chat.
- Validate Slack APIs with a local SDK/helper that loads credentials privately and reports assertions/error categories, not whole responses. Never put a token in a command-line `curl` example.
- Do not screenshot token screens or publish unredacted network captures, logs, or transcripts.
- At login, 2FA, workspace selection, or installation consent, have the human complete the step.
- After changing external state, reopen the exact saved target or query it again. A successful click is not proof.

Read-only starting checks:

```bash
hermes slack manifest --help
hermes gateway --help
hermes gateway list
hermes gateway status
```

## Slack symptoms

| Symptom | Check next | Verification |
|---|---|---|
| Starter “Demo App” remains; Socket Mode off | Replace the entire starter manifest with the Hermes-generated JSON, not just its name | Reopen saved App Manifest and Socket Mode settings |
| Authentication fails | Confirm `xoxb-` is the installed Bot User OAuth Token and `xapp-` is the app-level token with `connections:write`; Client/Signing Secrets are wrong credential classes | Rerun setup in the correct home; local `auth.test` succeeds and gateway connects |
| Correct-looking tokens, wrong bot/workspace | Token prefix is not identity proof; check the token source and active home | `auth.test`, followed by `users.info` for its exact returned user, matches the intended workspace/bot |
| Bot cannot receive DMs | Check Messages-tab permission, `message.im`, saved manifest, installation, user authorization, and gateway status | Authorized human sends a harmless 1:1 DM and gets a reply |
| DMs work, channels do not | Check `message.channels`/`message.groups`, `channels:history`/`groups:history`, reinstall requirements, bot invitation, mention, and any channel allowlist | Mention in an invited test channel produces the expected threaded reply |
| Group DM fails but 1:1 DM works | Check `message.mpim`, group-DM scopes, membership, mention/shared-surface controls, and channel restrictions | Test that specific group DM; do not infer from a 1:1 result |
| Replies follow an old thread without a new mention | Default human thread continuation may be enabled | Test top-level mention gating and intended strict/thread mention policy separately |
| Blank allowed-users response does not enable access | The tested plugin did not present a generic open-access prompt; blank is not consent | Restricted Member IDs or explicit `SLACK_ALLOW_ALL_USERS=true` is saved locally, owning gateway restarted, second-account policy test completed |
| Scheduled output goes elsewhere | Inspect the chosen home channel and per-job delivery target | Send an approved harmless test to the exact destination; home channel is not an authorization restriction |
| Bot-to-bot reply loop | Disable peer traffic unless needed; use `allow_bots: mentions`, not `all` | Each peer message itself mentions its target; passive acknowledgments do not trigger more turns |
| File attachment unreadable | Check generated file scopes, reinstall, bot membership, and file access | Test a benign work attachment, not a private file |
| Native slash command rejected inside a thread | Slack does not deliver native slash commands in thread replies | Consult installed-version docs for the `!command` alternative; test a harmless command |

Rotate credentials when exposed or invalid; do not rotate blindly to fix a missing event subscription. Reinstall after relevant scope/event changes when required. Preserve the desired Agent/Assistant view when refreshing the manifest.

## Gateway and surface mismatches

### Named gateway installation is refused

The tested host already used the gateway multiplexer. Default-profile consolidation removed the need for a separate named coordinator gateway. Inspect `hermes gateway list`, status, and installed help. Confirm desktop, CLI, and Slack are intended to use the same default home.

Do not repeat the historical standalone/`--force` bypass as a standard fix. Do not run migration/consolidation without checking other profiles and obtaining approval for affected services. A second physical computer instead gets its own independent local default home and a different Slack app/token pair.

### Setup appeared successful, but Slack still uses old settings

Check that setup ran in the intended real Terminal and active home, then identify the service that actually owns Slack. Inherited environment variables, another profile, or an existing OAuth token source may explain the mismatch. Inspect those privately without printing values. Restart the owning gateway using installed-version commands; read status back and send a fresh test message.

### Service installed, but availability after restart is unproven

Inspect install options and choose start-now and login/boot behavior explicitly. A macOS user service is not automatically a boot-time system service. Exercise the required login/restart scenario and verify Slack delivery afterward. Do not confuse a service installer exit code with verified continuous operation.

### Automation is looking at the wrong browser tab

In the tested investigation, browser CDP `page_info` identified an automation tab rather than the user's visible Chrome window. Before interacting, verify the exact browser target, URL, app/workspace, and—when the user means their visible window—the actual native window. Do not keep editing a background app copy based on an assumed match.

## Branding and installed identity

### Developer defaults changed, but Slack search still shows the old bot name

Developer App Home defaults and reinstall did not update the existing installed bot's searchable identity in the tested case. Open the workspace's **Installed Apps → app → App Details → Configuration → Bot User → Edit → Save Changes**. Reopen the saved settings and validate `auth.test` + `users.info` for the exact installed user. Then check Slack search.

Generic navigation:

```text
https://app.slack.com/apps-manage/<TEAM_ID>/integrations/installed
https://<workspace>.slack.com/marketplace/<APP_ID>-<slug>?tab=settings
```

`bots.info` may show a different app-oriented name. A stopped gateway is unrelated to whether Slack persisted its installed bot name.

### Icon upload/save did not persist — unresolved

The tested case still showed **Add App Icon** in Basic Information after repeated save attempts; API icon metadata remained at defaults. No proven fix is documented. Another upload or reinstall must not be presented as a known remedy.

For the next investigation, preserve the actual source image privately, record its dimensions/type, and collect the precise upload/crop error and sanitized network result. Verify the saved Basic Information page and supplementary `bots.info` icon metadata after any attempted change. Remove tokens/cookies/headers and private IDs from evidence; do not publish a raw HAR. Mark branding unresolved while reporting messaging tests independently.

## Privacy claims that need correction

| Claim | Supported replacement |
|---|---|
| “Personal skills removed, so the OS is sandboxed” | Work-only context is cleaner; terminal/desktop access remains unless enforced separately |
| “Fresh chat means no personal history exists” | Fresh chat drops loaded conversational context; historical stores may remain searchable |
| “No local sync process, so no remote agent can access this” | No sync/peer evidence was found within the inspected local scope; remote systems were not certified |
| “Origin metadata means the same agent is running elsewhere” | Metadata may describe a copied skill's source; investigate actual sync/peer configuration |
| “Home channel restricts users” | Home channel is a delivery destination; explicit user authorization is separate |
| “Separate user conversations isolate credentials” | Sessions can have separate histories while sharing local tools, skills, memory, credentials, and filesystem access |

If an audit excluded binary archives, cached history, or another computer, list those exclusions. Never fill missing evidence with an absolute claim.

## Closeout checklist

- [ ] Root cause category identified instead of changing unrelated settings.
- [ ] Saved Slack target or local service status read back after changes.
- [ ] Harmless end-to-end test exercised on the affected surface.
- [ ] Authorization and identity checked separately from connectivity.
- [ ] No credentials, private IDs, personal paths, or transcript excerpts published.
- [ ] Remaining blockers stated plainly, especially icon persistence and untested hard/remote isolation.

Authoritative reference: [Hermes Slack documentation](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack), together with installed CLI help. UI labels and service behavior may vary by release.
