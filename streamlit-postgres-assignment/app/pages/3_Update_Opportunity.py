import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from auth import require_admin
from queries import get_all_opportunities, get_opportunity_by_id, update_opportunity
from utils import CATEGORIES, WORK_MODES, STATUSES, EXPERIENCE_LEVELS, CURRENCIES
import datetime

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

require_admin()

st.title("✏️ Update Opportunity")

try:
    df = get_all_opportunities()
    if df.empty:
        st.info("No opportunities found.")
        st.stop()

    df["label"] = df["opportunity_id"].astype(str) + " — " + df["company_name"] + " | " + df["job_title"]
    options = df["label"].tolist()
    selected_label = st.selectbox("Select Opportunity to Update", options)
    selected_id = int(selected_label.split(" — ")[0])

    record = get_opportunity_by_id(selected_id)
    if not record:
        st.error("Record not found.")
        st.stop()

    st.markdown("---")
    with st.form("update_form"):
        col1, col2 = st.columns(2)
        with col1:
            company_name = st.text_input("Company Name", value=record["company_name"])
            job_title = st.text_input("Job Title", value=record["job_title"])
            category = st.selectbox("Category", CATEGORIES, index=CATEGORIES.index(record["category"]) if record["category"] in CATEGORIES else 0)
            city = st.text_input("City", value=record.get("city") or "")
            country = st.text_input("Country", value=record.get("country") or "")
            work_mode = st.selectbox("Work Mode", WORK_MODES, index=WORK_MODES.index(record["work_mode"]) if record.get("work_mode") in WORK_MODES else 0)
            experience_level = st.selectbox("Experience Level", EXPERIENCE_LEVELS, index=EXPERIENCE_LEVELS.index(record["experience_level"]) if record.get("experience_level") in EXPERIENCE_LEVELS else 0)
        with col2:
            required_skills = st.text_area("Required Skills", value=record.get("required_skills") or "")
            salary_min = st.number_input("Salary Min", value=float(record["salary_min"] or 0), step=1000.0)
            salary_max = st.number_input("Salary Max", value=float(record["salary_max"] or 0), step=1000.0)
            currency = st.selectbox("Currency", CURRENCIES, index=CURRENCIES.index(record["currency"]) if record.get("currency") in CURRENCIES else 0)
            deadline_val = record["application_deadline"] if record.get("application_deadline") else datetime.date.today()
            application_deadline = st.date_input("Application Deadline", value=deadline_val)
            status = st.selectbox("Status", STATUSES, index=STATUSES.index(record["status"]) if record.get("status") in STATUSES else 0)
            source_link = st.text_input("Source Link", value=record.get("source_link") or "")

        submitted = st.form_submit_button("💾 Save Changes", type="primary")

    if submitted:
        try:
            update_opportunity(selected_id, {
                "company_name": company_name, "job_title": job_title, "category": category,
                "city": city, "country": country, "work_mode": work_mode,
                "required_skills": required_skills, "salary_min": salary_min or None,
                "salary_max": salary_max or None, "currency": currency,
                "experience_level": experience_level, "application_deadline": application_deadline,
                "status": status, "source_link": source_link or None,
            })
            st.success("✅ Opportunity updated successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
except Exception as e:
    st.error(f"Failed to load data: {e}")
