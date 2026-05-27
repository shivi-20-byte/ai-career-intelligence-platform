# src/skill_taxonomy.py

SKILL_TAXONOMY = {
    "programming": ["python", "r", "java", "scala"],
    "data": ["sql", "pandas", "numpy"],
    "ml": ["scikit-learn", "xgboost", "lightgbm"],
    "deep_learning": ["tensorflow", "pytorch"],
    "nlp": ["bert", "spacy", "transformers"],
    "cloud": ["aws", "gcp", "azure"],
    "mlops": ["docker", "kubernetes"]
}

def map_skill_category(skill: str) -> str:
    """
    Maps a skill to a high-level category using the skill taxonomy.
    """
    skill = skill.lower().strip()
    
    for category, skills in SKILL_TAXONOMY.items():
        if skill in skills:
            return category
            
    return "other"

