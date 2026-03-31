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

import requests

BASE_URL = "http://127.0.0.1:8000"

def login(username, password):
    resp = requests.post(
        f"{BASE_URL}/api/auth/login",
        data={
            "username": username,
            "password": password
        },
        headers={
            "Content-Type": "application/x-www-form-urlencoded"
        }
    )

    return _handle(resp)

def _handle(resp):
    try:
        data = resp.json()
    except Exception:
        raise Exception(f"Non-JSON response: {resp.text}")

    if resp.status_code >= 400:
        raise Exception(data.get("detail", "Unknown error"))

    return data

def get(path: str, params: dict = None): return _handle(requests.get(f'{BASE_URL}{path}', headers=_headers(), params=params))
def post(path: str, data: dict):         return _handle(requests.post(f'{BASE_URL}{path}', headers=_headers(), json=data))