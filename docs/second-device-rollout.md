# Second-device rollout

## Before connecting a machine

- Install the same current Hermes release family and run `hermes doctor`.
- Give the machine one role and one profile; do not clone live `~/.hermes` state.
- Verify the workstation has only the local applications and folders needed for that role.
- Exchange only the minimum connection details through a secret channel. Never commit `API_SERVER_KEY`, Slack tokens, OAuth tokens, or `.env`.

## Recommended order

1. Clone this repository.
2. Read the role template under `templates/machines/`.
3. Create the local profile and run a harmless smoke task.
4. Register the machine in the Notion board as `available`.
5. Connect through Hermes Desktop connections/Bot Mode, or use the documented peer commands only after reading `hermes peer --help` and the Bot Mode docs.
6. Run one supervised task; capture artifact path and verification.

## Peer example (only after a protected API server exists)

The Hermes Bot Mode documentation documents this shape; replace placeholders locally and keep keys out of shell history where possible:

```bash
hermes peer add <machine> --url http://<host>:8377 --key <API_SERVER_KEY>
hermes peer list
hermes peer status <machine> <run_id>
```

Do not expose the API server directly to the public internet. Prefer a private network/VPN and firewall allowlists. On Windows, confirm the local firewall rule and bind address before enabling remote access.

## Specialist acceptance test

The specialist must return:

- task ID and role;
- exact workspace and artifact path;
- commands run and verification result;
- remaining risks or manual steps;
- whether the coordinator must approve publication.

A second device is not production-ready until a coordinator can route one task, inspect the result, and recover from a failed or disconnected run.
