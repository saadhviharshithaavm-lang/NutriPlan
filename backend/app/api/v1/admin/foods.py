"""REQ-4.7.1, REQ-4.7.2 — implemented in Milestone 5."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/admin/foods", tags=["admin"])


@router.get("")
def list_foods() -> None:
    raise not_implemented("Admin food CRUD", "Milestone 5")
