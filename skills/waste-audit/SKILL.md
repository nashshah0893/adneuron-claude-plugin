---
name: waste-audit
description: Reviews AdNeuron's stored open workspace waste findings and data-health evidence. Use for suspected wasted spend or connection health. The legacy findings list does not establish a requested period, affected account or verified monetary loss.
---

# Waste and data-health review

Read `references/adneuron-rules.md` first.

## What the current findings tool establishes

`scan_for_waste` returns at most 100 open workspace findings, ordered by its stored estimate,
without a continuation cursor. Although it accepts `lookback_days` and echoes `period_days`,
its current query does not filter findings by that period. Do not describe these rows as this
week's/month's waste or a completed audit of the requested dates. `created_at` dates the finding
record; it does not establish when the underlying spend happened.

The response includes finding identifiers, type, severity, title, description, status, creation
time and a legacy estimate field. It does not provide structured account/campaign identifiers,
source evidence or a verified currency for each finding. A name in a title/description is a
clue, not a verified account association. Never attribute a row to the selected account merely
because the user selected it or a description sounds relevant.

## Workflow

1. State the limitation before presenting results: these are open workspace findings, with the
   requested period and account attribution unverified. Show only returned fields. The 100-row
   bound means the response is not an exhaustive inventory when more findings may exist.
2. If the user asked for an account/date-specific assessment, offer a separately supported
   scoped performance/query read for that selected account and window. Keep that evidence
   separate; it does not retroactively prove a stored finding's identity, period or cause.
3. When freshness/access is in question, `get_platform_connection_health` checks stored
   connection/sync data. It does not verify events, all reporting history or the findings' dates.
4. No findings means none returned. It does not prove the account is waste-free, the detector
   ran, or a sync will necessarily create findings. Follow any supported refresh guidance.
5. Present a concise table of the available title/type, severity, record date and status, plus
   limitations and one useful next check. Do not invent evidence, account labels or campaign IDs.
6. Do not treat `estimated_waste_usd` as proof of USD, a compatible currency, a requested-period
   loss or actual recoverable savings. By default withhold monetary-loss totals until scope,
   currency and evidence are independently established. If the user requests raw fields, retain
   the source field name and explicitly label its currency/period/evidence as unverified.
7. A detector suggestion is not a measured cause or executable plan. A supported optimization
   recommendation still requires the separate authenticated AdNeuron approval route; never
   execute it through a user-requested route merely because the user asked for an audit.
