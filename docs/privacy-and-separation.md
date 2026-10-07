# Privacy and machine separation

This playbook distinguishes **work-only agent context**, **independent local state**, and **enforced access isolation**. They are different outcomes. Cleaning a Hermes home and writing a work-only policy does not sandbox an agent that retains terminal, browser, desktop, or filesystem tools.

The tested outcome was a local work-oriented setup with personal-only skills and personal-containing old backups removed, mixed work material selectively sanitized, and useful work operations retained. Open Slack access was accepted afterward as an explicit trade-off. This document does not certify other computers, remote schedulers, or an OS-level boundary.

## 1. Define the boundary and get approval

Before changing anything, record privately:

- The physical computer, OS account, actual active Hermes home, intended default profile, and work directories.
- Which entry surfaces may use that home: local CLI, desktop, and that computer's Slack app.
- Who may reach the bot, including workspace guests, and what local tool capabilities those users can trigger.
- The work integrations, curated skills, and operational references that must survive cleanup.
- The private sources to remove from agent context, and the credentials/assets that must remain inaccessible if hard separation is required.
- Whether this task permits inspection only, selective cleanup, credential revocation, or OS/account changes. Do not infer permission to delete unrelated personal data or modify a remote machine.

Use a dedicated work OS account, a work browser profile, and enforced permissions for strong separation. If that boundary is not in place, document the remaining exposure rather than calling the setup isolated.

## 2. Inventory locally, without leaking the inventory

Resolve the active home from the selected profile and launch environment. Default installations normally use `~/.hermes`; an explicit `HERMES_HOME` or named profile can change it. Do not inspect every profile indiscriminately or modify another profile without authorization.

Review locally, in small batches:

| Area | Inspect for |
|---|---|
| Policy/context | `SOUL.md`, user/memory files, project context files, custom prompts, launch instructions, channel prompts and startup bindings |
| Skills | Main skill files, linked references/templates/scripts, registries, origin metadata, symlinks and copied bundles |
| Historical material | Sessions, transcript stores, logs, exports, old backups, cached history and archival copies |
| Integrations | Local credential stores, configured MCP/connectors, browser profiles, provider accounts, Slack token sources; inspect names/paths without printing secrets |
| Background execution | Local cron definitions, launch services, running processes, sync/watch jobs, peer/relay configuration, mounted/shared directories |
| Repository/work assets | Personal identifiers embedded in work docs, private link destinations, copied messages, asset names, private project mappings |

Never `cat` or print credential stores into chat. Use a local helper that returns key names, existence, file permissions, and boolean checks rather than values. Do not publish full session or process listings: they can contain private paths, message content, or command-line credentials.

Inspect symlink targets and the physical location of the home. A directory under the local filesystem does not establish independence if a symlink, mounted share, sync service, or background copier points elsewhere.

### Evidence limits

- A local directory plus no observed symlinks, peers, or relevant sync processes supports **local independent state in the inspected scope**.
- It does not prove that an uninspected remote scheduler cannot read a share or send a request.
- No SSH inspection of another computer was performed in the tested audit. Do not report that computer as audited or disconnected.
- A copied skill's source/origin metadata is not evidence of a live shared agent. Conversely, a local copy alone does not rule out separate synchronization.
- A spot check is not a complete audit. Record excluded files and inaccessible systems explicitly.

## 3. Classify before editing

Create a private review inventory with a decision for each item. Publish only a sanitized completion report, not the inventory contents.

| Classification | Action |
|---|---|
| Personal-only skill/context | Remove from the approved active work scope after checking dependencies |
| Mixed personal/work material | Edit narrowly: remove personal portions, retain operational procedures and legitimate work references |
| Work-only skill/reference | Preserve; validate that linked dependencies still resolve |
| Credential or OAuth store | Keep local and secured, or disconnect/revoke with explicit approval; never copy to the repository or another computer |
| Old backup containing removed context | Handle explicitly; do not leave an automatically discoverable copy that reintroduces the same material |
| Binary/archive/cache not examined | Mark excluded, quarantine from agent access if approved, and review separately when needed |
| Ambiguous item | Ask the owner or retain outside the enabled context pending review; do not guess that it is expendable |

