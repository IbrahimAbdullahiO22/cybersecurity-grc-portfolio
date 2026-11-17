# Cross-Industry Control and Assurance Mapping

**Scope:** Illustrative mapping for fictional enterprises. Framework references do not automatically establish regulatory applicability.

| Domain | Financial services | Cloud/SaaS | Manufacturing/OT | Healthcare |
|---|---|---|---|---|
| Governance | GLBA applicability and oversight; FFIEC examination guidance | ISO 27001 ISMS governance; SOC 2 scope | OT safety and cybersecurity governance under NIST SP 800-82 / IEC 62443 | HIPAA Security Rule applicability; HITRUST CSF as an assurance framework |
| Identity and access | Privileged access and periodic review evidence | Tenant and service identity controls; shared-responsibility boundaries | Engineering workstation, remote maintenance, and operator access | Workforce access, ePHI authorization, termination controls |
| Monitoring | Logging and escalation evidence | Cloud service logs and SOC 2 testing evidence | OT-aware monitoring without disrupting operations | Audit controls and review evidence for ePHI systems |
| Resilience | Incident response and recovery governance | Availability, backup, recovery and provider dependencies | Process safety, availability, recovery sequencing | Clinical continuity and recovery safeguards |
| Third parties | Vendor oversight and contract assurance | Subprocessors, provider reports, customer responsibilities | Integrator and remote support access | Business associate obligations when applicable |

## Questions for each assessment
1. What legal, contractual, or policy requirement applies, and to which entity or system?
2. Which control objective is being tested?
3. What is the defined population, period, and test method?
4. What evidence demonstrates design and operating effectiveness?
5. Is the result a confirmed exception, assurance limitation, or unverified claim?
6. Who owns remediation, and what evidence would support closure?

## Important distinctions
- **GLBA:** Federal law; specific obligations depend on entity and applicable rules.
- **FFIEC:** Supervisory/examination guidance, not a standalone statute.
- **SOC 2:** Attestation report; evaluate period, scope, exceptions, and complementary user entity controls.
- **ISO 27001:** Certifiable ISMS standard; certification scope matters.
- **NIST SP 800-82:** OT security guidance.
- **IEC 62443:** Family of industrial automation and control security standards.
- **HIPAA:** Applicable federal requirements; assess covered-entity/business-associate context.
- **HITRUST CSF:** Control and assurance framework; not a replacement for legal applicability analysis.
