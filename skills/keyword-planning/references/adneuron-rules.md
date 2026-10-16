# AdNeuron Working Rules

Apply these rules to every answer that uses AdNeuron tools (the `adneuron` MCP server).

## Start of a conversation

- Call `list_accounts` once to learn the connected accounts: platform, name, internal UUID, currency, connection state, last sync time, and whether an account is a labeled **sample** account. Reuse the result for the rest of the conversation.
- Never present sample-account data as the user's real data. If only sample accounts exist, say so and offer `connect_account`.
- If tools fail with an auth or token error, call `get_connections_status`. When a connection is missing or expired, call `connect_account` with `google_ads` or `meta` and give the user the returned URL to reconnect.
- If no AdNeuron tools are available at all, tell the user the AdNeuron connector isn't connected in Claude and stop.

## Quota

- AdNeuron plans include a monthly tool-call quota (the free plan has 15). `get_usage` and `get_plan_limits` are free and never use quota.
- Plan calls before making them. Prefer one broad call over several narrow ones, reuse results already in the conversation, and never repeat a call with the same arguments.
- If a call fails because of a quota or plan limit, say so plainly, call `get_usage` to show where the user stands, and offer `get_billing_portal` if they want to upgrade. Don't retry.

## Date ranges

- Most tools accept only `lookback_days` of 7, 30, 60 or 90, over **complete local dates** in the account's timezone (today is excluded). GA4 tools accept `days` from 7 to 90.
- Map the user's request to the nearest supported window and say which one you used. Example: "last week" → 7 days; "this month" or "last month" → 30 days, stating the window isn't calendar-aligned.
- Always state the window, account timezone, currency and last sync time from the tool output.

## Accuracy

- Report only what the tools return. When a metric is missing, unavailable or marked unverified, say so instead of estimating.
- Never add or average amounts across currencies. Report each currency separately and say no combined total is shown.
- Ad platforms revise conversions for several days. When data is recent, note that the latest days' conversions may still rise.
- Google Ads and Meta Ads count conversions under different attribution rules. Don't treat their conversions or ROAS as directly comparable without saying so.
- Formulas: CTR = clicks / impressions; CPC = spend / clicks; CPA = spend / conversions; ROAS = conversion value / spend; CPM = spend / impressions x 1000. % change = (current − previous) / previous, shown as "n/a" when previous is zero.
- Round currency to 2 decimals, percentages to 1 decimal, counts to whole numbers.

## Changes to campaigns

- Analysis skills never change anything. Only the `campaign-changes` skill writes, and only after the user explicitly confirms the exact change.

## Privacy

- Keep account data inside the conversation. Don't send it to other tools or services unless the user asks.
