#!/usr/bin/env python3
"""
populate_jira.py - turn the meeting backlog into Jira issues.

Reads jira/backlog.json (Epics -> Tasks -> Sub-tasks) and either:
  --csv     write jira/jira_import.csv for the Jira "Import issues from CSV" wizard
            (no network, no credentials)
  --create  create the issues live via the Jira Cloud REST API (v3)
  --dry-run with --create: print what would be created, call nothing

Stdlib only. Works with python3 on a clean machine.

Live mode needs these environment variables:
  JIRA_BASE_URL    e.g. https://astrioninnovation.atlassian.net
  JIRA_EMAIL       your Atlassian account email
  JIRA_API_TOKEN   create at https://id.atlassian.com/manage-profile/security/api-tokens
  JIRA_PROJECT_KEY defaults to the projectKey in backlog.json (AIPROG)

Owner -> Jira account mapping lives in OWNER_ACCOUNTS below; unmapped owners
are left unassigned and the owner name is kept in a label and the description.
Issue type names default to Epic / Task / Sub-task; override with env if your
project renames them (JIRA_TYPE_EPIC, JIRA_TYPE_TASK, JIRA_TYPE_SUBTASK).
"""

import argparse
import base64
import csv
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
BACKLOG_PATH = os.path.join(HERE, "backlog.json")
CSV_PATH = os.path.join(HERE, "jira_import.csv")

# Map an owner string from backlog.json to a Jira accountId.
# Add teammates here once you have their account IDs (lookupJiraAccountId / the
# Jira people directory). Unmapped owners are left unassigned on purpose so the
# import never fails on a missing user.
OWNER_ACCOUNTS = {
    "Shane": "712020:dcbf8806-9eb3-4e3a-ae5a-fbbe73cec77d",
    # "Sully": "<accountId>",
    # "Dave": "<accountId>",
    # "Jake": "<accountId>",
    # "Brad": "<accountId>",
    # "Con / Rob": "<accountId>",
}


def load_backlog():
    with open(BACKLOG_PATH, encoding="utf-8") as fh:
        return json.load(fh)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def labels_for(item, prefix, extra=None):
    out = [prefix]
    for lbl in item.get("labels", []):
        out.append(slug(lbl))
    owner = item.get("owner")
    if owner:
        out.append("owner-" + slug(owner))
    if item.get("gating"):
        out.append("gating")
    if item.get("day"):
        out.append("day-%d" % item["day"])
    for e in extra or []:
        out.append(slug(e))
    # de-dup, keep order
    seen, result = set(), []
    for lbl in out:
        if lbl and lbl not in seen:
            seen.add(lbl)
            result.append(lbl)
    return result


def first_owner_account(owner):
    if not owner:
        return None
    if owner in OWNER_ACCOUNTS:
        return OWNER_ACCOUNTS[owner]
    # try the first name token (e.g. "Shane + Sully" -> "Shane")
    first = re.split(r"[+/]", owner)[0].strip()
    return OWNER_ACCOUNTS.get(first)


# ---------------------------------------------------------------- CSV mode ----
def write_csv(backlog):
    prefix = backlog["meta"].get("labelPrefix", "mtg629")
    epics = {e["key"]: e for e in backlog["epics"]}
    rows = []

    def desc_with_owner(item):
        owner = item.get("owner")
        body = item.get("description", "")
        return ("Owner: %s\n\n%s" % (owner, body)) if owner else body

    for e in backlog["epics"]:
        rows.append({
            "Issue Id": e["key"],
            "Issue Type": "Epic",
            "Summary": e["summary"],
            "Epic Name": e["summary"][:60],
            "Parent Id": "",
            "Description": desc_with_owner(e),
            "Labels": " ".join(labels_for(e, prefix)),
            "Owner": e.get("owner", ""),
            "Status": e.get("status", ""),
            "Due Date": "",
        })
    for t in backlog["tasks"]:
        rows.append({
            "Issue Id": t["key"],
            "Issue Type": "Task",
            "Summary": t["summary"],
            "Epic Name": "",
            "Parent Id": t.get("epic", ""),
            "Description": desc_with_owner(t),
            "Labels": " ".join(labels_for(t, prefix)),
            "Owner": t.get("owner", ""),
            "Status": t.get("status", "To Do"),
            "Due Date": t.get("due", ""),
        })
    for s in backlog["subtasks"]:
        rows.append({
            "Issue Id": s["key"],
            "Issue Type": "Sub-task",
            "Summary": s["summary"],
            "Epic Name": "",
            "Parent Id": s.get("parent", ""),
            "Description": desc_with_owner(s),
            "Labels": " ".join(labels_for(s, prefix)),
            "Owner": s.get("owner", ""),
            "Status": s.get("status", "To Do"),
            "Due Date": s.get("due", ""),
        })

    cols = ["Issue Id", "Issue Type", "Summary", "Epic Name", "Parent Id",
            "Description", "Labels", "Owner", "Status", "Due Date"]
    with open(CSV_PATH, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=cols)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    print("Wrote %d rows -> %s" % (len(rows), CSV_PATH))
    print("Counts: %d epics, %d tasks, %d sub-tasks"
          % (len(backlog["epics"]), len(backlog["tasks"]), len(backlog["subtasks"])))


