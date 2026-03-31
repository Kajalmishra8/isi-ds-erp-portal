"""
Dark-themed UI primitives — all rendered via st.markdown HTML.
"""
import streamlit as st

# Color accent map
_ACCENTS = {
    "blue":   ("#1D4ED8", "#3B82F6", "rgba(59,130,246,.15)",  "#93C5FD"),
    "purple": ("#5B21B6", "#8B5CF6", "rgba(139,92,246,.15)",  "#C4B5FD"),
    "teal":   ("#0F766E", "#14B8A6", "rgba(20,184,166,.15)",  "#5EEAD4"),
    "green":  ("#065F46", "#10B981", "rgba(16,185,129,.15)",  "#6EE7B7"),
    "red":    ("#991B1B", "#EF4444", "rgba(239,68,68,.15)",   "#FCA5A5"),
    "yellow": ("#78350F", "#F59E0B", "rgba(245,158,11,.15)",  "#FDE68A"),
    "gray":   ("#1E293B", "#475569", "rgba(71,85,105,.15)",   "#94A3B8"),
}


def page_header(title: str, subtitle: str = "", icon: str = ""):
    icon_html = (f'<span style="font-size:18px;margin-right:8px;'
                 f'vertical-align:middle;">{icon}</span>') if icon else ""
    sub_html  = (f'<p style="font-size:12px;color:#64748B;margin:4px 0 0;'
                 f'letter-spacing:.01em;">{subtitle}</p>') if subtitle else ""
    st.markdown(f"""
    <div style="margin-bottom:22px;padding-bottom:16px;
                border-bottom:1px solid rgba(255,255,255,.07);">
      <div style="display:flex;align-items:center;">
        {icon_html}
        <h1 style="font-size:20px;font-weight:700;color:#F1F5F9;
                   letter-spacing:-.02em;margin:0;line-height:1.3;">{title}</h1>
      </div>
      {sub_html}
    </div>
    """, unsafe_allow_html=True)


def stat_card(label: str, value, icon: str = "",
              color: str = "blue", delta: str = ""):
    g1, g2, bg, fg = _ACCENTS.get(color, _ACCENTS["blue"])
    delta_html = (f'<div style="font-size:10px;color:#34D399;font-weight:500;'
                  f'margin-top:6px;">{delta}</div>') if delta else ""
    st.markdown(f"""
    <div style="background:#0D1424;border:1px solid rgba(255,255,255,.07);
                border-radius:10px;padding:16px 18px;
                border-top:2px solid {g2};position:relative;overflow:hidden;">
      <div style="position:absolute;top:0;left:0;right:0;height:2px;
                  background:linear-gradient(90deg,{g1},{g2});"></div>
      <div style="display:flex;justify-content:space-between;
                  align-items:flex-start;margin-bottom:10px;">
        <span style="font-size:10px;font-weight:600;color:#475569;
                     text-transform:uppercase;letter-spacing:.09em;">{label}</span>
        <span style="font-size:16px;background:{bg};border-radius:6px;
                     padding:3px 6px;line-height:1;">{icon}</span>
      </div>
      <div style="font-size:30px;font-weight:700;color:#F1F5F9;
                  letter-spacing:-.02em;line-height:1;">{value}</div>
      {delta_html}
    </div>
    """, unsafe_allow_html=True)


def section_label(text: str):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;margin:20px 0 12px;">
      <span style="font-size:10px;font-weight:600;color:#475569;
                   text-transform:uppercase;letter-spacing:.1em;
                   white-space:nowrap;">{text}</span>
      <div style="flex:1;height:1px;background:rgba(255,255,255,.06);"></div>
    </div>
    """, unsafe_allow_html=True)


def info_banner(text: str, color: str = "blue"):
    _, _, bg, fg = _ACCENTS.get(color, _ACCENTS["blue"])
    st.markdown(f"""
    <div style="background:{bg};border-left:3px solid;
                border-image:linear-gradient(180deg,{_ACCENTS[color][0]},{_ACCENTS[color][1]}) 1;
                border-radius:0 6px 6px 0;padding:9px 14px;
                font-size:12px;color:{fg};font-weight:500;margin-bottom:14px;">
      {text}
    </div>
    """, unsafe_allow_html=True)


def empty_state(title: str, message: str, icon: str = "📭"):
    st.markdown(f"""
    <div style="text-align:center;padding:40px 24px;
                background:#0D1424;border:1px solid rgba(255,255,255,.07);
                border-radius:10px;">
      <div style="font-size:32px;margin-bottom:10px;">{icon}</div>
      <div style="font-size:14px;font-weight:600;color:#94A3B8;
                  margin-bottom:6px;">{title}</div>
      <div style="font-size:12px;color:#475569;">{message}</div>
    </div>
    """, unsafe_allow_html=True)


def role_badge(role: str) -> str:
    """Returns inline HTML badge string for a role."""
    if role == "admin":
        return ('<span style="font-size:9px;font-weight:600;'
                'background:rgba(59,130,246,.2);color:#93C5FD;'
                'padding:2px 7px;border-radius:10px;'
                'border:1px solid rgba(59,130,246,.3);">ADMIN</span>')
    return ('<span style="font-size:9px;font-weight:600;'
            'background:rgba(20,184,166,.2);color:#5EEAD4;'
            'padding:2px 7px;border-radius:10px;'
            'border:1px solid rgba(20,184,166,.3);">STUDENT</span>')


def result_banner(result: str, grade: str, pct: float):
    is_pass = result == "PASS"
    bg   = "rgba(52,211,153,.1)"  if is_pass else "rgba(248,113,113,.1)"
    fg   = "#34D399"              if is_pass else "#F87171"
    bdr  = "rgba(52,211,153,.3)"  if is_pass else "rgba(248,113,113,.3)"
    icon = "✅" if is_pass else "❌"
    st.markdown(f"""
    <div style="background:{bg};border:1px solid {bdr};border-radius:8px;
                padding:14px 20px;margin-top:14px;
                display:flex;align-items:center;justify-content:space-between;">
      <div style="font-size:14px;font-weight:700;color:{fg};">
        {icon}&nbsp; Result: {result}
      </div>
      <div style="font-size:13px;color:{fg};font-weight:500;">
        Grade: <b>{grade}</b> &nbsp;·&nbsp; {pct}%
      </div>
    </div>
    """, unsafe_allow_html=True)