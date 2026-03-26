from sqlalchemy import Column, String
from app.database import Base


class Admin(Base):
    __tablename__ = "admins"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)