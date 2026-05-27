import streamlit as st
import pandas as pd
import ast
import pdfplumber
import re
from wordsegment import load, segment

# Load wordsegment
load()

st.set_page_config(page_title="AI Skill Gap Analyzer", layout="wide")

st.title("🧠 AI-Powered Job Market Skill Gap Analyzer")

# -----------------------------
# Helper Functions
# -----------------------------

def extract_resume_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def smart_spacing_fix(text):
    words = []
    for token in text.split():
        if token.islower() and len(token) > 12:
            words.extend(segment(token))
        else:
            words.append(token)
    return " ".join(words)


def clean_resume_text(text):
    text = re.sub(r"\(cid:\d+\)", "", text)
    text = re.sub(r"\s+", " ", text)
    return smart_spacing_fix(text)


def load_skill_vocab():
    with open("data/processed/skill_vocab.txt", "r") as f:
        return set([line.strip() for line in f.readlines()])


def extract_skills(text, vocab):
    text = text.lower()
    return list(set([skill for skill in vocab if skill in text]))


# -----------------------------
# Skill Weighting
# -----------------------------
HIGH_VALUE = {"python", "sql", "machine learning", "deep learning", "nlp", "statistics"}
MEDIUM_VALUE = {"tensorflow", "pytorch", "pandas", "numpy", "data visualization"}

def get_weight(skill):
    if skill in HIGH_VALUE:
        return 3
    elif skill in MEDIUM_VALUE:
        return 2
    return 1


# -----------------------------
# UI Upload
# -----------------------------
uploaded_file = st.file_uploader("📄 Upload Your Resume (PDF)", type=["pdf"])

if uploaded_file:
    st.success("Resume uploaded successfully!")

    # Extract text
    raw_text = extract_resume_text(uploaded_file)
    clean_text = clean_resume_text(raw_text)

    # Load vocab & extract skills
    vocab = load_skill_vocab()
    user_skills = extract_skills(clean_text, vocab)

    st.subheader("✅ Extracted Skills")
    st.write(user_skills)

    # Load job data
    df = pd.read_csv("data/processed/jobs_with_clusters.csv")

    def safe_eval(x):
        try:
            return ast.literal_eval(x)
        except:
            return []

    df["skills_list"] = df["skills_list"].apply(safe_eval)

    # Aggregate clusters
    cluster_skills = {}
    for cluster in df["role_cluster"].unique():
        skills = df[df["role_cluster"] == cluster]["skills_list"]
        all_skills = set()
        for s in skills:
            all_skills.update(s)
        cluster_skills[cluster] = all_skills

    # Compute best role
    user_skills_set = set(user_skills)
    results = []

    for cluster, skills in cluster_skills.items():
        match = user_skills_set.intersection(skills)
        missing = skills - user_skills_set

        matched_weight = sum(get_weight(s) for s in match)
        total_weight = sum(get_weight(s) for s in skills)

        score = (matched_weight / total_weight * 100) if total_weight else 0

        results.append((cluster, score, match, missing))

    best = sorted(results, key=lambda x: x[1], reverse=True)[0]

    # Display results
    st.subheader("🎯 Best Role Match")
    st.write(f"Role Cluster: {best[0]}")
    st.write(f"Fit Score: {round(best[1],2)}%")

    st.subheader("✅ Your Strengths")
    st.write(list(best[2]))

    st.subheader("🚨 Skills To Learn")
    st.write(list(best[3])[:10])

    # -----------------------------
    # Roadmap
    # -----------------------------
    st.subheader("🗺️ Learning Roadmap")

    missing_skills = list(best[3])[:10]

    roadmap = {
        "Week 1-2 (Foundation)": [],
        "Week 3-4 (Core ML)": [],
        "Week 5-6 (Specialization)": [],
        "Week 7 (Tools)": [],
        "Week 8 (Cloud)": []
    }

    for skill in missing_skills:
        if skill in {"statistics", "mathematics"}:
            roadmap["Week 1-2 (Foundation)"].append(skill)
        elif skill in {"deep learning", "machine learning"}:
            roadmap["Week 3-4 (Core ML)"].append(skill)
        elif skill in {"nlp", "computer vision"}:
            roadmap["Week 5-6 (Specialization)"].append(skill)
        elif skill in {"spark", "hadoop"}:
            roadmap["Week 7 (Tools)"].append(skill)
        else:
            roadmap["Week 8 (Cloud)"].append(skill)

    for phase, skills in roadmap.items():
        if skills:
            st.write(f"### {phase}")
            st.write(skills)