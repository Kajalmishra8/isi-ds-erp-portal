#backend>app>routers>student.py

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db, require_student, get_current_user
from app.services import student_service
from app.models.user import User

router = APIRouter(
    prefix='/api/student',
    tags=['Student'],
    dependencies=[Depends(require_student)]
)

@router.get('/marksheet')
def get_marksheet(
    enroll_no: str = Query(...),
    exam_id: str = Query(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return student_service.get_marksheet(db, enroll_no, exam_id, current_user)

@router.get('/exams')
def available_exams(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return student_service.get_exams_for_student(db, current_user)










# old code
# # app/routers/student.py
# from fastapi import APIRouter, Depends, Query
# from sqlalchemy.orm import Session
# from app.dependencies import get_db, require_student, get_current_user
# from app.services import student_service
# from app.models.user import User

# router = APIRouter(prefix='/api/student', tags=['Student'], dependencies=[Depends(require_student)])

# @router.get('/marksheet')
# def get_marksheet(
#     enroll_no: str = Query(...),
#     exam_id: str = Query(...),
#     db: Session = Depends(get_db),
#     current_user: User = Depends(get_current_user)
# ):
#     return student_service.get_marksheet(db, enroll_no, exam_id, current_user)

# @router.get('/exams')
# def available_exams(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
#     return student_service.get_exams_for_student(db, current_user)