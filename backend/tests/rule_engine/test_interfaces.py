"""Confirm every rule_engine stage exposes its documented interface and
raises NotImplementedError rather than fabricating a result (master prompt
Section 7: "Implement only the structural interfaces at this milestone").
"""

import pytest

from app.rule_engine import filters, nutrition, planner, ranking, validator, variety
from app.rule_engine.types import ProfileInput

SAMPLE_PROFILE = ProfileInput(
    age=28,
    gender="female",
    height_cm=165.0,
    weight_kg=60.0,
    activity_level="moderately_active",
    dietary_preference="vegetarian",
    allergies=frozenset({"peanuts"}),
    health_goal="weight_loss",
    weekly_budget_inr=1500.0,
    cooking_time_limit_minutes=30,
)


def test_nutrition_target_resolution_not_yet_implemented() -> None:
    with pytest.raises(NotImplementedError):
        nutrition.resolve_nutrition_target(SAMPLE_PROFILE)


def test_dietary_filter_not_yet_implemented() -> None:
    with pytest.raises(NotImplementedError):
        filters.filter_by_dietary_preference([], "vegetarian")


def test_allergen_filter_not_yet_implemented() -> None:
    with pytest.raises(NotImplementedError):
        filters.filter_by_allergens([], frozenset({"peanuts"}))


def test_ranking_not_yet_implemented() -> None:
    with pytest.raises(NotImplementedError):
        ranking.rank_candidates([], target=None, feedback_scores={})


def test_variety_enforcement_not_yet_implemented() -> None:
    with pytest.raises(NotImplementedError):
        variety.enforce_variety([], [])


def test_plan_validation_not_yet_implemented() -> None:
    with pytest.raises(NotImplementedError):
        validator.validate_plan(plan=None, target=None)


def test_planner_generation_not_yet_implemented() -> None:
    import datetime

    with pytest.raises(NotImplementedError):
        planner.generate_weekly_plan(SAMPLE_PROFILE, datetime.date(2026, 1, 5))


def test_max_meal_repeats_constant_matches_req_4_2_6() -> None:
    # REQ-4.2.6: "shall avoid repeating the same meal more than twice."
    assert variety.MAX_MEAL_REPEATS_PER_WEEK == 2


def test_feedback_weights_match_project_description_section_10_3() -> None:
    from app.models.enums import FEEDBACK_WEIGHTS, FeedbackType

    assert FEEDBACK_WEIGHTS[FeedbackType.FAVORITE] == 3
    assert FEEDBACK_WEIGHTS[FeedbackType.LIKE] == 1
    assert FEEDBACK_WEIGHTS[FeedbackType.SKIP] == -1
    assert FEEDBACK_WEIGHTS[FeedbackType.DISLIKE] == -3
