# Local creative applications: setup and proof

This is a local workstation runbook, not a remote render-farm requirement. Hermes can use native MCP servers and local GUI control on the same computer as Blender, Figma, and DaVinci Resolve. Install only the applications that computer needs. Do not dispatch another computer, open public ports, or change production projects just to prove connectivity.

Pair this page with the [replication checklist](replication-checklist.md). Authenticate and configure the intended **work-only profile** first. The reference setup uses one work-only `default` profile for both Desktop and Slack on each computer; it does not require a separate creative profile. Keep unrelated profiles and their authorization intact.

## Evidence and limits

The following reference-workstation results were reported by the setup operator. They are observations, not minimum versions or guarantees for another installation:

| Component | Observed result | What it does not prove |
|---|---|---|
| Hermes | `v0.21.5+8508.g0e37a43` (2026.9.24 build) | Every future CLI has the same flags. |
| Blender | Blender 5.2.1 LTS; live `get_addon_status` reported addon 1.8, protocol 13 matching the client, prompt/scene telemetry off | A rendered deliverable, or successful restart on every machine. |
| Figma | Official remote OAuth MCP; 41 tools discovered; native `whoami` confirmed a work-domain account; authorized metadata read returned the requested node | Edit access to every file, or a finished design task. |
| Resolve | Bundled native `ResolveMCP` stdio server; 14 tools discovered; live `get_resolve_status` returned running `true`, version 21.1 | Timeline edits, render/export success, or that all distributions bundle the server. |
| Computer use | Local macOS doctor confirmed Accessibility and Screen Recording | Correct targeting of every dialog/window, or remote desktop control. |

Tool counts are snapshots and can change. A listed tool is not proof of a live app connection. No end-to-end Slack creative-task artifact was demonstrated in this setup session.

## Before installing or repairing anything

Run these read-only discovery commands in the intended profile:

```sh
hermes --version
hermes profile list
hermes config path
hermes mcp --help
hermes mcp add --help
hermes mcp list
hermes computer-use --help
```

Check the selected Desktop profile and the gateway profile too; a sticky CLI default is not proof of either. For a named profile, use the installed CLI's `hermes -p <profile> ...` selector consistently. Do not run setup under one profile and test tools under another.

For the examples below, set local shell variables yourself:

- `REPO_DIR`: this repository's actual local checkout, e.g. `$HOME/Projects/Assistant-test`.
- `UVX_BIN`: the actual absolute `uvx` executable path.
- `BLENDER_BIN`: the actual Blender executable, not just its containing `.app` directory.
- `ADDONS_DIR`: the user addon directory for the installed Blender major/minor version.
- `RESOLVE_MCP`: the installed native Resolve MCP executable, if present.

These are example shell variables, not secrets or Hermes configuration keys. Discover paths on each machine. Do not copy the reference operator's home directory. Examples use POSIX shells; on Windows use native paths and the installed shell's syntax, and validate the entire connection again. WSL is not automatically the Windows interactive GUI desktop.

Use `hermes config set KEY VALUE` for ordinary Hermes settings and the `hermes mcp` CLI for registrations; do not hand-edit live YAML. Credentials belong only in the active profile's private credential store or `.env`, never this checkout. Do not copy OAuth stores, browser profiles, or another computer's Slack tokens.

## Blender: match the client, addon, and live bridge

### Discover the existing installation

1. Confirm the Blender executable and application version locally.
2. Check which addon Blender actually loads, including its module path. A pre-existing `blender_mcp/__init__.py` package can shadow a freshly installed loose `blender_mcp.py` file.
3. Record the addon/client protocol versions and current bridge settings privately. Back up existing addon source before replacing it. Do not delete an entire addons directory or unrelated addons.
4. Find `uvx`. The reference computer had an executable at `$HOME/.hermes/bin/uvx`, but that is a fallback to inspect, not a fleet-wide assumption:

```sh
command -v uvx
# If absent, inspect your installed Hermes/uv locations before proceeding.
# Set UVX_BIN to the verified absolute executable path.
```

