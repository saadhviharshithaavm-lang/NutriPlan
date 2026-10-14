"""User account (SRS REQ-4.1.1, REQ-4.1.2, Section 5.3)."""

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import UserRole
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.feedback import Feedback
    from app.models.meal_plan import MealPlan
    from app.models.user_profile import UserProfile


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    # Hash only — never store or transmit plaintext passwords (SRS Section 5.3).
    # Hashing itself is implemented in Milestone 1 (see core/security.py).
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(
        Enum(UserRole, name="user_role"), nullable=False, default=UserRole.USER
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    profile: Mapped["UserProfile | None"] = relationship(
        back_populates="user", uselist=False, cascade="all, delete-orphan"
    )
    meal_plans: Mapped[list["MealPlan"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    feedback_events: Mapped[list["Feedback"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