# --------------------------------------------------------------- API mode ----
def adf(text):
    """Minimal Atlassian Document Format doc from plain text (REST v3)."""
    paras = [p for p in (text or "").split("\n") if p.strip() != ""] or [""]
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph",
             "content": [{"type": "text", "text": p}]}
            for p in paras
        ],
    }


class Jira:
    def __init__(self, base, email, token):
        self.base = base.rstrip("/")
        auth = base64.b64encode(("%s:%s" % (email, token)).encode()).decode()
        self.headers = {
            "Authorization": "Basic " + auth,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def create_issue(self, fields):
        url = self.base + "/rest/api/3/issue"
        data = json.dumps({"fields": fields}).encode()
        req = urllib.request.Request(url, data=data, headers=self.headers, method="POST")
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    return json.loads(resp.read().decode())
            except urllib.error.HTTPError as exc:
                body = exc.read().decode(errors="replace")
                if exc.code in (429, 500, 502, 503) and attempt < 3:
                    wait = 2 ** attempt
                    print("  retry in %ds (HTTP %d)" % (wait, exc.code))
                    time.sleep(wait)
                    continue
                raise SystemExit("Jira API error %d: %s" % (exc.code, body))
            except urllib.error.URLError as exc:
                if attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                raise SystemExit("Network error: %s" % exc)


def build_fields(item, project_key, issue_type, prefix, parent_key=None):
    fields = {
        "project": {"key": project_key},
        "summary": item["summary"],
        "issuetype": {"name": issue_type},
        "description": adf(item.get("description", "")),
        "labels": labels_for(item, prefix),
    }
    if item.get("due"):
        fields["duedate"] = item["due"]
    if parent_key:
        fields["parent"] = {"key": parent_key}
    acct = first_owner_account(item.get("owner"))
    if acct:
        fields["assignee"] = {"id": acct}
    return fields


def create_all(backlog, dry_run):
    base = os.environ.get("JIRA_BASE_URL")
    email = os.environ.get("JIRA_EMAIL")
    token = os.environ.get("JIRA_API_TOKEN")
    project = os.environ.get("JIRA_PROJECT_KEY") or backlog["meta"]["jira"]["projectKey"]
    t_epic = os.environ.get("JIRA_TYPE_EPIC", "Epic")
    t_task = os.environ.get("JIRA_TYPE_TASK", "Task")
    t_sub = os.environ.get("JIRA_TYPE_SUBTASK", "Sub-task")
    prefix = backlog["meta"].get("labelPrefix", "mtg629")

    if not dry_run and not all([base, email, token]):
        raise SystemExit(
            "Set JIRA_BASE_URL, JIRA_EMAIL, JIRA_API_TOKEN (and optionally "
            "JIRA_PROJECT_KEY) to create issues. Use --dry-run to preview.")

    jira = None if dry_run else Jira(base, email, token)
    created = {}  # backlog key -> jira key

    def make(item, issue_type, parent_backlog_key=None):
        parent_key = created.get(parent_backlog_key) if parent_backlog_key else None
        fields = build_fields(item, project, issue_type, prefix, parent_key)
        if dry_run:
            print("[dry-run] %-8s %-9s parent=%-10s %s"
                  % (item["key"], issue_type, parent_key or "-", item["summary"][:70]))
            created[item["key"]] = item["key"]
            return
        res = jira.create_issue(fields)
        created[item["key"]] = res["key"]
        print("created %-9s %-10s %s" % (issue_type, res["key"], item["summary"][:70]))

    print("Project %s on %s%s"
          % (project, base or "(dry-run)", "  [DRY RUN]" if dry_run else ""))
    for e in backlog["epics"]:
        make(e, t_epic)
    for t in backlog["tasks"]:
        make(t, t_task, t.get("epic"))
    for s in backlog["subtasks"]:
        make(s, t_sub, s.get("parent"))
    print("Done: %d issues%s" % (len(created), " (dry run)" if dry_run else ""))


def main():
    ap = argparse.ArgumentParser(description="Populate Jira from the meeting backlog.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--csv", action="store_true", help="write jira_import.csv (offline)")
    g.add_argument("--create", action="store_true", help="create issues via the Jira REST API")
    ap.add_argument("--dry-run", action="store_true", help="with --create: preview only")
    args = ap.parse_args()

    backlog = load_backlog()
    if args.csv:
        write_csv(backlog)
    else:
        create_all(backlog, args.dry_run)


if __name__ == "__main__":
    main()
