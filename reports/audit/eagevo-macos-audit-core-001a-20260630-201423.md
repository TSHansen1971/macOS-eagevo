# EAGEVO-MACOS-AUDIT-CORE-001A Report

## Result

GREEN

## Created UTC

2026-06-30T20:14:23Z

## Initial append

```text
appended_sequence: 1
entry_hash: 8f7e7509856eed7263d0d78b97ab75ee53d026ebbbc64c1e56fddc253d862659
```

## eagevo-audit status

```text
== eagevo-audit ==
platform: macOS
role: Eagevo Control Plane for macOS
mode: manual-append-only-hash-chain
automatic_collection: disabled
enforcement: disabled
launchd: disabled

OK: exists: /Library/Eagevo/audit
OK: exists: /Library/Logs/Eagevo/audit
OK: exists: /usr/local/lib/eagevo/audit
OK: exists: /usr/local/lib/eagevo/audit/audit-core-contract.json
OK: exists: /Library/Logs/Eagevo/audit/audit-events.jsonl
OK: exists: /Library/Eagevo/audit/audit-head.json

audit_verify: GREEN
entries: 1
last_hash: 8f7e7509856eed7263d0d78b97ab75ee53d026ebbbc64c1e56fddc253d862659

overall: GREEN
```

## eagevo-audit verify

```text
audit_verify: GREEN
entries: 1
last_hash: 8f7e7509856eed7263d0d78b97ab75ee53d026ebbbc64c1e56fddc253d862659
```

## eagevo-baseline verify

```text
== eagevo-status ==
platform: macOS
role: Eagevo Control Plane for macOS
mode: contract-only
enforcement: disabled

OK: exists: /Library/Eagevo
OK: exists: /Library/Application Support/Eagevo
OK: exists: /Library/Logs/Eagevo
OK: exists: /usr/local/lib/eagevo
OK: exists: /usr/local/lib/eagevo/foundation-contract.json
OK: exists: /usr/local/bin/eagevo-status
OK: exists: /usr/local/bin/eagevo-baseline

== launchd enforcement check ==
OK: absent: /Library/LaunchDaemons/*eagevo*
OK: absent: /Library/LaunchAgents/*eagevo*
OK: absent: /Users/tostha-dev/Library/LaunchAgents/*eagevo*

overall: GREEN
```

## Boundary

No automatic audit collection, no LaunchDaemon, no LaunchAgent, no enforcement, no AI runtime, no agent execution, no external logging.
