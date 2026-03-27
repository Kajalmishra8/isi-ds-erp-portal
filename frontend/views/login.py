#frontend>views>login.py
import streamlit as st
from utils.api_client import login

def show():
    st.markdown("## ERP Portal Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Login")

    if submitted:
        if not username or not password:
            st.warning("Enter credentials")
            return

        res = login(username, password)

        if res:
            st.session_state["token"] = res["access_token"]
            st.session_state["role"] = res["role"]
            st.session_state["username"] = username

            # redirect
            if res["role"] == "admin":
                st.session_state["current_page"] = "admin_dashboard"
            else:
                st.session_state["current_page"] = "student_marksheet"

            st.rerun()




# Old 2
# import streamlit as st
# import pandas as pd
# from utils.api_client import get

# def show():
#     st.markdown("## Dashboard")

#     stats = get("/api/admin/dashboard") or {}
#     recent = get("/api/admin/marks/recent?limit=10") or []

#     col1, col2, col3 = st.columns(3)

#     col1.metric("Total Students", stats.get("total_students", 0))
#     col2.metric("Total Exams", stats.get("total_exams", 0))
#     col3.metric("Total Subjects", stats.get("total_subjects", 0))

#     st.divider()

#     st.markdown("### Recently Added Marks")

#     if recent:
#         df = pd.DataFrame(recent)
#         st.dataframe(df, use_container_width=True)
#     else:
#         st.info("No recent marks")

#     st.divider()

#     st.markdown("### Quick Actions")

#     c1, c2, c3, c4 = st.columns(4)

#     if c1.button("Students"):
#         st.session_state["current_page"] = "admin_students"
#         st.rerun()

#     if c2.button("Exams"):
#         st.session_state["current_page"] = "admin_exams"
#         st.rerun()

#     if c3.button("Subjects"):
#         st.session_state["current_page"] = "admin_subjects"
#         st.rerun()

#     if c4.button("Marks"):
#         st.session_state["current_page"] = "admin_marks"
#         st.rerun()


# Old 1
# frontend/pages/login.py
# import streamlit as st
# from utils.api_client import login

# def show():
#     st.markdown('<style>div.block-container{max-width:420px;margin:auto;padding-top:80px;}</style>', unsafe_allow_html=True)
#     st.markdown('## ERP Portal')
#     st.markdown('##### Welcome back! Sign in to continue.')
#     st.divider()
#     with st.form('login_form', clear_on_submit=False):
#         username = st.text_input('Username', placeholder='Enter username')
#         password = st.text_input('Password', type='password', placeholder='Enter password')
#         role     = st.selectbox('Role', ['student', 'admin'])
#         submitted = st.form_submit_button('Sign In', use_container_width=True, type='primary')
#         if submitted:
#             if not username or not password:
#                 st.warning('Please fill all fields.')
#             else:
#                 with st.spinner('Authenticating...'):
#                     result = login(username, password)
#                 if result:
#                     if result.get('role') != role:
#                         st.error('Role mismatch. Please select the correct role.')
#                     else:
#                         st.session_state['token']        = result['access_token']
#                         st.session_state['role']         = result['role']
#                         st.session_state['username']     = username
#                         st.session_state['current_page'] = 'admin_dashboard' if role=='admin' else 'student_marksheet'
#                         st.rerun()