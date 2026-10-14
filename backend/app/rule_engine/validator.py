"""Final constraint validation — the pipeline's last word on every plan.

Implements the "non-negotiable constraints" principle from SRS Section 2.5
and 5.2, and the REQ-4.2.8 / REQ-4.5.5 infeasibility-reporting behaviour. See
docs/requirements/open-decisions.md, decision D2, for the governing
interpretation of "closest feasible plan": fill every slot that can be filled
without violating a hard constraint, and explicitly flag any slot that
cannot, rather than ever serving a constraint-violating meal.

This module is intentionally kept independent of the ranking/variety stages
so it can be reused unchanged as the post-LLM validator in the future Phase 2
architecture (Project Description Section 11): "its output is passed back
through the same constraint validator before it is shown to anyone."

Not implemented this milestone (master prompt Section 13).
"""

from app.rule_engine.types import (
    MealCandidate,
    NutritionTarget,
    ValidationResult,
    WeeklyPlanResult,
)


def validate_meal_candidate(
    candidate: MealCandidate,
    *,
    dietary_preference: str,
    allergies: frozenset[str],
    cooking_time_limit_minutes: int,
    per_meal_budget_inr: float,
) -> ValidationResult:
    """Re-check a single candidate against every hard constraint.

    Used both for original plan generation and meal replacement (REQ-4.5.2,
    4.5.3), and — in Phase 2 — to re-check an LLM-suggested substitution
    before it reaches the user.
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")


def validate_plan(plan: WeeklyPlanResult, target: NutritionTarget) -> ValidationResult:
    """Validate an assembled weekly plan: every filled slot must already
    satisfy validate_meal_candidate, and every infeasible slot must carry a
    stated reason (REQ-4.2.8). A plan is never "valid" merely because it is
    complete — completeness without constraint compliance is a validation
    failure.
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")
