import streamlit as st
import PyPDF2

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Recruiter Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🤖 AI Recruiter Assistant")

st.write("Upload candidate resume PDF file")

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

# -----------------------------
# PDF Text Extraction Function
# -----------------------------
def extract_text_from_pdf(pdf_file):

    text = ""

    try:

        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page in pdf_reader.pages:

            extracted_text = page.extract_text()

            if extracted_text:
                text += extracted_text

    except Exception as e:

        st.error(f"Error reading PDF: {e}")

    return text

# -----------------------------
# Resume Processing
# -----------------------------
if uploaded_file is not None:

    st.success("Resume uploaded successfully ✅")

    with st.spinner("Reading Resume..."):

        resume_text = extract_text_from_pdf(uploaded_file)

    # -----------------------------
    # Check Empty Resume
    # -----------------------------
    if resume_text.strip() == "":

        st.warning("No readable text found in PDF")

    else:

        # -----------------------------
        # Show Resume Content
        # -----------------------------
        st.subheader("📄 Resume Content")

        st.text_area(
            "Extracted Text",
            resume_text,
            height=300
        )

        # -----------------------------
        # Resume Analysis
        # -----------------------------
        st.subheader("🤖 Resume Analysis")

        skills = []

        skill_keywords = [
            "python",
            "java",
            "sql",
            "html",
            "css",
            "javascript",
            "machine learning",
            "ai",
            "data science",
            "flutter",
            "react",
            "django",
            "flask",
            "c++",
            "mongodb",
            "mysql",
            "git",
            "github"
        ]

        resume_lower = resume_text.lower()

        for skill in skill_keywords:

            if skill in resume_lower:
                skills.append(skill)

        # -----------------------------
        # Display Skills
        # -----------------------------
        if skills:

            st.write("### ✅ Detected Skills")

            for skill in skills:
                st.write(f"- {skill}")

        else:

            st.warning("No skills detected")

        # -----------------------------
        # Resume Score
        # -----------------------------
        score = len(skills) * 10

        if score > 100:
            score = 100

        st.write(f"### 📊 Resume Score: {score}/100")

        # -----------------------------
        # Suggestions
        # -----------------------------
        st.write("### 💡 Suggestions")

        if score >= 70:

            st.success("Good Resume 👍")

        elif score >= 40:

            st.warning("Resume can be improved")

        else:

            st.error("Add more technical skills and projects")