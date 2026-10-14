"""Ingredient (Food) with per-100g nutrition and price (SRS Section 3.2 Food Database)."""

from typing import TYPE_CHECKING

from sqlalchemy import Column, Enum, ForeignKey, Numeric, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.enums import Unit
from app.models.mixins import TimestampMixin

if TYPE_CHECKING:
    from app.models.allergen import Allergen
    from app.models.recipe_ingredient import RecipeIngredient

ingredient_allergens = Table(
    "ingredient_allergens",
    Base.metadata,
    Column("ingredient_id", ForeignKey("ingredients.id", ondelete="CASCADE"), primary_key=True),
    Column("allergen_id", ForeignKey("allergens.id", ondelete="CASCADE"), primary_key=True),
)


class Ingredient(TimestampMixin, Base):
    __tablename__ = "ingredients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), unique=True, index=True, nullable=False)
    unit: Mapped[Unit] = mapped_column(Enum(Unit, name="unit"), nullable=False)

    # Nutrition per 100 units (100g / 100ml), consistent basis for aggregation.
    calories_per_100_units: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    protein_g_per_100_units: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    carbs_g_per_100_units: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    fat_g_per_100_units: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)

    # Illustrative development price only — not a verified market price (see
    # docs/requirements/open-decisions.md and master prompt Section 6).
    price_per_unit_inr: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    allergens: Mapped[list["Allergen"]] = relationship(
        secondary=ingredient_allergens, back_populates="ingredients"
    )
    recipe_ingredients: Mapped[list["RecipeIngredient"]] = relationship(
        back_populates="ingredient"
    )