The previous `blender-mcp` client discovered tools even while the bridge refused connections on port 9876. The working reference path switched the client to **`mcp-for-blender`** and updated the addon to match. Do not treat compatibility-client discovery as successful setup.

### Install/update the addon with approval

The reference installation used this package command with a version-specific user directory:

```sh
# macOS example only: replace 5.2 with your installed Blender major/minor.
ADDONS_DIR="$HOME/Library/Application Support/Blender/5.2/scripts/addons"
env -u PYTHONPATH -u PYTHONHOME "$UVX_BIN" mcp-for-blender install-addon --addons-dir "$ADDONS_DIR"
```

This writes addon files and can download package code; review/approve it first. For other operating systems, obtain the user addon directory from the installed Blender preferences/runtime rather than reusing the macOS path.

**Known layout trap:** the installer wrote `blender_mcp.py`, but an old `blender_mcp/__init__.py` package already existed and won module resolution. On the reference machine, that package contained only its initializer and cache. The repair backed up the old source, copied the fresh installer source into the package initializer, verified hashes, and removed only the duplicate loose module after verification. This is not permission to overwrite a richer package on another machine.

The repository helper [scripts/fix_blender_addon_layout.py](../scripts/fix_blender_addon_layout.py) is intended to inspect/repair this shadowing case with backups and verification. Inspect its actual usage and implementation before invoking it. Its tests and behavior must be validated separately; the application observations above do not certify the helper. Stop for manual review if layout/content differs from the known simple case.

### Enable the bridge in Blender, not in host Python

In the running local Blender, enable the `blender_mcp` addon and start its bridge. The following operations were exercised by a Blender Python launcher on the reference installation. They are **Blender-runtime Python**, not commands for Hermes's Python environment:

```python
import bpy
bpy.ops.preferences.addon_enable(module='blender_mcp')
prefs = bpy.context.preferences.addons['blender_mcp'].preferences
prefs.telemetry_consent = False
bpy.context.scene.blendermcp_port = 9876
bpy.context.scene.blendermcp_auto_start_server = True
bpy.ops.blendermcp.start_server()
bpy.ops.wm.save_userpref()
```

Inspect the installed addon's properties first because releases can change these names. Do not start a second bridge if one is already running. The bridge must listen on local loopback only; verify the actual listener address, not merely the client host setting. Do not bind `0.0.0.0`, forward the port, or open a public firewall rule.

The helper [scripts/enable_blender_bridge.py](../scripts/enable_blender_bridge.py) is intended to perform the Blender-runtime enabling/startup operations. Read its usage before choosing a Blender `--python` invocation or another execution route. Helper-script validation is separate from the manually exercised setup.

Save **user preferences**, not the startup scene or the user's current `.blend`. The reference saved addon enablement/preferences; addon registration/load handlers support auto-start. Scene properties set during the session are not proven to survive every new scene merely because preferences were saved. Reopen Blender and run a live status call before declaring unattended startup ready. Never save a production scene just to persist bridge configuration.

Prompt/scene telemetry consent was set to false. This is not a promise of zero data collection: minimal nonsensitive anonymous usage may still exist, and model/tool services have their own data policies.

### Register the local client with Hermes

Once the addon is current and the bridge is live, register the reviewed client in an **interactive Terminal**:

```sh
hermes mcp add blender --command "$UVX_BIN" \
  --env BLENDER_HOST=127.0.0.1 BLENDER_PORT=9876 \
  --args mcp-for-blender
hermes mcp list
hermes mcp test blender
```

`--args` must be last: it consumes the remaining arguments. Discovery-first `mcp add` can ask which tools to enable; complete the confirmation and then read the registration back. An EOF in a noninteractive process can cancel without saving. Do not assume a discovery printout means the server was registered.

**Python contamination trap:** standalone `uvx` run from a Hermes terminal environment imported Python 3.14 libraries into a Python 3.12 package environment and failed on `pydantic_core`. For standalone package commands, `env -u PYTHONPATH -u PYTHONHOME ...` avoided the inherited contamination. Do not fix this by pip-installing packages into Hermes's managed runtime. The registered MCP subprocess has its own environment handling; test that path independently instead of assuming the standalone shell failure applies to it.

