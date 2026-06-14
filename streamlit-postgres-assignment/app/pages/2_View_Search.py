import streamlit as st
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from queries import search_opportunities
from utils import CATEGORIES, WORK_MODES, STATUSES, EXPERIENCE_LEVELS, dataframe_to_csv_bytes

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("🔍 View & Search Opportunities")

# Sidebar filters
with st.sidebar:
    st.header("🔎 Filters")
    keyword = st.text_input("Search keyword", placeholder="company, title, skill...")
    category = st.selectbox("Category", [""] + CATEGORIES)
    city = st.text_input("City")
    work_mode = st.selectbox("Work Mode", [""] + WORK_MODES)
    status = st.selectbox("Status", [""] + STATUSES)
    experience_level = st.selectbox("Experience Level", [""] + EXPERIENCE_LEVELS)
    salary_min = st.number_input("Min Salary", min_value=0, step=5000, value=0)
    salary_max = st.number_input("Max Salary (0 = no limit)", min_value=0, step=5000, value=0)
    search_btn = st.button("🔍 Search", type="primary")

if search_btn or True:  # always load on first visit
    try:
        df = search_opportunities(
            keyword=keyword,
            category=category,
            city=city,
            work_mode=work_mode,
            status=status,
            salary_min=salary_min if salary_min > 0 else None,
            salary_max=salary_max if salary_max > 0 else None,
            experience_level=experience_level,
        )
        st.markdown(f"**{len(df)} record(s) found**")

        # Quick KPI row
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total", len(df))
        col2.metric("Open", len(df[df["status"] == "Open"]) if not df.empty else 0)
        col3.metric("Companies", df["company_name"].nunique() if not df.empty else 0)
        col4.metric("Categories", df["category"].nunique() if not df.empty else 0)

        st.divider()

        if df.empty:
            st.info("No records match your filters.")
        else:
            st.dataframe(df, use_container_width=True, hide_index=True)

            csv = dataframe_to_csv_bytes(df)
            st.download_button(
                label="⬇️ Export as CSV",
                data=csv,
                file_name="opportunities_export.csv",
                mime="text/csv"
            )
    except Exception as e:
        st.error(f"Error loading data: {e}")
