# davinci

- Computer: Davincis-MacBook-Pro. Resolve and Adobe Podcast live here.
- Hermes profile: astra
- Hermes: `/Users/davinci/.local/bin/hermes -p astra`
- Clone: `/Users/davinci/Assistant-test`
- Overnight slot: 02:30 America/Los_Angeles (`30 2 * * *`)
- Model pin: openai-api / gpt-5.6-sol. Do not use gpt-6-astra for this pass.
- Scheduler: user LaunchAgent `ai.hermes.learning-tick` runs `hermes -p astra cron tick` at 02:30. The Slack gateway on this Mac stays off.
- Writes: `inbox/davinci/` and new `lessons/<slug>.md` from work this machine actually did. Do not rewrite masonpc's inbox.
