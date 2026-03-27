#backend>app>models>exam.py

from sqlalchemy import Column, String, SmallInteger, Boolean
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base
import uuid

class Exam(Base):
    __tablename__ = "exams"

    exam_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_name = Column(String(100))
    year = Column(SmallInteger)

    # 🔥 ADD THESE (match your service)
    semester = Column(SmallInteger)
    is_active = Column(Boolean, default=True)









   
# old code 
# from sqlalchemy import Column, String, SmallInteger
# from sqlalchemy.dialects.postgresql import UUID
# from app.database import Base
# import uuid

# class Exam(Base):
#     __tablename__ = "exams"

#     exam_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     exam_name = Column(String(100))
#     year = Column(SmallInteger)