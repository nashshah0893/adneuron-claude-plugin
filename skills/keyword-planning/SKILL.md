---
name: keyword-planning
description: Plans Google Ads keywords, budgets and campaign types with AdNeuron's Keyword Planner access. Use when the user asks for "keyword ideas", "search volume for", "how much would it cost to advertise on", "what budget do I need", "which campaign type should I use", "Search vs Performance Max", or wants to plan a new Google Ads campaign.
---

# Keyword and Campaign Planning

Help the user plan a new or expanded Google Ads effort: keywords, expected costs, and campaign type.

## Before calling tools

1. Read `references/adneuron-rules.md` once per conversation and follow it.
2. Keyword tools need a connected Google Ads account `id` from `list_accounts` (used only for Keyword Planner access). If there's no Google Ads account, offer `connect_account` with `google_ads`.
3. Gather from the conversation: product or service, 1-10 seed keywords, target country (ISO code, default US) and language (default en). Ask only for what's missing and essential.

## Workflow

1. **Ideas**: call `research_keywords` with `seed_keywords`, `account_id`, `country_code`, `language`. Returns ideas with search volume, competition and estimated CPC.
2. **Shortlist**: group ideas by intent (high-intent/transactional, research, brand, irrelevant). Propose up to 20 target keywords, leaving out irrelevant and very low-volume terms, and suggest obvious negative keywords.
3. **Budget**: after the user agrees on the shortlist (or if they asked for a budget directly), call `get_budget_recommendation` with `account_id`, `keywords` (max 20) and `target_location`. Present the Conservative, Moderate and Aggressive tiers with estimated clicks and spend.
4. **Campaign type** (if they're planning a campaign): call `select_google_campaign_type`. It uses the brand profile and connected accounts; present the top recommendation and its reasons.

## Build the answer

- **Keyword table**: keyword, monthly searches, competition, estimated CPC, intent group.
- **Budget tiers table** when fetched, plus which tier fits the user's stated budget or goals.
- **Recommended setup**: campaign type, ad-group themes from the intent groups, starter negative keywords.
- State that Keyword Planner figures are historical estimates, not guarantees.
- If the user wants to create the campaign, give them the setup to build in Google Ads. Any change made through AdNeuron needs their explicit approval; if AdNeuron says campaign creation isn't available yet, say so.
