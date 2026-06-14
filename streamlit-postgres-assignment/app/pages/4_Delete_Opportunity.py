import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from auth import require_admin
from queries import get_all_opportunities, get_opportunity_by_id, delete_opportunity

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

require_admin()

st.title("🗑️ Delete Opportunity")
st.warning("⚠️ Deletion is permanent and cannot be undone.")

try:
    df = get_all_opportunities()
    if df.empty:
        st.info("No opportunities available.")
        st.stop()

    df["label"] = df["opportunity_id"].astype(str) + " — " + df["company_name"] + " | " + df["job_title"]
    selected_label = st.selectbox("Select Opportunity to Delete", df["label"].tolist())
    selected_id = int(selected_label.split(" — ")[0])

    record = get_opportunity_by_id(selected_id)
    if record:
        st.markdown("### Preview of selected record")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Company:** {record['company_name']}")
            st.write(f"**Title:** {record['job_title']}")
            st.write(f"**Category:** {record['category']}")
            st.write(f"**City:** {record.get('city', 'N/A')}")
            st.write(f"**Work Mode:** {record.get('work_mode', 'N/A')}")
        with col2:
            st.write(f"**Status:** {record.get('status', 'N/A')}")
            st.write(f"**Experience:** {record.get('experience_level', 'N/A')}")
            st.write(f"**Deadline:** {record.get('application_deadline', 'N/A')}")
            st.write(f"**Salary:** {record.get('salary_min', 0)} – {record.get('salary_max', 0)} {record.get('currency', '')}")

    st.divider()
    confirm = st.checkbox("✅ I confirm I want to permanently delete this record.")
    if st.button("🗑️ Delete", type="primary", disabled=not confirm):
        try:
            delete_opportunity(selected_id)
            st.success("✅ Record deleted successfully!")
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")
except Exception as e:
    st.error(f"Failed to load data: {e}")
