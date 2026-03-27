#backend>app>schemas>marks.py

from pydantic import BaseModel
from typing import Optional

class MarksCreate(BaseModel):
    std_id: str
    exam_id: str
    sub_id: str
    marks_obtained: Optional[int]

class MarksResponse(BaseModel):
    mark_id: str
    std_id: str
    exam_id: str
    sub_id: str
    marks_obtained: Optional[int]
    semester: Optional[int]

    class Config:
        from_attributes = True










# Old MarksResponse
# class MarksResponse(BaseModel):
#     mark_id: str
#     std_id: str
#     exam_id: str
#     sub_id: str
#     marks_obtained: Optional[int]

#     class Config:
#         from_attributes = True