Do **not** delete the entire skills root as a shortcut. Work capability is part of the acceptance criteria. The tested cleanup preserved curated work skills and removed personal portions from mixed files; its file counts were machine-specific, not replication targets.

If a backup is needed, put it in an approved protected location outside the enabled agent context, with appropriate access restrictions and a retention decision. A backup under the same unrestricted account is not a hard privacy boundary. Do not create a new personal-containing backup inside the repository or skill search tree merely to make editing feel reversible.

## 4. Perform selective cleanup

1. Pause relevant background writers if authorized, so cleanup does not race a sync, curator, gateway, or export process. Record which work services need resuming.
2. Remove approved personal-only skills/context and obsolete personal-containing backups from the work agent's accessible/active scope.
3. For mixed skills, read the full file and its linked references before editing. Strip personal examples, private mappings, obsolete source links, and identity-specific instructions while preserving useful work operations.
4. Recheck linked references, scripts, and templates. Removing a top-level personal paragraph is insufficient if a linked file still embeds the same context.
5. Treat large registries as mixed assets: inspect relevant sections and make narrow patches. Preserve legitimate work entries and IDs in the private local operational material. Do not publish those IDs in the public playbook.
6. If origin metadata grants writable access to a source skill outside the local work scope, make that reference local/read-only using the supported metadata/workflow. Do not edit the remote source as a side effect or assume the source copy is another live agent.
7. Review saved memory and policy separately from historical sessions. Removing a skill does not remove a remembered personal detail or a transcript containing it.
8. Record exclusions, especially binary archives, old cached histories, and remote systems. Do not claim every byte was sanitized when those were not inspected.

Keep edits inside the approved computer/profile. Do not copy another machine's assets, another person's Hermes home, or their OAuth stores. If a public guide needs examples, create neutral placeholders rather than copying real IDs, email addresses, account paths, or transcript excerpts.

## 5. Install a work-only policy, then start fresh

Use the intended home's supported policy/context mechanism, such as its `SOUL.md`. A policy should state:

- Work requests and approved work directories/integrations are the scope.
- Personal files, accounts, messages, and context are out of scope even if technically reachable.
- No import of another machine's memory, sessions, credentials, or user assets.
- Shared-channel output must not reveal private local paths, identifiers, secrets, or personal material.
- External writes, account changes, permission changes, and destructive operations require the agreed approval process.
- Unclear ownership or requests beyond scope must be escalated instead of improvised.

This is a behavior rule, **not an access-control mechanism**. Terminal and desktop tools may still operate with the OS account's full privileges. Secret redaction and command approvals are useful defense in depth, but neither guarantees that personal files cannot be read or disclosed.

**Start a fresh conversation on each surface after cleanup.** A running conversation retains pre-cleanup context already loaded into it. Restart affected processes if they snapshot policy/configuration at startup; use the supported fresh-session action for the installed surface. Do not resume an old personal-containing session to verify that the agent has forgotten it.

Keep or dispose of historical stores according to the authorized retention policy. If old sessions remain searchable by the work agent, a fresh chat alone is not enough: restrict access to that history or handle it explicitly. Do not claim all history was removed unless it actually was.

## 6. Use enforced separation when privacy must be hard

For an agent reachable from Slack, a strong boundary requires more than a clean prompt:

- **Dedicated work OS account:** no read access to personal home directories, personal cloud mounts, or personal backups. Test filesystem permissions under the actual service identity.
- **Dedicated work browser:** separate profile and work-only sign-ins. A browser profile alone is not a security boundary if the agent can open other profiles or control the whole desktop; restrict those capabilities or use a dedicated work session/device.
- **Filesystem permissions/ACLs:** grant only necessary work directories. Ensure the gateway does not run with broader privileges than intended. Test representative denied paths without reading their content.
- **Credential separation:** work-scoped accounts and OAuth consent; no copied personal credential pools. Restrict access to browser credential stores, keychains, mounted secrets, and other local integrations.
- **Tool controls:** disable unnecessary tools and restrict terminal/desktop/browser reach where supported. Verify on the actual Slack surface, not only in local CLI settings.
- **Network and remote controls:** inspect authorized peer, relay, scheduler, and sync systems independently. Local inspection cannot certify them.
- **Execution isolation where appropriate:** a dedicated machine, restricted VM/container, or equivalent boundary may be needed. Desktop-control and host-mounted folders can defeat an otherwise isolated environment; test the real configuration.

