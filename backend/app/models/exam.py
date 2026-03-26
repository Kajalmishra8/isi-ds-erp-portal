from sqlalchemy import Column, String, SmallInteger
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Exam(Base):
    __tablename__ = "exams"

    exam_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_name = Column(String(100))
    year = Column(SmallInteger)