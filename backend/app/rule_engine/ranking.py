"""Stage 7: rank eligible (already hard-constraint-filtered) candidates.

Implements Appendix B Rules 5, 8 and REQ-4.4.3, REQ-4.4.4, REQ-4.5.4. Ranking
is a **soft** concern: it orders candidates that have already survived
filters.py, and must never be used to re-admit a candidate that failed a hard
constraint.

Not implemented this milestone (master prompt Section 13).
"""

from app.models.enums import FEEDBACK_WEIGHTS, FeedbackType
from app.rule_engine.types import FeedbackSignal, MealCandidate, NutritionTarget

# Re-exported for convenience; the canonical source of truth is
# app.models.enums.FEEDBACK_WEIGHTS (Project Description Section 10.3).
__all__ = ["FEEDBACK_WEIGHTS", "FeedbackType", "rank_candidates", "score_feedback"]


def score_feedback(signals: list[FeedbackSignal]) -> dict[int, int]:
    """Sum feedback weights per recipe_id (Favorite +3, Like +1, Skip -1,
    Dislike -3) to produce a per-recipe preference score (REQ-4.4.3, 4.4.4).
    """
    raise NotImplementedError("Planned for Milestone 3 (rule engine implementation).")


def rank_candidates(
    candidates: list[MealCandidate],
    target: NutritionTarget,
    feedback_scores: dict[int, int],
) -> list[MealCandidate]:
    """Order candidates by nutrition fit, budget fit, and feedback score,
    highest-priority first. Must not mutate or re-admit filtered-out
    candidates.
    """
    raise NotImplementedError("Planned for Milestone 3 (rule engine implementation).")
