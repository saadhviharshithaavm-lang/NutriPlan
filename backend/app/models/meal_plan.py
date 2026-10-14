"""Weekly meal plan, owned by a user (SRS REQ-4.2.1)."""

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.planned_meal import PlannedMeal
    from app.models.user import User


class MealPlan(TimestampMixin, Base):
    __tablename__ = "meal_plans"
    __table_args__ = (UniqueConstraint("user_id", "week_start_date"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    # Monday of the planned week; a user has at most one plan per week.
    week_start_date: Mapped[date] = mapped_column(Date, nullable=False)

    user: Mapped["User"] = relationship(back_populates="meal_plans")
    planned_meals: Mapped[list["PlannedMeal"]] = relationship(
        back_populates="meal_plan", cascade="all, delete-orphan"
    )
