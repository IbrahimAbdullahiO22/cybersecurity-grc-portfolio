# Project 04 — NIST Risk Management Framework (RMF)

**Portfolio case study | Fictional PrairieTrust Healthcare Services (PTHS)**

## Executive overview
A simulated, pre-deployment RMF assessment of a cloud-based patient management system. The work demonstrates security categorization, selected NIST SP 800-53 control mapping, evidence evaluation, remediation tracking, authorization recommendation, and continuous monitoring. **No live systems were assessed and no formal authorization was issued.**

## Deliverables
| File | Contents |
|---|---|
| `PTHS_RMF_Assessment_Workbook.xlsx` | Categorization, control selection, assessment findings, POA&M, monitoring plan |
| `PTHS_Security_Assessment_Report.docx` | Scope, method, findings, evidence limitations and recommendations |
| `PTHS_Authorization_Recommendation.docx` | AO decision support and residual-risk considerations |

## Scenario findings
- **RMF-01 / AC-2:** Three service accounts initially lack documented owners. Subsequent remediation is reported complete but not independently verified.
- **RMF-02 / CP-9 and CP-10:** Daily backups are reported; successful restoration testing has not been documented. In the monitoring scenario, remediation remains overdue.
- **RMF-03 / IA-2:** MFA is reported configured; enforcement has not been independently verified. **Not a confirmed control failure.**

## Method
1. Define preliminary system scope and impact under **FIPS 199**.
2. Map illustrative requirements to selected controls from **NIST SP 800-53 Rev. 5**.
3. Evaluate simulated evidence, distinguish findings from verification gaps, and record limitations.
4. Track proposed remediation in a POA&M and prepare an authorization recommendation.
5. Define monitoring and escalation requirements.

**RMF reference:** NIST SP 800-37 Rev. 2 (Prepare, Categorize, Select, Implement, Assess, Authorize, Monitor). The selected controls do **not** constitute a complete or tailored High baseline.

## Key assumptions and limitations
- Preliminary overall system impact **High**. Confidentiality and integrity High; availability High remains subject to validation and could differ after review of downtime tolerance and dependencies.
- Control owners, remediation deadlines, monitoring frequencies and priorities are **proposals**, not approved PTHS policy.
- System boundary, full baseline tailoring, inherited controls, provider responsibilities, actual technical evidence and AO decision are outside the supplied scenario.
- Assessment statements are **simulated**, not claims of actual compliance or control testing.

## Skills demonstrated
Security categorization · Control mapping · Evidence sufficiency · Security assessment documentation · POA&M management · Risk-based authorization support · Continuous monitoring · Executive communication
