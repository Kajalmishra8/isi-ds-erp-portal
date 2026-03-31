#frontend>views>login.py
import streamlit as st
from utils.api_client import login

def show():
    st.markdown("## ERP Portal Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Login")

    if submitted:
        if not username or not password:
            st.warning("Enter credentials")
            return

        res = login(username, password)

        if res:
            st.session_state["token"] = res["access_token"]
            st.session_state["role"] = res["role"]
            st.session_state["username"] = username

            # redirect
            if res["role"] == "admin":
                st.session_state["current_page"] = "admin_dashboard"
            else:
                st.session_state["current_page"] = "student_marksheet"

            st.rerun()