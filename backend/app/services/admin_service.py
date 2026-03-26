# app/services/admin_service.py

from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from fastapi import HTTPException

from app.models.user import User
from app.models.student import Student
from app.models.exam import Exam
from app.models.subject import Subject
from app.models.marks import Mark

from app.utils.password import hash_password

from app.schemas.student import StudentCreate
from app.schemas.exam import ExamCreate
from app.schemas.subject import SubjectCreate
from app.schemas.marks import MarksCreate

import uuid

# ---------------- DASHBOARD ----------------

def get_dashboard_stats(db: Session) -> dict:
    return {
        'total_students': db.query(func.count(Student.std_id)).scalar(),
        'total_exams': db.query(func.count(Exam.exam_id)).scalar(),
        'total_subjects': db.query(func.count(Subject.sub_id)).scalar(),
    }

# ---------------- STUDENTS ----------------

def create_student(db: Session, payload: StudentCreate):
    if db.query(Student).filter(Student.enroll_no == payload.enroll_no).first():
        raise HTTPException(status_code=400, detail='Enroll number already exists')

    user = User(
        username=payload.username,
        password=hash_password(payload.password),
        designation='student'
    )
    db.add(user)
    db.flush()

    student = Student(
        enroll_no=payload.enroll_no,
        first_name=payload.first_name,
        last_name=payload.last_name,
        semester=payload.semester,
        user_id=user.user_id
    )

    db.add(student)
    db.commit()
    db.refresh(student)

    return student

def get_students(db: Session, search: str, page: int, limit: int):
    q = db.query(Student)

    if search:
        q = q.filter(
            Student.enroll_no.ilike(f'%{search}%') |
            Student.first_name.ilike(f'%{search}%')
        )

    total = q.count()
    data = q.offset((page - 1) * limit).limit(limit).all()

    return {
        'total': total,
        'page': page,
        'data': data
    }

# ---------------- EXAMS ----------------

def create_exam(db: Session, payload: ExamCreate):
    exam = Exam(**payload.model_dump())
    db.add(exam)
    db.commit()
    db.refresh(exam)
    return exam

def get_exams(db: Session):
    return db.query(Exam).all()

# ---------------- SUBJECTS ----------------

def create_subject(db: Session, payload: SubjectCreate):
    subject = Subject(**payload.model_dump())
    db.add(subject)
    db.commit()
    db.refresh(subject)
    return subject

def get_subjects(db: Session):
    return db.query(Subject).all()

# ---------------- MARKS ----------------

def create_marks(db: Session, payload: MarksCreate):

    # ✅ Convert string → UUID
    try:
        std_id = uuid.UUID(payload.std_id)
        exam_id = uuid.UUID(payload.exam_id)
        sub_id = uuid.UUID(payload.sub_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid UUID format")

    # ✅ Validate existence
    student = db.query(Student).filter(Student.std_id == std_id).first()
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')

    exam = db.query(Exam).filter(Exam.exam_id == exam_id).first()
    if not exam:
        raise HTTPException(status_code=404, detail='Exam not found')

    subject = db.query(Subject).filter(Subject.sub_id == sub_id).first()
    if not subject:
        raise HTTPException(status_code=404, detail='Subject not found')

    # ✅ Business rule
    if payload.marks_obtained > subject.max_marks:
        raise HTTPException(
            status_code=400,
            detail=f'Marks exceed max ({subject.max_marks})'
        )

    # ✅ Insert
    mark = Mark(
        std_id=std_id,
        exam_id=exam_id,
        sub_id=sub_id,
        marks_obtained=payload.marks_obtained
    )

    db.add(mark)
    db.commit()
    db.refresh(mark)

    return mark

def get_recent_marks(db: Session, limit: int):
    return db.query(Mark).order_by(desc(Mark.created_at)).limit(limit).all()