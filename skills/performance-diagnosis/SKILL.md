---
name: performance-diagnosis
description: Investigates changes in Google Ads or Meta Ads performance with AdNeuron, including spend, clicks, selected outcomes, pixel activity, ad-set learning and creative evidence. Use for why-results-changed or troubleshooting questions.
---

# Performance diagnosis

Read `references/adneuron-rules.md` first. Separate observations, missing evidence and hypotheses.

## Start with the change

1. Resolve the selected account, intended result and requested dates. Choose a tool that supports
   that scope; disclose limitations instead of translating yesterday into a week automatically.
2. `explain_change` supports CTR, ROAS, spend, conversions, impressions and clicks, over its
   current 7/30/60/90-day equal completed-day windows. Use only an applicable returned metric.
   For CPA/CPC, obtain compatible spend and the exact result/click counts; a missing outcome or
   zero denominator keeps the ratio unavailable. Do not compare different populations/windows.
3. Read the tool's source/freshness/coverage and compare the actual returned windows. A recent
   sync timestamp alone is not proof of complete or comparable measurement. When relevant,
   `get_platform_connection_health` checks stored connection/sync status; it does not establish
   that events fire or explain why performance changed.

## Choose one relevant next check

| Question | Tool and boundary |
|---|---|
| Website events missing or pixel selection | `list_meta_pixels`, then `get_meta_pixel_stats` for the selected account/pixel |
| Is the selected ad set learning? | Resolve it with `list_meta_ad_sets`, then `get_meta_learning_status` using its required AdNeuron UUID |
| What creative/configuration is in an ad? | `get_meta_ad_creatives` and the selected account's ad list |
| What does Meta ad performance show? | `analyze_meta_ad_performance`, only when its returned readiness/coverage allows it |
| Is fatigue evidence available? | `detect_meta_creative_fatigue`; missing/unsupported diagnostics remain unavailable |
| Google query, targeting or review issue | `analyze_google_search_terms`, `get_google_campaign_targeting` or `get_google_ad_policy_violations`, as relevant |

Do not run this table as a checklist or inspect every ad set automatically. Listed tools or
formats may be gated; follow unavailable, reconnect, partial and pending responses honestly.

## Explain clearly

- Show actual current/prior values and supported changes with spend/result volume and dates.
- Pixel stats cover 1–7 rolling UTC days including today, separate from ad-attributed campaign
  results. Present their returned event view/visual data; no invented bucket totals, prior-period
  comparison, low/normal/as-expected assessment or learning conclusion from website counts.
- Learning is Meta's status for one selected ad set. Unknown means unknown, not completed or
  healthy. Learning and pixel activity do not establish a universal event threshold or a cause.
- Native fatigue evidence needs its exact source, scope, metric and period. Frequency alone
  proves neither saturation nor fatigue; do not fabricate scores, recommendations or diagnostic
  fields. If the tool is unavailable, retain usable performance without a fatigue verdict.
- Label explanations as observed or still to verify. Suggest one useful next action based on
  the evidence; any campaign/budget change follows the separate approval rules.
