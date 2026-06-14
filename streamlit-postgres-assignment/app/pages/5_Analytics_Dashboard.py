import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from queries import (get_kpis, get_category_distribution, get_work_mode_distribution,
                     get_status_distribution, get_salary_by_category, get_top_cities,
                     get_experience_distribution)

if not st.session_state.get("logged_in"):
    st.warning("Please log in first.")
    st.stop()

st.title("📊 Analytics Dashboard")

try:
    # KPIs
    kpis = get_kpis()
    st.subheader("📌 Key Performance Indicators")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    c1.metric("Total Opportunities", kpis["total"])
    c2.metric("Open", kpis["open"])
    c3.metric("Companies", kpis["companies"])
    c4.metric("Avg Salary (PKR)", f"{int(kpis['avg_salary'] or 0):,}")
    c5.metric("⏰ Closing Soon", kpis["deadline_soon"])
    c6.metric("❌ Expired", kpis["expired"])

    st.divider()

    # Charts row 1
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📂 By Category")
        df_cat = get_category_distribution()
        fig = px.bar(df_cat, x="category", y="count", color="category",
                     color_discrete_sequence=px.colors.qualitative.Set2)
        fig.update_layout(showlegend=False, xaxis_title="", yaxis_title="Count")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("🌐 Work Mode Distribution")
        df_mode = get_work_mode_distribution()
        fig2 = px.pie(df_mode, names="work_mode", values="count",
                      color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig2, use_container_width=True)

    # Charts row 2
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("📋 Status Breakdown")
        df_status = get_status_distribution()
        colors = {"Open": "#2ecc71", "Closed": "#e74c3c", "Expired": "#95a5a6", "Shortlisted": "#3498db"}
        fig3 = px.pie(df_status, names="status", values="count",
                      color="status", color_discrete_map=colors)
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("🏙️ Top Cities")
        df_cities = get_top_cities()
        fig4 = px.bar(df_cities, x="count", y="city", orientation="h",
                      color="count", color_continuous_scale="Blues")
        fig4.update_layout(yaxis_title="", xaxis_title="Count", showlegend=False)
        st.plotly_chart(fig4, use_container_width=True)

    # Charts row 3
    col5, col6 = st.columns(2)
    with col5:
        st.subheader("💰 Avg Salary by Category (PKR)")
        df_sal = get_salary_by_category()
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(name="Avg Min", x=df_sal["category"], y=df_sal["avg_min"], marker_color="#3498db"))
        fig5.add_trace(go.Bar(name="Avg Max", x=df_sal["category"], y=df_sal["avg_max"], marker_color="#e74c3c"))
        fig5.update_layout(barmode="group", xaxis_title="", yaxis_title="PKR")
        st.plotly_chart(fig5, use_container_width=True)

    with col6:
        st.subheader("👤 Experience Level Distribution")
        df_exp = get_experience_distribution()
        fig6 = px.funnel(df_exp, x="count", y="experience_level",
                         color_discrete_sequence=["#9b59b6", "#3498db", "#2ecc71"])
        st.plotly_chart(fig6, use_container_width=True)

except Exception as e:
    st.error(f"Error loading analytics: {e}")
