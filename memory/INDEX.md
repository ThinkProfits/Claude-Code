# ThinkProfits shared memory — index

Durable facts and team rules, shared by everyone who uses this repo. One fact per file. Read the relevant file before client work. Add or update a file (and this index) whenever you learn something that the next person, or the next Claude session, will need.

## Clients and prospects
- [AANMC](aanmc-context.md): GSC access, Oct 2026 click-loss diagnosis, open questions
- [Jamie Davis Towing](jamie-davis-towing-context.md): site facts, Sept 2026 schema audit, get sign-off before H1/title/city-focus edits
- [John Sadler Plumbing & Heating](john-sadler-context.md): services, service areas, approvals, Semrush project
- [Mujo](mujo-context.md): `wp-mujo` MCP test results (2026-10-08): what it can write (Rank Math schema via REST), watch-outs, suspicious plugin flag
- [Mujo textbook authors + ISBNs (sheet)](mujo-textbook-authors.xlsx): 38 titles, all variant ISBNs, authors from VitalSource (13/38 so far), data flags. Rebuild with `clients/mujo/authors-sheet/build_sheet.py`
- [SPIEDR](spiedr-context.md): Semrush project 2084675, tracking quirks, internal-linking gaps, `wp-spiedr` MCP
- [Hotel Conchita](hotel-conchita-prospect.md): cold prospect, Website + Local SEO pitch

## Workflows and tools
- [Lovable build manager role](lovable-build-manager-role.md): Claude owns briefs, design calls and QA for Lovable page builds; verify, don't relay
- [GBP brain/body split](gbp-brain-body-split.md): Claude researches and writes, Codex executes via handoff files in `gbp-handoffs/`
- [GBP audit quota blocked](gbp-audit-quota-blocked.md): gbp-audit MCP is hard-blocked at 0 req/min and needs a Cloud Console fix
- [Blog automation FAQ/accordion](blog-automation-faq-accordion-architecture.md): Make.com Google Doc to WordPress pipeline design
- [Google Ads Keyword Planner MCP](google-ads-keyword-planner-mcp.md): local server setup and account IDs
- [GSC MCP auth](gsc-mcp-thinkprofits-auth.md): signed in as the agency account; how to re-auth

## Standards (all clients)
- [Blog topic cannibalization check](blog-topic-cannibalization-check.md): check existing content before pitching topics
- [People Also Ask research](paa-research-standard.md): always pull PAA questions into research and FAQs
- [Page-update doc format](page-update-doc-format.md): Current | Replacement side-by-side layout
- [Service page vs blog format](service-page-vs-blog-format.md): service pages are scannable conversion layouts
- [Core pages before niche pages](strategy-core-pages-before-niche.md): low-authority domains fix core pages first
- [Schema for non-medical therapy practices](schema-type-nonmedical-therapy-practices.md): LocalBusiness + ProfessionalService, not MedicalBusiness
