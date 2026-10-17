---
name: budget-review
description: Reviews budgets, spend pacing and budget allocation for Google Ads and Meta Ads accounts using AdNeuron. Use when the user asks "how much am I spending", "am I on track with my budget", "are we overspending", "budget pacing", "show my budgets", "which campaigns are limited by budget", or "where should I move budget".
---

# Budget Review

Show where budget is set, how fast it's being spent, and where reallocation could help.

## Before calling tools

1. Read `references/adneuron-rules.md` once per conversation and follow it.
2. If the user states a target ("we have $10k a month"), use it as the planned budget.

## Workflow

1. Call `list_ad_budgets` (optional `account_id`, optional `period` DAILY or LIFETIME). It returns budgets grouped by their real owner: a Google Ads shared budget appears once even when several campaigns use it, and Meta ad-set budgets belong to the ad set, not the campaign. Don't double-count shared budgets.
2. Call `get_performance_summary` with `lookback_days: 7` for recent actual spend. Add `list_top_performers` (`sort_by: spend`) only if campaign-level spend isn't already in the results.
3. Compute, per budget owner and in total (per currency):
   - **Daily budget**: the daily amount; for lifetime budgets, remaining budget / remaining days when dates are returned, otherwise report the lifetime amount only.
   - **Average daily spend** = 7-day spend / 7.
   - **Utilization** = average daily spend / daily budget. Label: under-spending (< 80%), healthy (80-105%), at or over budget (> 105%). Google Ads can spend up to 2x the daily budget on a given day while averaging to the budget over a month, so a single-day overshoot isn't an error.
   - **30-day projection** = average daily spend x 30, compared with the user's stated monthly target if given.
4. If `owner_unknown_count` is above zero, say how many campaigns have no resolved budget owner and that a fresh sync in AdNeuron should fix it.

## Build the answer

- **Headline**: total daily budget, average daily spend, projected 30-day spend, and whether that's on track against the user's target.
- **Budget table**: owner (campaign, ad set or shared budget), platform, daily budget, average daily spend, utilization, label. Sort by the largest gap.
- **Allocation insight**: compare each owner's share of spend with its share of conversions or conversion value (from `get_performance_summary`). Flag efficient owners that are budget-limited (at or over budget with good CPA or ROAS) and weak owners taking a large share.
- **Recommendations** (up to 3): specific moves with reasoning. If the user wants to apply one, follow the changes rule in the reference: describe the exact change and that it needs their explicit approval, and explain how to make it in Google Ads or Meta Ads Manager if AdNeuron says it isn't available yet.
- **Scope line**: window, timezone, currency, last sync.

## Do not

- Do not sum budgets across currencies.
- Do not apply budget changes from this skill.
