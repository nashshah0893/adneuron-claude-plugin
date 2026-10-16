---
name: ga4-analysis
description: Analyzes Google Analytics 4 traffic, conversions and attribution through AdNeuron. Use when the user asks about GA4, website traffic, sessions, users, "which channels drive conversions", "paid vs organic", "attribution paths", "bot traffic", "traffic quality", "GA4 events", or "does GA4 match Google Ads".
---

# GA4 Analysis

Answer website analytics questions from the user's connected GA4 property, and connect them back to ad performance.

## Before calling tools

1. Read `references/adneuron-rules.md` once per conversation and follow it.
2. Every GA4 tool needs `account_id` as the GA4 property ID in the form `properties/123456`. Find it in `list_accounts`. If there are several properties, ask which one; if there is none, say GA4 isn't connected to AdNeuron.
3. GA4 tools take `days` from 7 to 90 (default 30).

## Pick the right tool

| User wants | Call |
|---|---|
| Traffic volume | `get_ga4_sessions`, `get_ga4_users` |
| Which channels perform | `get_ga4_channel_performance` |
| Paid vs. organic | `get_ga4_paid_vs_organic` |
| Conversions | `get_ga4_conversions` |
| Specific events | `get_ga4_events` with `event_names` (e.g. `["purchase", "sign_up"]`) |
| Conversion paths | `get_ga4_attribution` with `conversion_event` (default `purchase`) |
| Bots and low-quality traffic | `get_ga4_traffic_quality` |
| GA4 vs. Google Ads conversion gap | `detect_ga4_discrepancy` |

Use the one or two tools that answer the question; don't sweep every GA4 tool.

## Build the answer

- **Answer first** in 1-2 sentences.
- **Table** of the relevant metrics by channel, source or event.
- **Interpretation**: what it means for the ad accounts. Example: paid search sessions with a high bounce rate point to landing-page or keyword-intent problems; high bot share from a source means that source's ad clicks may be inflated.
- When GA4 and ad-platform numbers differ, explain that GA4 uses its own attribution model and session-based counting, so some difference is expected; flag only large or systematic gaps.
- **Scope line**: property, window, and timezone if returned.
