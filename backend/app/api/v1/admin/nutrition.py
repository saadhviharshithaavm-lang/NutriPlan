"""REQ-4.7.1, REQ-4.7.4 — implemented in Milestone 5."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/admin/nutrition", tags=["admin"])


@router.get("")
def list_nutrition_values() -> None:
    raise not_implemented("Admin nutrition value CRUD", "Milestone 5")
