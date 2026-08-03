from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI model (loads once when program starts)
model = SentenceTransformer("all-MiniLM-L6-v2")


def calculate_similarity(job_description, resumes):
    """
    Compare each resume with the job description
    and return ranked results.
    """

    results = []

    # Convert JD into an embedding
    jd_embedding = model.encode(job_description)

    for file_name, resume_text in resumes.items():

        # Convert resume into an embedding
        resume_embedding = model.encode(resume_text)

        # Calculate similarity
        similarity = cosine_similarity(
            [jd_embedding],
            [resume_embedding]
        )[0][0]

        score = float(round(similarity * 100, 2))

        results.append({
            "Candidate": file_name,
            "Score": score
        })

    # Sort by highest score
    results = sorted(results,
                     key=lambda x: x["Score"],
                     reverse=True)

    return results