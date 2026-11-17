# Enterprise Technology Risk & Remediation Assessment

**Organization:** PrairieTrust Healthcare Services (fictional)  
**Reporting date:** November 14, 2026  
**Evidence:** Synthetic E-01 through E-16

## Executive overview
This preliminary assessment covers EHR access, critical vulnerability remediation, third-party risk and issue closure governance. Evidence does not establish a security incident, exploitation or patient-data compromise.

## Risk register (simulated RSA Archer records)
| Risk ID | Risk statement | Inherent rating | Residual rating | Treatment | Accountable owner |
|---|---|---|---|---|---|
| PTHS-RISK-001 | Active former-employee EHR accounts may enable inappropriate access | High (provisional) | High (provisional) | Mitigate | EHR business service owner |
| PTHS-RISK-002 | Overdue critical scheduling-server vulnerability may affect clinical scheduling | Critical (provisional) | Not determinable | Mitigate | Patient scheduling business owner |
| PTHS-RISK-003 | Incomplete vendor assurance may expose patient scheduling data | High (provisional) | Pending assessment | Hold production onboarding; mitigate | Patient scheduling business owner |

Ratings require confirmation against approved likelihood/impact criteria; vulnerability severity alone does not determine enterprise risk.

## PTHS-RISK-001 — EHR access governance
**Confirmed:** 12 former employees retain active EHR accounts (E-01).  
**Unverified:** Privileged access reviews reportedly completed but signed evidence unavailable (E-02); MFA reported enabled but not independently validated (E-03). Policy remains draft/unapproved (E-04).

**Remediation owner:** IAM Manager. Reconcile authoritative HR terminations to EHR users; disable inappropriate accounts; inspect relevant activity; address process failures; validate through independent account exports, disablement timestamps and approvals. No improper use is assumed.

## PTHS-RISK-002 — Critical vulnerability
**Confirmed:** Critical scheduling-server vulnerability remains unpatched 14 calendar days past due (E-05). **Unverified:** Compensating control effectiveness (E-06). **Record inconsistency:** Closed issue lacks verification/evidence (E-07). **Additional issue:** Separate High IAM issue seven days overdue (E-08).

**Remediation owner:** Infrastructure Manager. Confirm asset and exposure; expedite authorized patch or equivalent corrective action; assess interim safeguards; obtain change record and post-remediation scan; independently verify and approve closure. Investigate E-07 without assuming work was never performed.

## PTHS-RISK-003 — Vendor assurance
MediBridge Cloud Services proposes to process patient names, appointment information and clinic identifiers (E-09). BAA not executed and applicability needs review (E-10); two SOC 2 Type II access-review exceptions unassessed (E-11); encryption, MFA and subprocessor evidence incomplete (E-12).

**Remediation coordination:** TPRM, Privacy Officer, Legal, Security. Hold production onboarding pending data classification, HIPAA/business associate analysis, BAA if required, SOC 2 exception assessment, safeguard validation, subprocessor review and authorized approvals. A separately authorized synthetic-data test is not production PHI approval.

## ServiceNow IRM issue governance
For each issue record: unique ID, linked risk, owner, severity, due date, action plan, evidence requests, status, verifier, verification date, escalation and closure approval. An issue is **not verified closed** solely because its status is Closed. Escalate overdue items; no new risk acceptance is approved.

## Assurance and scope limitations
The evidence packet is selected and incomplete. It cannot support an enterprise-wide closure rate or conclusions about actual compromise. Management owns remediation, GRC coordinates tracking and escalation, and Internal Audit independently tests where required.
