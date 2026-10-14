# Requirements Traceability Matrix

Source of truth: `NutriPlan-SRS.docx` (Version 1.0, Section 4, REQ-4.1.1 – REQ-4.7.5).
Supporting source: `NutriPlan-Project-Description.docx` (business logic pipeline, Section 9–10).

This matrix maps each Release 1.0 functional requirement to its planned backend module,
frontend screen, and test coverage. **Status** reflects the state after Milestone 0
(Project Foundation) only — see `docs/development-roadmap.md` for the milestone plan.

Status legend:
- `scaffolded` — package/route/page shell exists, returns `501 Not Implemented` or a static shell; no business logic yet.
- `model-only` — the database entity exists; no API or UI yet.
- `not started` — nothing built yet.

## 4.1 User Registration and Profile Management

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.1.1 | Register with unique email + password | `api/v1/auth.py`, `models/user.py`, `services/auth_service.py` | Registration | `tests/api/test_auth.py` (future) | scaffolded (route stub) |
| REQ-4.1.2 | Login / logout | `api/v1/auth.py`, `core/security.py` | Login | `tests/api/test_auth.py` (future) | scaffolded (route stub) |
| REQ-4.1.3 | Capture profile attributes (age, gender, height, weight, activity level, dietary preference, allergies, health goal, weekly budget, cooking time) | `models/user_profile.py`, `schemas/profile.py`, `api/v1/profiles.py` | Profile Setup / Edit | `tests/models/test_user_profile.py` (future) | model-only |
| REQ-4.1.4 | Reject invalid/missing profile fields with inline errors | `schemas/profile.py` (Pydantic validators) | Profile Setup / Edit | `tests/schemas/test_profile.py` (future) | not started |
| REQ-4.1.5 | Edit any saved profile attribute | `api/v1/profiles.py`, `repositories/profile_repository.py` | Profile Setup / Edit | `tests/api/test_profiles.py` (future) | not started |

## 4.2 Weekly Meal Recommendation

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.2.1 | Generate 7-day plan (breakfast/lunch/dinner/snack) | `rule_engine/planner.py`, `api/v1/meal_plans.py` | Weekly Meal Plan | `tests/rule_engine/test_planner.py` (future) | scaffolded (interface only) |
| REQ-4.2.2 | Exclude meals violating dietary preference | `rule_engine/filters.py` | Weekly Meal Plan | `tests/rule_engine/test_filters.py` (future) | scaffolded (interface only) |
| REQ-4.2.3 | Exclude meals containing declared allergens | `rule_engine/filters.py`, `models/allergen.py` | Weekly Meal Plan | `tests/rule_engine/test_filters.py` (future) | model + interface only |
| REQ-4.2.4 | Filter by health-goal-derived nutrition target | `rule_engine/nutrition.py`, `rule_engine/filters.py` | Weekly Meal Plan | `tests/rule_engine/test_nutrition.py` (future) | scaffolded (interface only) |
| REQ-4.2.5 | Exclude recipes exceeding cooking-time limit | `rule_engine/filters.py` | Weekly Meal Plan | `tests/rule_engine/test_filters.py` (future) | scaffolded (interface only) |
| REQ-4.2.6 | Same meal must not repeat more than twice per week | `rule_engine/variety.py` | Weekly Meal Plan | `tests/rule_engine/test_variety.py` (future) | scaffolded (interface only) |
| REQ-4.2.7 | Approximate weekly nutritional balance | `rule_engine/ranking.py`, `rule_engine/validator.py` | Weekly Meal Plan | `tests/rule_engine/test_validator.py` (future) | scaffolded (interface only) |
| REQ-4.2.8 | Explicit infeasibility message when a slot cannot be filled | `rule_engine/validator.py`, `schemas/meal_plan.py` | Weekly Meal Plan (empty/error state) | `tests/rule_engine/test_validator.py` (future) | scaffolded (interface only) |

## 4.3 Grocery List Generator

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.3.1 | Aggregate identical ingredient quantities across the week | `rule_engine/planner.py` (grocery aggregation step) | Grocery List | `tests/rule_engine/test_planner.py` (future) | not started |
| REQ-4.3.2 | Remove duplicate ingredient entries | `rule_engine/planner.py` | Grocery List | `tests/rule_engine/test_planner.py` (future) | not started |
| REQ-4.3.3 | Regenerate grocery list on meal replacement | `api/v1/grocery.py`, `services/grocery_service.py` | Grocery List | `tests/api/test_grocery.py` (future) | not started |
| REQ-4.3.4 | Consistent, human-readable units | `models/ingredient.py` (unit field), `schemas/grocery.py` | Grocery List | `tests/schemas/test_grocery.py` (future) | model-only |

## 4.4 Feedback System

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.4.1 | Mark a meal Like / Dislike / Skip / Favorite | `api/v1/feedback.py`, `models/feedback.py` | Meal Details | `tests/api/test_feedback.py` (future) | model-only |
| REQ-4.4.2 | Store feedback with user ID, meal ID, type, timestamp | `models/feedback.py` | Meal Details | `tests/models/test_feedback.py` (future) | model-only |
| REQ-4.4.3 | Lower future priority for Dislike/Skip | `rule_engine/ranking.py` (feedback weighting) | — (affects future plans) | `tests/rule_engine/test_ranking.py` (future) | scaffolded (interface only) |
| REQ-4.4.4 | Raise priority for Like/Favorite; prioritize similar meals for Favorite | `rule_engine/ranking.py` | — (affects future plans) | `tests/rule_engine/test_ranking.py` (future) | scaffolded (interface only) |

