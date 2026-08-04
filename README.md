[6:16 pm, 04/08/2026] chandangowdam910: # Resume Screening Agent - Scoring Method

## Overview
The Resume Screening Agent ranks resumes based on similarity with the Job Description.

## Scoring Components

### 1. Skill Matching (50%)
Required skills from the Job Description are compared with candidate skills.

Formula:

Skill Score = (Matched Skills / Required Skills) × 50


### 2. Education Matching (20%)
Points are given when the candidate has a relevant degree.

Examples:
- BE
- B.Tech
- BCA
- MCA
- M.Tech


### 3. Experience Matching (10%)
Candidates get points if work experience is detected in the resume.


### 4. NLP Similarity Score (20%)
Sentence Transformer model:

all-MiniLM-L6-v2

is used to calculate semantic similarity between the resume and Job Description.


## ATS Score Formula

ATS Score =
Skill Score +
Education Score +
Experience Score +
NLP Similarity Score


## Recommendation

85+  : Shortlist

65-84 : Interview

Below 65 : Reject
[6:37 pm, 04/08/2026] chandangowdam910: # 🤖 Resume Screening Agent using NLP

## Overview

Resume Screening Agent is an AI-powered application that automatically evaluates and ranks resumes based on a given Job Description (JD).

The system uses Natural Language Processing (NLP) techniques to calculate resume relevance, extract candidate information, and generate an ordered shortlist.

---

## Features

✅ Upload Job Description

✅ Upload multiple resumes

✅ Supports:
- PDF
- DOCX
- TXT

✅ Extracts:
- Candidate Name
- Email
- Phone Number
- Skills
- Education
- Experience

✅ NLP-based resume matching

✅ ATS score calculation

✅ Candidate ranking

✅ Recommendation generation

✅ Export results:
- CSV
- JSON

✅ Handles 10+ resumes in a single run

---

## Technology Stack

### Backend
- Python
- Flask

### NLP / Machine Learning
- Sentence Transformers
- Cosine Similarity

### Libraries
- Pandas
- Scikit-learn
- PyMuPDF
- python-docx

### Frontend
- HTML
- CSS
- Bootstrap

---

## Project Architecture

resume-screening-agent|
|--apps.py
|--parser.py
|--scorer.py
|--skills.py
|--templates|--candidate.html
            |--index.html
            |--results.html
|--job description|--jd.txt
|--sample_resumes|--resume1.txt
                  |--chandan_resume.pdf
                  |--resume2.txt
                  |--resume3.txt
                  |--resume4.pdf
                  |--resume5.pdf
                  |--resume6.pdf
                  |--resume7.docx
                  |--resume8.docx
|--output|--ranked_candidates.csv
          |--ranked_candidates.json
|--SCORING_METHOD.md

