"""
Modern Dark-Glass ERP Theme
Design: Deep navy base + neon blue accent + glass panels + premium typography.
"""

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg:           #080C14;
    --bg2:          #0A0F1C;
    --bg3:          #0D1424;
    --bg4:          #111827;
    --surface:      #0D1424;
    --surface2:     #111827;
    --border:       rgba(255,255,255,.07);
    --border2:      rgba(255,255,255,.11);
    --accent:       #3B82F6;
    --accent-dim:   rgba(59,130,246,.15);
    --accent-glow:  rgba(59,130,246,.25);
    --purple:       #8B5CF6;
    --purple-dim:   rgba(139,92,246,.15);
    --teal:         #14B8A6;
    --teal-dim:     rgba(20,184,166,.15);
    --success:      #34D399;
    --success-dim:  rgba(52,211,153,.15);
    --warning:      #FBBF24;
    --danger:       #F87171;
    --danger-dim:   rgba(248,113,113,.15);
    --txt:          #F1F5F9;
    --txt2:         #94A3B8;
    --txt3:         #64748B;
    --txt4:         #475569;
    --txt5:         #334155;
    --font:         'Inter', sans-serif;
    --mono:         'JetBrains Mono', monospace;
    --r:  7px;
    --rl: 10px;
    --rx: 14px;
}

*,*::before,*::after { box-sizing: border-box; }

html,body,
[data-testid="stAppViewContainer"],
[data-testid="stApp"] {
    font-family: var(--font) !important;
    background: var(--bg) !important;
    color: var(--txt) !important;
}

/* ── Strip Streamlit chrome ── */
#MainMenu,footer,header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display:none !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--bg2) !important;
    border-right: 1px solid var(--border) !important;
    min-width: 220px !important; max-width: 220px !important;
}
[data-testid="stSidebar"] > div:first-child {
    background: var(--bg2) !important; padding:0 !important;
}
[data-testid="stSidebar"] * { font-family: var(--font) !important; }

/* ── Main content ── */
[data-testid="stMain"], .main { background: var(--bg) !important; }
.block-container { padding: 24px 32px !important; max-width: 1200px !important; }

/* ── Buttons ── */
.stButton > button {
    font-family: var(--font) !important;
    font-size: 12px !important; font-weight: 500 !important;
    border-radius: var(--r) !important;
    border: 1px solid var(--border2) !important;
    background: var(--surface) !important;
    color: var(--txt2) !important;
    padding: 7px 14px !important;
    transition: all .15s !important;
    height: auto !important; line-height: 1.5 !important;
    box-shadow: none !important;
}
.stButton > button:hover {
    border-color: var(--accent) !important;
    color: #93C5FD !important;
    background: var(--accent-dim) !important;
}

/* ── Form submit ── */
[data-testid="stForm"] [data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #1D4ED8, #3B82F6) !important;
    color: #fff !important; border: none !important;
    font-weight: 600 !important; font-size: 12px !important;
    padding: 9px 20px !important; width: 100% !important;
    border-radius: var(--r) !important;
    box-shadow: 0 0 20px rgba(59,130,246,.3) !important;
}
[data-testid="stForm"] [data-testid="stFormSubmitButton"] > button:hover {
    box-shadow: 0 0 28px rgba(59,130,246,.45) !important;
    background: linear-gradient(135deg, #2563EB, #60A5FA) !important;
}

/* ── Inputs ── */
.stTextInput > div > div > input,
.stNumberInput > div > div > input,
.stTextArea > div > div > textarea {
    font-family: var(--font) !important; font-size: 12px !important;
    border: 1px solid var(--border2) !important;
    border-radius: var(--r) !important;
    background: var(--bg4) !important; color: var(--txt) !important;
    padding: 8px 12px !important;
    transition: border-color .15s, box-shadow .15s !important;
}
.stTextInput > div > div > input:focus,
.stNumberInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,.15) !important;
    outline: none !important;
}

/* ── Labels ── */
[data-testid="stWidgetLabel"] p,
.stTextInput label, .stNumberInput label,
.stSelectbox label, .stTextArea label, .stCheckbox label {
    font-size: 10px !important; font-weight: 600 !important;
    color: var(--txt3) !important; letter-spacing: .08em !important;
    text-transform: uppercase !important; margin-bottom: 4px !important;
}

/* ── Forms ── */
[data-testid="stForm"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--rl) !important;
    padding: 24px !important;
}

