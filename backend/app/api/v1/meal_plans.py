"""REQ-4.2.1-4.2.8 (generation) and REQ-4.5.1-4.5.5 (replacement) —
implemented in Milestone 3/4 once app/rule_engine/planner.py is built.
"""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/meal-plans", tags=["meal-plans"])


@router.post("/generate")
def generate_weekly_plan() -> None:
    raise not_implemented("Weekly meal plan generation", "Milestone 3")


@router.get("/current")
def get_current_plan() -> None:
    raise not_implemented("Weekly meal plan retrieval", "Milestone 3")


@router.post("/{plan_id}/meals/{planned_meal_id}/replace")
def replace_meal(plan_id: int, planned_meal_id: int) -> None:
    raise not_implemented("Meal replacement", "Milestone 4")
