# Student Create
from pydantic import BaseModel
from typing import Optional

class StudentCreate(BaseModel):
    username: str
    password: str
    enroll_no: str
    first_name: Optional[str]
    last_name: Optional[str]
    semester: Optional[int]

# Response
class StudentCreate(BaseModel):
    username: str
    password: str
    enroll_no: str
    first_name: Optional[str]
    last_name: Optional[str]
    semester: Optional[int]





# Old code
# class StudentCreate(BaseModel):
#     enroll_no: str
#     first_name: Optional[str]
#     last_name: Optional[str]
#     semester: Optional[int]

# class StudentResponse(BaseModel):
#     std_id: str
#     enroll_no: str
#     first_name: Optional[str]
#     last_name: Optional[str]
#     semester: Optional[int]

#     class Config:
#         from_attributes = True