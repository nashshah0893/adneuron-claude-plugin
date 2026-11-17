---
name: budget-review
description: Reviews Google Ads and Meta Ads budget ownership, spend pacing and a user's budget target with AdNeuron. Use for budget totals, spending pace, underspend or allocation questions. Does not execute changes.
---

# Budget review

Read `references/adneuron-rules.md` before calling tools.

## Workflow

1. Resolve the selected business/accounts and currencies. Use the user's stated monthly target
   and dates if supplied; do not invent a spending target or mix unrelated clients.
2. Read budgets live for each relevant account. Google: `list_google_campaigns` (each campaign's
   own budget) and `list_google_shared_budgets` (budgets shared by several campaigns, with their
   period). Meta: `list_meta_campaigns` (campaign budgets) and `list_meta_ad_sets` (ad-set
   budgets; null when the campaign holds the budget). Respect the real owner: count a shared
   Google budget once, never once per campaign, and never add a Meta campaign budget to the
   budgets of its own ad sets. State each budget's period; a shared budget isn't always daily.
3. Get compatible actual spend using `get_performance_summary` or a targeted performance tool.
   Match each owner to its actual member campaigns/ad sets and dates. Account-wide spend cannot
   stand in for one ad-set's spend; a partial listing is not the owner's complete population.
4. Calculate pacing only when the denominator, observed complete days, ownership and coverage
   are known. Report a lifetime budget as a total; remaining/daily equivalents need the actual
   remaining budget and schedule. Never imply a daily spending target or cap is a guaranteed pace.
5. Label a projection as a simple extrapolation of the observed period, state the days used and
   compare it only with the user's compatible target/currency. No universal healthy-utilization
   bands, fixed 30-day calendar assumption or guarantee that more budget scales results.
6. If budget ownership or history is unresolved, preserve usable budget data and say pacing is
   unavailable. Follow any returned refresh guidance; a fresh sync is not a guaranteed repair.

## Answer

- Lead with what can be established about the user's target and pacing.
- Show owner, currency, native daily/lifetime budget, compatible observed spend, dates and any
  supported projection in a compact table/chart. Keep unknowns visible.
- Describe possible causes of a gap as hypotheses. Average CPA/ROAS and a large spend share do
  not establish incremental returns or justify moving money by themselves.
- Recommend investigation or a change only when the selected measurement and evidence support
  it. If the user asks for a change, use `campaign-management`: show it and get an explicit yes.
  This review itself makes no account changes.
