---
name: waste-audit
description: Reviews AdNeuron's Google Ads and Meta Ads waste findings and data-health evidence. Use for ad-account audits, suspected wasted spend, stale data, negative-keyword gaps or connection health. Findings are not automatically confirmed waste.
---

# Waste and data-health review

Read `references/adneuron-rules.md` first.

1. Use `scan_for_waste` for stored findings over its supported period, and retain each finding's
   scope, evidence, timestamp and status. This scan is workspace-wide: do not present it as a
   complete selected-account audit unless that account's coverage is established.
2. When freshness/access is in question, check `get_platform_connection_health`. Its stored
   token/sync data cannot confirm live events, absence of errors, or complete reporting history.
3. No findings means no findings returned. It does not prove the account is waste-free, that
   the detector ran, or that syncing will necessarily generate findings. Explain the actual
   coverage/readiness information and use returned refresh guidance when applicable.
4. Follow up on an individual finding only with a relevant, scoped performance/query/creative
   read. Preserve stale, missing, unsupported or incomplete evidence rather than guessing loss.
5. Show findings with evidence, affected account/campaign, limitations and one useful next step.
   Treat loss amounts as estimates only if the source supports that interpretation; do not sum
   overlapping estimates, infer recovered savings or turn spend without verified results into
   confirmed waste. Separate currencies and observation periods.
6. Distinguish a detector suggestion from a measured cause or an executable plan. If a change
   is warranted, explain the exact proposal and use AdNeuron's authenticated recommendation
   approval route. This audit does not make changes or use a user-requested route to execute
   an optimization recommendation.
