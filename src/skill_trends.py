import pandas as pd

# Load processed job-skill data
df = pd.read_csv("data/processed/jobs_skills_processed.csv")

# Convert posting_date to datetime
df["posting_date"] = pd.to_datetime(df["posting_date"])

# Explode skills list into separate rows
skills_df = df.explode("skills_list")

# Create month column for trend analysis
skills_df["month"] = skills_df["posting_date"].dt.to_period("M")

# Calculate skill demand trends
skill_trends = (
    skills_df
    .groupby(["month", "skills_list"])
    .size()
    .reset_index(name="count")
)

# Save trends
skill_trends.to_csv("data/processed/skill_trends.csv", index=False)

print("Skill trends saved to data/processed/skill_trends.csv")
