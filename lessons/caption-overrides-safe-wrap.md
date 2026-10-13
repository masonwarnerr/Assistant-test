# Apply safe wrapping to corrected caption text

Status: verified local worker procedure, 2026-10-12.

- Scope: captioned vertical review exports where names, answers, or other text is manually corrected after ASR grouping.
- Prerequisites: an approved base movie or editable timeline, the intended caption safe area, and the actual corrected text.
- Source: local worker correction, isolated caption revision, complete decode, source-bound comparison, and audio-payload verification.

Run manually corrected or overridden text through the same measured wrapping and safe-bound checks as ordinary ASR caption groups. A typography pilot that passes for generated groups does not prove a long corrected line will fit.

Preserve already exported movies. Make an isolated caption-only revision from the approved base, changing only caption content, wrapping, or placement needed for the correction. Do not rebuild or overwrite picture and audio to solve a caption-bound problem.

Check every corrected caption against the vertical safe area, fully decode the revision, compare video timing and native AV source bounds with the base, and compare the extracted AAC payload hash when available. If payload identity cannot be checked, report the weaker audio evidence rather than claiming the audio is unchanged.
