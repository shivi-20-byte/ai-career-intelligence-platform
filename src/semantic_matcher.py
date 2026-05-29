import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pdfplumber
import re

print("Starting Semantic Matching Engine...\n")

# -----------------------------
# LOAD MODEL
# -----------------------------
print("Loading AI embedding model...")

model = SentenceTransformer(
    'sentence-transformers/all-MiniLM-L6-v2'
)

print("Model loaded successfully!\n")


# -----------------------------
# LOAD JOB DATA
# -----------------------------
df = pd.read_csv(
    "data/processed/jobs_processed.csv"
)

print("Jobs Loaded:", len(df))


# -----------------------------
# LOAD RESUME
# -----------------------------
RESUME_PATH = "data/raw/resume.pdf"


def extract_resume_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


print("\nReading resume...")

resume_text = extract_resume_text(RESUME_PATH)

resume_text = re.sub(r"\s+", " ", resume_text)

print("Resume loaded!")


# -----------------------------
# EMBEDDINGS
# -----------------------------
print("\nGenerating embeddings...")

job_descriptions = df["clean_description"].fillna("").tolist()

job_embeddings = model.encode(
    job_descriptions,
    show_progress_bar=True
)

resume_embedding = model.encode([resume_text])

print("Embeddings generated!")


# -----------------------------
# SIMILARITY CALCULATION
# -----------------------------
print("\nCalculating semantic similarity...")

similarities = cosine_similarity(
    resume_embedding,
    job_embeddings
)[0]

df["similarity_score"] = similarities


# -----------------------------
# TOP MATCHES
# -----------------------------
top_matches = df.sort_values(
    by="similarity_score",
    ascending=False
).head(10)


# -----------------------------
# DISPLAY RESULTS
# -----------------------------
print("\nTOP JOB MATCHES:\n")

for i, row in top_matches.iterrows():

    print("=" * 60)

    print(f"Job Title: {row['job_title']}")
    print(f"Company: {row['company']}")
    print(f"Location: {row['location']}")
    print(f"Similarity Score: {round(row['similarity_score']*100, 2)}%")

    print("\nSkills Found:")
    print(row["skills_extracted"])

    print("\n")


# -----------------------------
# SAVE RESULTS
# -----------------------------
output_path = "data/processed/job_matches.csv"

top_matches.to_csv(output_path, index=False)

print("=" * 60)
print("\nTop matches saved successfully!")
print(f"Saved to: {output_path}")

print("\nSemantic Matching Pipeline Completed!")