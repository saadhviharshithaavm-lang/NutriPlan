"""Shared enumerations used across models, schemas, and the rule engine.

Values are drawn directly from the SRS and Project Description where the
document is explicit (health goal, activity level, feedback type). Where the
documents are not explicit (gender options, dietary preference set), a
reasonable Indian-context default set is assumed and documented inline — see
docs/requirements/open-decisions.md for the broader assumptions log.
"""

import enum


class UserRole(enum.StrEnum):
    USER = "user"
    ADMIN = "admin"


class Gender(enum.StrEnum):
    """Not enumerated explicitly in the SRS; assumed set for profile capture."""

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class ActivityLevel(enum.StrEnum):
    """Per Project Description Section 8.1 (activity-adjusted calorie baseline)."""

    SEDENTARY = "sedentary"
    MODERATELY_ACTIVE = "moderately_active"
    VERY_ACTIVE = "very_active"


class DietaryPreference(enum.StrEnum):
    """Not exhaustively enumerated in the SRS beyond "Vegetarian" examples;
    this set reflects common Indian dietary categories and is an assumption
    to be confirmed with the Product Owner.
    """

    OMNIVORE = "omnivore"
    VEGETARIAN = "vegetarian"
    VEGAN = "vegan"
    EGGETARIAN = "eggetarian"
    PESCATARIAN = "pescatarian"


class HealthGoal(enum.StrEnum):
    """Per SRS REQ-4.2.4 and Project Description Section 8.3."""

    WEIGHT_LOSS = "weight_loss"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"


class MealSlot(enum.StrEnum):
    """The four fixed meal categories (SRS Section 2.5 / Appendix A).

    Mirrors the seeded MealCategory rows by name; kept as an enum as well so
    the rule engine and schemas can reference slots without a DB round trip.
    """

    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"


class FeedbackType(enum.StrEnum):
    """Per SRS REQ-4.4.1 and Project Description Section 10.3 (scoring)."""

    FAVORITE = "favorite"
    LIKE = "like"
    SKIP = "skip"
    DISLIKE = "dislike"


class Unit(enum.StrEnum):
    """Consistent units for ingredient quantities (SRS REQ-4.3.4)."""

    GRAM = "g"
    KILOGRAM = "kg"
    MILLILITER = "ml"
    LITER = "l"
    PIECE = "piece"
    TABLESPOON = "tbsp"
    TEASPOON = "tsp"
    CUP = "cup"


# Feedback weights per Project Description Section 10.3 / master prompt Section 7.
FEEDBACK_WEIGHTS: dict[FeedbackType, int] = {
    FeedbackType.FAVORITE: 3,
    FeedbackType.LIKE: 1,
    FeedbackType.SKIP: -1,
    FeedbackType.DISLIKE: -3,
}
