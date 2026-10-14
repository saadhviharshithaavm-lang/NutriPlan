# Open Decisions and Implementation Assumptions

This document records ambiguities in the SRS / Project Description and the assumptions made
to resolve them during Milestone 0 scaffolding. None of these override the SRS; where the
SRS is silent, an assumption is stated explicitly and flagged for Product Owner confirmation.

## Source documents

- `docs/requirements/NutriPlan-SRS.docx` — SRS v1.0, authored by Anvita Arun, Sandhya Venkatesh,
  Saadhvi H (VIT Chennai, 2026-07-20). Treated as the Release 1.0 requirements baseline.
- `docs/requirements/NutriPlan-Project-Description.docx` — Detailed Project Description by the
  same team. Treated as supporting architectural/business-logic reference.
- `docs/requirements/NutriPlan-Team-Submission.docx` — short project title/description submission
  naming the three team members and student IDs. Kept for provenance only; not a requirements
  source.

**Assumption A0 (provenance):** The repository's scaffolding instructions referenced generic
filenames (`NutriPlan-SRS.docx`, `NutriPlan-Project-Description.docx`) without specifying which
of several similarly-named files on disk were authoritative. The SRS was unambiguous (its
internal title page matches exactly). For the Project Description, two differently-authored
drafts existed under different student IDs; the one from the same three-person team as the SRS
(student ID 24BCE1173) was used, not an unrelated draft under a different ID (24BCE1987 "1").
No WBS image was found attached to either document — see TBD note below.

## Unresolved TBD items carried over from the SRS (Appendix C)

These are already flagged as TBD in the SRS itself and are not resolved here; implementation
should treat them as placeholders:

- TBD-1: Hosting provider, server OS, database engine version — this scaffold assumes local
  Docker Compose + PostgreSQL for development; production hosting is unspecified.
- TBD-2: User documentation delivery format (in-app / help center / PDF) — not built in Milestone 0.
- TBD-3: Concurrent user target beyond 100 — no load testing performed yet.
- TBD-4: Uptime SLA — not applicable until a hosting decision is made.
- TBD-5: Phase 2 LLM Reasoning Layer — explicitly out of scope for all of Phase 1, including
  this milestone.

## Decisions made during scaffolding

### D1 — "Admin CRUD over categories" vs. "exactly four fixed categories"

The SRS requires both: (a) REQ-4.7.5 grants administrators CRUD over meal Category records, and
(b) Section 2.5 / Appendix A fix the category set to exactly breakfast, lunch, dinner, snack
("each meal belongs to exactly one meal category" — of these four). These two statements are in
tension: free-form category CRUD would let an admin delete or add categories, breaking the
four-category assumption the rule engine and data model depend on.

**Resolution:** `MealCategory` is a seeded, migration-managed table containing exactly four rows.
Administrator CRUD (REQ-4.7.5) is interpreted as **read and update** of those four rows' display
metadata (name, description, display order) — not creation or deletion of category rows. This
preserves both requirements without allowing the category count to drift. This interpretation is
an assumption, not a literal reading of REQ-4.7.5, and should be confirmed with the Product Owner
before Milestone 5 (Admin Panel) is implemented.

### D2 — "Closest feasible plan" (REQ-4.2.8, Section 4.2.2) vs. hard-constraint inviolability

The SRS's stimulus/response text says "the system displays a warning and the closest feasible
plan" when constraints can't all be met, while Section 2.5 and Section 5.2 state hard constraints
(diet, allergy, budget, cooking time) "may never be overridden... under any rule-priority
conflict."

**Resolution:** "Closest feasible plan" cannot mean a plan that violates a hard constraint. It is
interpreted as: fill every slot that *can* be filled without violating diet, allergy, budget, or
cooking-time constraints, and explicitly mark any slot that cannot be filled as infeasible with a
stated reason (REQ-4.2.8), rather than silently omitting it or substituting a constraint-violating
meal. Soft constraints (variety, exact nutrition balance) may be relaxed to produce the closest
feasible result; hard constraints may not. This is documented as the governing interpretation for
`rule_engine/validator.py`.

