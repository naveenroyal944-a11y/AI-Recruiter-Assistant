import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Job description
job_description = """
Looking for AI Engineer with Python NLP and machine learning skills
"""

# Read CSV file
data = pd.read_csv("candidates.csv")

# Convert job description into embedding
job_embedding = model.encode([job_description])

results = []

print("\nCandidate Rankings:\n")

# Loop through candidates
for index, row in data.iterrows():

    name = row["name"]

    resume = row["resume"]

    resume_embedding = model.encode([resume])

    similarity = cosine_similarity(job_embedding, resume_embedding)

    score = similarity[0][0] * 100

    results.append((name, score))

# Sort candidates

results.sort(key=lambda x: x[1], reverse=True)

# Print rankings
for rank, result in enumerate(results, start=1):

    print(f"{rank}. {result[0]} --> {result[1]:.2f}% match")

# Best candidate
best_candidate = results[0]

print("\nBest Candidate Selected:")
print(f"{best_candidate[0]} with {best_candidate[1]:.2f}% match")