---
name: keyword-planning
description: Researches Google Ads keyword ideas, historical cost estimates and campaign planning with AdNeuron. Use for search volume, keyword themes, budget options or planning a Google Search campaign; does not promise traffic or create a campaign automatically.
---

# Keyword and campaign planning

Read `references/adneuron-rules.md` first.

1. Resolve a connected Google Ads account with `list_accounts`; Keyword Planner uses that
   account's access. Gather the business/service, location and language from existing context.
   Ask only for essential missing details; do not silently assume US or English from API defaults.
2. Call `research_keywords` with the relevant account, 1–10 seed keywords, country and language,
   following the live schema. Show returned volume, competition, CPC/currency and limitations as
   historical estimates, never guaranteed clicks, sales or current auction prices.
3. Group ideas by intent and relevance. Low volume alone does not make a high-intent keyword
   unsuitable. Present a short, reasoned shortlist and clearly label suggested negatives.
4. When useful, call `get_budget_recommendation` for a chosen shortlist (maximum 20 keywords)
   and location. Describe returned Conservative/Moderate/Aggressive tiers as modelled scenarios;
   estimated traffic shares are assumptions, not outcomes or a reason to spend more automatically.
5. For a new campaign, use `select_google_campaign_type` and its actual supported-family guidance.
   Do not rank unsupported campaign types or promise a full Performance Max lifecycle.
6. Present a concise keyword table, optional scenario comparison, suggested structure and one
   follow-up. If the user wants to create the campaign, continue with `campaign-creation` using
   the real prepare/confirm/execute route when available. Do not default to manual Ads Manager
   instructions when AdNeuron can handle it; if it cannot, explain that specific limitation.

No native account changes occur during research. Approval of keyword ideas is not approval to
create, activate or change spend. Existing-account optimization recommendations retain the
separate AdNeuron approval requirement.
