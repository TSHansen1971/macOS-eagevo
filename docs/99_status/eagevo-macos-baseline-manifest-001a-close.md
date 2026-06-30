# EAGEVO-MACOS-BASELINE-MANIFEST-001A-CLOSE

## Result

GREEN

## Closed UTC

2026-06-30T21:59:08Z

## Scope

Closed the first baseline-manifest baseline for macOS-eagevo.

## Snapshot

{367f1c0f-c130-4c51-bec0-0f9a8dc5a28f}

## Manifest SHA256

a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e

## Manifest path verification

/usr/local/lib/eagevo/baseline-manifest.json: a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e

/Library/Eagevo/baseline-manifest.json: a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e

## Verification: eagevo-status

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
entries: 2
last_hash: 44485971e4934c690d98076d310f335d23550ae9d737f367963607d9324fd2b1
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

## Verification: eagevo-audit verify

```text
audit_verify: GREEN
entries: 2
last_hash: 44485971e4934c690d98076d310f335d23550ae9d737f367963607d9324fd2b1
```

## Verification: eagevo-baseline verify

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
entries: 2
last_hash: 44485971e4934c690d98076d310f335d23550ae9d737f367963607d9324fd2b1
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

## Security boundary

No automatic status collection, no automatic audit collection, no LaunchDaemon, no LaunchAgent, no enforcement, no AI runtime, no agent autonomy, no agent tool execution, and no external logging.
