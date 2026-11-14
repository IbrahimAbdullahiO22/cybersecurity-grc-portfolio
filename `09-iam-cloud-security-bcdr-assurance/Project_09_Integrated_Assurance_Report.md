# Project 09 — Integrated Enterprise Security Assurance Report

**PrairieTrust Healthcare Services (fictional)**  
**Simulated role:** Senior GRC & Technology Risk Analyst  
**Assessment basis:** 30 synthetic observations across IAM, PAM, Azure Cloud, and BC/DR

## A. Consolidated assurance assessment

| ID | Classification | Established observation and required validation |
|---|---|---|
| IAM-01 | Confirmed deprovisioning exception | 12/120 terminated EHR users exceeded 24 hours; verify account activity and remediation |
| IAM-02 | Assurance limitation / potential deficiency | 9/40 transfers retained permissions; establish removal deadline |
| IAM-03 | Assurance limitation | Signed review lacks entitlement and decision records |
| IAM-04 | Assurance limitation | 3/15 privileged approvals not supplied |
| IAM-05 | Assurance limitation | MFA configuration does not prove enforcement |
| IAM-06 | Unsupported assertion | Management effectiveness claim needs independent testing |
| PAM-01 | Assurance limitation | 4/12 permanent Global Admin assignments; verify approvals and policy |
| PAM-02 | Assurance limitation | 6/30 activation justifications missing; requirement not established |
| PAM-03 | Assurance limitation | MFA enforcement evidence not supplied |
| PAM-04 | Confirmed rotation exception, subject to exception verification | 4/25 credentials exceeded 30-day requirement |
| PAM-05 | Assurance limitation | 3/18 session recordings unavailable; requirement unverified |
| PAM-06 | Assurance limitation | Two emergency accounts used; post-use review evidence absent |
| PAM-07 | Assurance limitation | 3/8 service-account owners not documented |
| PAM-08 | Unsupported assertion | PIM/CyberArk deployment alone does not establish effectiveness |
| CLD-01 | Assurance limitation | Guest OS patch compliance for 12 VMs not supplied |
| CLD-02 | Confirmed policy-evaluation finding | 4/30 storage accounts flagged; public exposure unverified |
| CLD-03 | Open security recommendations | Two high-severity findings; exploitability and deadlines unverified |
| CLD-04 | Assurance limitation | 2/6 subscription Owner approvals not supplied |
| CLD-05 | Assurance limitation | Activity Log enabled; database-specific logging unverified |
| CLD-06 | Confirmed policy-evaluation finding | Three region-policy findings; parameters and exemptions unverified |
| CLD-07 | Assurance limitation / unsupported claim | Encryption and key controls lack independent evidence |
| CLD-08 | Unsupported assertion | 82% Secure Score does not establish HIPAA compliance |
| BCDR-01 | Confirmed recovery-test exception | 13-hour EHR recovery vs 8-hour RTO; 5-hour gap |
| BCDR-02 | Confirmed recovery-test exception | 6-hour potential data loss vs 4-hour RPO; 2-hour gap |
| BCDR-03 | Assurance limitation | Backup success reported; restoration not demonstrated |
| BCDR-04 | Assurance limitation | Laboratory system business-approved recovery objectives not supplied |
| BCDR-05 | Assurance limitation | Clinical exercise participation evidence not supplied |
| BCDR-06 | Third-party assurance limitation | Provider certification not application-specific recovery evidence |
| BCDR-07 | Assurance limitation | Alternate-site execution and capacity unverified |
| BCDR-08 | Unsupported assertion | Daily backups and provider DR plan do not prove resilience |

**Five most significant observations:** BCDR-01 (EHR RTO failure), BCDR-02 (EHR RPO failure), IAM-01 (late deprovisioning), PAM-04 (overdue rotation), and CLD-02 (storage policy finding). The first four establish control/test exceptions, subject to any applicable approved credential exception; CLD-02 establishes policy-evaluation noncompliance but not actual exposure.

## B. Five prioritized enterprise risks

| Risk | Supporting evidence | Risk statement | Likelihood | Impact | Overall | Owner | Treatment and measurable closure |
|---|---|---|---|---|---|---|---|
| ER-01 EHR disruption and recovery data gap | BCDR-01/02 | A disaster may exceed clinical recovery tolerances | Medium* | High | High* | IT DR Manager; Backup Manager | Mitigate; representative retest ≤8h RTO and ≤4h RPO with clinical and integrity validation |
| ER-02 Former-user EHR access | IAM-01/03 | Delayed deprovisioning may permit inappropriate EHR access | Medium* | High | High* | IAM Manager | Mitigate; investigate all 12, review activity, retest complete subsequent termination population against 24h |
| ER-03 Privileged credential compromise | PAM-04/06/07 | Delayed rotations and unverified governance may increase privileged misuse risk | Medium* | High | High* | PAM Operations Manager | Mitigate; resolve four rotation exceptions, verify emergency reviews and service-account ownership, independently retest |
| ER-04 Azure storage exposure | CLD-02/04/05 | Inappropriate anonymous access could expose sensitive data | Medium* | High* | High* | Azure Cloud Security Manager | Mitigate; validate all four settings and data sensitivity, correct or formally except, independently confirm |
| ER-05 Scheduling compromise/disruption | CLD-03/01; BCDR-03 | Vulnerabilities combined with unverified recovery could prolong service disruption | Medium* | High | High* | Cloud Infrastructure Manager | Mitigate; validate two recommendations, VM patch evidence, and representative successful restoration |

*All risk ratings are provisional. A control exception or policy finding does not itself prove a breach, exploit, outage, or its probability.*

## C. Cross-domain dependencies

1. **IAM + PAM + Azure RBAC (IAM-01, PAM-01, PAM-06, CLD-04):** Lifecycle governance, elevated access approval, and subscription permissions should be reconciled to authoritative identity and approval records. Independently test assignments and deprovisioning without assuming the observations concern the same identities.
2. **Cloud vulnerabilities + BC/DR (CLD-03, CLD-01, BCDR-03, BCDR-07):** Preventive workload security and tested restoration jointly determine disruption exposure. Validate vulnerabilities and independently observe scheduling restoration and capacity.
3. **PAM monitoring + Azure logging (PAM-05, PAM-06, CLD-05):** Session evidence, emergency review records, and resource-specific cloud logs jointly support detection and accountability. Trace authorized test events across applicable logging sources; do not assume missing recordings mean unmonitored activity.

## D. Integrated 30/60/90-day remediation and audit plan

### Days 1–30: Validate and escalate
- **Management:** Investigate EHR RTO/RPO failures, 12 late EHR deactivations, four overdue credential rotations, four Azure storage policy findings, and two high-severity vulnerability recommendations. Assign owners and due dates.
- **Independent Audit:** Obtain authoritative populations, policies, logs, test reports, exemptions, and technical configurations; verify calculations and classify evidence accurately.
- **Deliverables:** Validated findings register, evidence inventory, root-cause assignments, initial executive risk report. Escalate actual exposure or exploitation if discovered.
### Days 31–60: Remediate and independently test
- **Management:** Correct validated weaknesses, update procedures, conduct patient scheduling restoration testing, and prepare EHR recovery retest.
- **Independent Audit — IAM-01:** Reconcile all 120 terminations and recalculate 24-hour deactivation intervals; verify the 12 exceptions and subsequent control performance.
- **Independent Audit — PAM-04:** Reconcile 25 managed credentials; calculate rotation intervals, examine approved exceptions, and verify remediation.
- **Independent Audit — CLD-02:** Reconcile 30 storage accounts; inspect four flagged configurations, container settings, policy parameters, and exemptions.
- **Independent Audit — BCDR-01/02:** Recalculate original RTO/RPO results and evaluate representative retest design.
- **Independent Audit — BCDR-03:** Observe isolated representative restoration; verify usability, integrity, and approved recovery objectives.
- **Deliverables:** Remediation evidence packages, test workpapers, updated risk register, documented unresolved limitations.
### Days 61–90: Retest and report
- **Management:** Complete remediation and demonstrate recovery capability with technical and clinical owners.
- **Independent Audit:** Verify EHR ≤8h RTO and ≤4h RPO; test subsequent IAM and PAM control periods; verify Azure storage settings; observe patient scheduling restoration and evaluate remaining assurance gaps.
- **Closure:** Require source evidence, accountable approval, independent retest, and measurable results. Retain historical exceptions even if future tests pass.
- **Reporting:** Weekly owner status, monthly CIO/CISO consolidated assurance, escalation of unresolved High risks and formal risk acceptance where appropriate.

## E. Audit Committee executive brief

**To:** Audit Committee  
**From:** Senior GRC & Technology Risk Analyst  
**Subject:** Integrated Security and Resilience Assurance

PrairieTrust cannot currently support an unqualified conclusion that its identity, privileged access, Azure cloud, and disaster recovery controls operate effectively. The integrated review identified confirmed control exceptions, failed recovery-test objectives, Azure Policy findings, and evidence limitations that require management action and independent validation.

The most consequential confirmed findings involve clinical recovery and access governance. The EHR recovery exercise required 13 hours against an approved eight-hour recovery time objective and demonstrated six hours of potential data loss against a four-hour recovery point objective. Twelve of 120 terminated EHR users remained active beyond the required 24-hour deprovisioning period. Four of 25 CyberArk-managed credentials exceeded the documented 30-day rotation requirement, subject to validation of approved exceptions. Separately, Azure Policy flagged four storage accounts against anonymous public access restrictions; actual public exposure has not been established.

Priority enterprise risks include prolonged clinical disruption, inappropriate EHR access, privileged credential compromise, potentially exposed cloud data, and patient scheduling disruption. These risks are interconnected: weak identity governance can increase privileged access exposure, inadequate logging can reduce investigative visibility, and unverified recovery capability can amplify the consequences of cloud service disruption. The evidence does not establish that a breach, actual outage, or patient data loss occurred.

The CIO and CISO should sponsor a coordinated 30/60/90-day remediation program with named IAM, PAM, cloud infrastructure, backup, and disaster recovery owners. Independent Audit should validate source populations, inspect technical configurations, test remediation, and report unresolved High risks to executive governance. Historical exceptions must remain documented even after subsequent successful retesting.

Broad management claims that Azure is secure, HIPAA compliant, or that PrairieTrust is resilient are not supportable on the available evidence. Microsoft infrastructure assurance, an 82% Defender Secure Score, daily backup reports, and provider disaster recovery certification do not establish PrairieTrust-specific effectiveness. Stronger assurance requires independently verified access and credential controls, resolved cloud findings, demonstrated application recovery within approved objectives, and an appropriately scoped HIPAA safeguards assessment.

---
**Portfolio disclaimer:** This report is based entirely on fictional, synthetic evidence. It does not represent a production audit or a legal determination of HIPAA compliance.