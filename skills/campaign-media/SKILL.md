---
name: campaign-media
description: Helps the user choose, check and upload images and videos for Google Ads and Meta Ads with AdNeuron, and use them in ads. Shows exactly what will be uploaded and gets the user's explicit yes first. Uploading alone creates no ad.
---

# Campaign images and videos

Read `references/adneuron-rules.md`. Choosing, uploading, using media in an ad and turning an
ad on are separate steps. Say which one is about to happen before it happens.

## Choose media

1. Resolve the account and what the media is for (platform, ad format, placement or role).
2. Offer images and videos already in the account first, using the server's library tools
   (for example `discover_meta_assets` or `list_google_image_library`).
3. For new media, follow the upload tool's description for what it accepts: an existing asset
   ID, a public link, or a file the user attached. If you can't pass the user's file, ask for a
   public link shared as "anyone with the link" or offer an account image. Never invent a hash,
   asset ID or link, and never pass a path on the user's computer.
4. When the upload tool offers a check-only mode, use it first to measure size and format and
   preview the media. Compare it with the platform's guidance for the intended placement and
   tell the user about any mismatch. Offer an edited version only if the user agrees.

## Upload

1. Show the account and the exact files and their roles, and get the user's explicit yes.
2. Call the upload tool once. Report each item separately: uploaded (with its ID), failed (with
   the reason), or unconfirmed. Don't call a whole batch ready when only part of it is.
3. A video may still be processing after upload: check its status as the reply says and don't
   upload it again.
4. If an upload is unconfirmed, it may or may not have applied. Ask the user to check in the
   ad platform before trying again, and follow the reply's `next_step`.

## Use media in ads

- Uploading attaches nothing. Adding media to a campaign or ad is a separate change: show the
  exact campaign, ad and media, get the user's yes, then use the matching tool (for example
  `update_google_ad_assets`, an `add_*_ad` tool or `update_meta_ad`). New ads start paused
  unless the tool says otherwise.
- A whole new campaign belongs in the `campaign-creation` skill; changes to existing ads belong
  in `campaign-management`.
