#frontend>views>admin_marks.py

import streamlit as st
from utils.api_client import get, post

def show():
    st.markdown("## Add Marks")

    students = get("/api/admin/students") or {}
    exams = get("/api/admin/exams") or []
    subjects = get("/api/admin/subjects") or []

    student_map = {s["enroll_no"]: s["std_id"] for s in students.get("data", [])}
    exam_map = {e["exam_name"]: e["exam_id"] for e in exams}
    subject_map = {s["sub_name"]: s["sub_id"] for s in subjects}

    with st.form("marks_form"):
        enroll = st.selectbox("Student", list(student_map.keys()))
        exam = st.selectbox("Exam", list(exam_map.keys()))
        subject = st.selectbox("Subject", list(subject_map.keys()))
        marks = st.number_input("Marks", min_value=0, max_value=100)

        submitted = st.form_submit_button("Add Marks")

    if submitted:
        res = post("/api/admin/marks", {
            "std_id": student_map[enroll],
            "exam_id": exam_map[exam],
            "sub_id": subject_map[subject],
            "marks_obtained": marks
        })
        if res:
            st.success("Marks added")