import streamlit as st
import pandas as pd
from utils.api_client import get
from components.ui import page_header, section_label, empty_state, result_banner


def show():
    page_header("My Marksheet", "View your examination results and grades", "📄")

    exams = get("/api/student/exams") or []

    if not exams:
        empty_state(
            "No exams available",
            "No active exams for your semester yet. Check back later.",
            "📋",
        )
        return

    exam_map = {
        f"{e['exam_name']} ({e.get('year','')})": e["exam_id"]
        for e in exams
    }

    with st.form("marksheet_form"):
        section_label("Select Examination")
        selected  = st.selectbox("Exam", list(exam_map.keys()))
        submitted = st.form_submit_button(
            "View Marksheet →", use_container_width=True
        )

    if not submitted:
        return

    enroll_no = st.session_state.get("username", "")
    with st.spinner("Fetching your marksheet…"):
        data = get(
            f"/api/student/marksheet"
            f"?enroll_no={enroll_no}&exam_id={exam_map[selected]}"
        )

    if not data:
        return

    student = data.get("student", {})
    exam    = data.get("exam",    {})
    summary = data.get("summary", {})
    marks   = data.get("marks",   [])

    # ── Student info card ──────────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:#0D1424;border:1px solid rgba(255,255,255,.07);
                border-radius:10px;padding:18px 20px;margin-bottom:18px;">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;">
        <div>
          <div style="font-size:17px;font-weight:700;color:#F1F5F9;
                      letter-spacing:-.01em;">
            {student.get('name','')}</div>
          <div style="font-size:11px;color:#64748B;margin-top:4px;">
            Enroll No: <span style="color:#94A3B8;font-weight:500;">
              {student.get('enroll_no','')}</span>
            &nbsp;·&nbsp; Semester:
            <span style="color:#94A3B8;font-weight:500;">
              {student.get('semester','')}</span>
          </div>
        </div>
        <div style="text-align:right;">
          <div style="font-size:12px;font-weight:500;color:#64748B;">
            {exam.get('name','')} — {exam.get('year','')}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Summary metrics ────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Obtained", summary.get("total_obtained", 0))
    c2.metric("Maximum Marks",  summary.get("total_max",      0))
    c3.metric("Percentage",     f"{summary.get('percentage',  0)}%")
    c4.metric("Grade",          summary.get("grade", "—"))

    st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)

    # ── Subject-wise marks table ───────────────────────────────────────────
    # Backend returns keys: subject, code, obtained, max
    section_label("Subject-wise Marks")
    if marks:
        df = pd.DataFrame(marks)
        df.rename(columns={
            "subject": "Subject",
            "code":    "Code",
            "obtained":"Obtained",
            "max":     "Max Marks",
        }, inplace=True)
        if "Obtained" in df.columns and "Max Marks" in df.columns:
            df["Score %"] = (
                (df["Obtained"] / df["Max Marks"]) * 100
            ).round(1).astype(str) + "%"
        st.table(df)
    else:
        empty_state("No marks data", "No marks found for this exam.", "📊")

    # ── Result banner ──────────────────────────────────────────────────────
    result_banner(
        summary.get("result", ""),
        summary.get("grade", ""),
        summary.get("percentage", 0),
    )

    # ── CSV download ───────────────────────────────────────────────────────
    if marks:
        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        csv = df.to_csv(index=False).encode()
        st.download_button(
            "⬇️  Download Marksheet CSV",
            csv,
            file_name=f"marksheet_{enroll_no}.csv",
            mime="text/csv",
            use_container_width=True,
        )
