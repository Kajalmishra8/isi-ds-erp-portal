# frontend/components/header.py
import streamlit as st

def render_header():
    col1, col2, col3 = st.columns([2, 4, 2])
    with col1:
        st.markdown('## ERP Portal')
    with col2:
        st.markdown('<p style="text-align:center;color:#6B7280;font-size:14px;">Powered by FastAPI + Streamlit</p>', unsafe_allow_html=True)
    with col3:
        user = st.session_state.get('username', '')
        role = st.session_state.get('role', '')
        st.markdown(f'<p style="text-align:right;"><b>{user}</b> <span style="background:#EFF6FF;color:#2563EB;padding:2px 8px;border-radius:12px;font-size:12px;">{role}</span></p>', unsafe_allow_html=True)
        if st.button('Logout', key='logout_btn', use_container_width=True):
            for k in list(st.session_state.keys()): del st.session_state[k]
            st.rerun()
    st.divider()