"""REQ-4.6.1-4.6.4 — implemented in Milestone 5."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def get_dashboard_summary() -> None:
    raise not_implemented("Dashboard summary", "Milestone 5")
