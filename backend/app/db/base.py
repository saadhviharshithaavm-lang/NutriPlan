"""SQLAlchemy declarative base.

Alembic's env.py imports `Base.metadata` as its migration target, and
app/db/base_models.py (imported for side effects wherever metadata must be
complete, e.g. in Alembic env.py and conftest.py) ensures every model module
has registered its table with this metadata before migrations or
`create_all`-based test fixtures run.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass
