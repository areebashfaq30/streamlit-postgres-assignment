import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from auth import require_admin
from queries import insert_opportunity
from utils import CATEGORIES, WORK_MODES, STATUSES, EXPERIENCE_LEVELS, CURRENCIES
import datetime

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

require_admin()

st.title("➕ Add New Opportunity")
st.markdown("Fill in the form below to add a new internship or job opportunity.")

with st.form("add_opportunity_form"):
    col1, col2 = st.columns(2)
    with col1:
        company_name = st.text_input("Company Name *")
        job_title = st.text_input("Job Title *")
        category = st.selectbox("Category *", CATEGORIES)
        city = st.text_input("City")
        country = st.text_input("Country", value="Pakistan")
        work_mode = st.selectbox("Work Mode", WORK_MODES)
        experience_level = st.selectbox("Experience Level", EXPERIENCE_LEVELS)
    with col2:
        required_skills = st.text_area("Required Skills * (comma-separated)")
        salary_min = st.number_input("Salary Min", min_value=0.0, step=1000.0)
        salary_max = st.number_input("Salary Max", min_value=0.0, step=1000.0)
        currency = st.selectbox("Currency", CURRENCIES)
        application_deadline = st.date_input("Application Deadline", min_value=datetime.date.today())
        status = st.selectbox("Status", STATUSES, index=0)
        source_link = st.text_input("Source Link (URL)")

    submitted = st.form_submit_button("💾 Add Opportunity", type="primary")

if submitted:
    errors = []
    if not company_name.strip():
        errors.append("Company Name is required.")
    if not job_title.strip():
        errors.append("Job Title is required.")
    if not required_skills.strip():
        errors.append("Required Skills is required.")
    if salary_max and salary_min and salary_max < salary_min:
        errors.append("Salary Max must be >= Salary Min.")

    if errors:
        for e in errors:
            st.error(e)
    else:
        try:
            insert_opportunity({
                "company_name": company_name.strip(),
                "job_title": job_title.strip(),
                "category": category,
                "city": city.strip(),
                "country": country.strip(),
                "work_mode": work_mode,
                "required_skills": required_skills.strip(),
                "salary_min": salary_min if salary_min > 0 else None,
                "salary_max": salary_max if salary_max > 0 else None,
                "currency": currency,
                "experience_level": experience_level,
                "application_deadline": application_deadline,
                "status": status,
                "source_link": source_link.strip() if source_link else None,
            })
            st.success(f"✅ Opportunity '{job_title}' at '{company_name}' added successfully!")
            st.balloons()
        except Exception as e:
            st.error(f"Database error: {e}")