### D3 — Activity level not listed in REQ-4.1.3's literal field list

REQ-4.1.3 lists profile attributes as "age, gender, height, weight, dietary preference, allergies,
health goal, weekly budget, and cooking time" — omitting activity level. However, Section 2.2
("Product Functions") and the Project Description's nutrition calculation (Section 8.1, activity-
adjusted calorie baselines) both require activity level as an input.

**Resolution:** Activity level is included as a required `UserProfile` field. REQ-4.1.3's field
list is treated as representative, not exhaustive, since the nutrition engine it feeds cannot
function without it.

### D4 — Exact nutrition target formulas

The Project Description gives approximate activity-based calorie baselines (Sedentary ~1800,
Moderately Active ~2300, Very Active ~2800 kcal/day) and goal-based adjustments (Muscle Gain:
protein ≥ 120g/day, ~2600 kcal; Weight Loss: calories below target, protein above a minimum;
Maintenance: balanced around the activity-adjusted target) but does not give exact formulas for
the Weight Loss calorie reduction or the Maintenance macro split.

**Resolution:** These constants will be implemented as named, documented values in
`rule_engine/nutrition.py` (not implemented this milestone — structure only), sourced from the
Project Description Section 8, with any additional precision (e.g., exact Weight Loss calorie
deficit percentage) treated as an implementation assumption to be documented inline when the
module is built in a later milestone.

### D5 — Meal variety "similarity threshold" (Rule 7 / REQ-4.2.6)

REQ-4.2.6 gives a concrete rule ("no meal more than twice in 7 days"), but the Project
Description's Rule 7 describes a more general "category-similarity score... exceeds the
threshold" mechanism without specifying the threshold or similarity metric.

**Resolution:** Milestone 0 implements REQ-4.2.6's concrete rule as the structural contract for
`rule_engine/variety.py` (max 2 occurrences per meal per 7-day plan). The broader similarity-based
variety rule is left as a documented extension point for a later milestone, since no concrete
metric is specified.

### D6 — Budget breakdown method (weekly → daily → per-meal)

Section 10.2 of the Project Description specifies the breakdown order but not the split ratio
across days or across meal slots within a day (e.g., equal 1/7 per day, and equal 1/4 per meal
slot, vs. weighted by typical meal cost).

**Resolution:** Not implemented this milestone (structure only). Default assumption to be used
when `rule_engine/planner.py` is implemented: equal 1/7 split across days, and configurable
per-slot weights (default equal 1/4) across breakfast/lunch/dinner/snack, documented as named
constants rather than inline magic numbers, consistent with the SRS's prohibition on undocumented
constants (Section 2.5 / 5.4 Maintainability).

### D7 — Authentication mechanism

The SRS requires salted password hashing, HTTPS/TLS in transit, and RBAC (Section 5.3), but does
not mandate a specific session mechanism (cookie session vs. JWT). The Project Description lists
"Authentication service (e.g., OAuth provider)" only as an **optional external dependency for
Phase 2**, not a Phase 1 requirement.

**Resolution:** Phase 1 will implement first-party authentication (not OAuth) using password
hashing (`passlib`/`bcrypt` or Python 3.13's `hashlib` equivalents) and a server-issued session or
JWT token — the specific choice is deferred to Milestone 1 (Authentication), which this
Milestone 0 scaffold intentionally does not implement, per the master prompt's explicit
instruction not to build an insecure placeholder login system.

### D8 — Work Breakdown Structure image

The master prompt referenced a WBS image in the Detailed Project Description requiring manual
review. No embedded image was found in the extracted document content (tables and headings only).
If a WBS diagram exists only as a figure not captured by the extraction, it should be reviewed
manually and incorporated into `docs/development-roadmap.md` in a future milestone.

### D9 — Currency and numeric precision

All monetary fields are stored as exact decimal INR values (`NUMERIC` in PostgreSQL, not
floating point), per Section 2.5's INR-only requirement and general good practice for currency
data — the SRS does not specify a decimal precision, so 2 decimal places (paise) is assumed.
