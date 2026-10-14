"""NutriPlan FastAPI application entry point.

Run from inside backend/ with:
    python -m uvicorn app.main:app --reload
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.errors import register_exception_handlers
from app.core.logging import configure_logging

settings = get_settings()
configure_logging(settings.debug)

app = FastAPI(
    title=settings.app_name,
    description=(
        "NutriPlan Release 1.0 (Phase 1) API. Many endpoints are structural "
        "placeholders at this milestone and return HTTP 501 until their "
        "milestone lands — see docs/requirements/requirements-matrix.md."
    ),
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)

app.include_router(api_router, prefix=settings.api_v1_prefix)
