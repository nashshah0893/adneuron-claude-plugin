---
name: campaign-creation
description: Guides a user-requested Google Search or supported Meta image, video or carousel campaign through AdNeuron's draft, preview/preparation, exact confirmation and paused creation flow. Use when the user wants to create or launch a new campaign, subject to live tool availability.
---

# Create a campaign with the user

Read `references/adneuron-rules.md`. Use the current tool schema and returned `next_step`;
this skill never enables an unavailable recipe, account or write route.

## Understand and draft

1. Resolve the selected business, account and currency. Infer known business context from the
   conversation or `get_brand_profile` when useful. Ask what people should do after seeing the
   ad if the goal is missing. Do not default every advertiser to purchases or ask for every field.
2. Call `select_meta_campaign_type` or `select_google_campaign_type` for actual supported options.
   Recommend one suitable available option and explain why. If a family/destination is unavailable,
   disclose that limit rather than silently changing it. Meta special ad categories must follow
   the live guide; do not bypass restrictions by relabelling the business or audience.
3. Draft copy, targeting, budget and schedule from the user's brief and account-local assets.
   Label suggestions and their reasons. Resolve names with the available lookups: Meta Page,
   Instagram, pixel, targeting and media discovery; Google location search and keyword research
   as needed. Never invent native references, use another client's assets, or silently accept a
   platform default the user has not seen.
4. Media intake/upload is a separate confirmed operation when needed; use `campaign-media`.
   Prefer a compatible existing account-local asset. Never upload or activate merely to preview.

## Meta: preview → numbered plan → create

| Selected format | Preview | Create after confirmation |
|---|---|---|
| Single image | `preview_meta_image_campaign` | `create_meta_image_campaign` |
| Video | `preview_meta_video_campaign` | `create_meta_video_campaign` |
| Carousel | `preview_meta_carousel_campaign` | `create_meta_carousel_campaign` |

1. Explain that a new preview can replace this member's earlier waiting Meta creation plan for
   the account, including an incomplete edit. Earlier Create cards become unusable; cancellation
   cannot be undone. Do not preview to inspect progress or recover an uncertain launch.
2. Send everything known so far using the selected preview's schema. Follow its grouped missing
   fields and `next_step`; ask only for information the assistant cannot draft or look up. An
   incomplete preview is not permission to use an older ready plan.
3. Show the returned display/card and exact ready plan: account, goal, budget and currency,
   schedule, audience, identity, assets/copy, standard settings and paused outcome. Preserve any
   spending caveats. A daily budget is not a guaranteed daily charge; lifetime is a total.
4. Obtain the user's explicit confirmation naming the latest Plan N. A numbered Create button
   counts only if it posts that exact user's message. It is not a separate AdNeuron approval.
5. Call the matching create tool with the exact returned `plan_id` and `plan_number`; never
   reconstruct an old one-call payload, reuse an older confirmation or fabricate a number.
6. For edits, expiry or supersession, obtain a fresh ready plan and new confirmation. Preserve
   launch IDs and uncertainty; do not preview/create another plan to retry an ambiguous result.

## Google Search: prepare → confirm → execute

1. Use `prepare_google_search_campaign_for_user_request` only for the campaign the user requested.
   Follow its supported inputs, prerequisites, immutable plan and correction guidance.
2. Show the exact prepared campaign and spend, and obtain the required explicit confirmation.
3. Use `execute_user_requested_google_search_campaign_create` only with that exact returned plan
   and the current authority the server requires. Preparation or keyword approval is not execution.
4. If this is an AdNeuron-originated recommendation rather than the user's requested campaign,
   follow the separate approval route; do not substitute the user-requested route.

## Report the actual outcome

- Use the saved creation response: created/paused, partial, pending, uncertain or unavailable.
  Never claim every object exists, Meta approved it, or ads are live from a preview or receipt.
- For Meta launch progress, use `get_meta_campaign_launch_status` on the original plan. It reports
  stored launch progress, not current serving. Follow the returned recovery route for other runs.
- Creation and activation are separate decisions. Offer `campaign-management` only when the
  returned state says activation is possible; confirm the activation itself. Never resume an
  ended schedule or uncertain/incomplete campaign merely because creation was requested.
