import os
import json
import pandas as pd

from parser import load_resumes, load_job_description
from scorer import calculate_similarity


def main():
    # File paths
    jd_path = "job_description/jd.txt"
    resume_folder = "resumes"

    # Load data
    print("Loading Job Description...")
    job_description = load_job_description(jd_path)

    print("Loading Resumes...")
    resumes = load_resumes(resume_folder)

    # Calculate scores
    print("Calculating Similarity...")
    results = calculate_similarity(job_description, resumes)

    # Print results
    print("\n===== Resume Ranking =====")

    for i, candidate in enumerate(results, start=1):
        print("\n----------------------------------")
        print(f"Rank : {i}")
        print(f"Candidate : {candidate['Candidate']}")
        print(f"File : {candidate['File']}")
        print(f"Score : {candidate['Score']}%")
        print(f"Education : {candidate['Education']}")
        print(f"Experience : {candidate['Experience']}")
        print(f"Email : {candidate['Email']}")
        print(f"Phone : {candidate['Phone']}")
        print(f"Matched Skills : {candidate['Matched Skills']}")
        print(f"Missing Skills : {candidate['Missing Skills']}")
        print(f"Reason : {candidate['Reason']}")
        print(f"Recommendation : {candidate['Recommendation']}")
        print(f"Score : {candidate['Score']}")
        print(f"ATS Match : {candidate['ATS Match']:.2f}%")
        
    # Create output folder if not exists
    os.makedirs("output", exist_ok=True)

    # Save CSV
    df = pd.DataFrame(results)
    df.to_csv("output/ranked_candidates.csv", index=False)

    # Save JSON
    with open("output/ranked_candidates.json", "w") as file:
        json.dump(results, file, indent=4)

    print("\nResults saved successfully!")
    print("CSV  -> output/ranked_candidates.csv")
    print("JSON -> output/ranked_candidates.json")


if __name__ == "__main__":
    main()