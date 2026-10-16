# AdNeuron for Claude

Manage and understand your Google Ads, Meta Ads and Google Analytics 4 data in Claude. The plugin connects Claude to AdNeuron's hosted service and adds skills for reporting, budget review, diagnosis, waste audits, GA4 analysis, keyword planning and confirmed campaign changes.

## Install

In Claude, open **Customize → Plugins**, search for **AdNeuron**, and click **Add**.

In Claude Code:

```
/plugin install adneuron --marketplace nashshah0893/adneuron-claude-plugin
```

The first time Claude uses AdNeuron, you'll be sent to adneuron.ai to sign in and approve access. AdNeuron never receives your ad-platform password. Then link your ad accounts in AdNeuron, or ask Claude to "connect my Google Ads account".

## Requirements

- An AdNeuron account (free plan available) at https://adneuron.ai
- A connected Google Ads account. Meta Ads is available on request; GA4 is optional.
- A paid Claude plan (Pro, Max, Team or Enterprise)

## Skills

| Skill | What it does | Example prompt |
|---|---|---|
| `ad-performance-report` | Performance summary, top campaigns, Google vs. Meta, industry benchmarks | "How did my ads do in the last 30 days?" |
| `budget-review` | Budgets by owner, daily spend vs. budget, 30-day projection, reallocation ideas | "Am I on track for my $8,000 monthly budget?" |
| `performance-diagnosis` | Explains why ROAS, conversions, spend, CTR or clicks changed | "Why did my ROAS drop this week?" |
| `waste-audit` | Wasted spend, stale campaigns, negative-keyword gaps, tracking health | "Where am I wasting money?" |
| `ga4-analysis` | Sessions, channels, paid vs. organic, attribution, bot traffic | "Which channels drive purchases in GA4?" |
| `keyword-planning` | Keyword ideas, budget tiers, campaign type recommendation | "Find keywords and a budget for emergency plumbing in Austin." |
| `campaign-changes` | Budget changes and new paused campaigns, only after you confirm each change | "Raise the budget on Brand Search by 10%." |

## How changes work

Analysis skills never change your accounts. The `campaign-changes` skill makes a change only after showing you exactly what will happen and getting your confirmation. AdNeuron also enforces limits on its side: budget changes are capped at ±20% per change and require a paused campaign, anything new is created paused, and every change is logged with a way to roll it back.

## Usage limits

Each AdNeuron plan includes a monthly number of tool calls (15 on the free plan). The skills keep calls to a minimum. Ask Claude "how many AdNeuron calls have I used?" at any time; that check is free. Plans: https://adneuron.ai/pricing

## Privacy Policy

AdNeuron's privacy policy is at https://adneuron.ai/privacy. It covers what data is collected, how it is used and stored, third-party sharing, retention, and how to contact us. This plugin sends data only to AdNeuron's own service at mcp.adneuron.ai and stores nothing itself.

## Support

https://adneuron.ai/support
