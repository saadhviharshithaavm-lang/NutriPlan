"""Stage 8: enforce meal variety across the assembled week.

Implements REQ-4.2.6 (concrete rule: no meal more than twice in 7 days) as
the Milestone 0 structural contract. Appendix B Rule 7's broader
category-similarity mechanism is a documented future extension — see
docs/requirements/open-decisions.md, decision D5.

Not implemented this milestone (master prompt Section 13).
"""

from app.rule_engine.types import MealCandidate, PlannedSlot

# REQ-4.2.6: "shall avoid repeating the same meal more than twice within a
# single 7-day plan."
MAX_MEAL_REPEATS_PER_WEEK = 2


def count_recipe_occurrences(slots: list[PlannedSlot]) -> dict[int, int]:
    """Count how many times each recipe_id already appears in a partial plan."""
    raise NotImplementedError("Planned for Milestone 3 (rule engine implementation).")


def enforce_variety(
    candidates: list[MealCandidate], existing_slots: list[PlannedSlot]
) -> list[MealCandidate]:
    """Remove candidates that would push a recipe's weekly occurrence count
    above MAX_MEAL_REPEATS_PER_WEEK.
    """
    raise NotImplementedError("Planned for Milestone 3 (rule engine implementation).")
