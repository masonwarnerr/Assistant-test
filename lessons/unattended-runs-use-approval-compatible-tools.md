# Use approval-compatible tools in unattended runs

Status: verified local worker procedure, 2026-10-15.

- Scope: scheduled learning or repository-audit jobs that run without a user present to approve arbitrary code execution.
- Prerequisites: the job has explicit read scope and ordinary file/search or narrow terminal tools are available.
- Source: two consecutive local scheduled passes in which arbitrary Python execution was blocked and the inventory completed through approval-compatible read-only tools.

Do not weaken cron approvals to make a convenience script run. Use ordinary `read_file` and `search_files` calls for repository inventories. Batch independent reads in parallel. Use only narrow, read-only terminal commands that the unattended policy accepts when metadata or Git state requires them.

Treat each tool boundary separately. A successful repository-file fallback does not prove that a gateway-owned database, active application state, or another protected resource is readable. If the lifecycle guard blocks that target, preserve the guard and report the evidence boundary instead of copying private state or bypassing policy.

Check the blocked call's receipt first: it must show that no tool calls or writes occurred. Then complete the required inventory with approved tools, verify the expected file count and Git status, and review the exact staged paths before publication.