## 4.5 Meal Replacement

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.5.1 | Request replacement of a single meal | `api/v1/meal_plans.py` (replace endpoint) | Meal Details ("Replace Meal" action) | `tests/api/test_meal_plans.py` (future) | not started |
| REQ-4.5.2 | Replacement respects diet + allergy constraints | `rule_engine/filters.py`, `rule_engine/validator.py` | Meal Details | `tests/rule_engine/test_validator.py` (future) | scaffolded (interface only) |
| REQ-4.5.3 | Replacement does not exceed weekly budget | `rule_engine/validator.py` | Meal Details | `tests/rule_engine/test_validator.py` (future) | scaffolded (interface only) |
| REQ-4.5.4 | Replacement calorie value within tolerance of original | `rule_engine/ranking.py` | Meal Details | `tests/rule_engine/test_ranking.py` (future) | scaffolded (interface only) |
| REQ-4.5.5 | Notify user if no valid replacement exists | `rule_engine/validator.py`, `schemas/meal_plan.py` | Meal Details (error state) | `tests/rule_engine/test_validator.py` (future) | scaffolded (interface only) |

## 4.6 Dashboard

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.6.1 | Display total planned weekly calories | `api/v1/dashboard.py`, `services/dashboard_service.py` | Dashboard | `tests/api/test_dashboard.py` (future) | not started |
| REQ-4.6.2 | Display estimated spend vs. weekly budget | `services/dashboard_service.py` | Dashboard | `tests/api/test_dashboard.py` (future) | not started |
| REQ-4.6.3 | Display meal statistics (by category, by feedback) | `services/dashboard_service.py` | Dashboard | `tests/api/test_dashboard.py` (future) | not started |
| REQ-4.6.4 | Display favorited meals | `services/dashboard_service.py`, `models/feedback.py` | Dashboard | `tests/api/test_dashboard.py` (future) | not started |

## 4.7 Admin Panel

| REQ | Requirement | Backend module | Frontend screen | Test coverage | Status |
|---|---|---|---|---|---|
| REQ-4.7.1 | Restrict Admin Panel to Administrator role | `core/security.py` (role dependency), `api/v1/admin/*` | Admin Panel (route guard) | `tests/api/test_admin_auth.py` (future) | not started |
| REQ-4.7.2 | CRUD Food records | `api/v1/admin/foods.py`, `models/ingredient.py` | Admin Panel → Foods | `tests/api/test_admin_foods.py` (future) | model-only |
| REQ-4.7.3 | CRUD Recipe records (incl. ingredients, prep time) | `api/v1/admin/recipes.py`, `models/recipe.py`, `models/recipe_ingredient.py` | Admin Panel → Recipes | `tests/api/test_admin_recipes.py` (future) | model-only |
| REQ-4.7.4 | CRUD Nutrition Value records | `api/v1/admin/nutrition.py`, `models/recipe_nutrition.py` | Admin Panel → Nutrition | `tests/api/test_admin_nutrition.py` (future) | model-only |
| REQ-4.7.5 | CRUD meal Category records | `api/v1/admin/categories.py`, `models/meal_category.py` | Admin Panel → Categories | `tests/api/test_admin_categories.py` (future) | model-only, **see open-decisions.md: the four categories are fixed; "CRUD" is interpreted as update-only over seeded rows, not free create/delete** |

## Non-functional requirements (Section 5) — cross-cutting, not single-module

| Requirement | Where enforced | Status |
|---|---|---|
| 5.1 Performance (plan < 5s, grocery regen < 2s, 100 concurrent users) | `rule_engine/*` (algorithmic complexity), load testing (future) | not started — no performance target can be measured until the engine is implemented |
| 5.2 Safety (never serve an allergen; label estimates as non-medical) | `rule_engine/validator.py` (hard gate), UI disclaimer copy | validator interface scaffolded; UI disclaimer present in frontend shell |
| 5.3 Security (auth required, RBAC, hashed passwords, HTTPS/TLS) | `core/security.py`, deployment config | not started (explicitly deferred to Milestone 1 per master prompt Section 9) |
| 5.4 Quality attributes (usability, reliability, maintainability, availability) | cross-cutting | design intent documented in `docs/architecture/overview.md` |
| 5.5 Business rules (admin-only data writes, hard constraints precedence, one category per meal) | `rule_engine/validator.py`, `core/security.py` | validator interface scaffolded |

## Appendix B rule table → rule engine module mapping

| Rule | Module |
|---|---|
| Rule 1 (diet type eligibility) | `rule_engine/filters.py` |
| Rule 2 (goal → calorie/protein threshold) | `rule_engine/nutrition.py` + `rule_engine/filters.py` |
| Rule 3 (budget exceeded → replace highest-cost first) | `rule_engine/validator.py` + `rule_engine/ranking.py` |
| Rule 4 (cooking time ceiling) | `rule_engine/filters.py` |
| Rule 5 (disliked meal → lower priority) | `rule_engine/ranking.py` |
| Rule 6 (allergy exclusion) | `rule_engine/filters.py` |
| Rule 7 (repeat/variety threshold → swap) | `rule_engine/variety.py` |
| Rule 8 (favorite → similar meals) | `rule_engine/ranking.py` |
