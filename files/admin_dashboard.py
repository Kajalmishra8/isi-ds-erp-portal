import streamlit as st
import pandas as pd
from utils.api_client import get
from components.ui import page_header, stat_card, section_label, empty_state


def show():
    page_header("Dashboard", "System overview and recent activity", "📊")

    with st.spinner("Loading…"):
        stats  = get("/api/admin/dashboard") or {}
        recent = get("/api/admin/marks/recent?limit=8") or []

    # ── Stat cards ─────────────────────────────────────────────────────────
    c1, c2, c3 = st.columns(3)
    with c1:
        stat_card("Total Students", stats.get("total_students", 0),
                  "👥", "blue", "Enrolled")
    with c2:
        stat_card("Total Exams", stats.get("total_exams", 0),
                  "📋", "purple", "Active exams")
    with c3:
        stat_card("Total Subjects", stats.get("total_subjects", 0),
                  "📚", "teal", "All semesters")

    st.markdown("<div style='height:8px;'></div>", unsafe_allow_html=True)

    left, right = st.columns([2, 1], gap="large")

    with left:
        section_label("Recent Marks Activity")
        if recent:
            df = pd.DataFrame(recent)
            cols = [c for c in ["mark_id","marks_obtained","created_at"]
                    if c in df.columns]
            df = df[cols].copy()
            df.columns = [c.replace("_"," ").title() for c in df.columns]
            if "Created At" in df.columns:
                df["Created At"] = (
                    pd.to_datetime(df["Created At"]).dt.strftime("%d %b %Y, %H:%M")
                )
            st.table(df)
        else:
            empty_state("No activity yet", "Marks will appear here once added.", "✏️")

    with right:
        section_label("Quick Actions")
        actions = [
            ("➕  Add Student",  "admin_students"),
            ("➕  Add Exam",     "admin_exams"),
            ("➕  Add Subject",  "admin_subjects"),
            ("✏️  Enter Marks",   "admin_marks"),
        ]
        for label, page in actions:
            if st.button(label, key=f"qa_{page}", use_container_width=True):
                st.session_state["current_page"] = page
                st.rerun()
            st.markdown("<div style='height:2px;'></div>", unsafe_allow_html=True)

        st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
        section_label("System Status")
        st.markdown("""
        <div style="background:#0D1424;border:1px solid rgba(255,255,255,.07);
                    border-radius:8px;padding:12px 14px;">
          <div style="display:flex;align-items:center;gap:7px;margin-bottom:7px;">
            <span style="width:6px;height:6px;background:#34D399;border-radius:50%;
                         display:inline-block;box-shadow:0 0 6px #34D399;"></span>
            <span style="font-size:11px;font-weight:500;color:#94A3B8;">
              API Online</span>
          </div>
          <div style="display:flex;align-items:center;gap:7px;">
            <span style="width:6px;height:6px;background:#34D399;border-radius:50%;
                         display:inline-block;box-shadow:0 0 6px #34D399;"></span>
            <span style="font-size:11px;font-weight:500;color:#94A3B8;">
              Database Connected</span>
          </div>
        </div>
        """, unsafe_allow_html=True)
