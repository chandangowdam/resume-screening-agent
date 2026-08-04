import os
import shutil
from flask import Flask, render_template, request
from parser import load_job_description,load_resumes
from scorer import calculate_similarity

app = Flask(__name__)
latest_results=[]

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    upload_folder = "uploads"
    jd_folder = os.path.join(upload_folder, "jd")
    resume_folder = os.path.join(upload_folder, "resumes")

    os.makedirs(jd_folder, exist_ok=True)
    os.makedirs(resume_folder, exist_ok=True)

    # Save Job Description
    jd = request.files["jd"]
    jd_path = os.path.join(jd_folder, jd.filename)
    jd.save(jd_path)

    # Save Resumes
    resumes = request.files.getlist("resumes")

    for resume in resumes:
        resume.save(os.path.join(resume_folder, resume.filename))

    # Load uploaded files
    job_description = load_job_description(jd_path)
    resume_data = load_resumes(resume_folder)

    # Calculate ranking
    results = calculate_similarity(job_description, resume_data)

    global latest_results
    latest_results = results

    return render_template("results.html", results=results)

@app.route("/candidate/<int:index>")
def candidate(index):

    candidate = latest_results[index]

    return render_template(
        "candidate.html",
        candidate=candidate
    )

if __name__ == "__main__":
    app.run(debug=True)