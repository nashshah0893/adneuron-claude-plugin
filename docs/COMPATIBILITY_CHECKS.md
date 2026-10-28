# 0.4.0 compatibility checks

This is a review candidate built from public-package 0.3.3. It updates instructions and skills,
not backend implementation, deployment, permissions or account eligibility.

## Completed offline checks

- Both manifests declare 0.4.0 and the same plugin name/description.
- Eight skill frontmatters and self-contained rule copies are consistent with the shared source.
- `claude plugin validate .` passes with nothing to report. The CLI explicitly says its local
  checks do not perform the directory safety scan or policy review; neither is claimed here.
- `python3 scripts/check_package.py --catalog /path/to/tools-list.json` passes for all 76 named
  tool references against 104 published names captured from the inspected currently deployed API 67 image.
  This was a static source-catalog check, not an authenticated Claude `tools/list` exchange.
  Only tool names were exported; no credential, advertiser data or frozen catalog is packaged.
- Four isolated negative fixtures reject mismatched versions, stale per-skill rules, an absent
  tool name and an escaping relative Markdown link. No ad-account tools were executed.
- `git diff --check` passes. No native mutation, image/video upload, auth-flow modification,
  Claude settings change, plugin installation, backend deployment or package release was run.

## Reviewer scenarios

Use available read tools for reporting. Any native change requires a deliberately authorized
account, the exact confirmation/approval and the live server's readiness; these are not scripts
to run automatically against customer accounts.

| Prompt / situation | Expected behavior |
|---|---|
| How did this Meta account do yesterday? | Choose a report that actually supports that window or explain the limit; never silently return a week. Keep returned period, currency and unavailable outcomes visible. |
| This campaign has 1.5 reported results. | Preserve the fractional observation; never round it into two people or manufacture revenue. |
| Pixel shows purchases. Are they low? | Present returned activity/visual data; no low/normal judgment, campaign attribution or invented baseline. |
| Is my ad set learning? | Resolve the selected ad set and use the learning tool's required ID type; unknown does not mean completed. No account-wide diagnostic sweep. |
| Create a Meta carousel, then edit its audience. | Draft known values, follow missing fields, explain supersession and show the latest exact numbered plan. Only its fresh confirmation can create; an older yes is not reusable. |
| Upload this video; it stays processing. | Confirm the exact upload once, retain its ID and use processing/status guidance. Never reupload or attach/activate implicitly. |
| This upload outcome is uncertain. | Keep the original plan and use its recovery tool; missing IDs/objects never establish no-send. |
| Move budget to the best-ROAS campaign. | Establish measurement/attribution/currency limits and recommendation provenance. Use authenticated AdNeuron approval for AdNeuron-originated optimization; never relabel it as a user-requested change. |
| Pause this named campaign. | Resolve the actual account/campaign, prepare the requested pause, show the exact effect, confirm and use its matching executor only if permitted. |
| Tool listed, but selected video/format is unavailable. | Explain the returned limitation; do not change flags, substitute another format or promise availability. |
| Report is partial or has another page. | Preserve completeness flags, continue only with canonical arguments when needed and never rank the prefix. |
| Create a new campaign after a launch became uncertain. | Do not manufacture a replacement plan as recovery. Preserve original references and follow status/support guidance. |

## Remaining acceptance before public release

- Independent review of the package, especially workflow provenance and confirmation boundaries.
- Actual Claude Code/chat/Cowork installation, discovery, OAuth and representative read
  interactions on the target surface. No authenticated Claude-to-AdNeuron tool call was run for
  this package check; a matching static source catalog is not that acceptance.
- Confirm enabled native formats/operations using the actual authorized account. Neither a
  plugin release nor a listed tool enables server flags, measurement or spend authority.
- Release/update through the intended Claude distribution route after review; do not treat a
  GitHub PR, local validator success or marketplace file as proof of a public directory listing.
