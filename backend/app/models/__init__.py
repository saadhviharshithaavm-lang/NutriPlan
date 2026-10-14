"""Import every model module so Base.metadata is fully populated.

Alembic's env.py and test fixtures that use Base.metadata.create_all rely on
this module having been imported first.
"""

from app.models.allergen import Allergen
from app.models.feedback import Feedback
from app.models.ingredient import Ingredient, ingredient_allergens
from app.models.meal_category import MealCategory
from app.models.meal_plan import MealPlan
from app.models.planned_meal import PlannedMeal
from app.models.recipe import Recipe
from app.models.recipe_ingredient import RecipeIngredient
from app.models.recipe_nutrition import RecipeNutrition
from app.models.user import User
from app.models.user_profile import UserProfile, user_profile_allergens

__all__ = [
    "Allergen",
    "Feedback",
    "Ingredient",
    "ingredient_allergens",
    "MealCategory",
    "MealPlan",
    "PlannedMeal",
    "Recipe",
    "RecipeIngredient",
    "RecipeNutrition",
    "User",
    "UserProfile",
    "user_profile_allergens",
]
