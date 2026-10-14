"""Pre-calculated per-recipe nutrition and cost totals.

Stored (not computed on the fly) per the SRS assumption that "recipe
nutritional values are pre-calculated and available before meal generation."
Keeping an estimated total cost alongside nutrition lets the rule engine's
per-meal budget check (Project Description Section 9, Stage 5) read a single
row instead of summing recipe_ingredients * ingredient prices per request.
"""

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.recipe import Recipe


class RecipeNutrition(TimestampMixin, Base):
    __tablename__ = "recipe_nutrition"

    id: Mapped[int] = mapped_column(primary_key=True)
    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipes.id", ondelete="CASCADE"), unique=True, nullable=False
    )

    calories: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    protein_g: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    carbs_g: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    fat_g: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)

    # Illustrative development estimate only — not a verified market price.
    estimated_cost_inr: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    recipe: Mapped["Recipe"] = relationship(back_populates="nutrition")
