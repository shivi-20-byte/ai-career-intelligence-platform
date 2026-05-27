import pandas as pd
import re
from skills_taxonomy import map_skill_category

def normalize_skills(skill_str):
    if pd.isna(skill_str):
        return []
    
    skill_str = skill_str.lower()
    skill_str = re.sub(r"[\[\]']", "", skill_str)
    skills = re.split(r",|\|", skill_str)
    
    return [s.strip() for s in skills if len(s.strip()) > 1]

# Load data
df = pd.read_csv("data/raw/jobs.csv")

# Normalize skills
df["skills_list"] = df["required_skills"].apply(normalize_skills)

# Map skill categories
df["skill_categories"] = df["skills_list"].apply(
    lambda skills: list(set(map(map_skill_category, skills)))
)

# ✅ Synthetic Job Description (Feature for embeddings)
df["synthetic_description"] = (
    df["job_title"].astype(str) + " | " +
    df["industry"].astype(str) + " | " +
    df["required_skills"].astype(str)
)

# Save processed data
df.to_csv("data/processed/jobs_skills_processed.csv", index=False)
