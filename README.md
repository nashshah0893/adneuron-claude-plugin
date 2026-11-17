# AdNeuron for Claude

Work with Google Ads and Meta Ads through AdNeuron's hosted MCP service. This plugin adds
workflows for reporting, diagnosis, budget review, keyword planning, campaign creation,
media and explicitly confirmed campaign management. Actual operations depend on the connected
account, permissions and live AdNeuron availability; a listed tool does not enable every format.

## Install in Claude Code

Add the marketplace, then install the plugin:

```text
/plugin marketplace add nashshah0893/adneuron-claude-plugin
/plugin install adneuron@adneuron
```

See [Claude's installation guide](https://code.claude.com/docs/en/discover-plugins) for current
installation and update options. Claude chat/Cowork plugin or connector availability depends on
your account and organization; this repository is not proof of a public directory listing.

The hosted endpoint is `https://mcp.adneuron.ai/mcp`. Claude discovers the current tool catalog
from AdNeuron; this package does not embed backend implementations or a frozen tool schema.
The first connection uses AdNeuron's sign-in/authorization flow. Link the relevant ad account
in AdNeuron or use its connection tool. Never paste ad-platform passwords or API secrets into chat.

## Requirements

- An AdNeuron account and a connected Google Ads or Meta Ads account for native operations.
- An eligible Claude surface and any organization approval required for its plugins/connectors.
- The exact account permissions, selected assets and operation availability returned by AdNeuron.

## Workflows

| Skill | Use it for | Example |
|---|---|---|
| `ad-performance-report` | Account/campaign results, compatible comparisons and readable charts | How did my ads perform last week? |
| `budget-review` | Budget ownership, compatible spend pacing and user-target scenarios | How are we pacing against this month's budget? |
| `performance-diagnosis` | Changes, pixel events, selected ad-set learning and creative evidence | Why did results change, and what can we verify? |
| `waste-audit` | Stored findings with evidence, freshness and uncertainty | Review suspected wasted spend in this account. |
| `keyword-planning` | Google keyword ideas, historical cost estimates and supported campaign planning | Plan Search keywords for my plumbing business. |
| `campaign-creation` | Draft → show every setting → explicit yes → created paused | Help me create a Meta carousel campaign. |
| `campaign-media` | Choose, check and upload images/videos with an explicit yes; use them in ads | Upload this image to my Meta account. |
| `campaign-management` | Pause/resume, budgets, settings, targeting, keywords, ads and removal, each after an explicit yes | Lower this campaign's daily budget to $40. |

Skills follow the live schema, actual results and returned next steps. Pending or unverified
capabilities are not promised. Missing data stays unknown; fractional results, currencies,
actual dates, attribution and provisional periods remain visible.

## How changes work

Reporting is not permission to change an account. Before any change, Claude shows exactly what
will change (current and new values, in the account currency) and waits for your explicit yes.
New campaigns are created paused; turning one on is a separate change you confirm. Uploading
media creates no ad. Installing the plugin grants no authority to change anything, and
AdNeuron's own checks (permissions, account access, availability) still apply to every change.

## Usage, privacy and support

Use `get_usage` for current limits and usage; see [plans](https://adneuron.ai/pricing).
AdNeuron calls can count toward your plan. Reuse results while following necessary continuation
and recovery; do not bypass a limit or retry an ambiguous write.

The MCP connection sends requests to AdNeuron's hosted service. Confirmed operations can involve
Google/Meta, including selected media uploads. Account results and previews enter your Claude
conversation; the user's selected media may be retained/processed as described in AdNeuron's
[privacy policy](https://adneuron.ai/privacy). Never transfer account data to unrelated services
without the user's request. [Support](https://adneuron.ai/support).

## Maintainers

The shared source of workflow rules is `references/adneuron-rules.md`. Each skill carries a
copy under its own `references/` directory. After editing the shared source, copy it into every
`skills/*/references/` folder, then run `claude plugin validate .`.

This package contains only Markdown, JSON and the icon: the Claude plugin directory accepts
scripts and other file types only from verified organizations, so keep tooling out of this
repository. Name only tools the hosted server currently lists, and prefer describing the
behaviour each tool's own description defines over copying it. Update both manifest versions
for every package change.
