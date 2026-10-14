"""REQ-4.7.1, REQ-4.7.3 — implemented in Milestone 5."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/admin/recipes", tags=["admin"])


@router.get("")
def list_recipes() -> None:
    raise not_implemented("Admin recipe CRUD", "Milestone 5")
