"""A single recipe assigned to one day/slot of a weekly plan (SRS REQ-4.2.1).

`day_index` is 0-6 relative to the owning MealPlan.week_start_date (0 = that
Monday). This is an implementation choice, not specified verbatim by the SRS,
made so a slot can be identified without duplicating an absolute date.
"""

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, SmallInteger, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.meal_category import MealCategory
    from app.models.meal_plan import MealPlan
    from app.models.recipe import Recipe


class PlannedMeal(TimestampMixin, Base):
    __tablename__ = "planned_meals"
    __table_args__ = (
        UniqueConstraint("meal_plan_id", "day_index", "meal_category_id"),
        CheckConstraint("day_index >= 0 AND day_index <= 6", name="ck_planned_meal_day_index"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    meal_plan_id: Mapped[int] = mapped_column(
        ForeignKey("meal_plans.id", ondelete="CASCADE"), nullable=False, index=True
    )
    day_index: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    meal_category_id: Mapped[int] = mapped_column(
        ForeignKey("meal_categories.id"), nullable=False
    )
    recipe_id: Mapped[int] = mapped_column(ForeignKey("recipes.id"), nullable=False, index=True)

    meal_plan: Mapped["MealPlan"] = relationship(back_populates="planned_meals")
    meal_category: Mapped["MealCategory"] = relationship(back_populates="planned_meals")
    recipe: Mapped["Recipe"] = relationship(back_populates="planned_meals")
