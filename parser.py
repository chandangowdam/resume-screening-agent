import os
import pdfplumber
from docx import Document


def read_txt(file_path):
    """Read text from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(file_path):
    """Read text from a PDF file."""
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
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