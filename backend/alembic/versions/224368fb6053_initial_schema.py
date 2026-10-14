"""initial schema

Revision ID: 224368fb6053
Revises:
Create Date: 2026-10-13 23:18:26.599471

Creates the full Milestone 0 domain model (users, profiles, allergens,
ingredients, recipes, meal categories, meal plans, planned meals, feedback)
and seeds the four fixed MealCategory rows (breakfast, lunch, dinner, snack)
per docs/requirements/open-decisions.md, decision D1. No illustrative
food/recipe data is seeded here — see a future seed script for that,
clearly labelled as non-production sample data.
"""

from collections.abc import Sequence

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "224368fb6053"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None

# --- Enum type definitions (matching app/models/enums.py) ---
user_role_enum = postgresql.ENUM("user", "admin", name="user_role")
gender_enum = postgresql.ENUM("male", "female", "other", name="gender")
activity_level_enum = postgresql.ENUM(
    "sedentary", "moderately_active", "very_active", name="activity_level"
)
dietary_preference_enum = postgresql.ENUM(
    "omnivore", "vegetarian", "vegan", "eggetarian", "pescatarian", name="dietary_preference"
)
health_goal_enum = postgresql.ENUM(
    "weight_loss", "muscle_gain", "maintenance", name="health_goal"
)
feedback_type_enum = postgresql.ENUM(
    "favorite", "like", "skip", "dislike", name="feedback_type"
)
unit_enum = postgresql.ENUM(
    "g", "kg", "ml", "l", "piece", "tbsp", "tsp", "cup", name="unit"
)

ALL_ENUMS = [
    user_role_enum,
    gender_enum,
    activity_level_enum,
    dietary_preference_enum,
    health_goal_enum,
    feedback_type_enum,
    unit_enum,
]


