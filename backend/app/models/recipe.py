"""Recipe (SRS Section 3.2 Recipe Database, Section 4.7.3)."""

from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import DietaryPreference
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.feedback import Feedback
    from app.models.meal_category import MealCategory
    from app.models.planned_meal import PlannedMeal
    from app.models.recipe_ingredient import RecipeIngredient
    from app.models.recipe_nutrition import RecipeNutrition


class Recipe(TimestampMixin, Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Every recipe belongs to exactly one meal category (SRS Section 2.5).
    meal_category_id: Mapped[int] = mapped_column(
        ForeignKey("meal_categories.id"), nullable=False, index=True
    )

    # The strictest diet type this recipe satisfies, used by rule_engine.filters
    # (REQ-4.2.2). E.g. a VEGAN recipe is eligible for a VEGETARIAN user too;
    # this ordering is a rule_engine concern, not encoded here.
    dietary_preference: Mapped[DietaryPreference] = mapped_column(
        Enum(DietaryPreference, name="dietary_preference"), nullable=False
    )

    prep_time_minutes: Mapped[int] = mapped_column(nullable=False)

    meal_category: Mapped["MealCategory"] = relationship(back_populates="recipes")
    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="recipe", cascade="all, delete-orphan"
    )
    nutrition: Mapped["RecipeNutrition | None"] = relationship(
        back_populates="recipe", uselist=False, cascade="all, delete-orphan"
    )
    planned_meals: Mapped[list["PlannedMeal"]] = relationship(back_populates="recipe")
    feedback_events: Mapped[list["Feedback"]] = relationship(back_populates="recipe")
