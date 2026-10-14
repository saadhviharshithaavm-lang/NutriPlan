"""Verify every model registers with Base.metadata (needed by Alembic and by
Base.metadata.create_all-based integration tests)."""

import app.models  # noqa: F401  (populates Base.metadata)
from app.db.base import Base

EXPECTED_TABLES = {
    "users",
    "user_profiles",
    "user_profile_allergens",
    "allergens",
    "ingredients",
    "ingredient_allergens",
    "recipes",
    "recipe_ingredients",
    "recipe_nutrition",
    "meal_categories",
    "meal_plans",
    "planned_meals",
    "feedback_events",
}


def test_all_expected_tables_are_registered() -> None:
    assert EXPECTED_TABLES.issubset(set(Base.metadata.tables.keys()))


def test_users_email_column_is_unique() -> None:
    users_table = Base.metadata.tables["users"]
    email_column = users_table.columns["email"]
    assert email_column.unique or any(
        "email" in idx.columns.keys() and idx.unique for idx in users_table.indexes
    )


def test_recipe_belongs_to_exactly_one_meal_category() -> None:
    recipes_table = Base.metadata.tables["recipes"]
    assert "meal_category_id" in recipes_table.columns
    assert not recipes_table.columns["meal_category_id"].nullable
