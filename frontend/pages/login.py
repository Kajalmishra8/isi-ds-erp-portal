# frontend/pages/login.py
import streamlit as st
from utils.api_client import login

def show():
    st.markdown('<style>div.block-container{max-width:420px;margin:auto;padding-top:80px;}</style>', unsafe_allow_html=True)
    st.markdown('## ERP Portal')
    st.markdown('##### Welcome back! Sign in to continue.')
    st.divider()
    with st.form('login_form', clear_on_submit=False):
        username = st.text_input('Username', placeholder='Enter username')
        password = st.text_input('Password', type='password', placeholder='Enter password')
        role     = st.selectbox('Role', ['student', 'admin'])
        submitted = st.form_submit_button('Sign In', use_container_width=True, type='primary')
        if submitted:
            if not username or not password:
                st.warning('Please fill all fields.')
            else:
                with st.spinner('Authenticating...'):
                    result = login(username, password)
                if result:
                    if result.get('role') != role:
                        st.error('Role mismatch. Please select the correct role.')
                    else:
                        st.session_state['token']        = result['access_token']
                        st.session_state['role']         = result['role']
                        st.session_state['username']     = username
                        st.session_state['current_page'] = 'admin_dashboard' if role=='admin' else 'student_marksheet'
                        st.rerun()