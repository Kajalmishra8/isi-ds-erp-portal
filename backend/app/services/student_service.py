# app/services/student_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.student import Student
from app.models.exam import Exam
from app.models.marks import Mark
from app.models.user import User

def get_marksheet(db: Session, enroll_no: str, exam_id: str, current_user: User):
    student = db.query(Student).filter(Student.enroll_no == enroll_no).first()
    if not student:
        raise HTTPException(status_code=404, detail='Student not found')
    # Ensure student can only access own data
    if str(student.user_id) != str(current_user.user_id):
        raise HTTPException(status_code=403, detail='Access denied')
    exam = db.query(Exam).filter(Exam.exam_id == exam_id).first()
    if not exam: raise HTTPException(status_code=404, detail='Exam not found')
    marks = db.query(Mark).filter(Mark.std_id == student.std_id, Mark.exam_id == exam_id).all()
    total_obtained = sum(m.marks_obtained for m in marks)
    total_max      = sum(m.subject.max_marks for m in marks)
    percentage     = round((total_obtained / total_max * 100), 2) if total_max else 0
    return {
        'student': {'enroll_no': student.enroll_no, 'name': f'{student.first_name} {student.last_name}', 'semester': student.semester},
        'exam':    {'name': exam.exam_name, 'year': exam.year},
        'marks':   [{'subject': m.subject.sub_name, 'code': m.subject.sub_code, 'obtained': m.marks_obtained, 'max': m.subject.max_marks} for m in marks],
        'summary': {'total_obtained': total_obtained, 'total_max': total_max, 'percentage': percentage}
    }

def get_exams_for_student(db: Session, current_user: User):
    student = db.query(Student).filter(Student.user_id == current_user.user_id).first()
    if not student: raise HTTPException(status_code=404, detail='Student profile not found')
    from app.models.exam import Exam
    return db.query(Exam).filter(Exam.semester == student.semester, Exam.is_active == True).all()