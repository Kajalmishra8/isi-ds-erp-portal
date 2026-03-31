import streamlit as st

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Base ── */
html, body, [data-testid="stApp"] {
    font-family: 'Inter', sans-serif !important;
    background: #080C14 !important;
    color: #F1F5F9 !important;
}

/* ── Remove Streamlit default UI ── */
#MainMenu, footer, header {
    visibility: hidden !important;
}

/* ── Sidebar (FIXED PROPERLY) ── */
section[data-testid="stSidebar"] {
    background: #0A0F1C !important;
    border-right: 1px solid rgba(255,255,255,.07);
}

/* Sidebar buttons */
section[data-testid="stSidebar"] .stButton > button {
    background: transparent !important;
    color: #94A3B8 !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 10px 12px !important;
    text-align: left !important;
    width: 100% !important;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(255,255,255,.05) !important;
    color: #E2E8F0 !important;
}

/* ── Main Layout ── */
[data-testid="stMain"] {
    background: #080C14 !important;
}

/* IMPORTANT: DO NOT FORCE MARGINS */
.block-container {
    padding-top: 2rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── Buttons ── */
.stButton > button {
    border-radius: 6px !important;
    border: 1px solid rgba(255,255,255,.1) !important;
    background: #111827 !important;
    color: #CBD5F5 !important;
}

.stButton > button:hover {
    border-color: #3B82F6 !important;
    color: #93C5FD !important;
    background: rgba(59,130,246,.15) !important;
}

/* ── Inputs ── */
.stTextInput input {
    background: #111827 !important;
    border: 1px solid rgba(255,255,255,.1) !important;
    color: #F1F5F9 !important;
    border-radius: 6px !important;
}

.stTextInput input:focus {
    border-color: #3B82F6 !important;
    box-shadow: 0 0 0 2px rgba(59,130,246,.2) !important;
}

/* ── Forms ── */
[data-testid="stForm"] {
    background: #0D1424 !important;
    border: 1px solid rgba(255,255,255,.07) !important;
    border-radius: 10px !important;
    padding: 20px !important;
}

/* ── Tables ── */
.stDataFrame, .stTable {
    background: #0D1424 !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,.07) !important;
}

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: #0D1424 !important;
    border-radius: 10px !important;
    padding: 16px !important;
    border: 1px solid rgba(255,255,255,.07) !important;
}
</style>
"""

def inject_theme():
    st.markdown(THEME_CSS, unsafe_allow_html=True)