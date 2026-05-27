import pdfplumber
import re
from wordsegment import load, segment
import os

load()


def extract_resume_text(pdf_path: str) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text


def smart_spacing_fix(text: str) -> str:
    words = []

    for token in text.split():
        if token.islower() and len(token) > 12:
            split_words = segment(token)
            words.extend(split_words)
        else:
            words.append(token)

    return " ".join(words)

def clean_resume_text(text: str) -> str:
   
    text = re.sub(r"\(cid:\d+\)", "", text)

    
    text = re.sub(r"\s+", " ", text)

    
    text = smart_spacing_fix(text)

    return text.strip()


def load_skill_vocab():
    path = "data/processed/skill_vocab.txt"

    if not os.path.exists(path):
        print("ERROR: skill_vocab.txt not found!")
        print("Run: python -m src.build_skill_vocab")
        return set()

    with open(path, "r") as f:
        return set([line.strip() for line in f.readlines()])


def extract_skills_from_text(text: str, skill_vocab):
    text = text.lower()
    extracted = set()

    for skill in skill_vocab:
        if skill in text:
            extracted.add(skill)

    return list(extracted)


if __name__ == "__main__":
    print(" Resume Parser Started...\n")

    resume_path = "data/raw/Data Science Resume.pdf"

    if not os.path.exists(resume_path):
        print(" ERROR: Resume file not found!")
        print("Check path:", resume_path)
        exit()

    print(" Reading resume...")
    raw_text = extract_resume_text(resume_path)

    print(" Cleaning text...")
    clean_text = clean_resume_text(raw_text)

    print(" Loading skill vocabulary...")
    skill_vocab = load_skill_vocab()

    if not skill_vocab:
        print(" No skill vocabulary found. Exiting...")
        exit()

    print(" Extracting skills...")
    skills = extract_skills_from_text(clean_text, skill_vocab)

    print("\n FINAL OUTPUT:")
    print("Extracted Skills:")
    print(skills)

    print("\n🎉 Done!")