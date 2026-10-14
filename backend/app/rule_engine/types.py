"""Domain types for the rule engine.

These are plain dataclasses, independent of the SQLAlchemy models in
app/models/. Keeping the rule engine's inputs/outputs framework-agnostic
means every stage (nutrition, filters, ranking, variety, planner, validator)
can be unit-tested without a database, and the same types can be reused as
the Phase 2 LLM layer's input contract without redesigning the data model
(SRS Section 2.1).
"""

from dataclasses import dataclass, field
from datetime import date
from enum import StrEnum


class BmiCategory(StrEnum):
    UNDERWEIGHT = "underweight"
    NORMAL = "normal"
    OVERWEIGHT = "overweight"
    OBESE = "obese"


@dataclass(frozen=True)
class ProfileInput:
    """Validated profile attributes consumed by the rule engine (REQ-4.1.3)."""

    age: int
    gender: str
    height_cm: float
    weight_kg: float
    activity_level: str
    dietary_preference: str
    allergies: frozenset[str]
    health_goal: str
    weekly_budget_inr: float
    cooking_time_limit_minutes: int


@dataclass(frozen=True)
class NutritionTarget:
    """Output of Stage 2 (Project Description Section 9): concrete numeric
    targets the rest of the pipeline filters and ranks meals against.
    """

    bmi: float
    bmi_category: BmiCategory
    calorie_target: int
    protein_target_g: int


@dataclass(frozen=True)
class MealCandidate:
    """A recipe considered eligible at some stage of the pipeline."""

    recipe_id: int
    name: str
    meal_category: str
    dietary_preference: str
    prep_time_minutes: int
    calories: float
    protein_g: float
    carbs_g: float
    fat_g: float
    estimated_cost_inr: float
    allergens: frozenset[str]


@dataclass(frozen=True)
class FeedbackSignal:
    """A single stored feedback event, as read by the ranking stage."""

    recipe_id: int
    feedback_type: str
    weight: int


@dataclass(frozen=True)
class PlannedSlot:
    """One filled day/category slot in an assembled weekly plan."""

    day_index: int  # 0-6, relative to week_start_date
    meal_category: str
    recipe_id: int


@dataclass(frozen=True)
class InfeasibleSlot:
    """A day/category slot that could not be filled without violating a hard
    constraint (REQ-4.2.8) — see docs/requirements/open-decisions.md, D2.
    """

    day_index: int
    meal_category: str
    reason: str


@dataclass(frozen=True)
class WeeklyPlanResult:
    week_start_date: date
    slots: list[PlannedSlot] = field(default_factory=list)
    infeasible_slots: list[InfeasibleSlot] = field(default_factory=list)

    @property
    def is_fully_feasible(self) -> bool:
        return not self.infeasible_slots


@dataclass(frozen=True)
class GroceryItem:
    ingredient_name: str
    quantity: float
    unit: str


@dataclass(frozen=True)
class ValidationResult:
    """Output of validator.py: whether a plan or single meal satisfies every
    hard constraint. Hard constraints must never be relaxed to produce a
    "closest feasible" result (SRS Section 2.5 / 5.2; see open-decisions D2).
    """

    is_valid: bool
    violations: list[str] = field(default_factory=list)
