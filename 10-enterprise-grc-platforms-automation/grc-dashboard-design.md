# Executive GRC Dashboard — Excel / Power BI Design

**Reporting date:** November 14, 2026  
**Source:** Limited synthetic evidence packet; not an enterprise-wide issue inventory

| Indicator | Category | Supported value | Interpretation |
|---|---|---|---|
| Active former-employee EHR accounts | KRI | 12 | Confirmed active accounts |
| Critical vulnerability aging | KRI | 14 calendar days overdue | Beyond recorded due date |
| High IAM issue aging | KRI | 7 calendar days overdue | Beyond recorded due date |
| SOC 2 access-review exceptions | Assurance | 2 | Require impact/remediation review |
| Closed issues lacking verification | Data quality | 1 identified | E-07 closure inconsistency |
| Verified remediation closure rate | KPI | Not calculable | Complete eligible population unavailable |
| On-time verified remediation rate | KPI | Not calculable | Complete population and verification dates unavailable |

## Data preparation and model
Use Power Query to import authorized exports, normalize statuses/dates, validate unique issue IDs, reconcile evidence references, and flag null or inconsistent fields. Model Issue, Risk, Control, Owner, BusinessService, and Evidence tables with validated keys and appropriate cardinality. Preserve report-as-of date and source extraction timestamps.

## Dashboard views
- Supported KPI/KRI cards and evidence-quality exceptions
- Overdue issue aging by approved priority
- Open Critical issues and verification status
- Drill-through to issue ID, owner, linked evidence and reviewer
- Explicit coverage and data-quality limitations

## Example metric definitions
**Verified closure rate:** count of independently verified closed eligible issues / count of eligible issues × 100.  
**On-time remediation rate:** count of eligible issues independently verified by their approved due dates / count of eligible issues × 100.

Do not calculate these rates from the limited packet. Distinguish category flag counts from **unique flagged issues** to avoid double-counting.
