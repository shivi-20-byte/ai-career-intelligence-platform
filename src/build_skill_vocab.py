
import pandas as pd
import ast
import os

print(" Building Skill Vocabulary...\n")

# Load processed jobs data
path = "data/processed/jobs_skills_processed.csv"

if not os.path.exists(path):
    print(" ERROR: jobs_skills_processed.csv not found!")
    print("Run your skill_engineering.py first.")
    exit()

df = pd.read_csv(path)

all_skills = set()

for skills in df["skills_list"]:
    try:
        # Convert string list → actual list
        if isinstance(skills, str):
            skills = ast.literal_eval(skills)

        for skill in skills:
            all_skills.add(skill.lower().strip())

    except:
        continue

# Save vocabulary
os.makedirs("data/processed", exist_ok=True)

with open("data/processed/skill_vocab.txt", "w") as f:
    for skill in sorted(all_skills):
        f.write(skill + "\n")

print(" Skill vocabulary created!")
print(f"Total unique skills: {len(all_skills)}")
print("Saved at: data/processed/skill_vocab.txt")