#frontend>components>sidebar.py

import streamlit as st

ADMIN_PAGES  = {'Dashboard': 'admin_dashboard', 'Students': 'admin_students',
                'Exams': 'admin_exams', 'Subjects': 'admin_subjects', 'Marks': 'admin_marks'}
STUDENT_PAGES = {'My Marksheet': 'student_marksheet'}

def render_sidebar() -> str:
    role  = st.session_state.get('role', '')
    pages = ADMIN_PAGES if role == 'admin' else STUDENT_PAGES
    with st.sidebar:
        st.markdown('### Navigation')
        st.divider()
        current = st.session_state.get('current_page', list(pages.values())[0])
        for label, key in pages.items():
            active = 'background:#EFF6FF;color:#2563EB;' if current == key else ''
            if st.button(label, key=f'nav_{key}', use_container_width=True):
                st.session_state['current_page'] = key
                st.rerun()
    return st.session_state.get('current_page', list(pages.values())[0])