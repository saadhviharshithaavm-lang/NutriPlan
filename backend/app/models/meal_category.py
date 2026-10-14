"""Meal category.

Per docs/requirements/open-decisions.md (decision D1), this table is seeded
with exactly four rows (breakfast, lunch, dinner, snack) by migration. The
Admin Panel (REQ-4.7.5) may read and update these rows but the application
layer does not expose create/delete operations on this table, to preserve the
SRS's "every recipe belongs to exactly one of four meal categories" invariant.
"""

from typing import TYPE_CHECKING

from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.planned_meal import PlannedMeal
    from app.models.recipe import Recipe


class MealCategory(TimestampMixin, Base):
    __tablename__ = "meal_categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    display_order: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    recipes: Mapped[list["Recipe"]] = relationship(back_populates="meal_category")
    planned_meals: Mapped[list["PlannedMeal"]] = relationship(back_populates="meal_category")
