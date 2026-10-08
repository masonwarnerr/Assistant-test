# Resolve died mid-render: resume the same job

Status: worker report missing. masonpc reconstructed this from the local skill. The DaVinci agent has to write what it actually did.

- Scope: A render that dies because Resolve quit, not because the cut was wrong.
- Source: local skill on masonpc. Not a worker write-up.

Stop the stuck Astra process. Reopen Resolve. It may restore the same cloud project. Confirm the name before any LoadProject. Delete the partial mp4 that has no render receipt. Resume the existing render script. It should skip clips that already have a receipt and an mp4.

Do not rebuild timelines. Do not regrade. If he says quit Chrome and Settings to free RAM, do that only when Adobe is already finished. Do not quit chrome-adobe while Enhance is still uploading.

Check: same project, same timelines, only the missing clips rendered.
