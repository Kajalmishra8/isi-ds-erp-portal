#frontend>form>admin_subjects.py

import streamlit as st
import pandas as pd
from utils.api_client import get, post
from components.ui import page_header, section_label, empty_state, info_banner

def show():
    page_header("Subjects", "Manage academic subjects and their credit information", "📚")

    tab_list, tab_add = st.tabs(["  📋  Subject List  ", "  ➕  Add Subject  "])

    with tab_list:
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        data = get("/api/admin/subjects") or []

        if data:
            df = pd.DataFrame(data)
            display_cols = [c for c in ["sub_code","sub_name","max_marks","semester","sub_id"] if c in df.columns]
            df = df[display_cols].copy()
            rename = {
                "sub_code":"Code","sub_name":"Subject Name",
                "max_marks":"Max Marks","semester":"Sem","sub_id":"ID"
            }
            df.rename(columns=rename, inplace=True)
            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Max Marks": st.column_config.NumberColumn("Max Marks", format="%d", width="small"),
                    "Sem": st.column_config.NumberColumn("Sem", format="%d", width="small"),
                },
            )
            st.markdown(
                f'<p style="font-size:12px;color:#6B7280;margin-top:6px;">'
                f'{len(data)} subject(s) total</p>',
                unsafe_allow_html=True,
            )
        else:
            empty_state("No subjects yet", "Add your first subject using the 'Add Subject' tab.", "📚")

    with tab_add:
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        info_banner("Subject codes should be unique identifiers (e.g. CS101, MATH201).")

        with st.form("subject_form"):
            section_label("Subject Details")
            c1, c2 = st.columns(2)
            with c1:
                sub_name = st.text_input("Subject Name *", placeholder="e.g. Data Structures")
            with c2:
                sub_code = st.text_input("Subject Code *", placeholder="e.g. CS301")

            c1, c2 = st.columns(2)
            with c1:
                max_marks = st.number_input("Max Marks", min_value=1, max_value=500, value=100)
            with c2:
                semester = st.number_input("Semester", min_value=1, max_value=12, value=1)

            st.markdown("<div style='height:4px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Add Subject", use_container_width=True)

        if submitted:
            if not sub_name or not sub_code:
                st.warning("Subject name and code are required.")
            else:
                with st.spinner("Adding subject…"):
                    res = post("/api/admin/subjects", {
                        "sub_name":  sub_name,
                        "sub_code":  sub_code,
                        "max_marks": int(max_marks),
                        "semester":  int(semester),
                    })
                if res:
                    st.success(f"✅ Subject **{sub_name}** ({sub_code}) added.")