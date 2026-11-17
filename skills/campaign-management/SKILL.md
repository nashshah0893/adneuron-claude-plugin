---
name: campaign-management
description: Guides changes the user asks for on existing Google Ads and Meta Ads campaigns with AdNeuron — pause or resume, budgets, bids, names, dates, targeting, keywords, ads and removal. Shows the exact change and gets the user's explicit yes before any change.
---

# Change an existing campaign

Read `references/adneuron-rules.md`. This skill guides a change the user asked for; it never
supplies spend authority and makes no change on its own.

## Find the right object and tool

1. Resolve the account with `list_accounts`, then the exact campaign, ad set/ad group or ad with
   the platform's live lists (`list_google_campaigns`, `list_google_ad_groups`,
   `list_meta_campaigns`, `list_meta_ad_sets`, `list_meta_ads`). Don't pick the first similar
   name; ask only if the user's choice is ambiguous.
2. Pick the tool that matches the change. AdNeuron's tools are named by what they do — for
   example `pause_*`/`resume_*` for on/off, `update_*` for budgets, settings, targeting, keywords
   and ads, `remove_*` for removal. Use the tool list the server provides and read its
   description; it says what to show the user and which current values to pass.
3. If no tool covers the change, say so plainly and explain where to make it in Google Ads or
   Meta Ads Manager. Don't substitute a different change.

## Show, confirm, change

1. Read the current values the tool needs (for example from `get_google_campaign_details`,
   `get_meta_campaign_details` or the live lists) and show current and new values side by side,
   in the account currency. Say what the change does: pausing stops ads; resuming can start
   spending; a daily budget is an average, and some days spend more.
2. Get the user's explicit yes for exactly that change. Then call the tool once.
3. Report what the reply says:
   - Done: show the new value the reply read back.
   - Changed since you showed it: nothing was sent; show the current value and ask again.
   - Already in place: say so; nothing else was changed.
   - Uncertain or failed: say what's known, follow the reply's `next_step`, and don't repeat
     the change blindly.
4. A change affects only the object named. Follow the reply's `next_step` to check related
   objects (for example, a resumed campaign whose ad sets are still paused).

## Do not

- Don't change several objects in one step unless the tool says it does; one object per call.
- Don't apply an AdNeuron finding or your own suggestion without the user asking for that
  exact change.
- Don't remove anything the user didn't name. For Meta "delete", ask whether to archive or
  delete permanently. Google removal is permanent.
