"""REQ-4.1.3, REQ-4.1.4, REQ-4.1.5 — implemented in Milestone 1."""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/me")
def get_my_profile() -> None:
    raise not_implemented("Profile retrieval", "Milestone 1")


@router.put("/me")
def upsert_my_profile() -> None:
    raise not_implemented("Profile creation/edit", "Milestone 1")
