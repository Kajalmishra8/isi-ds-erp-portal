import streamlit as st

ADMIN_PAGES = [
    ("📊", "Dashboard",  "admin_dashboard"),
    ("👥", "Students",   "admin_students"),
    ("📋", "Exams",      "admin_exams"),
    ("📚", "Subjects",   "admin_subjects"),
    ("✏️",  "Marks",      "admin_marks"),
]
STUDENT_PAGES = [
    ("📄", "My Marksheet", "student_marksheet"),
]


def render_sidebar() -> str:
    role  = st.session_state.get("role", "")
    pages = ADMIN_PAGES if role == "admin" else STUDENT_PAGES
    current = st.session_state.get("current_page", pages[0][2])

    with st.sidebar:
        # ── Brand ─────────────────────────────────────────────────────
        st.markdown("""
        <div style="padding:18px 14px 14px;
                    border-bottom:1px solid rgba(255,255,255,.06);">
          <div style="display:flex;align-items:center;gap:9px;">
            <div style="width:28px;height:28px;
                        background:linear-gradient(135deg,#1D4ED8,#6366F1);
                        border-radius:7px;display:flex;align-items:center;
                        justify-content:center;font-size:14px;">🎓</div>
            <div>
              <div style="font-size:13px;font-weight:700;color:#F1F5F9;
                          letter-spacing:-.01em;">ERP Portal</div>
              <div style="font-size:10px;color:#334155;margin-top:1px;">
                Academic Suite</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Nav section label ─────────────────────────────────────────
        st.markdown("""
        <div style="padding:16px 14px 6px;">
          <span style="font-size:9px;font-weight:600;color:#334155;
                       text-transform:uppercase;letter-spacing:.12em;">
            Menu
          </span>
        </div>
        """, unsafe_allow_html=True)

        # ── Nav items ─────────────────────────────────────────────────
        for icon, label, key in pages:
            is_active = (current == key)
            css = "nav-active" if is_active else "nav-btn"
            st.markdown(f'<div class="{css}">', unsafe_allow_html=True)
            if st.button(
                f"{icon}  {label}",
                key=f"nav_{key}",
                use_container_width=True,
            ):
                st.session_state["current_page"] = key
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        # ── User footer ───────────────────────────────────────────────
        user = st.session_state.get("username", "")
        role_label = role.upper() if role else ""
        badge_bg  = "rgba(59,130,246,.2)"  if role=="admin" else "rgba(20,184,166,.2)"
        badge_fg  = "#93C5FD"              if role=="admin" else "#5EEAD4"
        badge_bdr = "rgba(59,130,246,.3)"  if role=="admin" else "rgba(20,184,166,.3)"
        initials  = user[:2].upper() if user else "??"

        st.markdown(f"""
        <div style="position:fixed;bottom:0;left:0;width:220px;
                    padding:12px 14px;
                    border-top:1px solid rgba(255,255,255,.06);
                    background:#0A0F1C;">
          <div style="display:flex;align-items:center;gap:8px;">
            <div style="width:26px;height:26px;border-radius:50%;
                        background:linear-gradient(135deg,#1E3A5F,#2563EB);
                        display:flex;align-items:center;justify-content:center;
                        font-size:9px;font-weight:600;color:#BFDBFE;
                        flex-shrink:0;">{initials}</div>
            <div>
              <div style="font-size:11px;font-weight:500;color:#94A3B8;
                          line-height:1.2;">{user}</div>
              <span style="font-size:9px;font-weight:600;
                           background:{badge_bg};color:{badge_fg};
                           padding:1px 6px;border-radius:10px;
                           border:1px solid {badge_bdr};">{role_label}</span>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

    return current
