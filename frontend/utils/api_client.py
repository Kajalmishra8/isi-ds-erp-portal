#frontend>utils>api_client.py

import requests
import streamlit as st
from typing import Optional

BASE_URL = st.secrets.get("API_BASE_URL", "http://localhost:8000")

def _headers() -> dict:
    token = st.session_state.get("token", "")
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

def _handle(resp: requests.Response):
    if resp.status_code >= 400:
        try:
            err = resp.json().get("detail", "Unknown error")
        except Exception:
            err = resp.text or "Unknown error"
        st.toast(f"⚠️ {err}", icon="⚠️")
        return None
    return resp.json()

def login(username: str, password: str):
    resp = requests.post(
        f"{BASE_URL}/api/auth/login",
        data={"username": username, "password": password},
    )
    data = _handle(resp)
    if not data:
        return None
    return {
        "access_token": data.get("access_token"),
        "role": data.get("role"),
    }

def get(path: str, params: dict = None):
    return _handle(
        requests.get(f"{BASE_URL}{path}", headers=_headers(), params=params)
    )

def post(path: str, data: dict):
    return _handle(
        requests.post(f"{BASE_URL}{path}", headers=_headers(), json=data)
    )