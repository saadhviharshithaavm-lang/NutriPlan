"""Allergen, represented structurally (SRS: "allergens must be represented
structurally so filtering does not rely exclusively on string matching").
"""

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.ingredient import Ingredient
    from app.models.user_profile import UserProfile


class Allergen(TimestampMixin, Base):
    __tablename__ = "allergens"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)

    ingredients: Mapped[list["Ingredient"]] = relationship(
        secondary="ingredient_allergens", back_populates="allergens"
    )
    user_profiles: Mapped[list["UserProfile"]] = relationship(
        secondary="user_profile_allergens", back_populates="allergies"
    )
