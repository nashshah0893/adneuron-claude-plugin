---
name: waste-audit
description: Finds wasted ad spend and tracking problems in Google Ads and Meta Ads using AdNeuron. Use when the user asks "where am I wasting money", "audit my ad account", "find wasted spend", "are my conversions tracking correctly", "health check my ads", "negative keyword gaps", or "any anomalies in my campaigns".
---

# Waste and Tracking Audit

Find spend that isn't producing results and confirm conversion data can be trusted.

## Before calling tools

Read `references/adneuron-rules.md` once per conversation and follow it.

## Workflow

1. Call `scan_for_waste` (`lookback_days`, default 30). It returns prioritized findings from AdNeuron's detectors: budget waste, stale campaigns, negative-keyword gaps and anomalies. If it returns no findings, say the scan has no results yet and that a fresh account sync in AdNeuron will populate it; don't conclude the account is waste-free.
2. Call `audit_conversion_tracking` to check token status, sync recency and account coverage per platform.
3. If the user has a GA4 property connected (a GA4 entry in `list_accounts`) and asks whether conversions are accurate, call `detect_ga4_discrepancy` with the GA4 property ID (format `properties/123456`). It flags double-counting or under-counting between Google Ads and GA4.

## Build the answer

- **Headline**: estimated wasted spend in the window (per currency) and the single biggest fix.
- **Findings table**, highest priority first: finding, campaign or ad group, wasted spend, evidence, recommended action.
- **Tracking health**: per platform, connection status, last sync, and any GA4 discrepancy with its likely cause (duplicate tags, different attribution windows, missing conversion import).
- **Action plan**: up to 5 steps in priority order. Mark which ones the user does in the ad platform and which `campaign-changes` can help with after confirmation.
- **Scope line**: window, timezone, currency, last sync.

## Do not

- Do not call a finding confirmed waste if the tracking audit shows stale data or broken conversion tracking; flag it as unverified until tracking is fixed.
- Do not make changes from this skill.
