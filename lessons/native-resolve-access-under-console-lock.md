# Test native Resolve access under managed console lock

Status: verified local worker procedure, 2026-10-13.

- Scope: deciding whether managed screen locking blocks authorized native Resolve work on the local Mac.
- Prerequisites: Resolve is already running, the native Resolve interface is available, and only read-only inspection is authorized for the acceptance test.
- Source: local worker test with console-lock readback and a non-mutating native Resolve query in the same session.

Separate managed console locking from system sleep before changing security or power settings. Preserve the security profile. Read only the console-lock boolean, then run a non-mutating native query for the current project and timeline state.

The local acceptance test succeeded while the console reported locked: the native interface read the current project, active timeline, timeline inventory, render state, and track counts without mutation. This establishes read-only scripting availability for that state. It does not prove that editing, rendering, browser automation, or desktop input will work through the lock screen.

If the native query fails, report the exact access boundary rather than weakening the lock policy or assuming all application work is blocked. Re-test each required action at its actual capability level before relying on unattended operation.
