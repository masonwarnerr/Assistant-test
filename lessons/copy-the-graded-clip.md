# Copy the clip he named, not a nearby one

Status: intent from Mason. Worker report missing. The node-check steps below were reconstructed on masonpc from the local skill, not from the DaVinci worker.

- Scope: Applying a hand grade across a shortform sequence.
- Source: Mason called the wrong-clip copy the main miss. masonpc did not ask the worker.

The source grade is the clip he named (first shot of timeline 02 in that pass). Copy that node tree and settings to the other picture clips he listed. Do not average. Do not reapply an older warmth value. Do not leave later shots on a different grade. Leave timeline 01 alone unless he says otherwise.

`CopyGrades` returning true is not proof. Node-graph object identity always differs. Grab a still of the named shot with karaoke disabled (otherwise the still grabs captions) and compare grade bodies after apply.

Check: other listed clips match that shot, not a later one.
