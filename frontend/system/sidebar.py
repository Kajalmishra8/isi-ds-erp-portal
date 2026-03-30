#frontend>sytem>sidebar.py

import streamlit as st

ADMIN_PAGES = [
    ("📊", "Dashboard",   "admin_dashboard"),
    ("👥", "Students",    "admin_students"),
    ("📋", "Exams",       "admin_exams"),
    ("📚", "Subjects",    "admin_subjects"),
    ("✏️", "Marks",        "admin_marks"),
]

STUDENT_PAGES = [
    ("📄", "My Marksheet", "student_marksheet"),
]

def render_sidebar() -> str:
    role  = st.session_state.get("role", "")
    pages = ADMIN_PAGES if role == "admin" else STUDENT_PAGES
    current = st.session_state.get("current_page", pages[0][2])

    with st.sidebar:
        # Logo / Brand
        st.markdown("""
        <div style="padding:24px 16px 20px;border-bottom:1px solid #1E293B;">
          <div style="display:flex;align-items:center;gap:10px;">
            <div style="width:30px;height:30px;background:#3B82F6;border-radius:8px;
                        display:flex;align-items:center;justify-content:center;
                        font-size:15px;">🎓</div>
            <div>
              <div style="font-size:14px;font-weight:700;color:#F1F5F9;
                          letter-spacing:-.01em;">ERP Portal</div>
              <div style="font-size:10px;color:#475569;margin-top:1px;">
                Academic Management</div>
            </div>
          </div>
        </div>
        """, unsafe_allow_html=True)

        # Nav label
        st.markdown("""
        <div style="padding:20px 16px 8px;">
          <span style="font-size:10px;font-weight:600;color:#475569;
                       text-transform:uppercase;letter-spacing:.1em;">Menu</span>
        </div>
        """, unsafe_allow_html=True)

        # Nav items
        for icon, label, key in pages:
            is_active = current == key
            css_class = "nav-active" if is_active else "nav-btn"
            indicator = (
                '<span style="width:4px;height:4px;background:#3B82F6;'
                'border-radius:50%;margin-left:auto;"></span>'
                if is_active else ""
            )
            st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
            if st.button(
                f"{icon}  {label}",
                key=f"nav_{key}",
                use_container_width=True,
            ):
                st.session_state["current_page"] = key
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div style="position:fixed;bottom:0;left:0;width:220px;
                    padding:16px;border-top:1px solid #1E293B;
                    background:#0F172A;">
          <div style="font-size:10px;color:#334155;text-align:center;
                      font-weight:500;">v1.0 · FastAPI + Streamlit</div>
        </div>
        """, unsafe_allow_html=True)

    return current