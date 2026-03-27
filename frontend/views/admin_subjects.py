#frontend>views>admin_subjects.py

import streamlit as st
from utils.api_client import get, post

def show():
    st.markdown("## Subjects")

    with st.form("subject_form"):
        sub_name = st.text_input("Subject Name")
        sub_code = st.text_input("Subject Code")
        max_marks = st.number_input("Max Marks", value=100)
        submitted = st.form_submit_button("Add Subject")

    if submitted:
        res = post("/api/admin/subjects", {
            "sub_name": sub_name,
            "sub_code": sub_code,
            "max_marks": max_marks
        })
        if res:
            st.success("Subject added")

    st.divider()

    data = get("/api/admin/subjects") or []
    if data:
        import pandas as pd
        st.dataframe(pd.DataFrame(data), use_container_width=True)