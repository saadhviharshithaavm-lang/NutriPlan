"""Database integration test — runs only when a reachable Postgres database
is configured (master prompt Section 11: "Database integration tests can run
against a dedicated test database where configured"). Skipped, not failed,
when no database is reachable (e.g. Docker not running), since Milestone 0
does not require a live database for the rest of the test suite to pass.
"""

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

import app.models  # noqa: F401  (populates Base.metadata)
from app.core.config import get_settings
from app.db.base import Base


def _database_is_reachable() -> bool:
    try:
        engine = create_engine(get_settings().database_url, pool_pre_ping=True)
        with engine.connect():
            return True
    except OperationalError:
        return False


pytestmark = pytest.mark.skipif(
    not _database_is_reachable(),
    reason="No reachable Postgres database configured (see backend/.env).",
)


def test_create_all_and_basic_round_trip() -> None:
    engine = create_engine(get_settings().database_url)
    Base.metadata.create_all(engine)
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            assert result.scalar_one() == 1
    finally:
        Base.metadata.drop_all(engine)
