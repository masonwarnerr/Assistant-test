# Adobe Podcast enhance, end to end

- Scope: Dialogue enhance on the DaVinci Mac before a Resolve sync.
- Date: 2026-10-08 (procedure already in local skill; promoted so other agents stop relearning it)
- Source: Mason, repeated. Local skill `slash-davinci-edit` and `references/adobe-podcast-picker.md`.

Chrome on that Mac is already the agent browser. Use the standing chrome-adobe profile on debug port 9223 with remote-allow-origins set. Do not quit it after a working login. Do not ask Mason to click Open.

Leave the file-chooser intercept off. A trusted click on Choose files opens the sheet. Go to the SSD `audio/` folder, step into it, and open the `*-plus3dB.wav`.

`Uploading…` from a CDP file inject is not an upload. Success is a clip duration or Enhancing speech. Download, then copy the enhanced wav onto the SSD audio folder next to the cameras. Do not leave it in Downloads. Do not tell him the setup is done while Enhance has not taken the file.

Check: Enhance shows duration or Enhancing speech, and the SSD has the enhanced wav.
