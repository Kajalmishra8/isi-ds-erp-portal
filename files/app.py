import streamlit as st

st.set_page_config(
    page_title="ERP Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Theme must be injected right after set_page_config
from components.theme import inject_theme
inject_theme()

# ── Import views ──────────────────────────────────────────────────────────────
# All imports are lazy (inside if-blocks) to avoid circular import issues.
# PAGE_MAP maps session key → (module, function_name) resolved at call time.

def _load_page(page_key: str):
    """Resolve and call the correct view function for the given page key."""
    routes = {
        "admin_dashboard":   ("views.admin_dashboard",   "show"),
        "admin_students":    ("views.admin_students",    "show"),
        "admin_exams":       ("views.admin_exams",       "show"),
        "admin_subjects":    ("views.admin_subjects",    "show"),
        "admin_marks":       ("views.admin_marks",       "show"),
        "student_marksheet": ("views.student_marksheet", "show"),
    }
    if page_key not in routes:
        st.error(f"Page '{page_key}' not found. Please navigate using the sidebar.")
        return
    module_path, fn_name = routes[page_key]
    import importlib
    mod = importlib.import_module(module_path)
    getattr(mod, fn_name)()


# ── Auth gate ─────────────────────────────────────────────────────────────────
if "token" not in st.session_state:
    import importlib
    login_mod = importlib.import_module("views.login")
    login_mod.show()
else:
    from components.header  import render_header
    from components.sidebar import render_sidebar

    render_header()
    st.markdown("<div style='height:6px;'></div>", unsafe_allow_html=True)
    page = render_sidebar()
    _load_page(page)
