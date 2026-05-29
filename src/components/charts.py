import streamlit as st
import plotly.express as px


def render_skill_chart(skill_df):

    st.markdown("## Market Skill Demand")

    top_skills = skill_df.head(10)

    fig = px.bar(
        top_skills,
        x="count",
        y="skill",
        orientation="h",
        template="plotly_dark",
        height=500
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending")
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )