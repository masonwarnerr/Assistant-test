# Deliver a verified Aspect review link with completed media

Status: verified local worker procedure, 2026-10-12.

- Scope: authorized visual-media or file-based document delivery through an Aspect review folder.
- Prerequisites: the exact destination and expected object inventory are verified, and creating the requested review share is within the approved delivery scope.
- Source: local worker share creation, exact-resource readback, and unauthenticated browser verification.

Verify every expected object at the exact destination before sharing. Create a directory share with only the required review permissions and set password, expiry, and visible metadata fields explicitly rather than relying on defaults. For view-only review, use the service's VIEW permission without adding download, organization, or administrative rights unless separately requested.

Read the share back by resource and confirm it is active, targets the intended directory, and exposes only the intended actions. Open the returned client URL in an unauthenticated browser and confirm the expected folder loads. Then include that verified URL in the first completion handoff; pending grade or QA can be labeled beside it rather than delaying the review link.

Internal directory IDs, asset IDs, mount paths, or a guessed URL are not substitutes for the returned client URL. If share creation is not authorized or anonymous opening fails, report the blocker and do not broaden permissions. Keep private review URLs out of the learning repository.
