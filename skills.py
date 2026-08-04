import re

SKILLS = [
    "Python", "Java", "C", "C++",
    "HTML", "CSS", "JavaScript",
    "Django", "Flask", "SQL",
    "MySQL", "SQLite", "Git",
    "GitHub", "REST API", "Bootstrap"
]

def extract_skills(text):
    found = []

    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill) + r"\b", text, re.IGNORECASE):
            found.append(skill)

    return found

EDUCATION = [
    "BE",
    "B.E",
    "BTech",
    "B.Tech",
    "BCA",
    "MCA",
    "M.Tech",
    "MBA"
]

def extract_education(text):
    text = text.upper()

    for edu in EDUCATION:
        if edu.upper() in text:
            return edu

    return "Not Found"

def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        if line.lower().startswith("name"):
            parts = line.split(":", 1)
            if len(parts) > 1:
                return parts[1].strip()

    return "Unknown Candidate"