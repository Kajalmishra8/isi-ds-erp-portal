#frontend>sytem>ui.py
#frontend>component>ui.py
"""
Reusable UI building blocks (pure HTML via st.markdown).
"""
import streamlit as st


# Page header
def page_header(title: str, subtitle: str = "", icon: str = ""):
    icon_part = f'<span style="font-size:20px;margin-right:10px;">{icon}</span>' if icon else ""
    sub_part  = f'<p style="font-size:13px;color:#6B7280;margin-top:4px;">{subtitle}</p>' if subtitle else ""
    st.markdown(f"""
    <div style="margin-bottom:24px;">
      <div style="display:flex;align-items:center;gap:4px;">
        {icon_part}
        <h1 style="font-size:22px;font-weight:700;color:#111827;
                   letter-spacing:-.02em;margin:0;line-height:1.3;">{title}</h1>
      </div>
      {sub_part}
    </div>
    """, unsafe_allow_html=True)


# Section label
def section_label(text: str):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;margin:24px 0 14px;">
      <span style="font-size:12px;font-weight:600;color:#6B7280;
                   text-transform:uppercase;letter-spacing:.08em;white-space:nowrap;">{text}</span>
      <div style="flex:1;height:1px;background:#E4E7EC;"></div>
    </div>
    """, unsafe_allow_html=True)


# Stat card
def stat_card(label: str, value, icon: str = "", color: str = "#3B82F6", delta: str = ""):
    delta_html = ""
    if delta:
        delta_html = f'<span style="font-size:11px;color:#10B981;font-weight:500;">{delta}</span>'
    st.markdown(f"""
    <div style="background:#fff;border:1px solid #E4E7EC;border-radius:12px;
                padding:20px 24px;box-shadow:0 1px 3px rgba(0,0,0,.06);">
      <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px;">
        <span style="font-size:11px;font-weight:600;color:#6B7280;
                     text-transform:uppercase;letter-spacing:.07em;">{label}</span>
        <span style="font-size:18px;background:{color}18;border-radius:8px;
                     padding:4px 7px;line-height:1;">{icon}</span>
      </div>
      <div style="font-size:32px;font-weight:700;color:#111827;
                  letter-spacing:-.02em;line-height:1;">{value}</div>
      {delta_html}
    </div>
    """, unsafe_allow_html=True)


# Badge
_BADGE_COLORS = {
    "blue":   ("#EFF6FF", "#2563EB"),
    "green":  ("#ECFDF5", "#059669"),
    "red":    ("#FEF2F2", "#DC2626"),
    "yellow": ("#FFFBEB", "#D97706"),
    "gray":   ("#F3F4F6", "#4B5563"),
}

def badge(text: str, color: str = "blue") -> str:
    bg, fg = _BADGE_COLORS.get(color, _BADGE_COLORS["gray"])
    return (f'<span style="display:inline-flex;align-items:center;padding:2px 8px;'
            f'border-radius:20px;font-size:11px;font-weight:600;'
            f'background:{bg};color:{fg};">{text}</span>')


# Empty state
def empty_state(title: str, message: str, icon: str = "📭"):
    st.markdown(f"""
    <div style="text-align:center;padding:48px 24px;background:#fff;
                border:1px solid #E4E7EC;border-radius:12px;">
      <div style="font-size:36px;margin-bottom:12px;">{icon}</div>
      <div style="font-size:15px;font-weight:600;color:#111827;margin-bottom:6px;">{title}</div>
      <div style="font-size:13px;color:#6B7280;">{message}</div>
    </div>
    """, unsafe_allow_html=True)


# Info banner
def info_banner(text: str, color: str = "blue"):
    bg, fg = _BADGE_COLORS.get(color, _BADGE_COLORS["blue"])
    st.markdown(f"""
    <div style="background:{bg};border-left:3px solid {fg};border-radius:0 8px 8px 0;
                padding:10px 16px;font-size:13px;color:{fg};font-weight:500;margin-bottom:16px;">
      {text}
    </div>
    """, unsafe_allow_html=True)


# Divider with label
def titled_divider(text: str = ""):
    if text:
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:12px;margin:20px 0;">
          <div style="flex:1;height:1px;background:#E4E7EC;"></div>
          <span style="font-size:11px;color:#9CA3AF;font-weight:500;
                       text-transform:uppercase;letter-spacing:.07em;">{text}</span>
          <div style="flex:1;height:1px;background:#E4E7EC;"></div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown('<hr style="border-color:#E4E7EC;margin:20px 0;">', unsafe_allow_html=True)