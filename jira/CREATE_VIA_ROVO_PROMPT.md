# Handoff: create the AIPROG board via the Atlassian Rovo connector

Use this when populating Jira from a **fresh Claude Code session** on this repo. A
new session loads the Rovo connector at startup; an already-running session that
predates the connector authorization will not pick up its tools.

Prerequisite: the Atlassian Rovo connector must be **Connected and authorized on the
work account** (shane.turner@astrion.us) with access to `astrioninnovation.atlassian.net`
and **Write** permission. A connector authorized on a personal Atlassian identity will
not see the astrion site (this was the original blocker).

Paste the prompt below into the new session.

---

```
Use the Atlassian Rovo connector to populate my Jira.

First verify the connector: call atlassianUserInfo (must show shane.turner@astrion.us)
and getAccessibleAtlassianResources (must list astrioninnovation.atlassian.net). If it
shows my gmail account or an empty list, stop and tell me.

Then read jira/backlog.json from this repo and create every issue in Jira project AIPROG
on astrioninnovation.atlassian.net:
- Create the 6 epics first, then the 29 tasks, then the 10 sub-tasks.
- Link hierarchy with the parent field: each task's parent = its epic's new key;
  each sub-task's parent = its parent task's new key.
- Set summary, description, labels, and duedate from the backlog.
- Assign issues whose owner is "Shane" to accountId 712020:dcbf8806-9eb3-4e3a-ae5a-fbbe73cec77d;
  leave other owners unassigned (their names are already in the labels/description).
- After creating, run a JQL count (project = AIPROG AND labels = mtg629) and report
  the totals: should be 45 issues (6 epics, 29 tasks, 10 sub-tasks).
```

---

## Notes for the new session

- `jira/backlog.json` is the single source of truth. Keys `E1..E6` are epics, `T-*` are
  tasks (each has an `epic` field), `D1..D10` are sub-tasks (each has a `parent` field).
- Issue-type names assumed: `Epic`, `Task`, `Sub-task`. If AIPROG renames them, read the
  project's issue types first (getJiraProjectIssueTypesMetadata) and map accordingly.
- Create-issue may be set to "ask" in the connector's tool permissions, so expect an
  approval prompt on the first create.
- If the Rovo path is unavailable, `jira/jira_import.csv` (CSV import) and
  `jira/populate_jira.py --create` (REST API with a work-account token, from a machine
  that can reach the Atlassian host) produce the same board.
