import streamlit as st
import pandas as pd
from utils.api_client import get, post
from components.ui import page_header, section_label, empty_state, info_banner


def show():
    page_header("Marks Entry", "Record examination marks for students", "✏️")

    # ── Load reference data ────────────────────────────────────────────────────
    students_resp = get("/api/admin/students", {"limit": 500}) or {}
    exams         = get("/api/admin/exams")    or []
    subjects      = get("/api/admin/subjects") or []
    students      = students_resp.get("data", [])

    if not students:
        info_banner("No students found. Add students before entering marks.", "yellow")
        return
    if not exams:
        info_banner("No exams found. Create an exam first.", "yellow")
        return
    if not subjects:
        info_banner("No subjects found. Add subjects first.", "yellow")
        return

    # Maps: display label → UUID
    student_map = {
        f"{s['enroll_no']} — {s['first_name']} {s['last_name']}": s["std_id"]
        for s in students
    }
    exam_map = {
        f"{e['exam_name']} ({e.get('year', '')})": e["exam_id"]
        for e in exams
    }
    subject_map = {
        f"{s.get('sub_code', '')} · {s['sub_name']}": s["sub_id"]
        for s in subjects
    }

    tab_entry, tab_recent = st.tabs(["  ✏️  Enter Marks  ", "  📋  Recent Entries  "])

    # ── Tab 1: Entry form ──────────────────────────────────────────────────────
    with tab_entry:
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        info_banner("Each student × exam × subject combination is unique.")

        with st.form("marks_form"):
            section_label("Select Student & Exam")
            c1, c2 = st.columns(2)
            with c1:
                sel_student = st.selectbox("Student *",  list(student_map.keys()))
            with c2:
                sel_exam    = st.selectbox("Exam *",     list(exam_map.keys()))

            section_label("Subject & Score")
            c1, c2 = st.columns(2)
            with c1:
                sel_subject = st.selectbox("Subject *",  list(subject_map.keys()))
            with c2:
                marks = st.number_input("Marks Obtained *", min_value=0, max_value=500, value=0)

            st.markdown("<div style='height:4px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Save Marks", use_container_width=True)

        if submitted:
            with st.spinner("Saving…"):
                res = post("/api/admin/marks", {
                    "std_id":         student_map[sel_student],
                    "exam_id":        exam_map[sel_exam],
                    "sub_id":         subject_map[sel_subject],
                    "marks_obtained": int(marks),
                })
            if res:
                st.success("✅ Marks saved successfully.")

    # ── Tab 2: Recent entries ──────────────────────────────────────────────────
    with tab_recent:
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        recent = get("/api/admin/marks/recent?limit=20") or []

        if recent:
            df = pd.DataFrame(recent)
            keep = [c for c in ["mark_id", "marks_obtained", "created_at"]
                    if c in df.columns]
            df = df[keep].copy()
            df.columns = ["ID", "Score", "Added At"]
            df["Added At"] = (
                pd.to_datetime(df["Added At"]).dt.strftime("%d %b %Y, %H:%M")
            )
            st.table(df)
        else:
            empty_state("No marks yet", "Saved marks will appear here.", "✏️")
