import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Page settings
st.set_page_config(
    page_title="AI Recruiter Assistant",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("AI Recruiter Assistant")

st.sidebar.write(
    "Upload resumes and check AI match scores"
)

# Load AI model
model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

# Main title
st.title("AI Recruiter Assistant")

# Subtitle
st.markdown(
    "### Smart AI Hiring Platform"
)

# Separator
st.markdown("---")

# Job description
job_description = st.text_area(
    "Enter Job Description",
    "Looking for AI engineer with Python and NLP skills"
)

# Upload resumes
uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# Extract PDF text
def extract_text_from_pdf(pdf_file):

    reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        text += page.extract_text()

    return text

# Resume ranking
if uploaded_files:

    results = []

    # Job embedding
    job_embedding = model.encode(
        [job_description]
    )

    # Process resumes
    for uploaded_file in uploaded_files:

        # Extract text
        resume_text = extract_text_from_pdf(
            uploaded_file
        )

        # Resume embedding
        resume_embedding = model.encode(
            [resume_text]
        )

        # Similarity
        similarity = cosine_similarity(
            job_embedding,
            resume_embedding
        )

        # Score
        score = similarity[0][0] * 100

        # Store result
        results.append(
            (uploaded_file.name, score)
        )

    # Sort candidates
    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Rankings heading
    st.subheader("Candidate Rankings")

    # Total candidates
    st.metric(
        "Total Candidates",
        len(results)
    )

    # Show rankings
    for rank, result in enumerate(
        results,
        start=1
    ):

        st.write(
            f"{rank}. "
            f"{result[0]} "
            f"--> "
            f"{result[1]:.2f}% Match"
        )

        st.progress(
            int(result[1])
        )

    # Best candidate
    best_candidate = results[0]

    # Top score
    st.metric(
        "Top Match Score",
        f"{best_candidate[1]:.2f}%"
    )

    # Best candidate message
    st.success(
        f"Best Candidate: "
        f"{best_candidate[0]}"
    )

    # Resume quality
    if best_candidate[1] >= 80:

        st.success(
            "Excellent Resume Match"
        )

    elif best_candidate[1] >= 60:

        st.warning(
            "Good Resume Match"
        )

    else:

        st.error(
            "Low Resume Match"
        )

    # Skills section
    skills = [
        "Python",
        "Machine Learning",
        "NLP",
        "AI",
        "Flask",
        "Streamlit"
    ]

    found_skills = []

    # Detect skills
    for skill in skills:

        if skill.lower() in resume_text.lower():

            found_skills.append(skill)

    # Show skills
    st.subheader("Skills Found")

    if found_skills:

        for skill in found_skills:

            st.write(
                "✔",
                skill
            )

    else:

        st.write(
            "No matching skills found."
        )

# Chatbot Section
st.markdown("---")

st.subheader("AI Recruiter Chatbot")

user_question = st.text_input(
    "Ask your question"
)

if user_question:

    question = user_question.lower()

    if "best candidate" in question:

        if uploaded_files:

            st.write(
                f"Best candidate is "
                f"{best_candidate[0]}"
            )

        else:

            st.write(
                "Please upload resumes first."
            )

    elif "top score" in question:

        if uploaded_files:

            st.write(
                f"Top score is "
                f"{best_candidate[1]:.2f}%"
            )

        else:

            st.write(
                "Please upload resumes first."
            )

    elif "skills" in question:

        st.write(
            "Important AI skills are Python, "
            "Machine Learning, NLP and Streamlit."
        )

    elif "hello" in question:

        st.write(
            "Hello! I am your AI Recruiter Assistant."
        )

    else:

        st.write(
            "I can help with recruitment, "
            "resume analysis and AI hiring."
        )