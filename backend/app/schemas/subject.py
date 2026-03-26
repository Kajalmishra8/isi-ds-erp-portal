from pydantic import BaseModel
from typing import Optional

class SubjectCreate(BaseModel):
    sub_code: Optional[str]
    sub_name: Optional[str]
    max_marks: Optional[int]

class SubjectResponse(BaseModel):
    sub_id: str
    sub_code: Optional[str]
    sub_name: Optional[str]
    max_marks: Optional[int]

    class Config:
        from_attributes = True