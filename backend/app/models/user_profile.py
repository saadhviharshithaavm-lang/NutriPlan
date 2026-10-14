"""User profile (SRS REQ-4.1.3): the attributes the rule engine consumes."""

from typing import TYPE_CHECKING

from sqlalchemy import Column, Enum, ForeignKey, Numeric, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import ActivityLevel, DietaryPreference, Gender, HealthGoal
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.allergen import Allergen
    from app.models.user import User

user_profile_allergens = Table(
    "user_profile_allergens",
    Base.metadata,
    Column(
        "user_profile_id",
        ForeignKey("user_profiles.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("allergen_id", ForeignKey("allergens.id", ondelete="CASCADE"), primary_key=True),
)


class UserProfile(TimestampMixin, Base):
    __tablename__ = "user_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False
    )

    age: Mapped[int] = mapped_column(nullable=False)
    gender: Mapped[Gender] = mapped_column(Enum(Gender, name="gender"), nullable=False)
    height_cm: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)
    weight_kg: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)

    # Included despite not being literally listed in REQ-4.1.3's field list —
    # see docs/requirements/open-decisions.md, decision D3.
    activity_level: Mapped[ActivityLevel] = mapped_column(
        Enum(ActivityLevel, name="activity_level"), nullable=False
    )

    dietary_preference: Mapped[DietaryPreference] = mapped_column(
        Enum(DietaryPreference, name="dietary_preference"), nullable=False
    )
    health_goal: Mapped[HealthGoal] = mapped_column(
        Enum(HealthGoal, name="health_goal"), nullable=False
    )
    weekly_budget_inr: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    cooking_time_limit_minutes: Mapped[int] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="profile")
    allergies: Mapped[list["Allergen"]] = relationship(
        secondary=user_profile_allergens, back_populates="user_profiles"
    )
