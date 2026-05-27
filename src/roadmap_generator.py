print(" Learning Roadmap Generator\n")

# Input (from your best role output)
missing_skills = [
    'statistics', 'deep learning', 'nlp',
    'hadoop', 'scala', 'gcp',
    'spark', 'mathematics', 'azure', 'docker'
]

# Priority groups
FOUNDATION = {'statistics', 'mathematics'}
CORE_ML = {'machine learning', 'deep learning'}
SPECIALIZATION = {'nlp', 'computer vision'}
TOOLS = {'spark', 'hadoop', 'scala'}
CLOUD = {'aws', 'gcp', 'azure'}
MLOPS = {'docker', 'kubernetes'}

roadmap = {
    "Week 1-2 (Foundation)": [],
    "Week 3-4 (Core ML)": [],
    "Week 5-6 (Specialization)": [],
    "Week 7 (Tools)": [],
    "Week 8 (Cloud & Deployment)": []
}

for skill in missing_skills:
    if skill in FOUNDATION:
        roadmap["Week 1-2 (Foundation)"].append(skill)
    elif skill in CORE_ML:
        roadmap["Week 3-4 (Core ML)"].append(skill)
    elif skill in SPECIALIZATION:
        roadmap["Week 5-6 (Specialization)"].append(skill)
    elif skill in TOOLS:
        roadmap["Week 7 (Tools)"].append(skill)
    elif skill in CLOUD or skill in MLOPS:
        roadmap["Week 8 (Cloud & Deployment)"].append(skill)
    else:
        roadmap["Week 5-6 (Specialization)"].append(skill)

# Display roadmap
for phase, skills in roadmap.items():
    if skills:
        print(f"\n📅 {phase}")
        for s in skills:
            print(f"  - {s}")

print("\n🎯 Roadmap Complete!")