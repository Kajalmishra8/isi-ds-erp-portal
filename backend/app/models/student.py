# app/models/student.py
import uuid
from sqlalchemy import Column, String, SmallInteger, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Student(Base):
    __tablename__ = 'students'
    std_id     = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id    = Column(UUID(as_uuid=True), ForeignKey('users.user_id', ondelete='CASCADE'), unique=True)
    enroll_no  = Column(String(30), unique=True, nullable=False, index=True)
    first_name = Column(String(50), nullable=False)
    last_name  = Column(String(50), nullable=False)
    phone      = Column(String(20))
    email      = Column(String(100), unique=True, nullable=False)
    semester   = Column(SmallInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    marks      = relationship('Mark', back_populates='student', cascade='all, delete-orphan')