#!/usr/bin/env python3
"""Search and validate a Fluent Like Native UTF-8 CSV lexicon."""
import argparse
import csv
import sys
from pathlib import Path

FIELDS = [
    "language", "term", "transliteration", "gloss", "function", "domain",
    "locale", "register", "medium", "audience", "example", "caution",
    "source_url", "source_date", "accessed_at", "confidence", "status", "notes",
]
REQUIRED = ["language", "term", "gloss", "function", "domain", "locale", "register", "medium", "confidence", "status"]
CONFIDENCE = {"low", "medium", "high"}
STATUS = {"draft", "needs-review", "verified-contextual", "retired"}


def read_rows(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != FIELDS:
            raise ValueError("CSV header does not match the documented schema")
        return list(reader)


def validate(path):
    rows = read_rows(path)
    issues = []
    for n, row in enumerate(rows, start=2):
        for field in REQUIRED:
            if not (row.get(field) or "").strip():
                issues.append(f"row {n}: missing {field}")
        conf, status = row.get("confidence"), row.get("status")
        if conf and conf not in CONFIDENCE:
            issues.append(f"row {n}: invalid confidence {conf!r}")
        if status and status not in STATUS:
            issues.append(f"row {n}: invalid status {status!r}")
        if status == "verified-contextual":
            for field in ("source_url", "accessed_at"):
                if not (row.get(field) or "").strip():
                    issues.append(f"row {n}: verified-contextual requires {field}")
    if issues:
        for issue in issues:
            print(issue, file=sys.stderr)
        return 1
    print(f"OK: {len(rows)} lexicon row(s) validated")
    return 0


def search(path, query, language=None):
    rows = read_rows(path)
    q = query.casefold()
    matches = []
    for row in rows:
        if language and row["language"].casefold() != language.casefold():
            continue
        haystack = " ".join((v or "") for v in row.values()).casefold()
        if q in haystack:
            matches.append(row)
    if not matches:
        print("No matching entries.")
        return 0
    for row in matches:
        print(f"{row['term']} [{row['language']}] — {row['gloss']} ({row['register']}; {row['locale']}; {row['status']}/{row['confidence']})")
        if row.get("function"):
            print(f"  Function: {row['function']}")
        if row.get("caution"):
            print(f"  Caution: {row['caution']}")
        if (row.get("source_url") or "").strip():
            print(f"  Source: {row['source_url']} (accessed {row.get('accessed_at') or 'date not recorded'})")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    p_validate = sub.add_parser("validate", help="check headers, required values, and evidence fields")
    p_validate.add_argument("csv_file", type=Path)
    p_search = sub.add_parser("search", help="find entries across term, gloss, and context fields")
    p_search.add_argument("csv_file", type=Path)
    p_search.add_argument("--query", required=True)
    p_search.add_argument("--language")
    args = parser.parse_args()
    try:
        if args.command == "validate":
            return validate(args.csv_file)
        return search(args.csv_file, args.query, args.language)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
