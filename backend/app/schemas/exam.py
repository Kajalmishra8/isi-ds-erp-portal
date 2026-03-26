from pydantic import BaseModel
from typing import Optional

class ExamCreate(BaseModel):
    exam_name: Optional[str]
    year: Optional[int]

class ExamResponse(BaseModel):
    exam_id: str
    exam_name: Optional[str]
    year: Optional[int]

    class Config:
        from_attributes = True