#backend>app>schemas>student.py

from pydantic import BaseModel
from typing import Optional

# Request schema
class StudentCreate(BaseModel):
    username: str
    password: str
    enroll_no: str
    first_name: Optional[str]
    last_name: Optional[str]
    semester: Optional[int]
    email: str

# Response schema
class StudentResponse(BaseModel):
    std_id: str
    enroll_no: str
    first_name: Optional[str]
    last_name: Optional[str]
    semester: Optional[int]
    email: str

    class Config:
        from_attributes = True