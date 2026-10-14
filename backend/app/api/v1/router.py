from fastapi import APIRouter

from app.api.v1 import auth, dashboard, feedback, grocery, health, meal_plans, profiles
from app.api.v1.admin import categories, foods, nutrition, recipes

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(profiles.router)
api_router.include_router(meal_plans.router)
api_router.include_router(grocery.router)
api_router.include_router(feedback.router)
api_router.include_router(dashboard.router)
api_router.include_router(foods.router)
api_router.include_router(recipes.router)
api_router.include_router(nutrition.router)
api_router.include_router(categories.router)
