# Project 02 — Enterprise Cybersecurity Risk Assessment

## Project Overview
This project demonstrates a simulated enterprise cybersecurity risk assessment for PrairieTrust Healthcare Services (PTHS), a fictional healthcare organization. The assessment applies structured risk identification, likelihood and impact analysis, risk treatment planning, remediation evidence evaluation, and management reporting.

**Project Type:** Independent cybersecurity GRC portfolio simulation  
**Status:** Completed assessment; proposed remediation actions are not represented as implemented  
**Risk Methodology:** Illustrative 5×5 likelihood and impact matrix

## Project Objectives
- Identify and document cybersecurity risks affecting sensitive healthcare information and critical systems.
- Assess likelihood and business impact to prioritize risks.
- Propose business risk owners, technical owners, and treatment strategies.
- Evaluate remediation evidence and determine whether closure criteria have been met.
- Communicate findings and recommendations to management.

## Risk Assessment Summary

| Risk ID | Risk Description | Likelihood | Impact | Score | Priority |
|---|---|---:|---:|---:|---|
| RISK-001 | Excessive EHR permissions and overdue access reviews | 3 | 4 | 12/25 | High |
| RISK-002 | Active EHR accounts belonging to 12 former employees | 4 | 5 | 20/25 | Critical |
| RISK-003 | Excessive shared-drive access to sensitive patient information | 3 | 4 | 12/25 | High |
| RISK-004 | Unpatched critical patient scheduling server | 4 | 5 | 20/25 | Critical |

Ratings are preliminary, scenario-based assessments using fictional evidence. They are not independently validated organizational risk ratings.

## Key Assessment Findings
- Former-employee accounts and an unpatched critical server represent the highest-priority risks under the illustrative scoring model.
- Excessive permissions and overdue access reviews create potential confidentiality exposure.
- RISK-003 remains open in the simulation because five accounts lack documented access justification and nested group permissions have not been validated.
- RISK-004 remains open because the tested patch has not yet been deployed to production.
- A completed technical change ticket alone is insufficient to establish effective remediation or authorize risk closure.

## Risk Treatment and Verification
The proposed treatment for all four risks is mitigation. Recommended actions include access reviews, timely account deprovisioning, least-privilege enforcement, patch deployment, compensating safeguards, and independent evidence validation. Business risk owner assignments and treatment timelines remain subject to management approval.

## Project Deliverables
- Sanitized Enterprise Cybersecurity Risk Register
- Enterprise Risk Committee Management Brief

## Skills Demonstrated
Cybersecurity Risk Assessment | Risk Registers | Risk Prioritization | Risk Ownership | Risk Treatment | Access Governance | Vulnerability Management Governance | Remediation Evidence Evaluation | Residual Risk | Executive Reporting

## Disclaimer
PrairieTrust Healthcare Services is a fictional organization. All scenarios, risk ratings, findings, and supporting materials are simulated for independent professional development. No actual patient data, real security incidents, organizational approvals, or production remediation activities are represented.
