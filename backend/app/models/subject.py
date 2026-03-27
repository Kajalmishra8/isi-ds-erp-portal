#backend>app>models>subject.py

# from sqlalchemy import Column, String, SmallInteger
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Subject(Base):
    __tablename__ = "subjects"

    sub_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    sub_code = Column(String(20))
    sub_name = Column(String(100))
    max_marks = Column(SmallInteger, default=100)
    semester = Column(SmallInteger) 