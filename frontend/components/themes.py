#frontend>components>themes.py

"""
Global CSS theme injected once at app startup.
Design: Refined enterprise — dark sidebar + clean white content.
"""

THEME_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600;9..40,700&family=DM+Mono:wght@400;500&display=swap');

:root {
    --bg:            #F7F8FA;
    --surface:       #FFFFFF;
    --border:        #E4E7EC;
    --border-light:  #F0F2F5;
    --sidebar-bg:    #0F172A;
    --sidebar-text:  #94A3B8;
    --sidebar-active:#1E293B;
    --sidebar-hi:    #F1F5F9;
    --accent:        #3B82F6;
    --accent-light:  #EFF6FF;
    --accent-dark:   #1D4ED8;
    --success:       #10B981;
    --success-light: #ECFDF5;
    --warning:       #F59E0B;
    --warning-light: #FFFBEB;
    --danger:        #EF4444;
    --danger-light:  #FEF2F2;
    --txt:           #111827;
    --txt2:          #6B7280;
    --txt3:          #9CA3AF;
    --r:   8px;
    --rl: 12px;
    --s0: 0 1px 3px rgba(0,0,0,.06),0 1px 2px rgba(0,0,0,.04);
    --s1: 0 4px 12px rgba(0,0,0,.08);
    --font: 'DM Sans', sans-serif;
    --mono: 'DM Mono', monospace;
}

*,*::before,*::after{box-sizing:border-box;}
html,body,[data-testid="stAppViewContainer"],[data-testid="stApp"]{
    font-family:var(--font)!important;
    background:var(--bg)!important;
    color:var(--txt)!important;
}
#MainMenu,footer,header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"]{display:none!important;}

/* ── Sidebar ── */
[data-testid="stSidebar"]{
    background:var(--sidebar-bg)!important;
    border-right:none!important;
    min-width:220px!important;
    max-width:220px!important;
}
[data-testid="stSidebar"]>div:first-child{
    background:var(--sidebar-bg)!important;
    padding:0!important;
}
[data-testid="stSidebar"] *{font-family:var(--font)!important;}

/* ── Main ── */
.block-container{padding:28px 36px!important;max-width:1180px!important;}
[data-testid="stMain"]{background:var(--bg)!important;}

/* ── Buttons ── */
.stButton>button{
    font-family:var(--font)!important;
    font-size:13px!important;font-weight:500!important;
    border-radius:var(--r)!important;
    border:1px solid var(--border)!important;
    background:var(--surface)!important;
    color:var(--txt)!important;
    padding:7px 16px!important;
    transition:all .14s ease!important;
    box-shadow:var(--s0)!important;
    height:auto!important;line-height:1.5!important;
}
.stButton>button:hover{
    background:var(--bg)!important;
    border-color:var(--accent)!important;
    color:var(--accent)!important;
    box-shadow:var(--s1)!important;
}

/* ── Inputs ── */
.stTextInput>div>div>input,
.stNumberInput>div>div>input,
.stTextArea>div>div>textarea{
    font-family:var(--font)!important;font-size:13px!important;
    border:1px solid var(--border)!important;
    border-radius:var(--r)!important;
    background:var(--surface)!important;color:var(--txt)!important;
    padding:8px 12px!important;
    transition:border-color .14s,box-shadow .14s!important;
}
.stTextInput>div>div>input:focus,
.stNumberInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus{
    border-color:var(--accent)!important;
    box-shadow:0 0 0 3px rgba(59,130,246,.1)!important;
    outline:none!important;
}
[data-testid="stWidgetLabel"] p,
.stTextInput label,.stNumberInput label,
.stSelectbox label,.stTextArea label,.stCheckbox label{
    font-size:11px!important;font-weight:600!important;
    color:var(--txt2)!important;letter-spacing:.06em!important;
    text-transform:uppercase!important;margin-bottom:5px!important;
}

/* ── Forms ── */
[data-testid="stForm"]{
    background:var(--surface)!important;
    border:1px solid var(--border)!important;
    border-radius:var(--rl)!important;
    padding:28px!important;
    box-shadow:var(--s0)!important;
}
[data-testid="stForm"] [data-testid="stFormSubmitButton"]>button{
    background:var(--accent)!important;color:#fff!important;
    border-color:var(--accent)!important;font-weight:600!important;
    font-size:13px!important;padding:9px 20px!important;width:100%!important;
}
[data-testid="stForm"] [data-testid="stFormSubmitButton"]>button:hover{
    background:var(--accent-dark)!important;
    border-color:var(--accent-dark)!important;color:#fff!important;
}

/* ── Metrics ── */
[data-testid="stMetric"]{
    background:var(--surface)!important;
    border:1px solid var(--border)!important;
    border-radius:var(--rl)!important;
    padding:20px 24px!important;box-shadow:var(--s0)!important;
}
[data-testid="stMetricLabel"]{
    font-size:11px!important;font-weight:600!important;
    color:var(--txt2)!important;text-transform:uppercase!important;
    letter-spacing:.06em!important;
}
[data-testid="stMetricValue"]{
    font-size:30px!important;font-weight:700!important;
    color:var(--txt)!important;line-height:1.2!important;
}

/* ── DataFrames ── */
[data-testid="stDataFrame"]{
    border:1px solid var(--border)!important;
    border-radius:var(--rl)!important;overflow:hidden!important;
    box-shadow:var(--s0)!important;
}
.dvn-scroller{background:var(--surface)!important;}

/* ── Alerts ── */
[data-testid="stAlert"]{border-radius:var(--r)!important;font-size:13px!important;}

/* ── Divider ── */
hr{border-color:var(--border)!important;margin:20px 0!important;}

/* ── Selectbox ── */
[data-baseweb="select"]>div{
    border:1px solid var(--border)!important;border-radius:var(--r)!important;
    background:var(--surface)!important;font-family:var(--font)!important;font-size:13px!important;
}
[data-baseweb="select"]>div:focus-within{
    border-color:var(--accent)!important;
    box-shadow:0 0 0 3px rgba(59,130,246,.1)!important;
}

/* ── Nav buttons (sidebar) ── */
.nav-btn>button{
    background:transparent!important;border:none!important;
    color:var(--sidebar-text)!important;
    text-align:left!important;font-size:13px!important;font-weight:400!important;
    padding:9px 14px!important;border-radius:6px!important;
    box-shadow:none!important;width:100%!important;margin:1px 0!important;
    transition:all .12s ease!important;
}
.nav-btn>button:hover{
    background:var(--sidebar-active)!important;
    color:var(--sidebar-hi)!important;border:none!important;box-shadow:none!important;
}
.nav-active>button{
    background:var(--sidebar-active)!important;
    color:var(--sidebar-hi)!important;
    border:none!important;font-weight:600!important;box-shadow:none!important;
}
.nav-active>button:hover{
    background:var(--sidebar-active)!important;color:var(--sidebar-hi)!important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:transparent;}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px;}
::-webkit-scrollbar-thumb:hover{background:var(--txt3);}

/* ── Spinner ── */
.stSpinner>div{border-top-color:var(--accent)!important;}
</style>
"""

def inject_theme():
    import streamlit as st
    st.markdown(THEME_CSS, unsafe_allow_html=True)