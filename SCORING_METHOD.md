# Resume Screening Agent - Scoring Method

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