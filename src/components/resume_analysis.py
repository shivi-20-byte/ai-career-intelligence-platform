import streamlit as st


def render_resume_analysis(clean_text):

    st.markdown("## Resume Insights")

    word_count = len(clean_text.split())

    if word_count < 250:
        quality = "Weak"
    elif word_count < 500:
        quality = "Moderate"
    else:
        quality = "Strong"

    st.markdown(
        f"""
        <div style="
            background-color:#161B22;
            padding:20px;
            border-radius:15px;
            border:1px solid #30363D;
        ">

        <h3>Resume Quality Assessment</h3>

        <p><strong>Word Count:</strong> {word_count}</p>

        <p><strong>Resume Strength:</strong> {quality}</p>

        <p>
        Improve your resume by adding:
        quantified achievements,
        technical projects,
        deployment experience,
        and measurable business impact.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )