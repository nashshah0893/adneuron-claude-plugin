---
name: campaign-creation
description: Helps the user plan and create a new Google Ads or Meta Ads campaign with AdNeuron. Drafts the campaign, shows every setting, gets the user's explicit yes, and creates it paused. Turning it on is a separate, confirmed step.
---

# Create a campaign with the user

Read `references/adneuron-rules.md`. Follow the server's current tools and each reply's
`next_step`; this skill never enables a campaign type the server doesn't offer.

## Choose what to build

1. Resolve the account and its currency with `list_accounts`. Use the conversation and, when
   useful, `get_brand_profile`. If the goal is missing, ask what people should do after seeing
   the ad; don't default everyone to purchases.
2. Call `select_google_campaign_type` or `select_meta_campaign_type`. They list the campaign
   types AdNeuron can create now, what each needs and which tools to call. Recommend one that
   fits and say why. If the type the user wants isn't offered, say so; don't switch silently.

## Draft

1. Draft the campaign from the user's brief: name, budget and currency, schedule, locations and
   audience, keywords (Google Search) or targeting (Meta), ads and copy, destination URL.
   Label what you suggested and why.
2. Look up IDs with the server's tools: locations and targeting searches, Meta Pages,
   Instagram accounts, pixels, audiences, and images or videos already in the account. Never
   invent an ID, hash or link.
3. For new images or videos, use the `campaign-media` skill first.
4. Say any default the user hasn't seen. For example, if no location is given, Google may
   default to the United States: say so before asking for the yes.

## Confirm and create

1. Show the complete campaign: account, campaign type, budget and currency, schedule, locations
   and audience, ad groups/ad sets, keywords, every ad's copy and media, and that it will be
   created paused. A daily budget is an average, and some days spend more; a lifetime budget is
   a total.
2. Get the user's explicit yes for exactly what you showed. Then call the matching create tool
   once with exactly those values.
3. If anything changes after the yes, show the new version and ask again.
4. If the reply says the same campaign was just created, show it and ask whether they want
   another; don't resend on your own.

## After creating

- Report what the reply says was created, with its IDs and status. Created paused is not
  approved by the platform or serving.
- If the result is partial or uncertain, say what's known and follow the reply's `next_step`;
  don't create it again to "retry".
- Turning the campaign on is a separate change: offer it, and if the user wants it, follow the
  `campaign-management` skill (show it, get a yes, then resume).
