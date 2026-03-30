import streamlit as st
import pandas as pd
from utils.api_client import get, post
from components.ui import page_header, section_label, empty_state, info_banner


def show():
    page_header("Students", "Manage student enrolments and profiles", "👥")

    tab_list, tab_add = st.tabs(["  📋  Student List  ", "  ➕  Add Student  "])

    with tab_list:
        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        col_search, col_limit, _ = st.columns([3, 1, 2])
        with col_search:
            search = st.text_input(
                "search", placeholder="Search by name or enroll no…",
                label_visibility="collapsed"
            )
        with col_limit:
            limit = st.selectbox("limit", [10, 25, 50],
                                 label_visibility="collapsed")

        data  = get("/api/admin/students",
                    {"search": search, "page": 1, "limit": limit}) or {}
        rows  = data.get("data", [])
        total = data.get("total", 0)

        if rows:
            df = pd.DataFrame(rows)
            keep = [c for c in ["enroll_no","first_name","last_name",
                                 "email","semester","phone"]
                    if c in df.columns]
            df = df[keep].rename(columns={
                "enroll_no":"Enroll No","first_name":"First Name",
                "last_name":"Last Name","email":"Email",
                "semester":"Sem","phone":"Phone",
            })
            st.markdown(
                f"<p style='font-size:11px;color:#475569;margin-bottom:8px;'>"
                f"Showing <b style='color:#64748B;'>{len(rows)}</b> of "
                f"<b style='color:#64748B;'>{total}</b> students</p>",
                unsafe_allow_html=True,
            )
            st.table(df)
        else:
            empty_state("No students found",
                        "Add your first student using the 'Add Student' tab.", "👥")

    with tab_add:
        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        info_banner("All fields marked with * are required.")

        with st.form("student_form"):
            section_label("Account Credentials")
            c1, c2 = st.columns(2)
            with c1:
                username   = st.text_input("Username *",  placeholder="e.g. john_doe")
            with c2:
                password   = st.text_input("Password *",  type="password",
                                           placeholder="Min 8 characters")

            section_label("Personal Information")
            c1, c2 = st.columns(2)
            with c1:
                first_name = st.text_input("First Name *", placeholder="John")
            with c2:
                last_name  = st.text_input("Last Name *",  placeholder="Doe")

            c1, c2 = st.columns(2)
            with c1:
                email = st.text_input("Email *", placeholder="john@example.com")
            with c2:
                phone = st.text_input("Phone",   placeholder="+91 98765 43210")

            section_label("Academic Details")
            c1, c2 = st.columns(2)
            with c1:
                enroll_no = st.text_input("Enroll Number *",
                                          placeholder="e.g. 2024CS001")
            with c2:
                semester  = st.number_input("Semester *",
                                            min_value=1, max_value=12, value=1)

            st.markdown("<div style='height:2px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button(
                "Create Student Account", use_container_width=True
            )

        if submitted:
            if not all([username, password, first_name, last_name, email, enroll_no]):
                st.warning("Please fill in all required (*) fields.")
            else:
                with st.spinner("Creating student…"):
                    res = post("/api/admin/students", {
                        "username":   username,
                        "password":   password,
                        "enroll_no":  enroll_no,
                        "first_name": first_name,
                        "last_name":  last_name,
                        "semester":   int(semester),
                        "email":      email,
                        "phone":      phone or "",
                    })
                if res:
                    st.success(
                        f"✅ Student **{first_name} {last_name}** created successfully.")
