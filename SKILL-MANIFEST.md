# Distributed instructions and helpers

## Included

- `AGENTS.md`: setup brief for a fresh local agent.
- `docs/`: local pilot, per-machine topology, exact Slack setup/naming, privacy cleanup, creative apps, acceptance gates, and troubleshooting.
- `templates/SOUL.work.md`: work-only identity example, not a live memory export.
- `templates/machines/`: optional role briefs. The default replication model is one shared work profile per computer, not one profile per surface.
- `scripts/fix_blender_addon_layout.py`: explicit-apply addon layout normalization with code backup and dry-run.
- `scripts/enable_blender_bridge.py`: run inside Blender; enables the local bridge and saves preferences, not project files.
- `tests/test_blender_helpers.py`: isolated fixture tests, not proof of live application readiness.
- `skills/agent-learning-sync/SKILL.md`: overnight pull, own-inbox write, push. Install into the active profile. The contract is `docs/recursive-learning.md`.
- `skills/hermes-agent/SKILL.md`: the original generic hub copy. Linked reference files from the installed skill are intentionally not distributed; consult official docs rather than assuming those files exist. Do not overwrite a complete locally installed Hermes skill with this partial copy.

## Intentionally excluded

No live profile/config, credentials, OAuth stores, browser accounts, memories, sessions, logs, personal information, private screenshots/media, full machine-specific skill trees, or private Figma file registries are distributed. Review any new skill before adding it to Git. A skill supplies operational knowledge, not installed software or service authorization.

Install the relevant reviewed work skills into the selected computer's active Hermes home separately. Keep service credentials and work asset mappings local. Read the current installed CLI/help and official docs when versioned instructions differ.
