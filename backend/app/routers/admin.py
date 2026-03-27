#backend>app>routers>admin.py

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.dependencies import get_db, require_admin
from app.services import admin_service
from app.schemas import student as s_schema, exam as e_schema
from app.schemas import subject as sub_schema, marks as m_schema
from app.models.user import User

router = APIRouter(prefix='/api/admin', tags=['Admin'], dependencies=[Depends(require_admin)])

@router.get('/dashboard')
def dashboard(db: Session = Depends(get_db)):
    return admin_service.get_dashboard_stats(db)

@router.post('/students', status_code=status.HTTP_201_CREATED)
def add_student(payload: s_schema.StudentCreate, db: Session = Depends(get_db)):
    return admin_service.create_student(db, payload)

@router.get('/students')
def list_students(search: str = '', page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    return admin_service.get_students(db, search, page, limit)

@router.post('/exams', status_code=status.HTTP_201_CREATED)
def add_exam(payload: e_schema.ExamCreate, db: Session = Depends(get_db)):
    return admin_service.create_exam(db, payload)

@router.get('/exams', response_model=list[e_schema.ExamResponse])
def list_exams(db: Session = Depends(get_db)):
    return admin_service.get_exams(db)

@router.post('/subjects', status_code=status.HTTP_201_CREATED)
def add_subject(payload: sub_schema.SubjectCreate, db: Session = Depends(get_db)):
    return admin_service.create_subject(db, payload)

@router.get('/subjects')
def list_subjects(db: Session = Depends(get_db)):
    return admin_service.get_subjects(db)

@router.post('/marks', status_code=status.HTTP_201_CREATED)
def add_marks(payload: m_schema.MarksCreate, db: Session = Depends(get_db)):
    return admin_service.create_marks(db, payload)

@router.get('/marks/recent')
def recent_marks(limit: int = 10, db: Session = Depends(get_db)):
    return admin_service.get_recent_marks(db, limit)