# MediBridge Vendor Security & Privacy Assessment

**Platform model:** OneTrust-style third-party risk workflow (simulation)  
**Vendor:** MediBridge Cloud Services  
**Decision:** **Hold — Not approved for production patient-data processing**

## Data and applicability
Proposed fields: patient names, appointment information, clinic identifiers (E-09). Privacy and Legal must determine whether data constitutes PHI in the proposed context, identify covered-entity/business-associate obligations, and execute a BAA **if required** before applicable PHI processing (E-10).

## Assurance findings and evidence requests
| Area | Current state | Requested evidence | Reviewer |
|---|---|---|---|
| Data flow / PHI | Applicability unconfirmed | Data-flow map, purposes, data elements, retention | Privacy Officer |
| Contract / BAA | Not executed | Signed BAA if required, contract safeguards | Legal |
| SOC 2 Type II | Two access-review exceptions | Report scope/period, exceptions, management response, remediation and testing | TPRM / Security |
| Encryption | Incomplete evidence | Configuration standards and relevant technical attestations | Security Architecture |
| MFA | Incomplete evidence | Administrative MFA configuration and validation | IAM / Security |
| Subprocessors | Not fully identified | Complete subprocessor list and downstream obligations | TPRM / Legal |

## OneTrust-style workflow
Register vendor → scope inherent risk → request questionnaire/evidence → review privacy and security obligations → assess exceptions → determine residual risk → route approval → monitor periodically.

## Decision rationale
A SOC 2 report does not automatically authorize onboarding; exceptions require context and impact analysis. Missing evidence is not itself proof of breach. Do not expose production PHI until mandatory reviews and authorized decisions are completed. Synthetic-data evaluation requires separate authorization.
