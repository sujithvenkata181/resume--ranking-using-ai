import streamlit as st

st.title("AI Resume Ranking System")

st.write("Upload resumes and compare them with a job description.")

job_description = st.text_area(
    "Enter Job Description"
)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if st.button("Analyze Resumes"):

    st.write("Analysis started...")