# app/models/user.py
import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = 'users'
    user_id    = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username   = Column(String(50), unique=True, nullable=False, index=True)
    password   = Column(String(255), nullable=False)
    designation = Column(String(10), nullable=False)  # 'admin' | 'student'
    is_active  = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())