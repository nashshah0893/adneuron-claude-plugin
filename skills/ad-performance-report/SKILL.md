---
name: ad-performance-report
description: Builds a performance report for connected Google Ads and Meta Ads accounts using AdNeuron. Use when the user asks "how are my ads doing", "summarize my Google Ads", "Meta ads performance last week", "top campaigns", "best ROAS campaigns", "compare Google vs Meta", "how do we compare to industry benchmarks", or wants a weekly or monthly ad report.
---

# Ad Performance Report

Turn AdNeuron's synced data into a clear, accurate performance report.

## Before calling tools

1. Read `references/adneuron-rules.md` once per conversation and follow it throughout.
2. Settle scope from the request without asking unless truly ambiguous:
   - **Accounts**: all connected accounts by default; one account if the user names it (match against `list_accounts`).
   - **Window**: 7 days by default; map other requests to 7/30/60/90 per the rules.

## Pick the right tool

| User wants | Call |
|---|---|
| Overall performance summary | `get_performance_summary` (`lookback_days`, optional `account_id`) |
| Best or biggest campaigns | `list_top_performers` (`sort_by`: spend, roas, conversions, clicks; `limit`) |
| Google Ads vs Meta Ads | `compare_platforms` |
| Industry comparison | `get_benchmark` (call `get_brand_profile` only if the user asks which industry is used) |
| Shareable multi-account report | `generate_report` (`include_ai_summary: true` only if asked for an executive summary) |

Answer most "how are my ads doing" questions with `get_performance_summary` plus, when a campaign breakdown helps, one `list_top_performers` call. Don't call more than three tools for a standard report.

## Build the answer

1. **Headline** (2-3 sentences): spend, primary results (conversions or conversion value), cost per result or ROAS, and the most important takeaway.
2. **Key metrics table**: spend, impressions, clicks, CTR, CPC, conversions, CPA, conversion value and ROAS when returned. One row per account or platform; separate currencies.
3. **Campaigns**: top campaigns with spend, results and efficiency; call out the strongest and weakest.
4. **Benchmarks** (only if fetched): user's CTR, CPC, conversion rate and ROAS vs. the industry average, noting the benchmark source the tool reports (WordStream 2024).
5. **Platform comparison** (only if fetched): describe each platform's results without recommending a budget split. `compare_platforms` does not authorize allocation advice, because attribution and freshness differ between platforms.
6. **Scope line**: window, timezone, currency, last sync, and any unavailable metrics or sample accounts.
7. Offer one follow-up: explain a change (`performance-diagnosis`), check budgets (`budget-review`), or scan for waste (`waste-audit`).

## Do not

- Do not invent metrics the tools didn't return, and don't compute ROAS without conversion value.
- Do not treat the report as permission to change campaigns; recommend changes and let the user decide.
