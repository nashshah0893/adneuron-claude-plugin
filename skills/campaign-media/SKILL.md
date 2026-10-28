---
name: campaign-media
description: Helps users select, prepare and explicitly upload images or videos, attach Search images, or add supported Meta ads through AdNeuron. Use for campaign images, video processing, carousel assets, upload status or media-operation recovery; it does not automatically create or activate campaigns.
---

# Campaign images and videos

Read `references/adneuron-rules.md`. Media selection, private preparation, native upload,
campaign use and activation are separate effects. Explain the applicable effect before it runs.

## Choose or prepare media

1. Resolve account/platform and the user's intended image/video role and destination. Reuse
   compatible native assets from `discover_meta_assets` or `discover_google_image_assets` when
   appropriate; `list_campaign_images` lists prepared account-local images separately.
2. Use `help_user_upload` when the user needs instructions. Follow the live input contract for
   Claude's available attachment references or an exact user-selected HTTPS URL. Never invent
   a public file URL/hash, pass a local path the hosted service cannot read, or manufacture
   ChatGPT-specific attachment fields for Claude. If the attachment cannot be passed, explain
   the supported intake method and request a usable user-selected source.
3. Use `prepare_campaign_images` for private image intake and `prepare_campaign_video` for
   supported video intake. Show returned dimensions, type, preview, role fit and limits. Private
   preparation changes AdNeuron's stored media, even when nothing is uploaded to Google/Meta.
   It is not permission to crop, replace, upload or use an asset in an ad without agreement.
4. Keep batch item identities, successes and failures separate. Do not resend successful items,
   treat unsupported files as valid, or claim an entire batch is ready from a partial result.

## Confirm the native upload

| Target | Prepare exact upload | Execute confirmed upload |
|---|---|---|
| Meta image | `prepare_meta_image_upload_for_user_request` | `execute_user_requested_image_upload` |
| Google image/logo | `prepare_google_image_upload_for_user_request` | `execute_user_requested_image_upload` |
| Meta video | `prepare_meta_video_upload_for_user_request` | `execute_user_requested_meta_video_upload` |

Show the account, exact files, roles and returned plan before confirmation. Use the executor's
actual schema and original immutable references. Upload creates a native asset, not an approved
ad or permission to attach it to every campaign. Honor all format/access/write/readiness gates.

## Use uploaded assets only when requested

- Google Search image use: prepare with `prepare_google_search_image_for_user_request`, show
  the selected campaign/image/role and exact effect, confirm, then use
  `execute_user_requested_google_search_image` with the original plan.
- Supported Meta new-ad use: `prepare_meta_ad_for_user_request`,
  `prepare_meta_image_ad_for_user_request` or `prepare_meta_dco_ad_for_user_request` according
  to the requested format and current schema. Follow the returned confirmation/execution route,
  such as `execute_user_requested_meta_image_ad`; do not create duplicates or substitute formats.
- Whole-campaign creation belongs to `campaign-creation`. Editing an existing ad belongs to
  `campaign-management`. Additional text/media variants share the shown budget; do not invent
  unshown combinations or claim results will improve.

## Pending, processing and uncertain

- An uploaded video can still be processing. Use `get_meta_video_status` when indicated; keep
  the same native video ID and wait as instructed. Do not reupload a pending video.
- For an uncertain upload, attachment or Meta add/edit, use
  `get_campaign_image_operation_status` with its original plan. This performs native reads and
  may update AdNeuron recovery state or release a verified lock; it never retries the mutation.
- Missing native IDs/objects do not prove no send. Preserve uncertainty, keep batch child plans
  separate, and follow the returned support/recovery guidance. Only a completed, verified result
  can establish that a particular asset/association/ad exists; it does not establish serving.
