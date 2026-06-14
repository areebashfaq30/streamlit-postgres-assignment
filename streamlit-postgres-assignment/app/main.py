import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from auth import login_page, logout, is_admin

st.set_page_config(
    page_title="Internship & Job Tracker",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Session state defaults ----------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "role" not in st.session_state:
    st.session_state["role"] = ""

# ---------- Auth gate ----------
if not st.session_state["logged_in"]:
    login_page()
    st.stop()

# ---------- Sidebar ----------
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/graduation-cap.png", width=60)
    st.title("🎓 Job Tracker")
    st.markdown(f"**User:** `{st.session_state['username']}`  \n**Role:** `{st.session_state['role']}`")
    st.divider()

    st.markdown("### Navigation")
    st.page_link("main.py", label="🏠 Home", icon="🏠")
    st.page_link("pages/1_Add_Opportunity.py", label="➕ Add Opportunity")
    st.page_link("pages/2_View_Search.py", label="🔍 View & Search")
    st.page_link("pages/3_Update_Opportunity.py", label="✏️ Update Opportunity")
    st.page_link("pages/4_Delete_Opportunity.py", label="🗑️ Delete Opportunity")
    st.page_link("pages/5_Analytics_Dashboard.py", label="📊 Analytics Dashboard")
    st.page_link("pages/6_CSV_Upload_Export.py", label="📂 CSV Upload & Export")
    st.page_link("pages/7_Duplicate_Detection.py", label="🔁 Duplicate Detection")
    st.page_link("pages/8_Deadline_Alerts.py", label="⏰ Deadline Alerts")
    st.page_link("pages/9_Database_Health_Check.py", label="💚 DB Health Check")
    st.divider()
    if st.button("🚪 Logout"):
        logout()

# ---------- Home content ----------
st.title("🎓 Internship & Job Tracking Dashboard")
st.markdown("**University of Central Punjab — Faculty of IT & CS**")
st.divider()

col1, col2 = st.columns([2, 1])
with col1:
    st.subheader("📋 Project Overview")
    st.markdown("""
    This dashboard helps faculty manage **internship and job opportunities** for students.
    It is built with **Streamlit**, connected to **PostgreSQL**, and fully containerized with **Docker Compose**.

    **Features:**
    - ➕ Add, ✏️ Update, 🗑️ Delete opportunities
    - 🔍 Search and filter records
    - 📊 Analytics with KPIs and charts
    - 📂 CSV upload (bulk insert) and export
    - 🔁 Duplicate detection
    - ⏰ Deadline alerts
    - 💚 Database health monitoring
    - 🔐 Role-based login (Admin / Viewer)
    """)

with col2:
    st.subheader("🛠️ Tech Stack")
    st.markdown("""
    | Tool | Purpose |
    |------|---------|
    | Streamlit | Web UI |
    | PostgreSQL | Database |
    | pgAdmin | DB Admin |
    | Docker Compose | Containers |
    | SQLAlchemy | ORM |
    | Plotly | Charts |
    | Pandas | Data Processing |
    """)

st.divider()
st.subheader("🏗️ System Architecture")
st.code("""
User Browser
    │
    ▼
Streamlit App Container  (port 8501)
    │
    ▼
PostgreSQL Container  ◄────►  pgAdmin Container
(port 5432)                   (port 5050)
    │
    ▼
Docker Volume (postgres_data) — Persistent Storage
    │
    ▼
GitHub Repository — Version Control & Collaboration
""")

st.subheader("👥 Team Members")
st.info("Update this section with your actual group member names and student IDs.")
st.markdown("""
| # | Name | Student ID | GitHub Username | Role |
|---|------|-----------|-----------------|------|
| 1 | Member 1 | BSIT-XXXX | @username1 | Backend / DB |
| 2 | Member 2 | BSIT-XXXX | @username2 | Frontend / UI |
| 3 | Member 3 | BSIT-XXXX | @username3 | Docker / DevOps |
""")
