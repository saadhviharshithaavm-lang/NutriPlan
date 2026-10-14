"""REQ-4.3.1-4.3.4 — implemented in Milestone 3."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/grocery-lists", tags=["grocery"])


@router.get("/current")
def get_current_grocery_list() -> None:
    raise not_implemented("Grocery list generation", "Milestone 3")
