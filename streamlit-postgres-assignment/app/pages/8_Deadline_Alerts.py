import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from queries import get_deadline_alerts
import datetime

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("⏰ Deadline Alerts")
st.markdown(f"**Today:** {datetime.date.today().strftime('%B %d, %Y')}")

try:
    df_soon, df_expired = get_deadline_alerts()

    col1, col2 = st.columns(2)
    col1.metric("⚡ Closing Within 7 Days", len(df_soon))
    col2.metric("❌ Expired / Past Deadline", len(df_expired))

    st.divider()

    st.subheader("⚡ Opportunities Closing Within 7 Days")
    if df_soon.empty:
        st.success("No opportunities closing within the next 7 days.")
    else:
        for _, row in df_soon.iterrows():
            days_left = (row["application_deadline"] - datetime.date.today()).days
            with st.expander(f"🔔 {row['company_name']} — {row['job_title']} ({days_left} day(s) left)"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Category:** {row['category']}")
                    st.write(f"**City:** {row['city']}")
                    st.write(f"**Work Mode:** {row['work_mode']}")
                with col2:
                    st.write(f"**Deadline:** {row['application_deadline']}")
                    st.write(f"**Status:** {row['status']}")
                    if row.get("source_link"):
                        st.markdown(f"[🔗 Apply Here]({row['source_link']})")

    st.divider()

    st.subheader("❌ Expired Opportunities")
    if df_expired.empty:
        st.success("No expired opportunities found.")
    else:
        st.dataframe(
            df_expired[["opportunity_id", "company_name", "job_title", "category", "city", "application_deadline", "status"]],
            use_container_width=True, hide_index=True
        )

except Exception as e:
    st.error(f"Error loading alerts: {e}")
