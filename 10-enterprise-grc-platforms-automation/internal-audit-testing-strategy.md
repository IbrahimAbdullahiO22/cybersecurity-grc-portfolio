# Internal Audit Testing Strategy

**Platform model:** AuditBoard-style workpapers (simulation)  
**Audit scope:** EHR offboarding, privileged-access reviews, vulnerability remediation, vendor due diligence

| Control area | Objective | Proposed procedures | Evidence | Preliminary conclusion |
|---|---|---|---|---|
| EHR offboarding | Timely removal of terminated-user access | Reconcile HR terminations to EHR population; inspect 12 active accounts; test disablement dates and follow-up | HR roster, EHR exports, tickets, logs | Confirmed access governance exception; no misuse established |
| Privileged-access reviews | Complete and authorized quarterly review | Validate privileged population, review period, reviewer approval and follow-up | Account inventory, signed attestations, exception logs | Signed evidence unavailable; review nonperformance not proven |
| Vulnerability remediation | Timely, verified remediation | Validate due date and aging, inspect patch/change evidence, assess compensating-control tests, investigate unsupported closure | Scans, changes, IRM records, test results | Confirmed overdue critical vulnerability; compensating control unverified; closure inconsistency |
| Vendor due diligence | Appropriate review before approval | Inspect privacy/BAA determination, SOC 2 exceptions, encryption/MFA, subprocessors and approvals | Assessments, contract, report, safeguards, approvals | Incomplete diligence; no breach or PHI processing established |

## Classification
- **Confirmed exception:** Demonstrated departure from required control outcome.
- **Insufficient evidence:** Cannot conclude control operated or failed from records available.
- **Unverified management assertion:** Activity or safeguard claimed without independent support.
- **Record inconsistency:** Workflow status conflicts with verification/evidence (e.g., E-07).

## Independence and closure
Management operates controls and implements corrective actions. GRC monitors risks and issues. Internal Audit independently evaluates testing and evidence, and verifies remediation when required by its methodology. AuditBoard-style workpapers should retain scope, sample criteria, procedures, references, results, management responses, and authorized closure decisions.
