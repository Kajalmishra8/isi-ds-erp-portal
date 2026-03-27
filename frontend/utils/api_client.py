#frontend>utils>api_client.py

import requests, streamlit as st
from typing import Optional

BASE_URL = st.secrets.get('API_BASE_URL', 'http://localhost:8000')

def _headers() -> dict:
    token = st.session_state.get('token', '')
    return {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

def _handle(resp: requests.Response):
    if resp.status_code >= 400:
        err = resp.json().get('detail', 'Unknown error')
        st.toast(f'Error: {err}')
        return None
    return resp.json()

def login(username: str, password: str):
    resp = requests.post(
        f'{BASE_URL}/api/auth/login',
        data={'username': username, 'password': password}
    )

    data = _handle(resp)
    if not data:
        return None

    return {
        "access_token": data.get("access_token"),
        "role": data.get("role")   # ✅ FIXED
    }

def get(path: str, params: dict = None): return _handle(requests.get(f'{BASE_URL}{path}', headers=_headers(), params=params))
def post(path: str, data: dict):         return _handle(requests.post(f'{BASE_URL}{path}', headers=_headers(), json=data))










#------------------------------------------------------------
# old login 2
# def login(username: str, password: str):
#     resp = requests.post(
#         f'{BASE_URL}/api/auth/login',
#         data={'username': username, 'password': password}
#     )

#     data = _handle(resp)
#     if not data:
#         return None
    
#     token = data.get("access_token")

#     role = "admin" if username == "admin" else "student"

#     return {
#         "access_token": token,
#         "role": role
#     }
#------------------------------------------------------------
# old login 1
# def login(username: str, password: str) -> Optional[dict]:
#     resp = requests.post(f'{BASE_URL}/api/auth/login',
#         data={'username': username, 'password': password})
#     return _handle(resp)
#------------------------------------------------------------


# Old code
# frontend/utils/api_client.py
# import requests, streamlit as st
# from typing import Optional

# BASE_URL = st.secrets.get('API_BASE_URL', 'http://localhost:8000')

# def _headers() -> dict:
#     token = st.session_state.get('token', '')
#     return {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# def _handle(resp: requests.Response):
#     if resp.status_code >= 400:
#         err = resp.json().get('detail', 'Unknown error')
#         st.toast(f'Error: {err}')
#         return None
#     return resp.json()

# def login(username: str, password: str):
#     resp = requests.post(
#         f'{BASE_URL}/api/auth/login',
#         data={'username': username, 'password': password}
#     )

#     data = _handle(resp)
#     if not data:
#         return None

#     token = data.get("access_token")

#     role = "admin" if username == "admin" else "student"

#     return {
#         "access_token": token,
#         "role": role
#     }

#---------------------------------------------------------------------
# # old -- def login(username: str, password: str) -> Optional[dict]:
# #     resp = requests.post(f'{BASE_URL}/api/auth/login',
# #         data={'username': username, 'password': password})
# #     return _handle(resp)
#---------------------------------------------------------------------

# def get(path: str, params: dict = None): return _handle(requests.get(f'{BASE_URL}{path}', headers=_headers(), params=params))
# def post(path: str, data: dict):         return _handle(requests.post(f'{BASE_URL}{path}', headers=_headers(), json=data))