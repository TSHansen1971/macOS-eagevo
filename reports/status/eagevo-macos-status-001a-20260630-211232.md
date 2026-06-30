# EAGEVO-MACOS-STATUS-001A Report

## Result

GREEN

## Created UTC

2026-06-30T21:12:32Z

## eagevo-status

```text
== eagevo-status ==
platform: macOS
role: Eagevo Control Plane for macOS
mode: read-only-aggregator
automatic_collection: disabled
enforcement: disabled
launchd: disabled

== foundation ==
OK: exists: /Library/Eagevo
OK: exists: /Library/Application Support/Eagevo
OK: exists: /Library/Logs/Eagevo
OK: exists: /usr/local/lib/eagevo
OK: exists: /usr/local/lib/eagevo/foundation-contract.json
OK: executable: /usr/local/bin/eagevo-status
OK: executable: /usr/local/bin/eagevo-baseline

== audit-core ==
OK: exists: /Library/Eagevo/audit
OK: exists: /Library/Logs/Eagevo/audit
OK: exists: /usr/local/lib/eagevo/audit
OK: exists: /usr/local/lib/eagevo/audit/audit-core-contract.json
OK: exists: /Library/Logs/Eagevo/audit/audit-events.jsonl
OK: exists: /Library/Eagevo/audit/audit-head.json
OK: executable: /usr/local/bin/eagevo-audit
audit_verify: GREEN
entries: 1
last_hash: 8f7e7509856eed7263d0d78b97ab75ee53d026ebbbc64c1e56fddc253d862659
OK: audit_verify_green

== status-core ==
OK: exists: /usr/local/lib/eagevo/status-core-contract.json

== launchd safety check ==
OK: absent: /Library/LaunchDaemons/*eagevo*
OK: absent: /Library/LaunchAgents/*eagevo*
OK: absent: /Users/tostha-dev/Library/LaunchAgents/*eagevo*

warnings: 0
overall: GREEN
```

## eagevo-baseline verify

```text
== eagevo-status ==
platform: macOS
role: Eagevo Control Plane for macOS
mode: read-only-aggregator
automatic_collection: disabled
enforcement: disabled
launchd: disabled

== foundation ==
OK: exists: /Library/Eagevo
OK: exists: /Library/Application Support/Eagevo
OK: exists: /Library/Logs/Eagevo
OK: exists: /usr/local/lib/eagevo
OK: exists: /usr/local/lib/eagevo/foundation-contract.json
OK: executable: /usr/local/bin/eagevo-status
OK: executable: /usr/local/bin/eagevo-baseline

== audit-core ==
OK: exists: /Library/Eagevo/audit
OK: exists: /Library/Logs/Eagevo/audit
OK: exists: /usr/local/lib/eagevo/audit
OK: exists: /usr/local/lib/eagevo/audit/audit-core-contract.json
OK: exists: /Library/Logs/Eagevo/audit/audit-events.jsonl
OK: exists: /Library/Eagevo/audit/audit-head.json
OK: executable: /usr/local/bin/eagevo-audit
audit_verify: GREEN
entries: 1
last_hash: 8f7e7509856eed7263d0d78b97ab75ee53d026ebbbc64c1e56fddc253d862659
OK: audit_verify_green

== status-core ==
OK: exists: /usr/local/lib/eagevo/status-core-contract.json

== launchd safety check ==
OK: absent: /Library/LaunchDaemons/*eagevo*
OK: absent: /Library/LaunchAgents/*eagevo*
OK: absent: /Users/tostha-dev/Library/LaunchAgents/*eagevo*

warnings: 0
overall: GREEN
```

## eagevo-audit verify

```text
audit_verify: GREEN
entries: 1
last_hash: 8f7e7509856eed7263d0d78b97ab75ee53d026ebbbc64c1e56fddc253d862659
```

## Boundary

No automatic status collection, no automatic audit collection, no LaunchDaemon, no LaunchAgent, no enforcement, no AI runtime, no agent execution, no external logging.
