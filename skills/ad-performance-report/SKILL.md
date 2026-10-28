---
name: ad-performance-report
description: Reports Google Ads and Meta Ads results with AdNeuron. Use for ad performance summaries, campaign results, top campaigns and platform comparisons. Keeps accounts, currencies, selected outcomes and incomplete data explicit.
---

# Ad performance report

Read `references/adneuron-rules.md` and follow it throughout.

## Workflow

1. Resolve the business/account and requested period from the conversation. Use `list_accounts`
   only when selection is unknown or changed. Default to a seven-completed-day summary when no
   period is given, and disclose it. Inspect the chosen tool's schema for other supported dates.
2. Use the smallest useful report:

   | Question | Tool |
   |---|---|
   | Overall account/workspace results | `get_performance_summary` |
   | Requested campaign ranking | `list_top_performers` |
   | Google versus Meta observations | `compare_platforms` |
   | One campaign, ad set or ad | `get_campaign_performance`, `get_ad_set_performance`, `get_ad_performance` |
   | Meta campaign-period results | `get_meta_campaign_performance` |
   | Google campaign settings and structure | `get_google_campaign_detail`, `get_google_campaign_structure` |
   | Meta ads and configured creatives | `list_meta_ads`, `get_meta_ad_creatives` |

   Resolve targets using the lists/reports and the ID type each tool accepts. Do not assume a
   native campaign ID works everywhere or force sync when the selected tool supports live reads.
3. Read source, actual dates, currency, coverage and `refresh`/pending states before interpreting
   figures. Explain when results are stored while a refresh is still running. Follow continuation
   only when needed to answer the question completely; never call a prefix the best/worst list.
4. For `list_top_performers`, report the actual returned sort and scope. It is workspace-wide;
   do not silently present it as a selected account's complete ranking. A fallback sort by clicks
   is a different descriptive view, not proof of the best business outcome.
5. Show a short headline and a readable table or chart using compatible returned values. Keep
   accounts/currencies separate and show spend and result volume beside efficiency. Name exact
   event definitions; Meta outcome/ROAS fields can remain unavailable even when delivery exists.
6. For an unresolved goal, show usable delivery/named events and ask only the missing question.
   Do not manufacture CPA/ROAS or imply incidental results established a campaign's intent.
7. Close with actual scope/freshness limits and one relevant follow-up. Offer pixel, learning or
   creative diagnostics only when they address the question; use `performance-diagnosis` for
   changes and `budget-review` for budget questions. Recommendations do not authorize changes.

## Limits

- No generic conversions total from overlapping event types or pooled cross-currency headline.
- No causal winner, wasted-spend or budget-allocation claim from descriptive average results.
- Preserve raw mode, missing values, fractional counts and provisional periods.
- Do not promise a report export, benchmark or unavailable diagnostic. Explain a returned limit
  and offer a supported view rather than claiming an absent tool exists.
