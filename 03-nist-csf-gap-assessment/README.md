# Project 03 — NIST CSF 2.0 Gap Assessment

**Scenario:** PrairieTrust Healthcare Services (PTHS), a fictional healthcare organization.  
**Purpose:** Demonstrate a GRC analyst workflow: assess evidence → document current and target profiles → identify gaps → propose remediation → brief management.

## Scope
Limited to four selected NIST CSF 2.0 outcomes; **not** a comprehensive CSF review or an actual audit.

| Evidence | CSF outcome | Result |
|---|---|---|
| E-01: drafted policy not formally approved | GV.PO-01 | Confirmed gap |
| E-02: no documented EHR access reviews identified in prior 12 months | PR.AA-05 | Confirmed gap |
| E-03: 12 former employees with active EHR accounts | PR.AA-01 | Confirmed gap |
| E-04: MFA reported enforced for all users | PR.AA-03 | No confirmed gap; independent verification required |

## Deliverables
- [`PTHS_CSF_2_0_Gap_Assessment.xlsx`](PTHS_CSF_2_0_Gap_Assessment.xlsx) — current/target profiles, gaps, proposed priorities, owners, actions, evidence, status, closure criteria.
- [`PTHS_Executive_Management_Report.docx`](PTHS_Executive_Management_Report.docx) — leadership summary, recommendations, management decisions, limitations.

## Key Recommendations
1. Promptly verify and disable inappropriate former-employee EHR access and review relevant authentication records.
2. Conduct a comprehensive EHR access review and establish a management-approved recurring review process.
3. Obtain formal policy approval and communicate governance expectations.
4. Verify MFA coverage and enforcement before asserting operating effectiveness or a control gap.

## Assumptions and Limitations
All case data are **simulated**. Priorities (Critical/High/Medium), owners, the proposed 15-business-day access review target, and quarterly reviews are **recommendations**, not verified organizational requirements. No remediation is represented as completed. No actual misuse or regulatory violation is established. Evidence-based independent verification is required before recommending closure.

## Skills Demonstrated
NIST CSF 2.0 mapping; control assessment; evidence sufficiency; gap analysis; risk prioritization; remediation tracking; executive reporting.
