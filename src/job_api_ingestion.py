import requests
import pandas as pd
import time
import os
from dotenv import load_dotenv

print("Starting Job API Ingestion Pipeline...\n")

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")

if not API_KEY:
    raise ValueError("RAPIDAPI_KEY not found in .env file")


# -----------------------------
# API Configuration
# -----------------------------
url = "https://jsearch.p.rapidapi.com/search"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}


# -----------------------------
# Job Roles To Fetch
# -----------------------------
roles = [
    "Data Scientist",
    "Machine Learning Engineer",
    "Software Engineer",
    "Backend Developer",
    "Frontend Developer",
    "DevOps Engineer",
    "Cloud Engineer",
    "Cybersecurity Analyst",
    "Business Analyst",
    "Product Manager",
    "UI UX Designer"
]


# -----------------------------
# Store All Jobs
# -----------------------------
all_jobs = []


# -----------------------------
# Fetch Jobs Role-by-Role
# -----------------------------
for role in roles:

    print(f"Fetching jobs for: {role}")

    querystring = {
        "query": role,
        "page": "1",
        "num_pages": "1",
        "date_posted": "all"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=querystring
        )

        data = response.json()

        jobs = data.get("data", [])

        print(f"Fetched {len(jobs)} jobs")

        for job in jobs:

            all_jobs.append({
                "job_title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_city"),
                "country": job.get("job_country"),
                "employment_type": job.get("job_employment_type"),
                "remote": job.get("job_is_remote"),
                "description": job.get("job_description"),
                "apply_link": job.get("job_apply_link"),
                "posted_date": job.get("job_posted_at_datetime_utc")
            })

        # avoid hitting rate limits
        time.sleep(1)

    except Exception as e:
        print(f"Error fetching {role}: {e}")


# -----------------------------
# Convert To DataFrame
# -----------------------------
df = pd.DataFrame(all_jobs)

print("\nTotal Jobs Collected:", len(df))


# -----------------------------
# Remove duplicates
# -----------------------------
df.drop_duplicates(
    subset=["job_title", "company"],
    inplace=True
)

print("After removing duplicates:", len(df))


# -----------------------------
# Save Raw Dataset
# -----------------------------
output_path = "data/raw/api_jobs.csv"

df.to_csv(output_path, index=False)

print(f"\nDataset saved to:\n{output_path}")

print("\nPipeline Completed Successfully!")