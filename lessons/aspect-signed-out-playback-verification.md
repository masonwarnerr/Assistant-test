# Verify signed-out Aspect review playback by time advance

Status: verified local worker procedure, 2026-10-20.

- Scope: signed-out QA of an authorized Aspect review link before delivery.
- Prerequisites: the intended client review URL is available and the isolated review tab may be activated without touching unrelated work tabs.
- Source: same-machine signed-out browser execution, player-state inspection, and observed playback advance.

Opening a folder, seeing a thumbnail, or receiving a successful media range response does not prove the movie plays. Open the intended asset with a true double-click on its thumbnail, not two ordinary clicks or a filename-only selection. Press Play and read the actual video state and current time.

If range fetches succeed but the player remains stalled in a hidden review tab, inspect the page visibility state. Bring only the isolated review tab to the front, then retry playback and read current time again. Do not activate, navigate, or close an unrelated authenticated browser tab to solve review-player QA.

The acceptance check is the intended signed-out asset loaded, current time advancing after Play, and no player error. If time does not advance, report playback as unverified even when the poster frame and network requests look healthy.
