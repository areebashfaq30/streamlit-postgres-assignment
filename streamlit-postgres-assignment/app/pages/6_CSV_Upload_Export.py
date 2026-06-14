import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from auth import require_admin, is_admin
from queries import get_all_opportunities, bulk_insert_opportunities, search_opportunities
from utils import validate_csv, dataframe_to_csv_bytes, REQUIRED_CSV_COLUMNS

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("📂 CSV Upload & Export")

tab1, tab2 = st.tabs(["⬆️ CSV Upload (Bulk Insert)", "⬇️ CSV Export"])

with tab1:
    if not is_admin():
        st.warning("⛔ Admin role required for CSV upload.")
    else:
        st.markdown("Upload a CSV file to bulk-insert opportunities into PostgreSQL.")
        st.markdown("**Required columns:** " + ", ".join(f"`{c}`" for c in REQUIRED_CSV_COLUMNS))

        uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
        if uploaded_file:
            try:
                df_upload = pd.read_csv(uploaded_file)
                st.markdown(f"**Rows in file:** {len(df_upload)}")
                st.dataframe(df_upload.head(5), use_container_width=True)

                is_valid, errors, df_clean = validate_csv(df_upload)

                if errors:
                    st.warning("⚠️ Validation issues found:")
                    for e in errors:
                        st.warning(f"  • {e}")

                if df_clean is not None and not df_clean.empty:
                    st.success(f"✅ {len(df_clean)} valid row(s) ready to insert.")
                    if st.button("💾 Insert Valid Rows into PostgreSQL", type="primary"):
                        try:
                            bulk_insert_opportunities(df_clean)
                            st.success(f"✅ {len(df_clean)} records inserted successfully!")
                            st.balloons()
                        except Exception as e:
                            st.error(f"Insert error: {e}")
                else:
                    st.error("No valid rows to insert after validation.")
            except Exception as e:
                st.error(f"Error reading CSV: {e}")

with tab2:
    st.markdown("Export opportunities from PostgreSQL to a CSV file.")

    col1, col2 = st.columns(2)
    with col1:
        from utils import CATEGORIES, WORK_MODES, STATUSES
        cat_filter = st.selectbox("Filter by Category", ["All"] + CATEGORIES)
        mode_filter = st.selectbox("Filter by Work Mode", ["All"] + WORK_MODES)
    with col2:
        status_filter = st.selectbox("Filter by Status", ["All"] + STATUSES)

    if st.button("📥 Prepare Export"):
        try:
            df_export = search_opportunities(
                category=cat_filter if cat_filter != "All" else "",
                work_mode=mode_filter if mode_filter != "All" else "",
                status=status_filter if status_filter != "All" else "",
            )
            st.info(f"{len(df_export)} records ready for export.")
            csv_bytes = dataframe_to_csv_bytes(df_export)
            st.download_button(
                label="⬇️ Download CSV",
                data=csv_bytes,
                file_name="opportunities_filtered_export.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"Export error: {e}")