Do not treat an account as separated merely because its name contains “work.” Verify which files, windows, browser sessions, integrations, and mounts the service account can actually access. Avoid privilege escalation and shared personal desktop control. If these checks cannot be completed, state “work-only context, not enforced OS isolation.”

## 7. Authorization and shared output

The [Slack playbook](slack.md) starts with explicit human allowlists and documents intentional open access. Choose the policy only after understanding tool reach.

- Open access may include guests who can reach the bot; it does not limit them to harmless questions.
- Channel membership, a home channel, and mention gating are not replacements for user authorization.
- Separate conversation histories do not isolate shared skills, global memory, credentials, files, or the OS account.
- Configure progress/status display conservatively in shared channels: tool progress can reveal command arguments and local paths even if the final answer is sanitized.
- Remote model/provider requests and Slack delivery are external data flows. Local file storage does not mean all processing stays on the computer. Review provider, tool, and workspace policies for the permitted work data.
- Keep secret redaction enabled; do not rely on it to identify all private identifiers or personal content.

## 8. Verify and report only the supported outcome

Run a fresh-session check for each intended surface:

1. Verify active home and selected policy using nonsecret local checks.
2. Confirm approved work skills and linked references still function on a harmless work task.
3. Ask the agent to describe its work scope, then compare against local configuration. Its answer is supporting evidence, not proof of access isolation.
4. Re-scan the reviewed text scope for approved personal markers using a local nonprinting helper. Return hit counts/pass-fail categories, not matching text. A clean keyword scan alone cannot certify semantic cleanup.
5. Check for dangling links, unintended remote writable sources, symlinks, sync/peer settings, and background writers within the approved scope.
6. Verify Slack authorization and harmless routing tests after restarting the owning gateway.
7. If hard separation is required, test denied filesystem/browser/desktop reach under the real service identity. Report blockers without opening personal content.

A portable completion record should contain only:

```text
Scope: this computer's intended work Hermes home
Context cleanup: complete / partial, with reviewed categories
Work capability: tested task and pass/fail
Local-state separation: evidence checked, within stated scope
Authorization: restricted / explicitly open, with test outcome
OS access isolation: enforced and tested / not established
Excluded material: categories only
Remote systems: inspected within authorization / not inspected
Fresh sessions: completed surfaces / remaining surfaces
Unresolved issues: concise nonsecret list
```

Do not publish local account names, private workspace/member IDs, proprietary file mappings, emails, credentials, or transcript logs. Report exact cleanup totals only when measured and clearly labeled as **this-machine results**; omit them when they do not help replication.

## Acceptance checklist

- [ ] Active work home confirmed; other profiles/machines untouched unless explicitly authorized.
- [ ] Personal-only material removed within scope; mixed work material sanitized selectively.
- [ ] Curated work skills and their linked dependencies preserved and exercised.
- [ ] Backups, history, caches, and excluded binary material addressed or disclosed.
- [ ] Local-state evidence does not overclaim remote isolation.
- [ ] Work-only policy loaded in fresh sessions; old live context not treated as erased.
- [ ] Slack access decision matches actual tool reach and residual privacy risk.
- [ ] Hard OS/browser/filesystem separation either tested or explicitly not established.
- [ ] No private identifiers, secrets, or transcript excerpts included in public output.

Reference: [Hermes documentation](https://hermes-agent.nousresearch.com/docs). Consult installed-version guidance for policy loading, profile resolution, tool restrictions, approvals, and gateway lifecycle; do not invent a sandbox feature to fill a privacy gap.
