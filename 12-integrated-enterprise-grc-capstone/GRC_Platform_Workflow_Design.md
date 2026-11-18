# Enterprise GRC Platform Workflow Design

**Simulation only — no live platform implementation or production access claimed.**

## Architecture and records
Choose **Archer IRM or ServiceNow IRM** as the primary authoritative risk/control repository, not two competing systems of record. Model `Business process → ER risk → CT control → assessment/test → RM finding → remediation → validation → authorized closure` with immutable or governed identifiers.

- **Archer / ServiceNow IRM (conceptual):** risk ownership, control library, assessment workflow, issue remediation, approvals, and CRO reporting.
- **OneTrust (conceptual):** MediBridge vendor due diligence, BAA status, privacy assessments, subprocessors, SOC 2 exceptions, approval routing.
- **AuditBoard (conceptual):** independent audit workpapers, finding ownership, management responses, closure testing, assurance conclusions.
- **Excel / Power BI / Python (proposed):** authorized exports, ID reconciliation, data-quality checks, exception flags, dashboards. No automation code was executed against live data.

## Reporting integrity — RM-01
| Field | Value |
|---|---|
| Source ticket | Closed |
| Management claim | All 12 accounts disabled |
| Independent verification | Not supplied |
| Assurance status | Verification pending |
| Verified closed | No |
| Historical exception | Confirmed; retained |

**Gate:** `Verified Closed = independent validation passed AND authorized closure approved`. Administrative ticket closure does not satisfy this rule.

## Analytics definitions
1. **Verified closure rate:** independently validated and approved closures / explicitly defined eligible finding population. State period and denominator.
2. **Overdue unverified remediation:** due date before reporting date and no verified closure. Missing due dates are data-quality exceptions, not automatically overdue.
3. **Confirmed finding areas:** count distinct finding IDs; do not count affected accounts as separate findings unless documented.
4. **Assurance evidence gaps:** count defined assessment records with missing required evidence, separately from control failures.
5. **Mandatory vendor onboarding blockers:** count unique vendors with unresolved mandatory approval/contractual conditions; not count of individual issues.

## Data controls
Use owner, division, source, evidence ID/date, risk/control/finding ID, approved due date, source status, assurance status, reviewer, validation outcome, approval, and change log. Validate ID uniqueness, referential integrity, source record counts, nulls, duplicates, and status normalization. Preserve least-privilege evidence access and audit trails.

## Segregation of duties
Business owner accepts accountability for treatment; technical team implements changes; Enterprise GRC monitors and reports; Internal Audit or designated independent reviewers evaluate assurance within their mandate; authorized executives approve eligible risk acceptance. Mandatory legal obligations cannot be waived through ordinary risk acceptance.
