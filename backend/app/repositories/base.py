"""Generic repository base class.

Repositories isolate persistence (SQLAlchemy queries) from services/ (business
logic) and api/ (HTTP concerns). No concrete repositories are implemented yet
this milestone — they land alongside each feature's route in later
milestones (see docs/development-roadmap.md).
"""

from sqlalchemy.orm import Session

from app.db.base import Base


class BaseRepository[ModelT: Base]:
    def __init__(self, db: Session, model: type[ModelT]) -> None:
        self.db = db
        self.model = model

    def get(self, id_: int) -> ModelT | None:
        return self.db.get(self.model, id_)
