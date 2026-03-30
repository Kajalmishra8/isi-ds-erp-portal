import streamlit as st
import pandas as pd
from utils.api_client import get
from components.ui import page_header, section_label, empty_state


def show():
    page_header("My Marksheet", "View your examination results and grades", "📄")

    # ── Load available exams ───────────────────────────────────────────────────
    exams = get("/api/student/exams") or []

    if not exams:
        empty_state(
            "No exams available",
            "There are no active exams for your semester right now.",
            "📋",
        )
        return

    # Build label → exam_id map
    exam_map = {
        f"{e['exam_name']} ({e.get('year', '')})": e["exam_id"]
        for e in exams
    }

    with st.form("marksheet_form"):
        section_label("Select Examination")
        selected = st.selectbox("Exam", list(exam_map.keys()))
        submitted = st.form_submit_button("View Marksheet →", use_container_width=True)

    if submitted:
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

        # ── Student info card ──────────────────────────────────────────
        st.markdown(f"""
        <div style="background:#fff;border:1px solid #E4E7EC;border-radius:12px;
                    padding:20px 24px;margin-bottom:20px;
                    box-shadow:0 1px 3px rgba(0,0,0,.06);">
          <div style="display:flex;justify-content:space-between;align-items:flex-start;">
            <div>
              <div style="font-size:18px;font-weight:700;color:#111827;">
                {student.get('name', '')}</div>
              <div style="font-size:13px;color:#6B7280;margin-top:3px;">
                Enroll No: <b>{student.get('enroll_no','')}</b>
                &nbsp;·&nbsp; Semester: <b>{student.get('semester','')}</b>
              </div>
            </div>
            <div style="text-align:right;font-size:13px;font-weight:500;color:#111827;">
              {exam.get('name','')} — {exam.get('year','')}
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Summary metrics ────────────────────────────────────────────
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total Obtained", summary.get("total_obtained", 0))
        c2.metric("Maximum Marks",  summary.get("total_max",      0))
        c3.metric("Percentage",     f"{summary.get('percentage',  0)}%")
        c4.metric("Grade",          summary.get("grade", "—"))

        st.markdown("<div style='height:20px;'></div>", unsafe_allow_html=True)

        # ── Subject-wise table ─────────────────────────────────────────
        section_label("Subject-wise Marks")
        if marks:
            # Backend returns: subject, code, obtained, max
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

        # ── Result banner ──────────────────────────────────────────────
        result  = summary.get("result", "")
        grade   = summary.get("grade", "")
        pct     = summary.get("percentage", 0)
        is_pass = result == "PASS"
        color   = "#ECFDF5" if is_pass else "#FEF2F2"
        fg      = "#059669" if is_pass else "#DC2626"
        icon    = "✅" if is_pass else "❌"

        st.markdown(f"""
        <div style="background:{color};border:1px solid {fg}30;border-radius:10px;
                    padding:16px 24px;margin-top:16px;display:flex;
                    align-items:center;justify-content:space-between;">
          <div style="font-size:15px;font-weight:700;color:{fg};">
            {icon} Result: {result}
          </div>
          <div style="font-size:14px;color:{fg};font-weight:500;">
            Grade: {grade} &nbsp;·&nbsp; {pct}%
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── CSV download ───────────────────────────────────────────────
        if marks:
            st.markdown("<div style='height:12px;'></div>", unsafe_allow_html=True)
            csv = df.to_csv(index=False).encode()
            st.download_button(
                "⬇️  Download Marksheet CSV",
                csv,
                file_name=f"marksheet_{enroll_no}.csv",
                mime="text/csv",
                use_container_width=True,
            )
