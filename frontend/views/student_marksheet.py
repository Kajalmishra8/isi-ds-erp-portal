#frontend>views>admin_marksheet.py

import streamlit as st
import pandas as pd
from utils.api_client import get

def show():
    st.markdown("## My Marksheet")

    exams = get('/api/student/exams') or []
    exam_map = {e['exam_name']: e['exam_id'] for e in exams}

    if not exams:
        st.warning("No exams available")
        return

    with st.form('marksheet_form'):
        exam_name = st.selectbox('Select Exam', list(exam_map.keys()))
        submitted = st.form_submit_button('View Marksheet', use_container_width=True)

    if submitted:
        with st.spinner("Fetching marksheet..."):
            data = get(
                f"/api/student/marksheet?enroll_no={st.session_state.get('username')}&exam_id={exam_map[exam_name]}"
            )

        if data:
            st.success(f"Marksheet for {data['student']['name']}")

            c1, c2, c3 = st.columns(3)
            c1.metric("Total", data['summary']['total_obtained'])
            c2.metric("Max", data['summary']['total_max'])
            c3.metric("Percentage", f"{data['summary']['percentage']}%")

            st.divider()

            df = pd.DataFrame(data['marks'])
            st.dataframe(df, use_container_width=True)

            st.success(
                f"Grade: {data['summary']['grade']} | Result: {data['summary']['result']}"
            )










# old # frontend/pages/student_marksheet.py
# import streamlit as st
# import pandas as pd
# from utils.api_client import get

# def show():
#     st.markdown('## My Marksheet')
#     exams = get('/api/student/exams') or []
#     exam_map = {e['exam_name']: e['exam_id'] for e in exams}
#     with st.form('marksheet_form'):
#         enroll_no = st.text_input('Enroll Number')
#         exam_name = st.selectbox('Select Exam', list(exam_map.keys()) if exam_map else ['No exams available'])
#         submitted = st.form_submit_button('View Marksheet', type='primary', use_container_width=True)
#     if submitted and enroll_no and exam_name in exam_map:
#         with st.spinner('Fetching marksheet...'):
#             data = get(f'/api/student/marksheet?enroll_no={enroll_no}&exam_id={exam_map[exam_name]}')
#         if data:
#             st.success(f"Marksheet for {data['student']['name']}")
#             c1, c2, c3 = st.columns(3)
#             c1.metric('Total Obtained', data['summary']['total_obtained'])
#             c2.metric('Total Max', data['summary']['total_max'])
#             c3.metric('Percentage', f"{data['summary']['percentage']}%")
#             st.divider()
#             df = pd.DataFrame(data['marks'])
#             st.dataframe(df, use_container_width=True)
#             csv = df.to_csv(index=False).encode()
#             st.download_button('Download CSV', csv, 'marksheet.csv', 'text/csv', use_container_width=True)