import streamlit as st
from utils.api_client import login as api_login


def show():
    st.markdown(
        "<style>.block-container{padding-top:80px!important;}</style>",
        unsafe_allow_html=True,
    )

    _, center, _ = st.columns([1, 1.2, 1])

    with center:
        # Brand mark
        st.markdown(
            "<div style='text-align:center;margin-bottom:8px;'>"
            "<div style='width:52px;height:52px;"
            "background:linear-gradient(135deg,#1D4ED8,#6366F1);border-radius:14px;"
            "display:inline-flex;align-items:center;justify-content:center;"
            "font-size:24px;box-shadow:0 0 28px rgba(59,130,246,.35);'>"
            "🎓</div></div>"
            "<h2 style='text-align:center;font-size:20px;font-weight:700;"
            "color:#F1F5F9;letter-spacing:-.02em;margin:0 0 4px;'>ERP Portal</h2>"
            "<p style='text-align:center;font-size:12px;color:#475569;"
            "margin:0 0 28px;'>Sign in to your account to continue</p>",
            unsafe_allow_html=True,
        )

        with st.form("login_form", clear_on_submit=False):
            st.markdown(
                "<p style='font-size:14px;font-weight:600;color:#94A3B8;"
                "margin-bottom:6px;'>Welcome back</p>",
                unsafe_allow_html=True,
            )
            username = st.text_input("Username", placeholder="Enter your username")
            password = st.text_input(
                "Password", type="password", placeholder="Enter your password"
            )
            st.markdown("<div style='height:4px;'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button(
                "Sign In →", use_container_width=True, type="primary"
            )

        if submitted:
            if not username or not password:
                st.warning("Please enter both username and password.")
                return
            with st.spinner("Authenticating…"):
                result = api_login(username, password)
            if result:
                st.session_state["token"]        = result["access_token"]
                st.session_state["role"]         = result["role"]
                st.session_state["username"]     = username
                st.session_state["current_page"] = (
                    "admin_dashboard"
                    if result["role"] == "admin"
                    else "student_marksheet"
                )
                st.rerun()
            else:
                st.error("Invalid credentials. Please try again.")

        st.markdown(
            "<p style='text-align:center;font-size:10px;color:#334155;"
            "margin-top:16px;'>Contact your administrator for account access</p>",
            unsafe_allow_html=True,
        )
