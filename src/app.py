import streamlit as st
import pandas as pd
import pdfplumber
import re

# -----------------------------
# COMPONENTS
# -----------------------------
from components.sidebar import render_sidebar
from components.metrics import render_metrics
from components.recommendations import render_recommendations
from components.charts import render_skill_chart
from components.roadmap import render_roadmap
from components.resume_analysis import render_resume_analysis

# -----------------------------
# SERVICES
# -----------------------------
from services.semantic_engine import (
    get_top_recommendations
)

from services.skill_engine import (
    compute_skill_analysis
)

from services.trend_engine import (
    load_skill_trends
)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Career Intelligence Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(
    """
    <style>

    .main {
        background-color: #0E1117;
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 0;
    }

    .hero-subtitle {
        color: #8B949E;
        font-size: 18px;
        margin-top: 0;
    }

    .section-divider {
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    .skill-pill {
        display:inline-block;
        background:#1F2937;
        padding:8px 14px;
        border-radius:20px;
        margin:5px;
        border:1px solid #30363D;
        font-size:14px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# SIDEBAR
# -----------------------------
render_sidebar()

# -----------------------------
# HERO SECTION
# -----------------------------
st.markdown(
    """
    <div class='hero-title'>
    AI-Powered Career Intelligence Platform
    </div>

    <div class='hero-subtitle'>
    Semantic Resume Analysis • Job Market Intelligence • Skill Gap Analytics
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# -----------------------------
# HELPERS
# -----------------------------
SKILLS = [
    "python", "sql", "machine learning",
    "deep learning", "tensorflow",
    "pytorch", "nlp", "docker",
    "aws", "azure", "gcp",
    "pandas", "numpy", "power bi",
    "tableau", "react", "django",
    "fastapi", "kubernetes",
    "statistics", "communication"
]


def extract_resume_text(file):

    text = ""

    with pdfplumber.open(file) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def clean_text(text):

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9+#. ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text


def extract_skills(text):

    skills_found = []

    for skill in SKILLS:

        if skill in text:
            skills_found.append(skill)

    return list(set(skills_found))


# -----------------------------
# MAIN FLOW
# -----------------------------
if uploaded_file:

    # -----------------------------
    # PROCESS RESUME
    # -----------------------------
    with st.spinner("Analyzing resume..."):

        raw_text = extract_resume_text(
            uploaded_file
        )

        clean_resume = clean_text(raw_text)

        user_skills = extract_skills(
            clean_resume
        )

    # -----------------------------
    # LOAD AI RESULTS
    # -----------------------------
    skill_analysis = compute_skill_analysis(
        user_skills
    )

    top_jobs = get_top_recommendations()

    trend_df = load_skill_trends()

    # -----------------------------
    # METRICS
    # -----------------------------
    render_metrics(
        fit_score=skill_analysis["fit_score"],
        matched_skills=len(
            skill_analysis["matched_skills"]
        ),
        missing_skills=len(
            skill_analysis["missing_skills"]
        ),
        total_jobs=len(top_jobs)
    )

    st.markdown("---")

    # -----------------------------
    # EXTRACTED SKILLS
    # -----------------------------
    st.markdown("## Resume Skills")

    for skill in user_skills:

        st.markdown(
            f"""
            <span class='skill-pill'>
            {skill}
            </span>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -----------------------------
    # JOB RECOMMENDATIONS
    # -----------------------------
    render_recommendations(
        top_jobs
    )

    st.markdown("---")

    # -----------------------------
    # MARKET TRENDS
    # -----------------------------
    render_skill_chart(
        trend_df
    )

    st.markdown("---")

    # -----------------------------
    # LEARNING ROADMAP
    # -----------------------------
    render_roadmap(
        skill_analysis["missing_skills"][:12]
    )

    st.markdown("---")

    # -----------------------------
    # RESUME ANALYSIS
    # -----------------------------
    render_resume_analysis(
        clean_resume
    )

    st.markdown("---")

    # -----------------------------
    # RAW TEXT
    # -----------------------------
    with st.expander(
        "View Parsed Resume Text"
    ):
        st.write(clean_resume)

else:

    st.info(
        "Upload a resume PDF to begin analysis."
    )
