#frontend>views>student_marksheet.py

import streamlit as st
import pandas as pd
from utils.api_client import get

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io

def generate_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    student = data["student"]
    summary = data["summary"]
    marks = data["marks"]

    # Title
    elements.append(Paragraph("<b>STUDENT MARKSHEET</b>", styles['Title']))
    elements.append(Spacer(1, 12))

    # Name
    elements.append(Paragraph(f"<b>Name:</b> {student['name']}", styles['Normal']))
    elements.append(Spacer(1, 12))

    # TABLE
    table_data = [["Subject", "Code", "Marks", "Max"]]

    for m in marks:
        table_data.append([
            m["subject"],
            m["code"],
            m["obtained"],
            m["max"]
        ])

    table = Table(table_data, colWidths=[130, 100, 100, 100])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 12))

    # 🔹 SUMMARY IN ONE LINE
    summary_text = (
        f"<b>Total:</b> {summary['total_obtained']} / {summary['total_max']} &nbsp;&nbsp;&nbsp;&nbsp;"
        f"<b>Percentage:</b> {summary['percentage']}% &nbsp;&nbsp;&nbsp;&nbsp;"
        f"<b>Grade:</b> {summary['grade']} &nbsp;&nbsp;&nbsp;&nbsp;"
        f"<b>Result:</b> {summary['result']}"
    )

    elements.append(Paragraph(summary_text, styles['Normal']))

    doc.build(elements)
    buffer.seek(0)

    return buffer


# MAIN UI
def show():
    st.markdown("## My Marksheet")

    exams = get('/api/student/exams') or []
    exam_map = {e['exam_name']: e['exam_id'] for e in exams}

    if not exams:
        st.warning("No exams available")
        return

    with st.form('marksheet_form'):
        exam_name = st.selectbox('Select Exam', list(exam_map.keys()))
        submitted = st.form_submit_button('View Marksheet', use_container_width=True)

    if submitted:
        with st.spinner("Fetching marksheet..."):
            data = get(
                "/api/student/marksheet",
                params={
                    "enroll_no": st.session_state.get("username"),
                    "exam_id": exam_map[exam_name]
                }
            )

        if data:
            st.success(f"Marksheet for {data['student']['name']}")

            summary = data['summary']

            # Metrics
            c1, c2, c3 = st.columns(3)
            c1.metric("Total", summary['total_obtained'])
            c2.metric("Max", summary['total_max'])
            c3.metric("Percentage", f"{summary['percentage']}%")

            st.progress(summary['percentage'] / 100)

            st.divider()

            # Table
            df = pd.DataFrame(data['marks'])
            st.dataframe(df, use_container_width=True)

            # PDF DOWNLOAD
            pdf = generate_pdf(data)
            st.download_button(
                "⬇️ Download PDF",
                data=pdf,
                file_name="marksheet.pdf",
                mime="application/pdf",
                use_container_width=True
            )

            # Final result
            st.success(
                f"Grade: {summary['grade']} | Result: {summary['result']}"
            )