import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from queries import get_duplicates

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("🔁 Duplicate Detection")
st.markdown("Identifies opportunities that share the same **Company Name**, **Job Title**, and **City**.")

try:
    df = get_duplicates()
    if df.empty:
        st.success("✅ No duplicate records found!")
    else:
        st.warning(f"⚠️ {len(df)} record(s) appear to be duplicates.")
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.info("💡 Review the duplicates above and use the **Delete Opportunity** page to remove unwanted entries.")
except Exception as e:
    st.error(f"Error checking duplicates: {e}")
