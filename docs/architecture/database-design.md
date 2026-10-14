# Database Design

Entities implemented in `backend/app/models/` and created by the initial Alembic migration
(`backend/alembic/versions/224368fb6053_initial_schema.py`). All monetary values use exact
`NUMERIC` columns in INR (see `docs/requirements/open-decisions.md`, decision D9).

## Entity-relationship diagram

```mermaid
erDiagram
    USERS ||--o| USER_PROFILES : has
    USERS ||--o{ MEAL_PLANS : owns
    USERS ||--o{ FEEDBACK_EVENTS : submits

    USER_PROFILES }o--o{ ALLERGENS : declares

    MEAL_CATEGORIES ||--o{ RECIPES : categorizes
    MEAL_CATEGORIES ||--o{ PLANNED_MEALS : slots

    RECIPES ||--o{ RECIPE_INGREDIENTS : uses
    RECIPES ||--o| RECIPE_NUTRITION : "has (precalculated)"
    RECIPES ||--o{ PLANNED_MEALS : "assigned as"
    RECIPES ||--o{ FEEDBACK_EVENTS : "receives"

    INGREDIENTS ||--o{ RECIPE_INGREDIENTS : "used in"
    INGREDIENTS }o--o{ ALLERGENS : contains

    MEAL_PLANS ||--o{ PLANNED_MEALS : contains

    USERS {
        int id PK
        string email UK
        string password_hash
        enum role
        bool is_active
    }
    USER_PROFILES {
        int id PK
        int user_id FK "unique"
        int age
        enum gender
        numeric height_cm
        numeric weight_kg
        enum activity_level
        enum dietary_preference
        enum health_goal
        numeric weekly_budget_inr
        int cooking_time_limit_minutes
    }
    ALLERGENS {
        int id PK
        string name UK
    }
    INGREDIENTS {
        int id PK
        string name UK
        enum unit
        numeric calories_per_100_units
        numeric protein_g_per_100_units
        numeric carbs_g_per_100_units
        numeric fat_g_per_100_units
        numeric price_per_unit_inr
    }
    MEAL_CATEGORIES {
        int id PK
        string name UK "fixed: breakfast/lunch/dinner/snack"
        int display_order
    }
    RECIPES {
        int id PK
        string name
        int meal_category_id FK
        enum dietary_preference
        int prep_time_minutes
    }
    RECIPE_INGREDIENTS {
        int id PK
        int recipe_id FK
        int ingredient_id FK
        numeric quantity
        enum unit
    }
    RECIPE_NUTRITION {
        int id PK
        int recipe_id FK "unique"
        numeric calories
        numeric protein_g
        numeric carbs_g
        numeric fat_g
        numeric estimated_cost_inr
    }
    MEAL_PLANS {
        int id PK
        int user_id FK
        date week_start_date
    }
    PLANNED_MEALS {
        int id PK
        int meal_plan_id FK
        int day_index "0-6"
        int meal_category_id FK
        int recipe_id FK
    }
    FEEDBACK_EVENTS {
        int id PK
        int user_id FK
        int recipe_id FK
        enum feedback_type
        datetime created_at
    }
```

## Notes on specific design choices

- **Allergens are structural, not string-matched.** `Allergen` is its own table, joined to
  `Ingredient` via `ingredient_allergens` and to `UserProfile` via `user_profile_allergens`
  (both many-to-many). The rule engine's allergy filter (`rule_engine/filters.py`) can
  therefore match by `allergen_id`, not by parsing ingredient name strings.
- **Every recipe belongs to exactly one meal category** via a non-nullable
  `recipes.meal_category_id` foreign key — there is no way to represent a recipe with zero or
  multiple categories.
- **`MealCategory` is fixed at four seeded rows** (breakfast, lunch, dinner, snack), created by
  the initial migration, not by application code. See
  `docs/requirements/open-decisions.md`, decision D1, for why admin "CRUD" over this table is
  narrowed to read/update only.
- **`RecipeNutrition` and `Ingredient`'s per-100-unit nutrition are both pre-calculated and
  stored**, not computed on the fly, per the SRS assumption that recipe nutrition is
  available before meal generation. `RecipeNutrition.estimated_cost_inr` is similarly a
  precomputed total so the rule engine's per-meal budget check can read one row instead of
  summing `recipe_ingredients × ingredient price` on every request.
- **`PlannedMeal.day_index`** (0–6) is relative to `MealPlan.week_start_date`, an
  implementation choice (not specified verbatim in the SRS) made to avoid duplicating an
  absolute date per slot. A `(meal_plan_id, day_index, meal_category_id)` unique constraint
  guarantees one recipe per day/slot.
- **Feedback events are append-only facts** (`feedback_events`), not a mutable "current
  preference" row — REQ-4.4.2 requires a timestamped event per feedback action, and the
  weighted scoring (`app/models/enums.FEEDBACK_WEIGHTS`) is computed by summing these events,
  not by overwriting a single score column.
- **Illustrative data only.** No food price, nutrition, or recipe data has been seeded beyond
  the four structural `MealCategory` rows. Any future seed script for sample foods/recipes
  must be clearly labelled as illustrative development data, not verified production data
  (master prompt Section 6).

## Migration strategy

The schema is created by a hand-written-but-validated initial Alembic migration (not
`Base.metadata.create_all()` at app startup), so that schema evolution is tracked and
reviewable going forward. The migration was applied and rolled back against a real
PostgreSQL 16 instance during this milestone (see `backend/tests/test_db_integration.py`
for the automated check); see the Milestone 0 completion report for details.
