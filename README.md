# AI-Powered Job Market Intelligence & Skill Gap Analyzer

An AI-driven platform that analyzes real-time job market demand, extracts in-demand skills using NLP, semantically matches resumes with job roles, and generates personalized learning roadmaps.

Built with modern AI/NLP pipelines, semantic embeddings, and interactive analytics dashboards.

---

## Overview

This project helps students and professionals identify:

* Which skills are currently in demand
* How well their resume matches market requirements
* Missing skills for target roles
* Recommended career paths
* Personalized upskilling roadmaps

Unlike traditional keyword-based systems, this platform uses semantic AI matching with Sentence Transformers to understand contextual similarity between resumes and job descriptions.

---

## Key Features

### Real-Time Job Market Data

* Fetches live job postings using JSearch API
* Supports multiple domains:

  * Data Science
  * Software Engineering
  * Cloud & DevOps
  * Cybersecurity
  * Product Management
  * Business Analytics

### NLP Skill Extraction

* Cleans and processes raw job descriptions
* Extracts technologies, tools, frameworks, and soft skills
* Builds market-wide skill trend analytics

### Semantic Resume Matching

* Uses Sentence Transformers embeddings
* Computes contextual similarity between resume and jobs
* Generates intelligent job recommendations

### Skill Gap Analysis

* Identifies missing high-demand skills
* Calculates role-fit score
* Detects resume strengths and weaknesses

### Personalized Learning Roadmap

* Generates structured learning paths
* Prioritizes foundational and advanced skills

### Interactive Dashboard

* Modern Streamlit-based analytics dashboard
* Market trend visualizations
* AI-powered recommendation interface

---

## Tech Stack

### Programming & Data

* Python
* Pandas
* NumPy

### AI / NLP

* Sentence Transformers
* Scikit-learn
* NLP preprocessing pipelines

### Visualization

* Streamlit
* Plotly

### Data Engineering

* REST APIs
* JSearch API
* JSON ingestion pipelines

### Resume Processing

* pdfplumber
* Regex-based NLP cleaning

---

## Project Architecture

```bash
job-market-intelligence/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── app.py
│   │
│   ├── components/
│   ├── services/
│   │
│   ├── job_api_ingestion.py
│   ├── nlp_job_processor.py
│   └── semantic_matcher.py
│
├── requirements.txt
├── README.md
└── .env
```

---

## Workflow Pipeline

```text
Job API
   ↓
Data Ingestion
   ↓
NLP Processing
   ↓
Skill Extraction
   ↓
Semantic Embeddings
   ↓
Resume Matching
   ↓
Skill Gap Analysis
   ↓
Dashboard Visualization
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/shivi-20-byte/job-market-intelligence.git
cd job-market-intelligence
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## API Setup

Create a `.env` file:

```env
RAPIDAPI_KEY=your_api_key_here
```

Get API key from:
https://rapidapi.com

---

## Run Data Pipeline

### 1. Fetch Job Data

```bash
python -m src.job_api_ingestion
```

### 2. Process NLP Data

```bash
python -m src.nlp_job_processor
```

### 3. Generate Semantic Matches

```bash
python -m src.semantic_matcher
```

### 4. Launch Dashboard

```bash
streamlit run src/app.py
```

---

## Dashboard Features

* Resume upload and parsing
* Semantic job recommendations
* Skill demand visualization
* Skill gap analytics
* Personalized roadmap generation
* Resume quality insights

---

## Future Improvements

* Advanced semantic skill graph
* Career trajectory prediction
* Salary intelligence
* Location-based hiring analytics
* FastAPI backend
* User authentication
* Cloud deployment
* Recruiter analytics mode

---

## Screenshots

Add dashboard screenshots here after UI polishing.

Example:

```md
![Dashboard](assets/screenshots/dashboard.png)
```

---

## Author

### Shivanshi Goyal

* GitHub: https://github.com/shivi-20-byte
* LinkedIn: https://linkedin.com/in/shivanshi201420

---

## License

This project is intended for educational and portfolio purposes.

---

#  If You Like This Project

Give it a star ⭐ on GitHub!
