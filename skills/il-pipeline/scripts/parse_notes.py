#!/usr/bin/env python3
"""Parse InvestorLists firm notes into a board. Input: notes.json saved from my_notes
(list of {firm_id, firm_name, text, created_at}). Lines in the shape
  [IL] <skill> | <YYYY-MM-DD> | status=<v> | next=<v> | due=<v> | path=<v> | <free>
are read; other lines are ignored. The latest [IL] line per firm wins.
Outputs board.json: rows (firm, batch, status, last_action, last_date, next, due, path),
due_now (due <= today), silent (no action in --silent-days, full mode only), by_status, by_batch.

Usage:
  python parse_notes.py notes.json board.json --today 2026-10-20 [--silent-days 14]
"""
import argparse
import json
import re
from collections import Counter
from datetime import date, timedelta

LINE = re.compile(r"^\[IL\]\s*(?P<skill>[\w-]+)\s*\|\s*(?P<date>\d{4}-\d{2}-\d{2})\s*\|(?P<rest>.*)$")
KEYS = ("status", "next", "due", "path")
CLOSED = ("passed", "meeting-booked", "second-meeting", "term-sheet")


def parse_line(s):
    m = LINE.match(s.strip())
    if not m:
        return None
    d = {"skill": m.group("skill"), "date": m.group("date"), "free": ""}
    for part in m.group("rest").split("|"):
        part = part.strip()
        if "=" in part and part.split("=")[0].strip() in KEYS:
            k, v = part.split("=", 1)
            d[k.strip()] = v.strip()
        elif part:
            d["free"] = (d["free"] + " " + part).strip()
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("notes")
    ap.add_argument("out")
    ap.add_argument("--today", required=True)
    ap.add_argument("--silent-days", type=int, default=14)
    a = ap.parse_args()
    today = date.fromisoformat(a.today)
    notes = json.load(open(a.notes))
    latest = {}
    batch_of = {}
    for n in notes:
        fid = str(n.get("firm_id"))
        for line in str(n.get("text", "")).splitlines():
            p = parse_line(line)
            if not p:
                continue
            st = p.get("status", "")
            if st.startswith("shortlisted-b"):
                batch_of[fid] = st.split("shortlisted-b", 1)[1]
            if fid not in latest or p["date"] >= latest[fid]["date"]:
                latest[fid] = {**p, "firm": n.get("firm_name", fid), "firm_id": fid}
    rows = []
    for fid, p in latest.items():
        rows.append({
            "firm": p["firm"], "firm_id": fid, "batch": batch_of.get(fid, ""),
            "status": p.get("status", ""), "last_action": p["skill"], "last_date": p["date"],
            "next": p.get("next", ""), "due": p.get("due", ""), "path": p.get("path", ""),
        })
    due_now = [r for r in rows if r["due"] and r["due"] <= a.today and r["status"] not in CLOSED]
    silent = [r for r in rows if date.fromisoformat(r["last_date"]) <= today - timedelta(days=a.silent_days)
              and r["status"].startswith("touch") and not r["due"]]
    out = {
        "rows": sorted(rows, key=lambda r: (r["due"] or "9999", r["last_date"])),
        "due_now": due_now,
        "silent": silent,
        "by_status": dict(Counter(r["status"] for r in rows)),
        "by_batch": dict(Counter(r["batch"] for r in rows if r["batch"])),
        "count": len(rows),
    }
    json.dump(out, open(a.out, "w"), indent=2)
    print(f"{len(rows)} firms, {len(due_now)} due now, {len(silent)} silent")


if __name__ == "__main__":
    main()