def upgrade() -> None:
    bind = op.get_bind()
    for enum_type in ALL_ENUMS:
        enum_type.create(bind, checkfirst=True)

    # Re-bind enum columns with create_type=False so create_table doesn't
    # attempt to CREATE TYPE a second time for enums used on multiple tables.
    user_role_col = postgresql.ENUM(
        "user", "admin", name="user_role", create_type=False
    )
    gender_col = postgresql.ENUM(
        "male", "female", "other", name="gender", create_type=False
    )
    activity_level_col = postgresql.ENUM(
        "sedentary",
        "moderately_active",
        "very_active",
        name="activity_level",
        create_type=False,
    )
    dietary_preference_col = postgresql.ENUM(
        "omnivore",
        "vegetarian",
        "vegan",
        "eggetarian",
        "pescatarian",
        name="dietary_preference",
        create_type=False,
    )
    health_goal_col = postgresql.ENUM(
        "weight_loss",
        "muscle_gain",
        "maintenance",
        name="health_goal",
        create_type=False,
    )
    feedback_type_col = postgresql.ENUM(
        "favorite", "like", "skip", "dislike", name="feedback_type", create_type=False
    )
    unit_col = postgresql.ENUM(
        "g", "kg", "ml", "l", "piece", "tbsp", "tsp", "cup", name="unit", create_type=False
    )

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("role", user_role_col, nullable=False, server_default="user"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.true()),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "allergens",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=100), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_allergens_name", "allergens", ["name"], unique=True)

    op.create_table(
        "meal_categories",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("display_order", sa.Integer(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_meal_categories_name", "meal_categories", ["name"], unique=True)

    op.create_table(
        "ingredients",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("unit", unit_col, nullable=False),
        sa.Column("calories_per_100_units", sa.Numeric(7, 2), nullable=False),
        sa.Column("protein_g_per_100_units", sa.Numeric(7, 2), nullable=False),
        sa.Column("carbs_g_per_100_units", sa.Numeric(7, 2), nullable=False),
        sa.Column("fat_g_per_100_units", sa.Numeric(7, 2), nullable=False),
        sa.Column("price_per_unit_inr", sa.Numeric(10, 2), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_ingredients_name", "ingredients", ["name"], unique=True)

    op.create_table(
        "ingredient_allergens",
        sa.Column(
            "ingredient_id",
            sa.Integer(),
            sa.ForeignKey("ingredients.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "allergen_id",
            sa.Integer(),
            sa.ForeignKey("allergens.id", ondelete="CASCADE"),
            primary_key=True,
        ),
    )

    op.create_table(
        "user_profiles",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id", ondelete="CASCADE"),
            nullable=False,
            unique=True,
        ),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("gender", gender_col, nullable=False),
        sa.Column("height_cm", sa.Numeric(5, 2), nullable=False),
        sa.Column("weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("activity_level", activity_level_col, nullable=False),
        sa.Column("dietary_preference", dietary_preference_col, nullable=False),
        sa.Column("health_goal", health_goal_col, nullable=False),
        sa.Column("weekly_budget_inr", sa.Numeric(10, 2), nullable=False),
        sa.Column("cooking_time_limit_minutes", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )

    op.create_table(
        "user_profile_allergens",
        sa.Column(
            "user_profile_id",
            sa.Integer(),
            sa.ForeignKey("user_profiles.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column(
            "allergen_id",
            sa.Integer(),
            sa.ForeignKey("allergens.id", ondelete="CASCADE"),
            primary_key=True,
        ),
    )

    op.create_table(
        "recipes",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column(
            "meal_category_id", sa.Integer(), sa.ForeignKey("meal_categories.id"), nullable=False
        ),
        sa.Column("dietary_preference", dietary_preference_col, nullable=False),
        sa.Column("prep_time_minutes", sa.Integer(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_recipes_name", "recipes", ["name"])
    op.create_index("ix_recipes_meal_category_id", "recipes", ["meal_category_id"])

    op.create_table(
        "recipe_ingredients",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "recipe_id",
            sa.Integer(),
            sa.ForeignKey("recipes.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column(
            "ingredient_id", sa.Integer(), sa.ForeignKey("ingredients.id"), nullable=False
        ),
        sa.Column("quantity", sa.Numeric(8, 2), nullable=False),
        sa.Column("unit", unit_col, nullable=False),
        sa.UniqueConstraint("recipe_id", "ingredient_id"),
    )
    op.create_index("ix_recipe_ingredients_recipe_id", "recipe_ingredients", ["recipe_id"])
    op.create_index(
        "ix_recipe_ingredients_ingredient_id", "recipe_ingredients", ["ingredient_id"]
    )

    op.create_table(
        "recipe_nutrition",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "recipe_id",
            sa.Integer(),
            sa.ForeignKey("recipes.id", ondelete="CASCADE"),
            nullable=False,
            unique=True,
        ),
        sa.Column("calories", sa.Numeric(7, 2), nullable=False),
        sa.Column("protein_g", sa.Numeric(7, 2), nullable=False),
        sa.Column("carbs_g", sa.Numeric(7, 2), nullable=False),
        sa.Column("fat_g", sa.Numeric(7, 2), nullable=False),
        sa.Column("estimated_cost_inr", sa.Numeric(10, 2), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )

    op.create_table(
        "meal_plans",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
        ),
        sa.Column("week_start_date", sa.Date(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.UniqueConstraint("user_id", "week_start_date"),
    )
    op.create_index("ix_meal_plans_user_id", "meal_plans", ["user_id"])

    op.create_table(
        "planned_meals",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "meal_plan_id",
            sa.Integer(),
            sa.ForeignKey("meal_plans.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("day_index", sa.SmallInteger(), nullable=False),
        sa.Column(
            "meal_category_id", sa.Integer(), sa.ForeignKey("meal_categories.id"), nullable=False
        ),
        sa.Column("recipe_id", sa.Integer(), sa.ForeignKey("recipes.id"), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.Column(
            "updated_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
        sa.UniqueConstraint("meal_plan_id", "day_index", "meal_category_id"),
        sa.CheckConstraint(
            "day_index >= 0 AND day_index <= 6", name="ck_planned_meal_day_index"
        ),
    )
    op.create_index("ix_planned_meals_meal_plan_id", "planned_meals", ["meal_plan_id"])
    op.create_index("ix_planned_meals_recipe_id", "planned_meals", ["recipe_id"])

    op.create_table(
        "feedback_events",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column(
            "user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False
        ),
        sa.Column(
            "recipe_id",
            sa.Integer(),
            sa.ForeignKey("recipes.id", ondelete="CASCADE"),
            nullable=False,
        ),
        sa.Column("feedback_type", feedback_type_col, nullable=False),
        sa.Column(
            "created_at", sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False
        ),
    )
    op.create_index("ix_feedback_events_user_id", "feedback_events", ["user_id"])
    op.create_index("ix_feedback_events_recipe_id", "feedback_events", ["recipe_id"])

    # Seed the four fixed meal categories (SRS Section 2.5 / open-decisions D1).
    # This is structural application data, not illustrative/sample content.
    meal_categories_table = sa.table(
        "meal_categories",
        sa.column("name", sa.String),
        sa.column("display_order", sa.Integer),
        sa.column("description", sa.Text),
    )
    op.bulk_insert(
        meal_categories_table,
        [
            {"name": "breakfast", "display_order": 1, "description": "Morning meal."},
            {"name": "lunch", "display_order": 2, "description": "Midday meal."},
            {"name": "dinner", "display_order": 3, "description": "Evening meal."},
            {"name": "snack", "display_order": 4, "description": "Between-meal snack."},
        ],
    )


def downgrade() -> None:
    op.drop_table("feedback_events")
    op.drop_table("planned_meals")
    op.drop_table("meal_plans")
    op.drop_table("recipe_nutrition")
    op.drop_table("recipe_ingredients")
    op.drop_table("recipes")
    op.drop_table("user_profile_allergens")
    op.drop_table("user_profiles")
    op.drop_table("ingredient_allergens")
    op.drop_table("ingredients")
    op.drop_table("meal_categories")
    op.drop_table("allergens")
    op.drop_table("users")

    bind = op.get_bind()
    for enum_type in ALL_ENUMS:
        enum_type.drop(bind, checkfirst=True)
