import pandas as pd


def load_semantic_matches():

    df = pd.read_csv(
        "data/processed/job_matches.csv"
    )

    return df


def get_top_recommendations(top_n=5):

    df = load_semantic_matches()

    top_jobs = df.sort_values(
        by="similarity_score",
        ascending=False
    ).head(top_n)

    return top_jobs