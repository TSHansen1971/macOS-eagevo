# EAGEVO-MACOS-MILESTONE-001A Report

## Result

GREEN

## Created UTC

2026-06-30T22:31:56Z

## Snapshot

{4070d86d-ccc8-456c-9a65-d125b58a8c19}

## Repo HEAD before milestone commit

47953e31969f23105e71fc0d0281785634663dfb

## eagevo-control-plane status

```text
== eagevo-control-plane ==
mode: read-only-index
enforcement: disabled
launchd: disabled

OK: exists: /usr/local/lib/eagevo/foundation-contract.json
OK: exists: /usr/local/lib/eagevo/audit/audit-core-contract.json
OK: exists: /usr/local/lib/eagevo/status-core-contract.json
OK: exists: /usr/local/lib/eagevo/baseline-manifest.json
OK: exists: /Library/Eagevo/baseline-manifest.json
OK: exists: /usr/local/lib/eagevo/control-plane-index.json
OK: exists: /Library/Eagevo/control-plane-index.json
OK: executable: /usr/local/bin/eagevo-status
OK: executable: /usr/local/bin/eagevo-baseline
OK: executable: /usr/local/bin/eagevo-audit
OK: executable: /usr/local/bin/eagevo-control-plane
OK: control_plane_index_sha256: 938c46fb6d97d0747b5f3ce7a3f3bb8fefa73a9808e12784e09ed681af2f3aba
OK: baseline_manifest_sha256: a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e
audit_verify: GREEN
entries: 3
last_hash: 9e77172451d55337c3f510161e09849b30cfa45a599d649242bc0d1086a343e6
OK: audit_verify_green
OK: absent: /Library/LaunchDaemons/*eagevo*
OK: absent: /Library/LaunchAgents/*eagevo*
OK: absent: /Users/tostha-dev/Library/LaunchAgents/*eagevo*

overall: GREEN

components: 5
repo_head_short: f4ddd1c
```

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
entries: 3
last_hash: 9e77172451d55337c3f510161e09849b30cfa45a599d649242bc0d1086a343e6
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
entries: 3
last_hash: 9e77172451d55337c3f510161e09849b30cfa45a599d649242bc0d1086a343e6
```

## Parity

```text
938c46fb6d97d0747b5f3ce7a3f3bb8fefa73a9808e12784e09ed681af2f3aba  /usr/local/lib/eagevo/control-plane-index.json
938c46fb6d97d0747b5f3ce7a3f3bb8fefa73a9808e12784e09ed681af2f3aba  /Library/Eagevo/control-plane-index.json
a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e  /usr/local/lib/eagevo/baseline-manifest.json
a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e  /Library/Eagevo/baseline-manifest.json
```

## Boundary

No automatic status collection, no automatic audit collection, no LaunchDaemon, no LaunchAgent, no enforcement, no AI runtime, no agent execution, no external logging.

## System change

None.