### Blender acceptance prompt

> Use the registered local Blender MCP. Discover the current schema and call `get_addon_status`. Report the actual Blender, addon, client/protocol versions, bridge connection status, and prompt/scene telemetry setting. Read the current scene non-destructively using an available scene-inspection tool. Do not execute scene-changing Python, save a scene/startup file, download assets, or start remote workers. If the bridge is unavailable or versions mismatch, stop and report the exact redacted error.

Pass only when the live app responds and protocols match. For a production-task gate, use an explicitly authorized disposable scene, save the requested `.blend` and render, reopen/inspect them, and visually QA the output. That task gate is additional work, not something this setup session already proved.

## Figma: official remote MCP and per-machine OAuth

Use the Hermes catalog rather than copying another client's configuration:

```sh
hermes mcp install figma
# Complete authentication interactively on this same computer:
hermes mcp login figma
hermes mcp list
hermes mcp test figma
```

The reference catalog registration saved the official endpoint **`https://mcp.figma.com/mcp`** with OAuth even when the initial non-TTY authentication probe failed. Check `mcp list` before re-adding duplicate registrations. Complete `login` in a real interactive Terminal and browser, choose the authorized work account, approve the requested consent yourself, and let the localhost callback finish on the computer running Hermes. Do not paste callback URLs or tokens into chat or move tokens between computers.

The observed catalog OAuth configuration used `client_name: ClaudeCode` for Figma's dynamic-client-registration compatibility gate. The agent actually running was Hermes. Do not mislabel the agent or manually create Codex TOML, copy bearer headers, or invent a replacement client-name override. If a future catalog changes this, use its current supported flow and retest.

OAuth success is not file access. An authenticated account must have permission for the specific work file and node. Keep private file/node IDs and work-asset registries out of this public repository. Examples must stay as `<AUTHORIZED_FILE_KEY>` and `<AUTHORIZED_NODE_ID>`; supply real values only in an approved private session. Preserve existing work-asset registries, and do not infer edit scope from read access.

### Figma acceptance prompt

> Use the registered Figma MCP read-only. Discover its live schemas. Call `whoami` and verify the authorized work account/domain privately without publishing its email. Then call `get_metadata` for `<AUTHORIZED_FILE_KEY>` and `<AUTHORIZED_NODE_ID>` supplied privately by the operator. Confirm the expected node is returned. Do not edit, create, publish, or share any design file; do not put identifiers or returned private design content in Git. Report authenticated identity verification and target read-access verification as separate gates.

For design-to-code work, fetch the exact node's `get_design_context` and `get_screenshot` before implementation; if context is truncated, inspect metadata and request a smaller node. Reuse actual supplied assets and the project's design system. For a design-editing task, inspect the currently available editing tools and obtain explicit file/node permission first. Discovery/read success does not establish an editing workflow.

## DaVinci Resolve: prefer the actual bundled native server

Open Resolve on this computer. Check the installed distribution/version for `ResolveMCP`; do not assume a universal bundle path. On the reference macOS installation the executable was:

```sh
RESOLVE_MCP="/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Applications/ResolveMCP"
test -x "$RESOLVE_MCP"
```

This is an installation example, not a path to fabricate if absent. On Windows/Linux or another distribution, discover the real installed executable. If the server is not bundled, report that prerequisite as missing and review version/vendor documentation before choosing an alternative.

The bundled native stdio server **worked with Hermes** on the reference machine. Older guidance saying it only works with Claude is not a reason to reject a tested connection. Register it in a real interactive Terminal:

```sh
hermes mcp add davinci-resolve --command "$RESOLVE_MCP"
# Answer the tool-selection/enable confirmation after reviewing permissions.
hermes mcp list
hermes mcp test davinci-resolve
```

