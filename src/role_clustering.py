import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans

# Load processed data
df = pd.read_csv("data/processed/jobs_skills_processed.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings from synthetic descriptions
embeddings = model.encode(
    df["synthetic_description"].tolist(),
    show_progress_bar=True
)

# Cluster jobs into role groups
kmeans = KMeans(n_clusters=4, random_state=42)
df["role_cluster"] = kmeans.fit_predict(embeddings)

# Save clustered data
df.to_csv("data/processed/jobs_with_clusters.csv", index=False)

print("Jobs with role clusters saved to data/processed/jobs_with_clusters.csv")
