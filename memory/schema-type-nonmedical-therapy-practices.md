---
name: schema-type-nonmedical-therapy-practices
description: Don't use MedicalBusiness schema.org type for non-medical counseling/therapy practices (LPCs, LCSWs, sex therapists) — use LocalBusiness + ProfessionalService instead
metadata:
  type: feedback
  originSessionId: ea9903ab-3a9e-4429-942f-88d7c4e4ae4b
  modified: 2026-09-08T15:27:58.857Z
---

For a licensed counseling/therapy practice that is NOT physician-led (LPC, LCSW, LMHC, AASECT-certified
sex therapist, etc. — not an MD/DO/psychiatrist), don't default to schema.org's `MedicalBusiness` type
for the Organization node, even though it's technically not disallowed.

**Why:** Researched this directly during a therapy-practice schema audit. Every
`MedicalBusiness` subtype in schema.org's actual hierarchy (Physician, Psychiatric, Dentist,
Dermatology, Geriatric, Gynecologic, Obstetric, Oncologic, Otolaryngologic, Pediatric, Pharmacy,
PlasticSurgery, Podiatric, PublicHealth, etc.) is either a physical medical specialty or a
physician-level practice. "Psychiatric" specifically means MD-level psychiatric medicine — not
psychotherapy/counseling by a non-physician license. Even schema.org's `PsychologicalTreatment`
type (defined as "counseling, dialogue and communication... without use of drugs") is nested under
`MedicalEntity → MedicalProcedure → TherapeuticProcedure` — the vocabulary has no dedicated
non-medical counseling type at all. Using `MedicalBusiness` with no accurate child type to pair it
with is a sign of a mismatched fit, not just a technicality, and it can cut against a practice's own
brand positioning (a practice that deliberately avoids medicalizing its work is undercut when the
business is labelled "medical"). Also worth checking: whether it matches the practice's
Google Business Profile category (mismatch between GBP category and schema type is a real local-SEO
inconsistency signal).

**How to apply:** For non-physician-led therapy/counseling/wellness practices, use
`["LocalBusiness", "ProfessionalService"]` for the Organization `@type` instead of
`["MedicalBusiness", "LocalBusiness"]`. Keep `Person` schema for the practitioner with accurate
`jobTitle`/`hasCredential` (this part is unaffected — Person isn't in the medical-only branch), and
keep `Service` schema for individual offerings (also unaffected, `Service` is a plain generic type).
This only changes the Organization-level type declaration. Applies broadly to ThinkProfits' other
therapy/counseling clients — check their existing schema before assuming it's fine.

Seen on 3 audits (2026-09-08). Two practices had this `MedicalBusiness` issue. A third had the *opposite*
problem: a bare `Organization` with no `LocalBusiness`/`ProfessionalService` at all, which under-claims
local-pack/map rich-result eligibility for a practice with a real physical address. Same target fix either
way: `["LocalBusiness", "ProfessionalService"]`. Check any new therapy/counseling client for both failure modes.

Also recurring on those audits: Wix sites tend to carry orphaned legacy JSON-LD scripts on the homepage
(a bare `LocalBusiness` and/or `WebSite` block with no `@id`, disconnected from the real `@graph`). Check
for this on any Wix client's homepage schema audit.
