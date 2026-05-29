import pandas as pd
import ast


HIGH_VALUE = {
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "statistics"
}

MEDIUM_VALUE = {
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "docker",
    "aws"
}


def get_weight(skill):

    if skill in HIGH_VALUE:
        return 3

    elif skill in MEDIUM_VALUE:
        return 2

    return 1


def load_processed_jobs():

    df = pd.read_csv(
        "data/processed/jobs_processed.csv"
    )

    return df


def parse_skill_list(skill_string):

    try:
        return ast.literal_eval(skill_string)

    except:
        return []


def compute_skill_analysis(user_skills):

    df = load_processed_jobs()

    df["skills_extracted"] = df[
        "skills_extracted"
    ].apply(parse_skill_list)

    all_market_skills = []

    for skills in df["skills_extracted"]:

        all_market_skills.extend(skills)

    market_skills = set(all_market_skills)

    user_skills = set(user_skills)

    matched = user_skills.intersection(
        market_skills
    )

    missing = market_skills - user_skills

    matched_weight = sum(
        get_weight(skill)
        for skill in matched
    )

    total_weight = sum(
        get_weight(skill)
        for skill in market_skills
    )

    fit_score = round(
        (matched_weight / total_weight) * 100,
        2
    )

    return {
        "fit_score": fit_score,
        "matched_skills": list(matched),
        "missing_skills": list(missing)
    }