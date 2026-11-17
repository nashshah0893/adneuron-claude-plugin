# Changelog

## 0.4.1

- Remove `scripts/check_package.py` and `docs/COMPATIBILITY_CHECKS.md`. The directory accepts
  scripts only from verified organizations, so 0.4.0 was refused by its automatic check.
- Update the skills for AdNeuron's current tools: one-call changes (`pause_*`, `resume_*`,
  `update_*`, `remove_*`) after an explicit yes, replacing the removed prepare/execute pairs;
  one-call campaign creation, created paused; current upload tools.
- Replace removed tool names: `list_ad_budgets`, `get_google_campaign_detail`,
  `get_google_campaign_structure`, `get_meta_campaign_performance`, `get_meta_ad_creatives`
  and `get_meta_learning_status`.

## 0.4.0 — compatibility update (refused by directory policy)

Review follow-up corrects legacy findings' unfiltered period/account/currency limits, ambiguous
zero-ranked observations, the bounded/non-targeted entity lists, and Meta ad analysis's actual
completion/error/cursor fields. Shared rules and reviewer counterexamples preserve these limits.

- Add user-requested campaign creation, media and campaign-management skills using current
  hosted tools, exact plan confirmation and separate recommendation approval.
- Update the five analysis skills for actual windows, source/coverage, fractional results,
  native diagnostic limits, current budget ownership and explicit unsupported measurements.
- Preserve continuation/status recovery instead of a blanket ban on repeated calls. Explain
  preview supersession and media recovery's saved-state effects without bypassing confirmations.
- Replace stale access/quota/creation assumptions and installation syntax. Avoid promising
  directory listing, enabled native formats, pending tools or completed native/client acceptance.
- Add one shared rule source, synchronized self-contained copies and a dependency-free package
  checker with optional tool-reference validation. Hosted endpoint is unchanged.

This is a package update, not a backend deployment, authority change or live-account validation.
