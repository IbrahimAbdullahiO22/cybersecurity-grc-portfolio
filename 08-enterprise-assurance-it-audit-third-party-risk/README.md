# Project 08 — Enterprise Assurance, IT Audit & Third-Party Risk

**Cybersecurity GRC Portfolio | Simulated Case Study**

## Overview
This project demonstrates an integrated assessment of technology assurance for **PrairieTrust Healthcare Services (PTHS)**, a fictional healthcare organization. The assessment considers SOC 1, SOC 2, SOX-style IT general controls, PCI DSS v4.0.1, and enterprise third-party risk management. It addresses a management question: can favorable vendor reports justify concluding that all technology controls are effective and all vendor renewals should proceed? **No: assurance must be assessed by scope, period, responsibilities, exceptions, and independently verified evidence.**

## Deliverables

| File | Purpose |
|---|---|
| [Enterprise Assurance Assessment](Project08_Enterprise_Assurance_Assessment.docx) | Executive assurance assessment, evidence classifications and cross-framework dependencies |
| [Enterprise Risk Register](Project08_Enterprise_Risk_Register.xlsx) | Five provisional risks (ER-01–ER-05), scoring and remediation tracking |
| [Independent Audit Testing Workpaper](Project08_Independent_Audit_Testing_Workpaper.docx) | Proposed audit procedures, populations, evidence requests, owners and separate closure criteria |
| [Executive Risk Committee Memo](Project08_Executive_Risk_Committee_Memo.docx) | Executive decisions, vendor renewal conditions, escalation and 30/60/90-day roadmap |

## Frameworks and concepts
- SOC 1 Type II: controls relevant to internal control over financial reporting (ICFR)
- SOC 2 Type II: selected Trust Services Criteria, report scope and complementary controls
- SOX-style ITGCs: access management, change management and IT operations (no direct SOX applicability assumed)
- PCI DSS v4.0.1: payment environment scoping, segmentation, authentication and vulnerability management
- TPRM and NIST SP 800-161: vendor tiering, supply-chain dependencies, resilience and evidence-based risk treatment

## Assessment approach
1. Preserve original scenario evidence across **SOC-01–SOC-08, ITGC-01–ITGC-08, PCI-01–PCI-08, TPRM-01–TPRM-08**.
2. Separate confirmed operating exceptions from missing evidence, scope exclusions, and unsupported assertions.
3. Document five provisional enterprise risks and apply the case's likelihood-impact matrix.
4. Propose independent tests and measurable closure criteria; do not present proposed tests as completed.
5. Recommend vendor-specific conditional decisions rather than blanket approval.

## Evidence traceability note
**SOC-03** is the ClearBridge analytics-module scope exclusion. **SOC-04** is the ClearBridge terminated-account deprovisioning exception. Enterprise risk **ER-04** is sourced to **SOC-04**.

## Key findings
- ClearBridge: sampled terminated-account delays and unresolved complementary access-review evidence.
- Financial reporting: late documented change approvals and September payroll reconciliation evidence gap.
- PCI: incomplete payment scoping and unverified segmentation; high-severity findings require exposure and deadline assessment.
- MedAxis: recovery exercise missed its RTO and RPO; subcontractor contractual and due-diligence evidence was not supplied.

## Integrity and confidentiality
**All entities, vendors, records, evidence IDs and observations are fictional and created for training.** No actual protected health information, payment card data, confidential SOC reports, customer records, or production audit results are included. Risk scores are illustrative and provisional; no real testing, certification, compliance attestation or vendor approval is claimed. Course grades are intentionally excluded from the public portfolio.

## How to view
Download Word files to inspect the assessment, testing methodology and executive memo; open the Excel workbook to explore the risk register and remediation tracker. Links above work when these files are uploaded together into the same GitHub folder.
