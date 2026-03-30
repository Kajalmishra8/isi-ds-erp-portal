import streamlit as st
from components.ui import role_badge


def render_header():
    user = st.session_state.get("username", "—")
    role = st.session_state.get("role", "")
    badge = role_badge(role)
    initials = (user[:2].upper()) if user else "??"

    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.markdown(
            '<div style="display:flex;align-items:center;gap:10px;padding:4px 0;">'
            '<div style="width:26px;height:26px;background:linear-gradient(135deg,#1D4ED8,#3B82F6);'
            'border-radius:7px;display:flex;align-items:center;justify-content:center;'
            'font-size:13px;flex-shrink:0;">🎓</div>'
            '<span style="font-size:14px;font-weight:700;color:#F1F5F9;'
            'letter-spacing:-.01em;">ERP Portal</span>'
            '</div>',
            unsafe_allow_html=True,
        )

    with col_right:
        c1, c2 = st.columns([3, 1])
        with c1:
            st.markdown(
                f'<div style="text-align:right;padding-top:3px;">'
                f'<div style="display:flex;align-items:center;justify-content:flex-end;gap:8px;">'
                f'<div style="width:24px;height:24px;border-radius:50%;'
                f'background:linear-gradient(135deg,#1E3A5F,#2563EB);'
                f'display:flex;align-items:center;justify-content:center;'
                f'font-size:9px;font-weight:600;color:#BFDBFE;">{initials}</div>'
                f'<span style="font-size:12px;font-weight:500;color:#94A3B8;">{user}</span>'
                f'&nbsp;{badge}'
                f'</div></div>',
                unsafe_allow_html=True,
            )
        with c2:
            if st.button("Sign out", key="logout_btn", use_container_width=True):
                for k in list(st.session_state.keys()):
                    del st.session_state[k]
                st.rerun()

    st.markdown(
        '<div style="height:1px;background:rgba(255,255,255,.07);margin:10px 0 0;"></div>',
        unsafe_allow_html=True,
    )
