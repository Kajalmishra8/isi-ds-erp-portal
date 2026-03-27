#frontend>views>admin_students.py

import streamlit as st
from utils.api_client import get, post

def show():
    st.markdown("## Students")

    st.subheader("Add Student")

    with st.form("student_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        enroll_no = st.text_input("Enroll No")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        semester = st.number_input("Semester", min_value=1, max_value=8)
        email = st.text_input("Email")

        submitted = st.form_submit_button("Add Student")

    if submitted:
        res = post("/api/admin/students", {
            "username": username,
            "password": password,
            "enroll_no": enroll_no,
            "first_name": first_name,
            "last_name": last_name,
            "semester": semester,
            "email": email
        })
        if res:
            st.success("Student added")

    st.divider()

    data = get("/api/admin/students") or {}
    if data.get("data"):
        import pandas as pd
        st.dataframe(pd.DataFrame(data["data"]), use_container_width=True)