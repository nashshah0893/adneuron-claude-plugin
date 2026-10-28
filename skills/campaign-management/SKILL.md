---
name: campaign-management
description: Guides explicitly requested campaign pause/resume, daily budget changes, post-creation activation and supported Meta ad edits using AdNeuron. Distinguishes a user's request from optimization recommendations and requires the correct confirmation or authenticated approval route.
---

# Campaign and budget changes

Read `references/adneuron-rules.md`. Use only the exact operation the user requested and the
currently available tool contract. This skill supplies guidance, never spend authority.

## Establish the change

1. Resolve the business/account and exact campaign or ad; use account-local reports/lists and
   current native reads when needed. Stored launch progress is not proof of current delivery.
   Do not pick the first similarly named campaign or infer internal UUIDs from a native ID.
2. Establish whether the user requested a specific change or AdNeuron suggested an optimization.
   For the latter use the separate authenticated AdNeuron approval route; a chat yes does not
   replace it and does not turn that recommendation into a user-requested operation.
3. Show old/current values when verified and the exact proposed account, targets, amount and
   currency, schedule/status effect and relevant risk. A resume/activation can start spending.
   Never disguise a percentage recommendation as an already-confirmed exact amount.

## User-requested campaign operations

Use the platform's matching pair and its returned fields; never guess an executor payload.

| Operation | Prepare | Execute after exact confirmation |
|---|---|---|
| Google pause | `prepare_google_campaign_pause_for_user_request` | `execute_user_requested_google_campaign_pause` |
| Google resume | `prepare_google_campaign_resume_for_user_request` | `execute_user_requested_google_campaign_resume` |
| Google daily budget | `prepare_google_daily_budget_change_for_user_request` | `execute_user_requested_google_daily_budget_change` |
| New Search campaign activation | `prepare_google_search_activation_for_user_request` | `execute_user_requested_google_search_activation` |
| Meta pause | `prepare_meta_campaign_pause_for_user_request` | `execute_user_requested_meta_campaign_pause` |
| Meta resume | `prepare_meta_campaign_resume_for_user_request` | `execute_user_requested_meta_campaign_resume` |
| Meta daily budget | `prepare_meta_daily_budget_change_for_user_request` | `execute_user_requested_meta_daily_budget_change` |

Preparation does not execute the change. Obtain the required explicit confirmation of the exact
returned plan before calling its user-requested executor. Changed targets/content, expiry or stale
state requires renewed preparation and confirmation, never reuse of an older yes.

For an optimization recommendation, use the corresponding exposed approval preparation tool
and its returned authenticated review link/next steps. Wait for the server-verified decision
before an approved executor; keep the immutable plan and target binding. If the server says the
approval route is unavailable, stop and explain the limitation rather than using the table above.

## Existing Meta ad edits

When requested and supported, use `prepare_meta_ad_update_for_user_request`, show the exact
proposed ad/status/copy/media/automation change and obtain confirmation before
`execute_user_requested_meta_ad_update`. A creative edit may require a confirmed pause-first
sequence and does not implicitly resume the ad. Surface that effect before confirmation. Treat
unsupported formats and stale native snapshots as limits, not permission to rebuild the ad.

## Verify and explain

- Retain the exact plan/run/native references. Report actual success, partial, pending, uncertain
  or rejected outcomes. An acknowledgement is not evidence of current serving or approval.
- Follow the original operation's status/recovery guidance. Never blindly repeat an uncertain
  write under a new plan or change another campaign as a workaround.
- No deletion, unrelated-account transfer, hidden budget increase, unrequested activation or
  automatic change follows from reporting, upload, draft approval or this skill being installed.
