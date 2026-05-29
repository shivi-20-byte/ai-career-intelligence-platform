import streamlit as st


def render_metrics(
    fit_score,
    matched_skills,
    missing_skills,
    total_jobs
):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Role Fit Score",
            value=f"{fit_score}%"
        )

    with col2:
        st.metric(
            label="Matched Skills",
            value=matched_skills
        )

    with col3:
        st.metric(
            label="Skill Gaps",
            value=missing_skills
        )

    with col4:
        st.metric(
            label="Jobs Analyzed",
            value=total_jobs
        )