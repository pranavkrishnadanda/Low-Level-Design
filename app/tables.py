from sqlalchemy import Column, String, DateTime
from database import Base
import uuid
from datetime import datetime,timezone

class Todo(Base):
    __tablename__ = 'reminders'

    todo_id     = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title       = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status      = Column(String, nullable=False, default="pending")
    created_at  = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at  = Column(DateTime, onupdate=lambda: datetime.now(timezone.utc))