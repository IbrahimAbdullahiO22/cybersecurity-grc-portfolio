# Project 12 — Integrated Enterprise GRC Capstone

**Fictional enterprise simulation | Portfolio demonstration | No production system access claimed**

## Executive overview
This project presents a cross-industry governance, risk, compliance, and IT audit assessment for **PrairieTrust Holdings**, a fictional organization spanning Healthcare, Financial Services, Cloud Technology, Manufacturing/OT, and Corporate IT. It integrates risk-to-control traceability, evidence-based testing, remediation governance, third-party due diligence, and executive reporting.

## Scope and methods
- Risk identification and provisional prioritization (not approved inherent/residual risk scores)
- NIST SP 800-53 AC-2, AC-3, AC-6, CM-6, CP-4; NIST SP 800-82; IEC 62443; HIPAA/HITECH; ISO 27001; ISO 22301; SOC 2 Type II; CSA CCM and NIST SP 800-161, where relevant
- Assessment distinguishes **confirmed exceptions**, **management assertions**, **evidence gaps**, and **verified closure**
- The supplied evidence supports findings, not a comprehensive opinion on all enterprise controls

## Key results
| Finding | Evidence-supported position |
|---|---|
| RM-01 | 12 historical late EHR deprovisionings; remediation reported but independently unverified |
| RM-02 | Recovery exercise exceeded RTO; remediation overdue; no retest |
| RM-03 | Three privileged-account approval emails supplied; two missing and criteria unavailable |
| RM-04 | Two confirmed storage anonymous-access policy violations; two additional flags unverified |
| RM-05 | OT vendor authorization and restriction documented; session-monitoring assurance unresolved |
| TP-01 | Required MediBridge BAA unexecuted; applicable production ePHI processing held |
| TP-02 | Two SOC 2 access-review exceptions; management-reported remediation unverified |

**No actual unauthorized access, breach, data exposure, or financial loss is established by this scenario.**

## Portfolio artifacts
1. [Executive Enterprise Risk Brief](Executive_Enterprise_Risk_Brief.pdf)
2. [Integrated Risk & Control Register](Integrated_Risk_Control_Register.xlsx)
3. [Audit Findings & Remediation Governance](Audit_Findings_Remediation_Governance.pdf)
4. [Third-Party, Cloud & Privacy Assessment](Third_Party_Cloud_Privacy_Assessment.pdf)
5. [GRC Platform Workflow Design](GRC_Platform_Workflow_Design.md)

## Tool and experience disclosure
Archer IRM, ServiceNow IRM, OneTrust, AuditBoard, Excel/Power BI, and Python workflows are **conceptual or simulated designs** for this project. The portfolio does not claim production configuration, platform access, independent audit authority, or regulatory certification.

## Data handling
All people, organizations, records, and findings are synthetic. No actual patient, employee, customer, or vendor records are included. Assessment scores are intentionally omitted from the public artifacts.
