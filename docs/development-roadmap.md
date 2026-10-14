# Development Roadmap

Milestone sequence for implementing the full SRS Release 1.0 scope on top of the
Milestone 0 foundation. Each milestone is scoped so it can be delivered as one or more
Agile sprints (SRS Section 2.5). This is a planning document, not a requirements source —
see `docs/requirements/requirements-matrix.md` for the authoritative requirement mapping.

## Milestone 0 — Project Foundation (this milestone)

Repository scaffold, FastAPI + React skeletons, database schema and initial migration,
rule engine package structure, Docker Compose, CI, and documentation. No business logic
implemented. See the Milestone 0 completion report (delivered in-conversation) for exact
status.

## Milestone 1 — Authentication and User Profiles

- Implement `core/security.py` for real: password hashing, login/logout, token/session
  issuance (REQ-4.1.1, REQ-4.1.2, Section 5.3).
- Implement profile create/edit (REQ-4.1.3–4.1.5) with validation (Pydantic schemas +
  React Hook Form/Zod on the frontend).
- Wire up route guards (`get_current_user`, `require_admin`) to real logic.
- Frontend: make Login/Register/Profile pages functional against the real API.

## Milestone 2 — Nutrition Calculation and Hard-Constraint Filtering

- Implement `rule_engine/nutrition.py` (BMI, activity-adjusted calorie target,
  goal-derived targets — see `docs/requirements/open-decisions.md`, decision D4 for the
  constants that need finalizing).
- Implement `rule_engine/filters.py` (diet, allergy, cooking-time, per-meal-budget hard
  filters) and `rule_engine/validator.py` (single-candidate and plan-level validation).
- Unit tests for every filter and the validator, including constraint-violation cases.

## Milestone 3 — Weekly Plan Generation and Grocery List

- Implement `rule_engine/ranking.py` and `rule_engine/variety.py`.
- Implement `rule_engine/planner.py`'s `generate_weekly_plan` and
  `aggregate_grocery_list`.
- Wire `api/v1/meal_plans.py` (`POST /generate`, `GET /current`) and
  `api/v1/grocery.py` to the real pipeline.
- Frontend: Weekly Meal Plan and Grocery List pages consume real data.

## Milestone 4 — Feedback and Meal Replacement

- Implement feedback storage and scoring (REQ-4.4.1–4.4.4) wired into
  `rule_engine/ranking.py`.
- Implement `rule_engine/planner.py`'s `replace_meal` and the
  `POST /meal-plans/{id}/meals/{id}/replace` endpoint (REQ-4.5.1–4.5.5).
- Frontend: Meal Details page's Like/Dislike/Skip/Favorite/Replace controls become live.

## Milestone 5 — Dashboard and Admin Panel

- Implement `services/dashboard_service.py` and `api/v1/dashboard.py`
  (REQ-4.6.1–4.6.4).
- Implement Admin Panel CRUD for Foods, Recipes, Nutrition Values (REQ-4.7.2–4.7.4), and
  read/update (not create/delete) for Categories (REQ-4.7.5 as narrowed by decision D1).
- Enforce `require_admin` role-gating end to end.

## Milestone 6+ — Hardening and Non-Functional Requirements

- Performance validation against SRS Section 5.1 targets (plan generation < 5s, grocery
  regeneration < 2s, 100 concurrent users).
- Security review: HTTPS/TLS in deployment, CSRF handling for state-changing requests,
  dependency audit.
- Resolve remaining SRS Appendix C TBD items (hosting, uptime SLA, documentation delivery
  format) with the Product Owner.

## Explicitly out of scope until a dedicated Phase 2 effort

- LLM Reasoning Layer (Project Description Section 11) — natural-language interaction,
  explanations, ingredient substitution suggestions, conversational nutrition Q&A.
- Any machine-learning-based ranking or recommendation.
- Cloud deployment and production infrastructure.
