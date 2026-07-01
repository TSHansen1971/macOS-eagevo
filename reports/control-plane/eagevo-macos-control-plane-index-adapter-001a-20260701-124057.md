# EAGEVO-MACOS-CONTROL-PLANE-INDEX-ADAPTER-001A Report

## Result

GREEN

## Created UTC

2026-07-01T12:40:57Z

## Start head

d7ca5e2

## Control-plane before audit append

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
OK: exists: /usr/local/lib/eagevo/macos-adapter/adapter-contract.json
OK: exists: /usr/local/lib/eagevo/macos-adapter-discovery.json
OK: exists: /Library/Eagevo/evidence/macos-discovery.json
OK: executable: /usr/local/bin/eagevo-status
OK: executable: /usr/local/bin/eagevo-baseline
OK: executable: /usr/local/bin/eagevo-audit
OK: executable: /usr/local/bin/eagevo-control-plane
OK: executable: /usr/local/bin/eagevo-macos-adapter
OK: control_plane_index_sha256: 0436263aad7b518c8903dadbc6f79edc9995e6fa9adca9e0541cd0c2707bc224
OK: baseline_manifest_sha256: a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e
OK: macos_adapter_evidence_sha256: 4da45d4d0de813b6b62809b0ea473722fa5c5b6a96367704ec5f70744c7174b2
audit_verify: GREEN
entries: 4
last_hash: 94787bcb4b1f3f2c43a84261a43625d8174a9a2be12f608d28ad30c2a90c013e
OK: audit_verify_green
OK: macos_adapter_verify_green
OK: absent: /Library/LaunchDaemons/*eagevo*
OK: absent: /Library/LaunchAgents/*eagevo*
OK: absent: /Users/tostha-dev/Library/LaunchAgents/*eagevo*

overall: GREEN

components: 6
repo_head_short: d7ca5e2
updated_by_step: EAGEVO-MACOS-CONTROL-PLANE-INDEX-ADAPTER-001A
```

## Audit append

```text
appended_sequence: 5
entry_hash: 30a2a4f2040f03dcd7e215a8261d07f399bacaf6aaa26d117823aec12a4b19ce
```

## Control-plane after audit append

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
OK: exists: /usr/local/lib/eagevo/macos-adapter/adapter-contract.json
OK: exists: /usr/local/lib/eagevo/macos-adapter-discovery.json
OK: exists: /Library/Eagevo/evidence/macos-discovery.json
OK: executable: /usr/local/bin/eagevo-status
OK: executable: /usr/local/bin/eagevo-baseline
OK: executable: /usr/local/bin/eagevo-audit
OK: executable: /usr/local/bin/eagevo-control-plane
OK: executable: /usr/local/bin/eagevo-macos-adapter
OK: control_plane_index_sha256: 0436263aad7b518c8903dadbc6f79edc9995e6fa9adca9e0541cd0c2707bc224
OK: baseline_manifest_sha256: a6721a9b0f2eee4ee1da4d41ae3584bc4a2e4de2c87bc737c2f0ca6e1d46d03e
OK: macos_adapter_evidence_sha256: 4da45d4d0de813b6b62809b0ea473722fa5c5b6a96367704ec5f70744c7174b2
audit_verify: GREEN
entries: 5
last_hash: 30a2a4f2040f03dcd7e215a8261d07f399bacaf6aaa26d117823aec12a4b19ce
OK: audit_verify_green
OK: macos_adapter_verify_green
OK: absent: /Library/LaunchDaemons/*eagevo*
OK: absent: /Library/LaunchAgents/*eagevo*
OK: absent: /Users/tostha-dev/Library/LaunchAgents/*eagevo*

overall: GREEN

components: 6
repo_head_short: d7ca5e2
updated_by_step: EAGEVO-MACOS-CONTROL-PLANE-INDEX-ADAPTER-001A
```

## Status

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
entries: 4
last_hash: 94787bcb4b1f3f2c43a84261a43625d8174a9a2be12f608d28ad30c2a90c013e
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

## Adapter verify

```text
== eagevo-macos-adapter ==
mode: read-only-evidence
enforcement: disabled
launchd: disabled

OK: exists: /usr/local/lib/eagevo/macos-adapter/adapter-contract.json
OK: exists: /usr/local/lib/eagevo/macos-adapter-discovery.json
OK: exists: /Library/Eagevo/evidence/macos-discovery.json
OK: evidence_sha256: 4da45d4d0de813b6b62809b0ea473722fa5c5b6a96367704ec5f70744c7174b2
OK: eagevo_launchd_match_count: 0

overall: GREEN
```

## Audit verify after append

```text
audit_verify: GREEN
entries: 5
last_hash: 30a2a4f2040f03dcd7e215a8261d07f399bacaf6aaa26d117823aec12a4b19ce
```

## Control-plane index parity

```text
0436263aad7b518c8903dadbc6f79edc9995e6fa9adca9e0541cd0c2707bc224  /usr/local/lib/eagevo/control-plane-index.json
0436263aad7b518c8903dadbc6f79edc9995e6fa9adca9e0541cd0c2707bc224  /Library/Eagevo/control-plane-index.json
```

## Adapter evidence parity

```text
4da45d4d0de813b6b62809b0ea473722fa5c5b6a96367704ec5f70744c7174b2  /usr/local/lib/eagevo/macos-adapter-discovery.json
4da45d4d0de813b6b62809b0ea473722fa5c5b6a96367704ec5f70744c7174b2  /Library/Eagevo/evidence/macos-discovery.json
```

## Boundary

Read-only control-plane index update. No automatic collection, no LaunchDaemon, no LaunchAgent, no enforcement, no AI runtime, no agent execution, no external logging.
