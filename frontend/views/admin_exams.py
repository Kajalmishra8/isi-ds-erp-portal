#frontend>views>admin_exams.py

import streamlit as st
from utils.api_client import get, post

def show():
    st.markdown("## Exams")

    with st.form("exam_form"):
        exam_name = st.text_input("Exam Name")
        year = st.number_input("Year", value=2026)
        semester = st.number_input("Semester", value=1)
        is_active = st.checkbox("Active", value=True)

        submitted = st.form_submit_button("Add Exam")

    if submitted:
        res = post("/api/admin/exams", {
            "exam_name": exam_name,
            "year": year,
            "semester": semester,
            "is_active": is_active
        })
        if res:
            st.success("Exam added")

    st.divider()

    data = get("/api/admin/exams") or []

    if data:
        import pandas as pd
        st.dataframe(pd.DataFrame(data), use_container_width=True)










# import streamlit as st
# from utils.api_client import get, post

# def show():
#     st.markdown("## Exams")

#     with st.form("exam_form"):
#         exam_name = st.text_input("Exam Name")
#         year = st.number_input("Year", value=2026)
#         submitted = st.form_submit_button("Add Exam")

#     if submitted:
#         res = post("/api/admin/exams", {
#             "exam_name": exam_name,
#             "year": year
#         })
#         if res:
#             st.success("Exam added")

#     st.divider()

#     data = get("/api/admin/exams") or []
#     if data:
#         import pandas as pd
#         st.dataframe(pd.DataFrame(data), use_container_width=True)