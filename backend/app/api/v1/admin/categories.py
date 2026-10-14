"""REQ-4.7.1, REQ-4.7.5 — implemented in Milestone 5.

Per docs/requirements/open-decisions.md (decision D1), this will expose read
and update of the four seeded MealCategory rows only — not create/delete —
to preserve the SRS's fixed four-category invariant.
"""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/admin/categories", tags=["admin"])


@router.get("")
def list_categories() -> None:
    raise not_implemented("Admin category read/update", "Milestone 5")
