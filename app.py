import os
import streamlit as st

from pypdf import PdfReader
from docx import Document
from huggingface_hub import InferenceClient
import pandas as pd


# -------------------------
# Read PDF
# -------------------------
def read_pdf(file):

    pdf = PdfReader(file)

    text = ""

    for page in pdf.pages:
        text += page.extract_text() or ""

    return text


# -------------------------
# Read DOCX
# -------------------------
def read_docx(file):

    doc = Document(file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


# -------------------------
# Read Resume
# -------------------------
def read_resume(file):

    file_name = file.name

    ext = os.path.splitext(file_name)[1].lower()

    if ext == ".pdf":
        return read_pdf(file)

    elif ext == ".docx":
        return read_docx(file)

    return ""


# -------------------------
# AI Resume Analysis
# -------------------------
def analyze_resume(resume_text, job_description):

    client = InferenceClient(
        api_key=os.getenv("HF_TOKEN")
    )

    prompt = f"""
You are an AI resume screening system.

Job Description:

{job_description}

Resume:

{resume_text}

Analyze the resume according to the job description.

Return exactly 5 lines(one word answers):

1. Candidate Name
2. Match Score
3. Skills Match
4. Experience Match
5. Recommendation

Give only the answer after each number.
Do not write labels such as Candidate Name: or Match Score:.
Use a percentage for Match Score.
"""

    response = client.chat.completions.create(

        model="Qwen/Qwen3.8-27B:ovhcloud",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        max_tokens=1000
    )

    return response.choices[0].message.content


# ==================================================
# STREAMLIT WEBPAGE
# ==================================================

st.title("AI Resume Ranking System")

st.write(
    "Upload resumes and compare them with a Job Description."
)


# -------------------------
# Job Description
# -------------------------

job_description = st.text_area(
    "Enter Job Description"
)


# -------------------------
# Upload Resumes
# -------------------------

uploaded_files = st.file_uploader(
    "Upload Resumes",
    type=["pdf", "docx"],
    accept_multiple_files=True
)


# -------------------------
# Analyze Button
# -------------------------

if st.button("Analyze Resumes"):

    if job_description == "":
        
        st.warning(
            "Please enter a Job Description."
        )

    elif not uploaded_files:

        st.warning(
            "Please upload at least one resume."
        )

    else:

        rows = []

        # -------------------------
        # Process Resumes
        # -------------------------

        for file in uploaded_files:

            st.write(
                "Processing:",
                file.name
            )

            # Read resume
            resume_text = read_resume(file)

            # AI analysis
            result = analyze_resume(
                resume_text,
                job_description
            )

            # Convert result into lines
            lines = result.splitlines()

            values = []

            for line in lines:

                if "." in line:

                    value = line.split(
                        ".",
                        1
                    )[1].strip()

                    if ":" in value:

                        value = value.split(
                            ":",
                            1
                        )[1].strip()

                    values.append(value)

            # Add result
            if len(values) == 5:

                rows.append(values)

            else:

                st.warning(
                    f"Could not extract results from {file.name}"
                )


        # -------------------------
        # Create Table
        # -------------------------

        if rows:

            table = pd.DataFrame(

                rows,

                columns=[
                    "Candidate",
                    "Match Score",
                    "Skills Match",
                    "Experience Match",
                    "Recommendation"
                ]
            )


            # -------------------------
            # Convert Score
            # -------------------------

            table["Match Score"] = (

                table["Match Score"]

                .str.extract(r"(\d+)")

                .astype(int)
            )


            # -------------------------
            # Rank Candidates
            # -------------------------

            table = table.sort_values(

                by="Match Score",

                ascending=False
            )


            # -------------------------
            # Add Rank
            # -------------------------

            table["Rank"] = range(

                1,

                len(table) + 1
            )


            # -------------------------
            # Arrange Columns
            # -------------------------

            table = table[

                [
                    "Rank",
                    "Candidate",
                    "Match Score",
                    "Skills Match",
                    "Experience Match",
                    "Recommendation"
                ]

            ]


            # -------------------------
            # Display Result
            # -------------------------

            st.subheader(
                "Final Resume Ranking"
            )

            st.dataframe(
                table,
                use_container_width=True
            )