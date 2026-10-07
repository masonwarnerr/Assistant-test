# Operating a local work agent

## Everyday use

Use the same work profile from desktop and Slack. New conversations share persistent work memory and skills, not one literal transcript. Use a fresh session after changing identity/provider/context. `/reload-mcp` loads changed MCP connections into open sessions; version-specific reconciliation may also detect changes. Do not restart a gateway during a live job just to refresh tools.

Typical work requests:

- "Read the current Blender scene and report what is there; do not edit it."
- "Read this authorized Figma node and identify assets needed for the brief."
- "Check the current Resolve project and timeline without changing them."
- "Create this asset in a new local work file, verify it, and return the path."

State scope, input/output paths, allowed changes, and acceptance criteria. For editing/rendering, protect existing projects and accepted assets. Require approval for destructive operations and publishing.

## Service and app health

```bash
hermes gateway status
hermes mcp list
hermes mcp test blender
hermes mcp test davinci-resolve
hermes mcp test figma
hermes computer-use doctor
```

Server tests discover tools; also exercise the live read-only tool for the intended application/account. Slack visibility and bot naming are distinct from transport health. A CLI test is not a real human Slack turn. The computer must be awake, online, and able to run the application.

For a confirmed idle gateway that needs refreshing:

```bash
hermes gateway restart
hermes gateway status
```

Read the exact new startup logs and verify Slack reconnection. Do not report success solely because restart was requested.

## Consolidating accidental desktop/Slack profile splits

This is a same-machine migration, not permission to clone another computer's state.

1. Inventory both profiles, services, memories, skill packages, and OAuth ownership. Audit personal context before exposing it to a shared Slack bot.
2. Choose the target work-only profile. Preserve its cleaned skills, credentials, and existing state.
3. Stop and uninstall the old setup gateway with the old profile explicitly selected; obtain approval if active work might be interrupted.
4. Transfer only that bot's required Slack variables locally using the secure configuration helper or a local secret editor. Never print values. Remove the source token pair so two gateways cannot bind it. Validate prefixes and policy without exposing secrets.
5. Merge only reviewed unique work memories/skills. Do not overwrite richer target skills, transplant OAuth stores, or blindly merge SQLite databases. Keep old setup transcripts in a retired local archive outside active `profiles/` if history must be preserved. A retained archive is not active memory.
6. Preserve unrelated specialist profiles rather than losing their authentication. Configure the host gateway using the installed CLI. Do not make a temporary standalone workaround permanent.
7. Start the target gateway, verify the actual Slack identity and Socket Mode connection, compare desktop/Slack toolsets, and run a real read-only integration call.
8. Start fresh conversations; report what moved, what was archived, and what still requires service authorization.

Where appropriate, check `hermes gateway migrate --dry-run` before applying the installed host-wide service migration. Review its plan: it can affect multiple local profile services.

## Separation and privacy

Follow [privacy and separation](privacy-and-separation.md). Never assume no outbound SSH proves complete isolation or absence of a remote scheduled push. Never delete remote data while cleaning local copies. Work-only prompt rules are not hard access control; use a dedicated OS account/browser and enforceable filesystem/network limits when confidentiality matters.

## Troubleshooting by layer

| Symptom | First check |
|---|---|
| Slack search cannot find the intended name | Installed workspace Bot User identity, not gateway/model |
| Slack bot visible but silent | Gateway, Socket Mode, tokens, user policy, invite/mention, then model |
| Open access did not happen | Explicit Slack allow-all policy; blank allowlist is not open access |
| Model returns 404 | Actual model entitlement for the configured provider/key |
| Figma tools missing | Correct profile's OAuth login and real tool discovery |
| Blender tools exist but calls fail | Local addon listener, addon protocol, module/package shadowing |
| Native Resolve unavailable | Actual app distribution/version and ResolveMCP binary; do not generalize an older restriction |
| Python native extension import fails during uvx setup | Remove inherited PYTHONPATH/PYTHONHOME; do not blindly reinstall managed Hermes packages |
| Browser page exists but user sees nothing | Exact native Chrome window and automation target, not CDP state alone |

## Repository maintenance

Use a short-lived docs/work branch. Stage only the intended runbook/code files, run tests and `git diff --check`, inspect for private state, and publish with authenticated Git. Never force-push over someone else's work. Verify the remote ref matches the exact commit before claiming it was pushed.

Never commit local credentials, live configs, OAuth, browser data, memories, sessions, logs, generated manifests, or private asset indexes. Keep local receipts outside Git. Include installed version, OS, profile and redacted error when reporting failures, not token values.

## Pilot reporting and routing

GitHub is the pilot's only shared durable layer. Use the direct DaVinci path when the Resolve Mac is available and Lloyd's local Slack-connected Flex path for work assigned there. No Notion queue or HTTP relay is required.

Copy the report template to `reports/<task-id>.md` only after it is concise and redacted. Put coordinator-verified reusable lessons in `lessons/<slug>.md`; raw logs, screenshots, Slack transcripts, caches, media, and sensitive or noisy reports stay local/ignored. The required contract and promotion flow are in [execution reports](execution-reports.md) and [shared learning](shared-learning.md).

Outbound HTTPS/polling may work despite blocked inbound SSH, but IRU/network restrictions must be tested from the target Mac before any future HTTP design; do not infer feasibility from SSH reachability.
