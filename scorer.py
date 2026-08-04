import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from skills import extract_skills, extract_education
from parser import extract_name, extract_email, extract_phone

# Load AI model (loads once when program starts)
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(job_description, resumes):

    results = []

    jd_embedding = model.encode(job_description)
    jd_skills = extract_skills(job_description)

    for file_name, resume_text in resumes.items():

        resume_embedding = model.encode(resume_text)


        education=extract_education(resume_text)

        candidate_name=extract_name(resume_text)

        email=extract_email(resume_text)

        phone=extract_phone(resume_text)

        education="Not Found"
        degrees=[
                    "BE",
                    "B.E",
                    "B.TECH",
                    "BTECH",
                    "BCA",
                    "MCA",
                    "M.TECH",
                    "MTECH",
                    "B.SC",
                    "BSC",
                    "M.SC",
                    "MSC",
                    "MBA"

                ]
        for degree in degrees:
            if degree.lower() in resume_text.lower():
                education=degree
                break

        experience = "Not Found"

        exp = re.search(r'(\d+)\s*(year|years)', resume_text, re.IGNORECASE)

        if exp:
            experience = exp.group()

       
        similarity = cosine_similarity(
        [jd_embedding],
        [resume_embedding]
    )[0][0]

        score = round(float(similarity * 100), 2)

        resume_skills = extract_skills(resume_text)

        matched = list(set(jd_skills) & set(resume_skills))
        missing = list(set(jd_skills) - set(resume_skills))

    # ATS Score Calculation
        skill_score = (len(matched) / len(jd_skills)) * 50
        education_score = 20 if education != "Not Found" else 0
        experience_score = 10 if experience != "Not Found" else 0
        ai_score = similarity * 20

        ats_score = float(round(
            skill_score + education_score + experience_score + ai_score,
            2
        ))

    # Recommendation based on ATS Score
        if ats_score >= 85:
            recommendation = "Shortlist"
        elif ats_score >= 65:
            recommendation = "Interview"
        else:
            recommendation = "Reject"

        resume_skills = extract_skills(resume_text)

        matched = list(set(jd_skills) & set(resume_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        if score >= 80:
            reason = "Excellent match for the job."
        elif score >= 60:
            reason = "Good match with some missing skills."
        else:
            reason = "Low match. Candidate lacks several required skills."

        print("Education Found:", education)
        results.append({
            "Candidate": candidate_name,
            "File": file_name,
            "Email": email,
            "Phone": phone,
            "Score": float(score),
            "Education":education,
            "Experience":experience,
            "Matched Skills": ", ".join(matched),
            "Missing Skills": ", ".join(missing),
            "Reason":reason,
            "Recommendation":recommendation,
            "ATS Match": float(ats_score),
        })

    results = sorted(results,
                     key=lambda x: x["Score"],
                     reverse=True)

    return results