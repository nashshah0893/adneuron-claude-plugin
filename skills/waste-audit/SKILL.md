---
name: waste-audit
description: Finds wasted ad spend and stale or disconnected data in Google Ads and Meta Ads using AdNeuron. Use when the user asks "where am I wasting money", "audit my ad account", "find wasted spend", "are my ad connections healthy", "health check my ads", "negative keyword gaps", or "any anomalies in my campaigns".
---

# Waste and Data-Health Audit

Find spend that isn't producing results and confirm the data behind it is fresh enough to trust.

## Before calling tools

Read `references/adneuron-rules.md` once per conversation and follow it.

## Workflow

1. Call `scan_for_waste` (`lookback_days`, default 30). It returns prioritized findings from AdNeuron's detectors: budget waste, stale campaigns, negative-keyword gaps and anomalies. If it returns no findings, say the scan has no results yet and that a fresh account sync in AdNeuron will populate it; don't conclude the account is waste-free.
2. Call `get_platform_connection_health` to check stored token status, last sync time and connected account count per platform. It uses stored data only; it does not verify conversion events or call the ad platforms.

## Build the answer

- **Headline**: estimated wasted spend in the window (per currency) and the single biggest fix.
- **Findings table**, highest priority first: finding, campaign or ad group, wasted spend, evidence, recommended action.
- **Connection health**: per platform, token status, last sync, connected accounts.
- **Action plan**: up to 5 steps in priority order. Say where each one is done (Google Ads or Meta Ads Manager); any change needs the user's explicit approval.
- **Scope line**: window, timezone, currency, last sync.

## Do not

- Do not call a finding confirmed waste if the connection-health check shows stale data or an expired or disconnected token; flag it as unverified until the data is refreshed. This check cannot tell whether conversion events are firing, so don't say tracking is working or broken.
- Do not make changes from this skill.
