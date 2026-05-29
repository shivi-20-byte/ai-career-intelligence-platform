import streamlit as st


def render_recommendations(top_jobs):

    st.markdown("## Recommended Roles")

    for _, row in top_jobs.iterrows():

        st.markdown(
            f"""
            <div style="
                background-color:#161B22;
                padding:20px;
                border-radius:15px;
                margin-bottom:15px;
                border:1px solid #30363D;
            ">

            <h3 style='margin-bottom:5px;'>
            {row['job_title']}
            </h3>

            <p style='color:#8B949E; margin-top:0;'>
            {row['company']} • {row['location']}
            </p>

            <p>
            <strong>Semantic Match:</strong>
            {round(row['similarity_score'] * 100, 2)}%
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )