# Deferred Notion task board

Notion is **not required for the pilot**. Git is the only shared durable layer, and the direct DaVinci plus local Lloyd paths should be proven before adding a queue. Keep this document as a future option, not an implementation dependency.

If a later phase needs a human-facing queue, preserve the rules below and explicitly decide what Notion adds over Git. Do not duplicate live state without an owner and reconciliation rule.

## OAuth/MCP rule

Use the already-connected Notion OAuth MCP integration or Hermes' MCP catalog/dashboard. Do not ask for, read, create, or store `NOTION_API_KEY`, `NOTION_TOKEN`, or an exported Notion secret. OAuth tokens stay in the active Hermes profile's local token store and are never committed.

Hermes' generic MCP configuration supports HTTP servers with `auth: oauth`, browser-based OAuth 2.1 PKCE, and `hermes mcp login <server>` / `hermes mcp test <server>`. Do not invent a Notion endpoint: select the official Notion MCP entry supplied by the connected catalog or use the endpoint shown by current Hermes/Notion documentation.

After a config change, use `/reload-mcp`; from a shell, test with:

```bash
hermes mcp test <server-name>
```

## Future database design

Suggested properties remain: task ID, name, status, priority, owner role, assignee, machine, acceptance criteria, artifact URL, source branch, due date, blocker, last update, and risk. A future queue must link back to the Git task report and commit; it must not become the authoritative execution log.

## OAuth troubleshooting

- MCP missing: run `hermes mcp test <server-name>` and inspect the active profile, not another machine's token store.
- Login needed: run `hermes mcp login <server-name>` or use the dashboard's OAuth flow.
- Permission/404: share the target Notion page/database with the authorized integration/account.
- Never copy `mcp-tokens` between machines.
