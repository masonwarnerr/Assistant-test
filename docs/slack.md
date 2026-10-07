# Slack gateway

Hermes' current Slack integration uses Slack Bolt Socket Mode. It needs a bot token (`xoxb-`) and app-level token (`xapp-`); it does not need a public HTTP endpoint.

## Verified setup

1. Create a Slack app at https://api.slack.com/apps using **Create New App → From an app manifest**.
2. On the coordinator device, generate the current manifest:

```bash
hermes slack manifest --agent-view --write
```

This writes `~/.hermes/slack-manifest.json`. Paste that JSON into Slack's App Manifest editor, save, and install the app to the workspace. For an existing legacy Assistant-view app, regenerate with `hermes slack manifest --write` as documented.

3. Enable Socket Mode in Slack. Create an app-level token with `connections:write`; keep the resulting `xapp-` token private.
4. Install the app and copy the bot token. Invite the bot to each channel explicitly with `/invite @Hermes Agent`.
5. Use the interactive gateway setup (preferred):

```bash
hermes gateway setup
hermes gateway
```

The setup flow stores credentials in the active Hermes home. If configuring through the environment, the official names are `SLACK_BOT_TOKEN`, `SLACK_APP_TOKEN`, and `SLACK_ALLOWED_USERS`; do not put real values in Git.

6. For a background service, verify the platform-specific service behavior first, then use the documented command:

```bash
hermes gateway install
```

## Safe fleet settings

DMs receive every message. Channels require an @mention; replies continue in the thread. Keep bot-to-bot traffic disabled by default. If peer collaboration is needed, use `allow_bots: mentions`, never `all`, and require each bot message to mention its target. This prevents answer loops.

Use the Slack Member IDs in `SLACK_ALLOWED_USERS`, not display names. Start with Mason only, test in a private channel, and expand allowlists deliberately.

## Upgrade check

After Hermes adds or changes commands, regenerate and update the Slack manifest:

```bash
hermes slack manifest --write
```

Then paste it into Slack → your app → Features → App Manifest and reinstall if Slack requests it.

Source: https://hermes-agent.nousresearch.com/docs/user-guide/messaging/slack
