#frontend>views>admin_dashboard.py

import streamlit as st
from utils.api_client import get

def show():
    st.markdown('## Dashboard')
    with st.spinner('Loading...'):
        stats  = get('/api/admin/dashboard') or {}
        recent = get('/api/admin/marks/recent?limit=10') or []
    col1, col2, col3 = st.columns(3)
    col1.metric('Total Students', stats.get('total_students', 0))
    col2.metric('Total Exams',    stats.get('total_exams', 0))
    col3.metric('Total Subjects', stats.get('total_subjects', 0))
    st.divider()
    st.markdown('#### Recently Added Marks')
    if recent:
        import pandas as pd
        df = pd.DataFrame(recent)[['mark_id','marks_obtained','created_at']]
        st.dataframe(df, use_container_width=True)
    else:
        st.info('No marks recorded yet.')
    st.divider()
    st.markdown('#### Quick Actions')
    c1, c2, c3, c4 = st.columns(4)
    pages = {'Add Student': 'admin_students', 'Add Exam': 'admin_exams',
             'Add Subject': 'admin_subjects', 'Add Marks': 'admin_marks'}
    for col, (label, page) in zip([c1,c2,c3,c4], pages.items()):
        if col.button(label, use_container_width=True):
            st.session_state['current_page'] = page
            st.rerun()