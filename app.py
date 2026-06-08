import streamlit as st
import pandas as pd

# Page settings
st.set_page_config(
    page_title="AI Recruiter Assistant",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("🤖 AI Recruiter Assistant")

st.write("Upload candidate CSV file and analyze candidate details.")

# Sidebar
st.sidebar.header("Menu")
option = st.sidebar.selectbox(
    "Choose Option",
    ["Home", "Upload Candidates", "About"]
)

# Home Page
if option == "Home":
    st.header("Welcome Recruiter 👋")

    st.write("""
    This AI Recruiter Assistant helps you:
    
    ✅ Upload candidate data  
    ✅ View candidate information  
    ✅ Analyze candidate skills  
    ✅ Shortlist candidates  
    
    """)

# Upload Candidates
elif option == "Upload Candidates":

    st.header("📂 Upload Candidate CSV")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:
            df = pd.read_csv(uploaded_file)

            st.success("File Uploaded Successfully ✅")

            st.subheader("Candidate Data")

            st.dataframe(df)

            st.subheader("Dataset Information")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Total Candidates", len(df))

            with col2:
                st.metric("Total Columns", len(df.columns))

            st.subheader("Columns")

            st.write(list(df.columns))

            # Search Candidate
            st.subheader("🔍 Search Candidate")

            search = st.text_input("Enter Candidate Name")

            if search:
                filtered_df = df[
                    df.astype(str).apply(
                        lambda row: row.str.contains(
                            search,
                            case=False
                        ).any(),
                        axis=1
                    )
                ]

                st.dataframe(filtered_df)

        except Exception as e:
            st.error(f"Error: {e}")

# About Page
elif option == "About":

    st.header("About Project")

    st.write("""
    Project Name: AI Recruiter Assistant
    
    Developed Using:
    - Python
    - Streamlit
    - Pandas
    
    Features:
    - Upload CSV
    - Candidate Search
    - Candidate Analysis
    
    """)

# Footer
st.markdown("---")
st.caption("Developed by Naveen")
```