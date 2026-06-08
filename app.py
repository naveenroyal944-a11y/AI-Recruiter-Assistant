import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Recruiter Assistant")

st.title("🤖 AI Recruiter Assistant")

st.write("Upload candidate CSV file")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File Uploaded Successfully")

    st.dataframe(df)