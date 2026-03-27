#backend>app>schemas>exam.py

from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ExamCreate(BaseModel):
    exam_name: Optional[str]
    year: Optional[int]
    semester: int   

class ExamResponse(BaseModel):
    exam_id: UUID
    exam_name: Optional[str]
    year: Optional[int]

    class Config:
        from_attributes = True