# AdNeuron Working Rules

Apply these rules to every answer that uses AdNeuron tools (the `adneuron` MCP server). They match the instructions the AdNeuron server sends; if the server's instructions differ, follow the server.

## Start of a conversation

- Call `list_accounts` once to learn the connected accounts: platform, name, `id`, currency, connection state, last sync time, and whether an account is labeled sample data. Pass an account's `id` as `account_id` to account-specific tools; omit it for workspace-wide answers. Reuse the result for the rest of the conversation.
- Results with `data_source: "sample"` or `is_sample_data: true` are clearly labeled fictional sample data, not real advertiser performance. Say so whenever you present them.
- If no ad account is connected, call `connect_account` (`google_ads` or `meta`) and give the user the link. If tools fail with a connection or token error, call `get_connections_status` first, then offer `connect_account` to reconnect.
- If no AdNeuron tools are available at all, tell the user the AdNeuron connector isn't connected in Claude and stop.
- Use only the tools the server lists. If a tool says it isn't available, tell the user plainly instead of working around it.

## Quota

- AdNeuron plans include a monthly tool-call quota (the free plan has 15). `get_usage` and `get_plan_limits` never use quota.
- Plan calls before making them. Prefer one broad call over several narrow ones, reuse results already in the conversation, and never repeat a call with the same arguments.
- If a call fails because of a quota or plan limit, say so plainly, call `get_usage` to show where the user stands, and offer `get_billing_portal` if they want to manage or upgrade their plan. Don't retry.

## Date ranges

- Reports cover **complete days** in each account's own time zone (today is excluded) and accept `lookback_days` of 7, 30, 60 or 90.
- Map the user's request to the nearest supported window and say which one you used. Example: "last week" → 7 days; "this month" or "last month" → 30 days, noting that the window isn't calendar-aligned.
- Quote the dates, time zone, currency and last sync time the tools return.

## Accuracy

- Report only what the tools return. When a metric is missing, unavailable or null, say so instead of estimating it or treating it as zero. Meta results (conversions, leads, ROAS) are still being verified by AdNeuron, so expect some to be marked unavailable.
- Never convert currencies, and never add or average amounts across different currencies. Report each currency separately and say no combined total is shown.
- Ad platforms revise conversions for several days. When data is recent, note that the latest days' conversions may still rise.
- Google Ads and Meta Ads count conversions under different attribution rules. Don't treat their conversions or ROAS as directly comparable without saying so.
- Formulas: CTR = clicks / impressions; CPC = spend / clicks; CPA = spend / conversions; ROAS = conversion value / spend; CPM = spend / impressions x 1000. % change = (current − previous) / previous, shown as "n/a" when previous is zero.
- Round currency to 2 decimals, percentages to 1 decimal, counts to whole numbers.

## Campaign and budget changes

- These skills analyze and recommend; they never change an account.
- If the user asks for a change, describe exactly what would change and that it needs their explicit approval. If AdNeuron says the change isn't available yet, tell them so and explain how to make it in Google Ads or Meta Ads Manager.

## Privacy

- Keep account data inside the conversation. Don't send it to other tools or services unless the user asks.
