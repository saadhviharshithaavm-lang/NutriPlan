"""Stage 3/5/6: hard-constraint filtering.

These filters implement Appendix B Rules 1, 2, 4, 6 and SRS REQ-4.2.2,
REQ-4.2.3, REQ-4.2.4, REQ-4.2.5. Every function here enforces a **hard**
constraint: diet type, allergies, budget, and cooking time must never be
relaxed to improve ranking, variety, or user satisfaction (SRS Section 2.5,
5.2; master prompt Section 7). Soft preferences belong in ranking.py, not
here.

Not implemented this milestone (master prompt Section 13).
"""

from app.rule_engine.types import MealCandidate, NutritionTarget


def filter_by_dietary_preference(
    candidates: list[MealCandidate], dietary_preference: str
) -> list[MealCandidate]:
    """Rule 1 / REQ-4.2.2: keep only meals compatible with the user's diet."""
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")


def filter_by_allergens(
    candidates: list[MealCandidate], allergies: frozenset[str]
) -> list[MealCandidate]:
    """Rule 6 / REQ-4.2.3: exclude any meal containing a declared allergen.

    This is a hard safety constraint (SRS Section 5.2) and must never be
    overridden by any other rule, including in a future Phase 2 LLM layer.
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")


def filter_by_nutrition_target(
    candidates: list[MealCandidate], target: NutritionTarget
) -> list[MealCandidate]:
    """Rule 2 / REQ-4.2.4: keep only meals meeting the goal-derived nutrition
    target (e.g. Weight Loss: calories below target and protein above a
    minimum; Muscle Gain: protein >= 120g/day).
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")


def filter_by_cooking_time(
    candidates: list[MealCandidate], cooking_time_limit_minutes: int
) -> list[MealCandidate]:
    """Rule 4 / REQ-4.2.5: exclude recipes whose prep time exceeds the user's
    available cooking time.
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")


def filter_by_per_meal_budget(
    candidates: list[MealCandidate], per_meal_budget_inr: float
) -> list[MealCandidate]:
    """Rule 3 (budget side): per-meal budget derived from the weekly budget
    breakdown (Project Description Section 10.2; see open-decisions D6).
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")
