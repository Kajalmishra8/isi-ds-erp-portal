#frontend>views>app.py

import streamlit as st

if st.button("RESET"):
    st.session_state.clear()
    st.rerun()

st.set_page_config(page_title='ERP Portal', layout='wide', initial_sidebar_state='expanded')

from components.header import render_header
from components.sidebar import render_sidebar
from views import login, admin_dashboard, admin_students, admin_exams, admin_subjects, admin_marks, student_marksheet

PAGE_MAP = {
    'admin_dashboard':   admin_dashboard.show,
    'admin_students':    admin_students.show,
    'admin_exams':       admin_exams.show,
    'admin_subjects':    admin_subjects.show,
    'admin_marks':       admin_marks.show,
    'student_marksheet': student_marksheet.show,
}

#-------------------------------------------------
# Old page_map
# PAGE_MAP = {
#     'admin_dashboard':   admin_dashboard.show,
#     'admin_students':    admin_students.show,
#     'admin_exams':       admin_exams.show,
#     'admin_subjects':    admin_subjects.show,
#     'admin_marks':       admin_marks.show,
#     'student_marksheet': student_marksheet.show,
# }
#-------------------------------------------------

if 'token' not in st.session_state:
    login.show()
else:
    render_header()
    page = render_sidebar()
    PAGE_MAP.get(page, lambda: st.error('Page not found'))()