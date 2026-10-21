# Project 02 — Enterprise Cybersecurity Risk Assessment & Risk Register

**Cybersecurity GRC Career Academy | Portfolio case study**  
**Organization:** PrairieTrust Healthcare Services (PTHS) — fictional  
**Project type:** Simulated enterprise cybersecurity risk assessment  
**Status:** Assessment and portfolio documentation prepared; no real-world implementation or approval implied

> **Simulation and confidentiality notice:** All organization details, risk scenarios, roles, counts, and evidence descriptions are fictional training material. This project does not represent an engagement with a real healthcare organization. No patient information, credentials, or production system data are included. Proposed remediation, ownership, timelines, and closure criteria are not evidence of actual implementation, approval, or validation.

## Project overview

This case study demonstrates how a GRC analyst can identify, score, prioritize, document, and communicate cybersecurity risks in a fictional healthcare environment. It includes a four-risk enterprise assessment and a **separately identified capstone exercise** focused on remediation evidence, independent validation, and executive reporting.

## Assessment approach

Inherent risk is scored using a **5 × 5 likelihood-and-impact matrix** (score = likelihood × impact). The project uses these **illustrative, project-defined** bands; they are not represented as NIST-prescribed thresholds.

| Score | Classification |
| --- | --- |
| 1–5 | Low |
| 6–10 | Medium |
| 11–15 | High |
| 16–25 | Critical |

Scores below are **inherent** ratings. Residual risk ratings have not been established from validated control-effectiveness evidence.

## Original four-risk assessment

| ID | Simulated risk scenario | Likelihood × Impact | Inherent rating | Documented assessment position |
| --- | --- | --- | --- | --- |
| RISK-001 | Excessive electronic health record (EHR) permissions and overdue access reviews | 3 × 4 = 12 | High | Mitigation proposed; implementation not verified |
| RISK-002 | Twelve former employees retain active EHR accounts | 4 × 5 = 20 | Critical | Mitigation proposed; implementation not verified |
| RISK-003 | Shared-drive access: 30 users retain access, 25 are approved, five lack verified authorization; nested-group access not tested | 3 × 4 = 12 | High | Open; authorization and effective-permission evidence outstanding |
| RISK-004 | Critical patient-scheduling server remains unpatched in the original assessment; patch tested but not deployed at that stage | 4 × 5 = 20 | Critical | Open; patch deployment and verification outstanding at that stage |

**Original-assessment priorities:** RISK-002 and RISK-004 both carry Critical inherent ratings. The register proposes accountable business risk owners and technical implementation owners, along with mitigation, evidence, escalation, and closure requirements. All assignments require management confirmation in the fictional scenario.

## Separate final-capstone validation appendix

The capstone is a **distinct simulated exercise**, not an update that silently replaces the original register. Its identifiers are prefixed with `C-` to prevent confusion with the original assessment.

| Capstone ID | Scenario and reported activity | Validation gap | Recommended status |
| --- | --- | --- | --- |
| C-RISK-003 | Excessive patient-record access; IAM reports reviewing 45 employees and removing 12 unnecessary permissions | No system-generated confirmation of all removals; remaining effective access not fully matched to approved duties | **Open — pending independent verification** |
| C-RISK-004 | Critical scheduling server; infrastructure team reports patch installation and successful application testing | No post-patch vulnerability scan or equivalent technical proof that the specific vulnerability was resolved | **Open — pending independent verification** |

The original `RISK-003` shared-drive scenario and `C-RISK-003` patient-record access scenario **are not the same finding**. Similarly, the original unpatched-server assessment and the later `C-RISK-004` reported-patch scenario are presented as separate exercise stages; neither is proof of actual deployment or closure.

### Evidence-based closure principles

- Confirm that access removals are reflected in system-generated reports and effective permissions, including inherited/group-based access.
- Compare retained access to approved business requirements and document exceptions.
- For a patched vulnerability, verify deployment and obtain an appropriately scoped post-patch scan or equivalent technical evidence; confirm operational functionality.
- Keep findings open until evidence is sufficient, independently evaluated, and closure is authorized under the applicable simulated process.
- Escalate overdue or materially unresolved risks; do not assume a reduced residual risk rating without a defensible assessment.

## Management communication

The accompanying executive brief summarizes the original four risks, highlights the two Critical priorities, identifies proposed treatment and accountability, and requests decisions on ownership, timelines, interim safeguards, and evidence-based closure. It separately describes the capstone evidence gaps without implying that the simulated committee approved any action.

## Portfolio deliverables

| Document | Purpose |
| --- | --- |
| [Sanitized Enterprise Risk Register](PTHS_Project02_Final_Sanitized_Risk_Register.docx) | Original four-risk register, methodology, proposed treatments, and clearly separated capstone appendix |
| [Executive Management Risk Brief](PTHS_Project02_Final_Executive_Management_Risk_Brief.docx) | Executive summary, priorities, decisions requested, and validation limitations |

*These relative links work when the two Word documents are uploaded to the same GitHub folder as this README.*

## Skills demonstrated

Risk identification and prioritization · Qualitative risk scoring · Risk treatment planning · Business-versus-technical accountability · IAM and vulnerability-management evidence review · Independent closure validation · Executive risk communication · Accurate simulated audit trails

## Assessment context

The GRC Academy's simulated Project 02 final capstone was graded **50/50** across risk assessment, treatment, validation, and executive reporting. This is an **internal learning assessment**, not a professional certification, third-party audit opinion, or evidence of operational remediation.

---

**Portfolio integrity:** This case study documents analytical recommendations and simulated evidence-review decisions, not actual cybersecurity operations performed for PTHS.
