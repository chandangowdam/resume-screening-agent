import os
import re
import fitz
from docx import Document


def read_txt(file_path):
    """Read text from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(file_path):
    text = ""

    doc = fitz.open(file_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text


def read_docx(file_path):
    """Read text from a DOCX file."""
    doc = Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text


def load_resumes(folder_path):
    """Load all resumes from a folder."""
    resumes = {}

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file.endswith(".txt"):
            resumes[file] = read_txt(file_path)

        elif file.endswith(".pdf"):
            resumes[file] = read_pdf(file_path)

        elif file.endswith(".docx"):
            resumes[file] = read_docx(file_path)

    return resumes


def load_job_description(jd_path):
    """Load the job description."""
    return read_txt(jd_path)


def extract_name(text):
    lines = text.split("\n")

    for line in lines:
        if line.lower().startswith("name:"):
            return line.split(":", 1)[1].strip()

    return "Unknown"


def extract_email(text):
    match = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
    if match:
        return match.group()
    return "Not Found"

def extract_phone(text):
    phone = re.search(r'(\+91[\s-]?)?[6-9]\d{9}', text)

    if phone:
        return phone.group()

    return "Not Found"

