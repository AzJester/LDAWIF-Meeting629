# Populating Jira from the meeting backlog

This folder turns the Astrion Mission Growth meeting (2026-06-29) into a trackable
Jira board in the **AI Program** space (`AIPROG`, board 136).

| File | What it is |
|------|------------|
| `backlog.json` | Single source of truth. Epics → Tasks → Sub-tasks, with owners, due dates, labels, gating flags, and the source rationale. Edit this, then regenerate the CSV. |
| `populate_jira.py` | Generates the CSV (offline) **and** creates the issues via the Jira REST API. Stdlib only. |
| `jira_import.csv` | Drop-in file for Jira's *Import issues from CSV* wizard. Regenerate with `--csv`. |

Hierarchy created: **6 Epics → 29 Tasks → 10 Sub-tasks** (the 10-day schedule). Day 5
(Sat 7/4) and Day 6 (Sun 7/5) are intentionally dark.

There are three ways to load it. Pick one.

## Option A — CSV import (no credentials, fastest)

1. Regenerate if you edited the backlog:
   ```bash
   python3 jira/populate_jira.py --csv
   ```
2. In Jira: **Filters → View all filters → Import issues from CSV** (or
   *Project settings → Import* on a team-managed project). Upload `jira_import.csv`,
   target project **AIPROG**.
3. In the field-mapping step:
   - `Issue Id` → **Issue Id**, `Parent Id` → **Parent** (this builds Epic→Task and
     Task→Sub-task links from the ids in the file).
   - `Issue Type`, `Summary`, `Description`, `Labels`, `Status`, `Due Date` → their like-named fields.
   - `Epic Name` → **Epic Name** (epics only).
   - `Owner` → map to **Assignee** if those people exist in your site, otherwise leave it
     unmapped — the owner is already in each label (`owner-…`) and the description.
4. Run the import.

## Option B — REST API script (repeatable, re-syncable)

1. Create an API token: https://id.atlassian.com/manage-profile/security/api-tokens
2. Export config:
   ```bash
   export JIRA_BASE_URL=https://astrioninnovation.atlassian.net
   export JIRA_EMAIL=you@astrion.us
   export JIRA_API_TOKEN=********
   export JIRA_PROJECT_KEY=AIPROG
   ```
3. Preview first, then create:
   ```bash
   python3 jira/populate_jira.py --create --dry-run   # prints, calls nothing
   python3 jira/populate_jira.py --create             # creates the issues
   ```

The script creates Epics first, then Tasks (parented to their Epic), then Sub-tasks
(parented to their Task). It assigns issues whose owner appears in `OWNER_ACCOUNTS`
(currently just Shane) and leaves the rest unassigned. Add teammates' account IDs to
`OWNER_ACCOUNTS` in `populate_jira.py` to auto-assign them.

If your project renames issue types, override:
`JIRA_TYPE_EPIC`, `JIRA_TYPE_TASK`, `JIRA_TYPE_SUBTASK`.

## Option C — Live push through the Rovo connector (Claude does it)

If the **Atlassian Rovo** connector is granted access to `astrioninnovation.atlassian.net`,
Claude can create the issues directly in conversation (no token, no CSV). To enable it:

1. In Claude: **Settings → Connectors → Atlassian Rovo → Reconnect/Configure**.
2. On Atlassian's consent screen, authorize with the **work account**
   (shane.turner@astrion.us), **select the `astrioninnovation.atlassian.net` site**, and
   keep **Write** permission. A personal/gmail Atlassian identity will not see the astrion
   site — that was the original blocker.
3. Use a **fresh Claude Code session** (an already-running session won't pick up a
   newly-authorized connector) and paste the prompt in `CREATE_VIA_ROVO_PROMPT.md`. Claude
   reads `backlog.json` and creates the issues.

## Keeping it in sync

`backlog.json` is the durable record and diffs cleanly in git. Update it as the sprint
moves, regenerate the CSV, or re-run the script. To avoid duplicate issues on re-runs,
import into a fresh sprint or filter out the `mtg629` label before re-creating.
