"""REQ-4.1.1, REQ-4.1.2 — implemented in Milestone 1.

See docs/requirements/open-decisions.md, decision D7.
"""

from fastapi import APIRouter

from app.api.v1.placeholders import not_implemented

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register")
def register() -> None:
    raise not_implemented("User registration", "Milestone 1")


@router.post("/login")
def login() -> None:
    raise not_implemented("User login", "Milestone 1")


@router.post("/logout")
def logout() -> None:
    raise not_implemented("User logout", "Milestone 1")
