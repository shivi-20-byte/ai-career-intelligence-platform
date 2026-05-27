import pandas as pd
import ast

print(" Skill Gap Analysis Started...\n")

# -----------------------------
# 1. Load job data with clusters
# -----------------------------
df = pd.read_csv("data/processed/jobs_with_clusters.csv")


# Convert skills_list from string → list safely
def safe_eval(x):
    try:
        return ast.literal_eval(x)
    except:
        return []


df["skills_list"] = df["skills_list"].apply(safe_eval)


# -----------------------------
# 2. Load user skills
# -----------------------------
user_skills = [
    'data visualization',
    'tensorflow',
    'pytorch',
    'python',
    'sql',
    'git'
]

user_skills = set([s.lower() for s in user_skills])

print(" Your Skills:", user_skills, "\n")


# -----------------------------
# 3. Skill Importance Weights
# -----------------------------
HIGH_VALUE = {
    "python", "sql", "machine learning", "deep learning",
    "nlp", "statistics", "data science"
}

MEDIUM_VALUE = {
    "tensorflow", "pytorch", "scikit-learn",
    "pandas", "numpy", "data visualization"
}


def get_skill_weight(skill):
    if skill in HIGH_VALUE:
        return 3
    elif skill in MEDIUM_VALUE:
        return 2
    else:
        return 1


# -----------------------------
# 4. Aggregate skills per role cluster
# -----------------------------
cluster_skills = {}

for cluster in df["role_cluster"].unique():
    skills_series = df[df["role_cluster"] == cluster]["skills_list"]

    all_skills = set()
    for skill_list in skills_series:
        all_skills.update(skill_list)

    cluster_skills[cluster] = all_skills


# -----------------------------
# 5. Compute role fit (SMART)
# -----------------------------
results = []

for cluster, skills in cluster_skills.items():
    match = user_skills.intersection(skills)
    missing = skills - user_skills

    # Weighted scoring
    matched_weight = sum(get_skill_weight(s) for s in match)
    total_weight = sum(get_skill_weight(s) for s in skills)

    fit_score = (matched_weight / total_weight * 100) if total_weight else 0

    # Sort missing skills by importance
    missing_sorted = sorted(
        list(missing),
        key=lambda x: get_skill_weight(x),
        reverse=True
    )

    results.append({
        "role_cluster": cluster,
        "fit_score": round(fit_score, 2),
        "matched_skills": list(match),
        "missing_skills": missing_sorted[:10]  # top 10 priority
    })


# -----------------------------
# 6. Sort by best fit
# -----------------------------
results = sorted(results, key=lambda x: x["fit_score"], reverse=True)

# -----------------------------
# 7. Show BEST role only
# -----------------------------
best_role = results[0]

print("\n🏆 BEST ROLE MATCH")
print(f" Role Cluster: {best_role['role_cluster']}")
print(f" Fit Score: {best_role['fit_score']}%")
print(f" Your Strengths: {best_role['matched_skills']}")
print(f" Skills To Learn: {best_role['missing_skills']}")