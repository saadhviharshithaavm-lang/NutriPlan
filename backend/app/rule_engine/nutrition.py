"""Stage 2: compute BMI and nutrition targets from a user profile.

Source: Project Description Section 8 ("Nutrition Profile Calculation") and
Section 9, Stage 2. Constants below are transcribed directly from that
section; exact formulas for the Weight Loss deficit and Maintenance macro
split are not fully specified there (see docs/requirements/open-decisions.md,
decision D4) and must be finalized, documented, and unit-tested before
resolve_nutrition_target() is implemented.

Not implemented this milestone (master prompt Section 13: "finished nutrition
recommendation calculations" is explicitly out of scope for Milestone 0).
"""

from app.rule_engine.types import NutritionTarget, ProfileInput

# Activity-adjusted baseline calories (Project Description Section 8.1).
ACTIVITY_CALORIE_BASELINES_KCAL: dict[str, int] = {
    "sedentary": 1800,
    "moderately_active": 2300,
    "very_active": 2800,
}

# BMI thresholds (standard WHO cutoffs; not restated numerically in the
# source documents beyond "BMI above 25" in Section 8.2).
BMI_UNDERWEIGHT_MAX = 18.5
BMI_NORMAL_MAX = 25.0
BMI_OVERWEIGHT_MAX = 30.0

# Health-goal-derived minimums (Project Description Section 8.3).
MUSCLE_GAIN_MIN_PROTEIN_G = 120
MUSCLE_GAIN_TARGET_CALORIES = 2600


def compute_bmi(weight_kg: float, height_cm: float) -> float:
    """BMI = weight_kg / height_m^2 (Project Description Section 8.2).

    Not implemented this milestone — see module docstring.
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")


def resolve_nutrition_target(profile: ProfileInput) -> NutritionTarget:
    """Resolve a profile's activity level, BMI, and health goal into a
    concrete NutritionTarget (Project Description Section 8.3 / Section 9
    Stage 2). Downstream filtering (filters.py) must use this target rather
    than re-deriving it from raw profile fields.

    Not implemented this milestone — see module docstring.
    """
    raise NotImplementedError("Planned for Milestone 2 (rule engine implementation).")