A non-TTY `Enable all?` prompt can hit EOF and cancel without saving, even after successful discovery. Use the interactive confirmation; automation should provide confirmation only for an explicitly approved server and the exact installed prompt flow, not a blanket approval bypass.

### Resolve acceptance prompt

> Use the local `davinci-resolve` MCP. Discover schemas, then call `get_resolve_status` read-only. Report actual running status and version; do not create/open/modify projects, timelines, media, or settings. Before proposing scripting code, inspect current `get_scripting_api`, `search`, and `get_whats_new` tools when available. Do not execute code as part of this check. If no native server is installed, stop rather than inventing a binary or claiming an untested community integration works.

For later approved scripting, prefer the server's sandboxed `run_script` route to unsafe execution and inspect its current schema/constraints. A sandbox is not permission to modify a user's production project. Work on a named duplicate or disposable test project, read back the target after changes, and verify an actual export before declaring an editing workflow complete. Community alternatives such as Gursky were not tested in this session; they are not the default verified path here.

## Computer use: local permissions and exact-window targeting

On the intended machine/profile:

```sh
hermes computer-use status
hermes computer-use doctor
# If backend installation is missing, review and approve first:
hermes computer-use install
# Use the installed permissions help for this platform:
hermes computer-use permissions --help
hermes tools
```

Enable Computer Use on the required surfaces through the installed `hermes tools` interface. The driver is cross-platform, but only **local macOS** permission checks were confirmed in the reference setup. On macOS the operator must grant the actual installed backend/host Accessibility and Screen Recording in System Settings when requested, then rerun doctor. A permission prompt is a human action, not a dialog the agent should silently approve. Other OSes need their own session/display/accessibility checks.

Discover the live `computer_use` schema before acting. Do not copy action fields, element indices, or coordinates from another version/machine. Prefer scoped app/window captures and fresh accessibility feedback; identify the specific PID/window when an app has multiple windows or a popup is targeted incorrectly. Browser CDP captures prove browser page state, **not** which native window is visible or where a native consent popup lives.

Keep input background-first so the operator can work. After an action, verify its actual effect. If background input is a confirmed no-op, use supported escalation only after fresh state inspection and explicit permission for any focus-stealing action. Do not guess repeated clicks or switch Spaces. Use browser tools for page DOM work and native computer use for application windows/browser chrome/native dialogs.

### Computer-use acceptance prompt

> Check local Computer Use health, discover its live tool schema, and capture only `<AUTHORIZED_APP>` with its correct PID/window if needed. Confirm that the screenshot and accessibility state belong to that application. Do not click permission dialogs, type secrets, expose other windows, or change app/project state. If the operator separately authorizes one reversible GUI action, perform it and capture/read back the exact result; distinguish permissions, capture success, and verified input success.

Do not claim remote control of another PC from this local check. A separate workstation must install and validate its own driver. Tool access over Slack still acts on the gateway computer, not on the Slack user's computer.

## Reloading and handoff

After registrations change, issue `/reload-mcp` as a separate command in the applicable session, or start a new session. Verify the current Desktop/CLI **and Slack** tool availability separately. If a gateway restart is required for profile/provider/identity changes, wait for active runs to finish and confirm it is idle before restarting. Never interrupt a creative job just to refresh tool discovery.

The final handoff should state: selected profile, app/client versions, configured servers, successful live read-only calls, permissions checked, and the next unproven task gate. Do not attach raw private logs, screenshots, account email, file IDs, or credential-store contents.

## Sources and version drift

- [Hermes documentation](https://hermes-agent.nousresearch.com/docs/) and [documentation index](https://hermes-agent.nousresearch.com/docs/llms.txt).
- [Hermes MCP guide](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) and [MCP configuration reference](https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference).
- [Hermes Computer Use](https://hermes-agent.nousresearch.com/docs/user-guide/features/computer-use).
- Installed `hermes ... --help`, actual application/tool schemas, and live read-only results take precedence over stale examples for the installed version. Inspect package/vendor documentation before approving downloaded addon/server code.

These instructions document the verified local path and its known failure modes. They do not certify every OS, application distribution, future package release, or helper script.
