import pandas as pd


def load_skill_trends():

    df = pd.read_csv(
        "data/processed/skill_trends.csv"
    )

    return df


def get_top_skills(top_n=10):

    df = load_skill_trends()

    return df.head(top_n)