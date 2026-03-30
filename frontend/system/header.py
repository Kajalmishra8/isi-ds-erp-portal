#frontend>sytem>header.py

import streamlit as st

def render_header():
    user = st.session_state.get("username", "")
    role = st.session_state.get("role", "")
    role_color = "#2563EB" if role == "admin" else "#059669"
    role_bg    = "#EFF6FF" if role == "admin" else "#ECFDF5"

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:8px;">'
            f'<span style="font-size:18px;font-weight:700;color:#111827;'
            f'letter-spacing:-.02em;">ERP Portal</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

    with col_right:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                f'<div style="text-align:right;padding-top:4px;">'
                f'<span style="font-size:13px;font-weight:500;color:#111827;">{user}</span>&nbsp;&nbsp;'
                f'<span style="background:{role_bg};color:{role_color};'
                f'padding:2px 9px;border-radius:20px;font-size:11px;font-weight:600;">'
                f'{role.upper()}</span>'
                f"</div>",
                unsafe_allow_html=True,
            )
        with c2:
            if st.button("Sign out", key="logout_btn", use_container_width=True):
                for k in list(st.session_state.keys()):
                    del st.session_state[k]
                st.rerun()

    st.markdown(
        '<div style="height:1px;background:#E4E7EC;margin:12px 0 0;"></div>',
        unsafe_allow_html=True,
    )