/* ── Tabs ── */
[data-testid="stTabs"] [role="tablist"] {
    border-bottom: 1px solid var(--border) !important;
    gap: 0 !important;
}
[data-testid="stTabs"] button[role="tab"] {
    font-family: var(--font) !important;
    font-size: 12px !important; font-weight: 500 !important;
    color: var(--txt3) !important;
    padding: 8px 16px !important;
    border-radius: 0 !important;
    border: none !important;
    border-bottom: 2px solid transparent !important;
    background: transparent !important;
    transition: all .15s !important;
}
[data-testid="stTabs"] button[role="tab"]:hover { color: var(--txt2) !important; }
[data-testid="stTabs"] button[aria-selected="true"] {
    color: #93C5FD !important;
    border-bottom-color: var(--accent) !important;
    background: transparent !important;
}

/* ── Tables (st.table) ── */
.stTable table {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--rl) !important;
    border-collapse: separate !important;
    border-spacing: 0 !important;
    font-size: 12px !important; width: 100% !important;
    overflow: hidden !important;
}
.stTable thead tr th {
    background: var(--bg4) !important;
    color: var(--txt3) !important;
    font-size: 10px !important; font-weight: 600 !important;
    text-transform: uppercase !important; letter-spacing: .07em !important;
    padding: 10px 14px !important;
    border-bottom: 1px solid var(--border) !important;
    border-right: none !important;
}
.stTable tbody tr td {
    color: var(--txt2) !important;
    padding: 9px 14px !important;
    border-bottom: 1px solid var(--border) !important;
    border-right: none !important;
    font-family: var(--font) !important;
}
.stTable tbody tr:last-child td { border-bottom: none !important; }
.stTable tbody tr:hover td { background: rgba(255,255,255,.025) !important; }

/* ── Metrics ── */
[data-testid="stMetric"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--rl) !important;
    padding: 16px 20px !important;
    position: relative !important; overflow: hidden !important;
}
[data-testid="stMetricLabel"] {
    font-size: 10px !important; font-weight: 600 !important;
    color: var(--txt3) !important; text-transform: uppercase !important;
    letter-spacing: .08em !important;
}
[data-testid="stMetricValue"] {
    font-size: 28px !important; font-weight: 700 !important;
    color: var(--txt) !important; line-height: 1.2 !important;
}

/* ── Selectbox ── */
[data-baseweb="select"] > div {
    border: 1px solid var(--border2) !important;
    border-radius: var(--r) !important;
    background: var(--bg4) !important;
    font-family: var(--font) !important; font-size: 12px !important;
    color: var(--txt) !important;
}
[data-baseweb="select"] > div:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 3px rgba(59,130,246,.15) !important;
}

/* ── Alerts ── */
[data-testid="stAlert"] {
    border-radius: var(--r) !important;
    font-size: 12px !important;
    font-family: var(--font) !important;
}

/* ── Divider ── */
hr { border-color: var(--border) !important; margin: 18px 0 !important; }

/* ── Checkbox ── */
[data-baseweb="checkbox"] {
    font-family: var(--font) !important; font-size: 12px !important;
    color: var(--txt2) !important;
}

/* ── Spinner ── */
.stSpinner > div { border-top-color: var(--accent) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border2); border-radius: 2px; }
::-webkit-scrollbar-thumb:hover { background: var(--txt5); }

/* ── Sidebar nav buttons ── */
.nav-btn > button {
    background: transparent !important; border: none !important;
    color: var(--txt3) !important;
    text-align: left !important; font-size: 12px !important;
    font-weight: 400 !important; padding: 8px 12px !important;
    border-radius: var(--r) !important; box-shadow: none !important;
    width: 100% !important; margin: 1px 0 !important;
    transition: all .12s !important;
}
.nav-btn > button:hover {
    background: rgba(255,255,255,.05) !important;
    color: var(--txt2) !important;
    border: none !important; box-shadow: none !important;
}
.nav-active > button {
    background: var(--accent-dim) !important;
    color: #93C5FD !important;
    border: none !important; font-weight: 500 !important;
    box-shadow: none !important;
}
.nav-active > button:hover {
    background: var(--accent-dim) !important;
    color: #93C5FD !important;
}

/* ── Download button ── */
.stDownloadButton > button {
    background: var(--surface) !important;
    border: 1px solid var(--border2) !important;
    color: var(--txt2) !important;
    font-size: 12px !important;
}
.stDownloadButton > button:hover {
    border-color: var(--accent) !important;
    color: #93C5FD !important;
    background: var(--accent-dim) !important;
}
</style>
"""


def inject_theme():
    import streamlit as st
    st.markdown(THEME_CSS, unsafe_allow_html=True)
