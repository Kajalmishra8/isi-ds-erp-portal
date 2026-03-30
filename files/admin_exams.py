import streamlit as st
import pandas as pd
from utils.api_client import get, post
from components.ui import page_header, section_label, empty_state, info_banner


def show():
    page_header("Exams", "Create and manage examination records", "📋")

    tab_list, tab_add = st.tabs(["  📋  Exam List  ", "  ➕  Create Exam  "])

    with tab_list:
        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        data = get("/api/admin/exams") or []

        if data:
            df = pd.DataFrame(data)
            keep = [c for c in ["exam_name","year","semester","is_active"]
                    if c in df.columns]
            df = df[keep].rename(columns={
                "exam_name":"Exam Name","year":"Year",
                "semester":"Sem","is_active":"Active",
            })
            if "Active" in df.columns:
                df["Active"] = df["Active"].map(
                    {True: "✅ Yes", False: "❌ No"}
                )
            st.markdown(
                f"<p style='font-size:11px;color:#475569;margin-bottom:8px;'>"
                f"{len(data)} exam(s) total</p>",
                unsafe_allow_html=True,
            )
            st.table(df)
        else:
            empty_state("No exams yet",
                        "Create your first exam using the 'Create Exam' tab.", "📋")

    with tab_add:
        st.markdown("<div style='height:14px;'></div>", unsafe_allow_html=True)
        info_banner("Exams are tied to a semester. Students only see active exams.")

        with st.form("exam_form"):
            section_label("Exam Details")
            c1, c2 = st.columns(2)
            with c1:
                exam_name = st.text_input("Exam Name *",
                                          placeholder="e.g. Mid-Term 2025")
            with c2:
                year = st.number_input("Year *", min_value=2000,
                                       max_value=2100, value=2025)
            c1, c2 = st.columns(2)
            with c1:
                semester  = st.number_input("Semester *",
                                            min_value=1, max_value=12, value=1)
            with c2:
                is_active = st.checkbox("Mark as Active", value=True)

            st.markdown("<div style='height:2px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Create Exam", use_container_width=True)

        if submitted:
            if not exam_name:
                st.warning("Exam name is required.")
            else:
                with st.spinner("Creating exam…"):
                    res = post("/api/admin/exams", {
                        "exam_name": exam_name,
                        "year":      int(year),
                        "semester":  int(semester),
                        "is_active": is_active,
                    })
                if res:
                    st.success(f"✅ Exam **{exam_name}** created.")
