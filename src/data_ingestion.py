import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/jobs.csv")

# Basic inspection
print(df.head())
print(df.columns)
print(df.info())
