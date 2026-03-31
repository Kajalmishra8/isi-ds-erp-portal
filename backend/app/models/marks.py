#backend>app>models>marks.py

import uuid
from sqlalchemy import Column, SmallInteger, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
# from app.utils.database import Base  
from app.database import Base

class Mark(Base):
    __tablename__ = 'marks'
    __table_args__ = (UniqueConstraint('std_id','exam_id','sub_id'),)

    mark_id        = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    std_id         = Column(UUID(as_uuid=True), ForeignKey('students.std_id', ondelete='CASCADE'), nullable=False, index=True)
    exam_id        = Column(UUID(as_uuid=True), ForeignKey('exams.exam_id', ondelete='CASCADE'), nullable=False, index=True)
    sub_id         = Column(UUID(as_uuid=True), ForeignKey('subjects.sub_id', ondelete='CASCADE'), nullable=False)

    marks_obtained = Column(SmallInteger, nullable=False)

    created_at     = Column(DateTime(timezone=True), server_default=func.now())
    updated_at     = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    student        = relationship('Student', back_populates='marks')
    exam           = relationship('Exam')
    subject        = relationship('Subject')