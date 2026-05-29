import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h1 style='font-size:28px; margin-bottom:0;'>
            Career Intelligence
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style='color:gray; margin-top:0;'>
            AI-Powered Job Market Analytics Platform
            </p>
            """,
            unsafe_allow_html=True
        )

        st.markdown("---")

        st.markdown(
            """
            ### Platform Features

            - Resume Intelligence
            - Semantic Job Matching
            - Skill Gap Analysis
            - Market Trend Analytics
            - Personalized Learning Roadmap
            - ATS Optimization Insights
            """
        )

        st.markdown("---")

        st.markdown(
            """
            ### Supported Domains

            - Data & AI
            - Software Engineering
            - Cloud & DevOps
            - Cybersecurity
            - Product Management
            - Business Analytics
            """
        )

        st.markdown("---")

        st.caption(
            "Built using NLP, Sentence Transformers, Machine Learning, and Streamlit"
        )