# Project 05 — NIST SP 800-53A Security Control Assessment

> **Portfolio simulation:** PrairieTrust Healthcare Services (PTHS) is fictional. All evidence IDs, accounts, and observations are training scenarios. No real organization, live configuration, or production system was assessed.

## Executive overview
Assessed the **Vendor Access Portal** account-management process against **NIST SP 800-53 Rev. 5 AC-2**, using **NIST SP 800-53A Rev. 5** assessment methods (examine, interview, test). Scenario evidence identifies **five active vendor accounts without documented approvals** and **two active accounts associated with contracts expired 45 days earlier**. These are **potential exceptions pending validation**, not confirmed unauthorized access. The populations may overlap.

## Deliverables
| File | Contents |
|---|---|
| `PTHS_Control_Assessment_Workbook.xlsx` | Assessment plan, evidence register, control workpaper, findings/action tracker, and monitoring/closure gates |
| `PTHS_Security_Control_Assessment_Report.docx` | Formal assessment narrative, evidence limitations, findings, and recommendations |
| `PTHS_Remediation_and_Closure_Brief.docx` | Management actions, evidence needed for closure, and governance responsibilities |

## Assessment approach
1. **Examine:** Reconcile the 40 reported active accounts to approvals, contracts, provisioning records, and logs.
2. **Interview:** Ask IAM, Vendor Management, and business owners about authorization and expiry workflows.
3. **Test:** With permission, validate account deactivation using a designated test account.

Only the **procedures were designed**. No interviews, account tests, or independent examination of underlying system exports occurred.

## Evidence-to-finding traceability
- **E-01:** Approval policy requires management authorization before account creation.
- **E-02:** 40 active vendor accounts reported.
- **E-03 → F-01:** Five accounts lack documented approval records; verify alternate sources and approval timing.
- **E-04 → F-02:** Two accounts linked to contracts expired 45 days ago; verify renewal or authorized extension.

## Key assessment conclusions
- AC-2 operating effectiveness **not demonstrated** by supplied scenario evidence.
- **F-01 and F-02: open / pending validation**, root causes undetermined.
- Risk severity and remediation deadlines require organizational assessment and approval.
- Finding closure requires validated evidence and approval through the defined governance process.

## Skills demonstrated
Control mapping; evidence sufficiency; assessment procedure design; audit finding development; root-cause uncertainty; remediation tracking; independent closure criteria; management communication.

## Framework references
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems and Organizations (AC-2)
- NIST SP 800-53A Rev. 5 — Assessing Security and Privacy Controls in Information Systems and Organizations

**Scope limitation:** This is a focused AC-2 simulation, not a comprehensive security control assessment or attestation.
