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
| `campaign-creation` | Draft → preview/preparation → confirmation → supported paused creation | Help me prepare a Meta carousel campaign. |
| `campaign-media` | Private image/video intake, confirmed upload, supported association and recovery | Upload this image to the selected Meta account. |
| `campaign-management` | Confirmed pause/resume/budget changes and supported Meta ad edits | Prepare a daily budget change for this campaign. |

Skills follow the live schema, actual results and returned next steps. Pending or unverified
capabilities are not promised. Missing data stays unknown; fractional results, currencies,
actual dates, attribution and provisional periods remain visible.

## Confirmation and approval

Reporting is not permission to change an account. A user-requested change requires the exact
plan and explicit confirmation; a recommendation to optimize existing campaigns uses AdNeuron's
separate authenticated approval route. Preparation, preview, upload, creation and activation
are different operations. Installing the plugin grants none of that authority.

Meta previews can cancel the member's earlier waiting creation plans for the account, including
incomplete edits. Previous cards cannot create afterward; returning to a draft needs a new plan.
The media-operation status tool can update saved recovery state without retrying a provider write.
Respect Claude's confirmation prompts and the server's permission/readiness checks.

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
self-contained copy under its own `references/` directory for plugin/client portability.
After editing the shared source, run:

```sh
python3 scripts/check_package.py --sync-rules
python3 scripts/check_package.py
claude plugin validate .
```

Optional: validate tool references against a fresh authenticated MCP `tools/list` JSON export:

```sh
python3 scripts/check_package.py --catalog /path/to/tools-list.json
```

Use only deployed tool names and follow server availability rather than adding a release-time
allowlist. Update both manifest versions for package changes. Validate locally, obtain independent
review and perform real Claude connection/interaction checks before claiming end-to-end acceptance.
[Compatibility evidence and reviewer scenarios](docs/COMPATIBILITY_CHECKS.md) distinguish local
validation from actual Claude/native acceptance.

Tool names/annotations are served by the backend; an annotation-only server change does not
require duplicating those definitions in this package. Users may need to refresh/reconnect their
Claude surface to see its latest discovery. Package updates follow that surface's update process.
