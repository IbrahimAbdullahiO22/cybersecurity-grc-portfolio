"""Synthetic GRC issue exception detection (no external systems or credentials).

Run: python grc_exception_detection.py
Illustrative data only. Exceptions require human investigation; no auto-closure.
"""
from datetime import date

REPORT_DATE = date(2026, 11, 14)
VALID_STATUSES = {"Open", "In Progress", "Pending Verification", "Closed"}

# Synthetic records illustrate logic; not a complete enterprise population.
ISSUES = [
    {"issue_id": "E-07", "status": "Closed", "verified": False,
     "evidence_present": False, "due_date": date(2026, 11, 10)},
    {"issue_id": "E-08", "status": "Open", "verified": False,
     "evidence_present": True, "due_date": date(2026, 11, 7)},
]


def check_issue(issue):
    required = {"issue_id", "status", "verified", "evidence_present", "due_date"}
    missing = required - issue.keys()
    if missing:
        raise ValueError(f"Missing fields: {sorted(missing)}")
    if not isinstance(issue["issue_id"], str) or not issue["issue_id"].strip():
        raise ValueError("Missing/invalid issue ID")
    if issue["status"] not in VALID_STATUSES:
        raise ValueError(f"Invalid status for {issue['issue_id']}")
    if type(issue["verified"]) is not bool or type(issue["evidence_present"]) is not bool:
        raise ValueError(f"Invalid boolean for {issue['issue_id']}")
    if type(issue["due_date"]) is not date:
        raise ValueError(f"Missing/invalid due date for {issue['issue_id']}")
    flags = []
    if issue["status"] == "Closed" and not issue["verified"]:
        flags.append("UNVERIFIED_CLOSURE")
    if not issue["evidence_present"]:
        flags.append("MISSING_EVIDENCE")
    if issue["due_date"] < REPORT_DATE and not issue["verified"]:
        flags.append("OVERDUE_UNRESOLVED")
    return flags


def main():
    seen = set()
    exceptions = []
    for issue in ISSUES:
        issue_id = issue.get("issue_id")
        if issue_id in seen:
            raise ValueError(f"Duplicate issue ID: {issue_id}")
        flags = check_issue(issue)
        seen.add(issue_id)
        if flags:
            exceptions.append({"issue_id": issue_id, "flags": flags})
    for record in exceptions:
        print(f"{record['issue_id']}: {', '.join(record['flags'])}")
    print(f"Unique flagged issues: {len(exceptions)}")
    print("Synthetic sample only — not an enterprise-wide metric")


if __name__ == "__main__":
    main()
