---
name: performance-diagnosis
description: Diagnoses why Google Ads or Meta Ads results changed, using AdNeuron. Use when the user asks "why did my ROAS drop", "why did conversions go down", "why is CPA up", "why did spend jump", "why did CTR fall", "what happened to my ads this week", or "what's driving the change".
---

# Performance Diagnosis

Explain what drove a change in results and where it happened, separating data problems from real performance changes.

## Before calling tools

1. Read `references/adneuron-rules.md` once per conversation and follow it.
2. Identify the metric and window:
   - `explain_change` supports `metric`: roas, ctr, spend, conversions, impressions, clicks. Map CPA questions to `conversions` plus `spend`, and CPC questions to `clicks` plus `spend`.
   - `lookback_days` 7, 30, 60 or 90 compares that window with the prior window of the same length. "Yesterday" or "this week" → 7.

## Workflow

1. Call `explain_change` with the metric, window and, if the user named one, `account_id`. It returns the comparison and a plain-English diagnosis.
2. For CPA or CPC questions, call `explain_change` a second time for the other component metric, then compute the ratio change yourself.
3. Rule out data problems before trusting a big drop in conversions: call `audit_conversion_tracking` (no arguments) and check token status and sync recency. A stale sync or expired token explains many "sudden drops".
4. Only if campaign detail is still needed, call `list_top_performers` for the same window.

## Build the answer

- **Answer first** (1-2 sentences): the main driver and where it happened.
- **Before vs. after table**: the metric and its components (impressions, CTR, clicks, conversion rate, spend, conversions, ROAS as relevant), previous vs. current and % change.
- **Where**: the campaigns or platform behind most of the change.
- **Causes**: label each as **shown in the data** or **to verify** in Google Ads or Meta Ads Manager (auction competition, creative fatigue, bid strategy learning, tracking edits, landing page issues). Never present a hypothesis as a finding.
- **Tracking check result**: one line confirming tracking and sync look healthy, or what's wrong.
- **Next checks**: 1-3 specific things to look at.
- **Scope line**: both windows, timezone, currency, last sync.

## Do not

- Do not compare windows of different lengths.
- Do not blame performance when the tracking audit shows stale or broken data; lead with the data issue instead.
