# Notion shared task board

## OAuth/MCP rule

Use the already-connected Notion OAuth MCP integration or Hermes' MCP catalog/dashboard. Do not ask for, read, create, or store `NOTION_API_KEY`, `NOTION_TOKEN`, or an exported Notion secret. OAuth tokens stay in the active Hermes profile's local token store and are never committed.

Hermes' generic MCP configuration supports HTTP servers with `auth: oauth`, browser-based OAuth 2.1 PKCE, and `hermes mcp login <server>` / `hermes mcp test <server>`. Do not invent a Notion endpoint: select the official Notion MCP entry supplied by the connected catalog or use the endpoint shown by the current Hermes/Notion documentation.

After a config change, use `/reload-mcp`; from a shell, test with:

```bash
hermes mcp test <server-name>
```

If the remote gateway is headless, use the documented dashboard or device-flow path rather than copying callback URLs or token files between machines.

## Database design

Create one database named **Fleet Tasks**. Suggested properties:

| Property | Type | Values / purpose |
|---|---|---|
| Name | title | Short imperative task name |
| Status | status/select | Inbox, Ready, In progress, Blocked, Review, Done, Cancelled |
| Priority | select | P0, P1, P2, P3 |
| Owner role | select | Coordinator, Resolve, Blender, Midjourney |
| Assignee | person/text | Human or bot/profile handle |
| Machine | text/select | Device or connection name |
| Acceptance criteria | rich text | Observable finish conditions |
| Artifact URL | URL | GitHub, drive, render, or delivery link |
| Source branch | text | Git branch/PR reference |
| Due | date | Optional deadline |
| Blocker | rich text | Dependency, approval, or missing input |
| Last update | date | Coordinator-maintained heartbeat |
| Risk | select | Low, Medium, High |

Views: **Inbox**, **My queue**, **By machine**, **Blocked**, **Review**, and **Done this week**. Keep views in Notion; the agent should query the database and update properties, not recreate views on every run.

## Lifecycle contract

Every task must have an owner role, acceptance criteria, and next action before leaving Inbox. Specialists may move a task to Blocked or Review but may not publish a final deliverable without coordinator approval. Done requires an artifact link and verification note.

Use stable task IDs in the page title or a dedicated text property, for example `FLEET-2026-001`. Link commits and artifacts; do not paste secrets or personal transcripts into page content.

## OAuth troubleshooting

- MCP missing: run `hermes mcp test <server-name>` and inspect the active profile, not another machine's token store.
- Login needed: run `hermes mcp login <server-name>` or use the dashboard's OAuth flow.
- Permission/404: share the target Notion page/database with the authorized integration/account.
- Remote callback issue: use the dashboard or device authorization documented in Hermes MCP docs; do not copy `mcp-tokens` between machines.

Sources: https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp and https://hermes-agent.nousresearch.com/docs/reference/mcp-config-reference
