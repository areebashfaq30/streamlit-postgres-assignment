import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from db import test_connection
from queries import get_db_health

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("💚 Database Health Check")

if st.button("🔄 Run Health Check", type="primary"):
    with st.spinner("Connecting to PostgreSQL..."):
        success, message = test_connection()

    if success:
        st.success("✅ Database connection successful!")

        try:
            health = get_db_health()

            col1, col2, col3 = st.columns(3)
            col1.metric("Total Rows", health["row_count"])
            col2.metric("Table", "opportunities")
            col3.metric("Status", "🟢 Online")

            st.divider()
            st.subheader("🖥️ PostgreSQL Version")
            st.code(health["version"])

            st.subheader("📋 Table Schema")
            st.dataframe(pd.DataFrame(health["columns"]), use_container_width=True, hide_index=True)

            if health["latest"]:
                st.subheader("🕐 Latest Record")
                latest = health["latest"]
                st.json({
                    "id": latest.get("opportunity_id"),
                    "company": latest.get("company_name"),
                    "title": latest.get("job_title"),
                    "created_at": str(latest.get("created_at")),
                })

        except Exception as e:
            st.error(f"Error fetching health data: {e}")
    else:
        st.error(f"❌ Connection failed: {message}")
        st.markdown("**Troubleshooting:**")
        st.markdown("- Is Docker running?")
        st.markdown("- Run `docker compose up -d` to start all services.")
        st.markdown("- Check `.env` or environment variables for correct credentials.")
else:
    st.info("Click the button above to test database connectivity.")
