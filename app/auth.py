import streamlit as st

# Simple hardcoded credentials (in a real app, use a database)
USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "viewer": {"password": "viewer123", "role": "Viewer"},
}


def login_page():
    st.title("🔐 Login")
    st.markdown("Please log in to access the dashboard.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if username in USERS and USERS[username]["password"] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = USERS[username]["role"]
            st.success(f"Welcome, {username}! Role: {USERS[username]['role']}")
            st.rerun()
        else:
            st.error("Invalid username or password.")

    st.info("**Demo credentials:**\n- Admin: `admin` / `admin123`\n- Viewer: `viewer` / `viewer123`")


def logout():
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["role"] = ""
    st.rerun()


def require_admin():
    """Call this at the top of admin-only pages."""
    if st.session_state.get("role") != "Admin":
        st.error("⛔ This page requires Admin access.")
        st.stop()


def is_admin():
    return st.session_state.get("role") == "Admin"
