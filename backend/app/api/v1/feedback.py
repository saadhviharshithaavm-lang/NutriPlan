"""REQ-4.4.1-4.4.4 — implemented in Milestone 4."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/feedback", tags=["feedback"])


@router.post("/recipes/{recipe_id}")
def submit_feedback(recipe_id: int) -> None:
    raise not_implemented("Feedback submission", "Milestone 4")
