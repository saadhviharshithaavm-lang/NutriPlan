"""Stages 1, 9, 10: orchestrate the full pipeline and assemble/aggregate.

planner.py is the only module that calls the other rule_engine modules in
sequence; nutrition.py, filters.py, ranking.py, variety.py, and validator.py
must remain independently callable and independently unit-testable (SRS
Section 5.4, Maintainability) rather than reaching into each other directly.

Pipeline order (Project Description Section 9 / master prompt Section 7):
  1. Collect and validate profile inputs.
  2. nutrition.resolve_nutrition_target
  3. filters.filter_by_dietary_preference, filter_by_allergens
  4. (candidate generation — query eligible recipes from the database)
  5. filters.filter_by_cooking_time
  6. filters.filter_by_per_meal_budget
  7. ranking.rank_candidates
  8. variety.enforce_variety
  9. assemble_weekly_plan (this module)
  10. validator.validate_plan
  11. aggregate_grocery_list (this module)

Not implemented this milestone (master prompt Section 13).
"""

from datetime import date

from app.rule_engine.types import (
    GroceryItem,
    MealCandidate,
    PlannedSlot,
    ProfileInput,
    WeeklyPlanResult,
)


def generate_weekly_plan(profile: ProfileInput, week_start_date: date) -> WeeklyPlanResult:
    """Run the full pipeline end to end for one user and one week.

    Must never return a slot filled with a candidate that fails
    validator.validate_meal_candidate; unfillable slots are reported via
    WeeklyPlanResult.infeasible_slots (REQ-4.2.8), never silently omitted.
    """
    raise NotImplementedError("Planned for Milestone 3 (rule engine implementation).")


def replace_meal(
    original: MealCandidate,
    candidates: list[MealCandidate],
    *,
    weekly_budget_remaining_inr: float,
    calorie_tolerance_fraction: float = 0.15,
) -> MealCandidate | None:
    """REQ-4.5.1-4.5.5: pick a replacement meeting the same diet/allergy
    constraints, within budget, and within a calorie tolerance of the
    original. Returns None (not a constraint-violating substitute) if no
    valid replacement exists (REQ-4.5.5).
    """
    raise NotImplementedError("Planned for Milestone 4 (rule engine implementation).")


def aggregate_grocery_list(slots: list[PlannedSlot]) -> list[GroceryItem]:
    """REQ-4.3.1-4.3.4: sum identical ingredient quantities (same ingredient,
    same unit) across every meal in the plan, deduplicated.
    """
    raise NotImplementedError("Planned for Milestone 3 (rule engine implementation).")
