# AdNeuron for Claude

Understand and manage your Google Ads and Meta Ads accounts in Claude. The plugin connects Claude to AdNeuron's hosted service and adds skills for performance reporting, budget review, change diagnosis, waste audits and keyword planning.

## Install

In Claude, open **Customize → Plugins**, search for **AdNeuron**, and click **Add**.

In Claude Code:

```
/plugin install adneuron --marketplace nashshah0893/adneuron-claude-plugin
```

The first time Claude uses AdNeuron, you'll be sent to adneuron.ai to sign in and approve access. AdNeuron never receives your ad-platform password. Then link your ad accounts in AdNeuron, or ask Claude to "connect my Google Ads account".

## Requirements

- An AdNeuron account (free plan available) at https://adneuron.ai
- A connected Google Ads account. Meta Ads is available on request.
- A Claude account on any plan (Free includes one custom connector). Setup guide: https://adneuron.ai/integrations/claude

## Skills

| Skill | What it does | Example prompt |
|---|---|---|
| `ad-performance-report` | Performance summary, top campaigns, Google vs. Meta | "How did my ads do in the last 30 days?" |
| `budget-review` | Budgets by owner, daily spend vs. budget, 30-day projection, reallocation ideas | "Am I on track for my $8,000 monthly budget?" |
| `performance-diagnosis` | Explains why ROAS, conversions, spend, CTR or clicks changed | "Why did my ROAS drop this week?" |
| `waste-audit` | Wasted spend, stale campaigns, negative-keyword gaps, tracking health | "Where am I wasting money?" |
| `keyword-planning` | Keyword ideas, budget tiers, campaign type recommendation | "Find keywords and a budget for emergency plumbing in Austin." |

## How changes work

AdNeuron manages campaigns and budgets, and every change needs your explicit approval before it runs. The skills in this plugin analyze and recommend; they never change your accounts on their own. When you ask for a change, Claude describes exactly what would change. If a change isn't available through AdNeuron yet, Claude says so and explains how to make it in Google Ads or Meta Ads Manager.

## Usage limits

Each AdNeuron plan includes a monthly number of tool calls (15 on the free plan). The skills keep calls to a minimum. Ask Claude "how many AdNeuron calls have I used?" at any time; that check is free. Plans: https://adneuron.ai/pricing

## Privacy Policy

AdNeuron's privacy policy is at https://adneuron.ai/privacy. It covers what data is collected, how it is used and stored, third-party sharing, retention, and how to contact us. This plugin sends data only to AdNeuron's own service at mcp.adneuron.ai and stores nothing itself.

## Support

https://adneuron.ai/support
