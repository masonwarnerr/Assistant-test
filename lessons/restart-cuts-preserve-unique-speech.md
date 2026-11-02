# Preserve unique speech when removing repeated takes

Status: verified local worker procedure, 2026-11-01.

- Scope: dialogue cleanup where a speaker restarts, repeats a clause, or replaces the tail of an earlier take.
- Prerequisites: the approved source or prior revision, native/source context, and an actual rendered movie that can be transcribed and decoded.
- Source: repeated reviewer correction on this Mac, source-word mapping, overlapping-window and full-render ASR, native join checks, waveform checks, and final render verification.

Do not delete a whole first take merely because a later take repeats part of it more cleanly. Mark the unique words in each formulation first. Preserve the chosen formulation through its last unique word, remove only the failed or repeated tail that the later take replaces, and join at the real shared word or phrase boundary. Tighten excessive lead-in silence only to measured phoneme guards; broad quiet buffers and transcript timestamps are not safe cut boundaries by themselves.

Whole-program ASR can normalize an audible restart that overlapping short windows expose. Compare the complete transcription of the actual delivered movie with an independent overlapping-window pass and native or original-source context. Review repeated clauses and abandoned formulations, not only filler keywords. Do not prime disputed phrases as evidence because a phrase-heavy prompt can hallucinate them into unrelated windows.

When the reviewer supplies exact desired wording, use that literal sentence as the editorial acceptance test. Verify the required clause occurs once and the excluded repeated clause occurs zero times in the actual render. Also verify every unique source word survives, inspect the affected joins with ASR and waveform evidence, fully decode the movie, and confirm unrelated picture and approved program audio remain preserved.

If no defensible word or phoneme boundary exists, retain the source unit or report the uncertainty. Never broaden the deletion for convenience, and never claim human listening from automated ASR or waveform checks.
