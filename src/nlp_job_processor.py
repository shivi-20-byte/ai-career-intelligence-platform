import pandas as pd
import re
from collections import Counter

print("Starting NLP Job Processing Pipeline...\n")

# -----------------------------
# Load Job Data
# -----------------------------
df = pd.read_csv("data/raw/api_jobs.csv")

print("Jobs Loaded:", len(df))


# -----------------------------
# Skill Vocabulary
# -----------------------------
SKILLS = [
    # Programming
    "python", "java", "c++", "javascript", "typescript",
    "sql", "scala", "r",

    # Data
    "pandas", "numpy", "matplotlib", "power bi",
    "tableau", "excel",

    # ML/AI
    "machine learning", "deep learning",
    "tensorflow", "pytorch", "scikit-learn",
    "nlp", "computer vision",

    # Cloud
    "aws", "azure", "gcp",

    # Big Data
    "spark", "hadoop", "kafka",

    # DevOps
    "docker", "kubernetes", "jenkins",

    # Web
    "react", "node.js", "fastapi", "django",

    # Cybersecurity
    "penetration testing", "network security",

    # Soft Skills
    "communication", "leadership",
    "problem solving"
]


# -----------------------------
# Text Cleaning
# -----------------------------
def clean_text(text):

    if pd.isna(text):
        return ""

    text = text.lower()

    text = re.sub(r"[^a-zA-Z0-9+#. ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text


# -----------------------------
# Extract Skills
# -----------------------------
def extract_skills(text):

    found_skills = []

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))


# -----------------------------
# Apply Processing
# -----------------------------
print("\nCleaning descriptions...")

df["clean_description"] = df["description"].apply(clean_text)

print("Extracting skills...")

df["skills_extracted"] = df["clean_description"].apply(
    extract_skills
)

# -----------------------------
# Skill Frequency Analysis
# -----------------------------
all_skills = []

for skills in df["skills_extracted"]:
    all_skills.extend(skills)

skill_counts = Counter(all_skills)

skill_df = pd.DataFrame(
    skill_counts.items(),
    columns=["skill", "count"]
)

skill_df = skill_df.sort_values(
    by="count",
    ascending=False
)

# -----------------------------
# Save Processed Data
# -----------------------------
processed_path = "data/processed/jobs_processed.csv"

df.to_csv(processed_path, index=False)

print("\nProcessed dataset saved!")

# -----------------------------
# Save Skill Trends
# -----------------------------
trend_path = "data/processed/skill_trends.csv"

skill_df.to_csv(trend_path, index=False)

print("Skill trends saved!")

# -----------------------------
# Display Top Skills
# -----------------------------
print("\nTop In-Demand Skills:\n")

print(skill_df.head(15))

print("\nPipeline Completed Successfully!")