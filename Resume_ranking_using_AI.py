from pypdf import PdfReader
from docx import Document
from huggingface_hub import InferenceClient
import pandas as pd

client = InferenceClient(
    api_key=" YOUR_HUGGINGFACE_API_KEY"
)

def read_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n"

    return text

def read_docx(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text

def analyze_resume(resume_text, job_description):

    prompt = f"""
Compare the resume with the job description.

JOB DESCRIPTION:
{'''Python Developer required.

Skills:
Python, SQL, REST API, FastAPI and Git.'''}

RESUME:
{resume_text}

Give me(single word answrers) in the following format:

1.rank(in numbers)
2.candidate name 
3.match score(in percentage)
4.key skills match
5.experience match
6.Recommendation
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen3.8-27B:ovhcloud",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        max_tokens=1500
    )

    return response.choices[0].message.content

job_description = """
Python Developer required.

Skills:
Python, SQL, REST API, FastAPI and Git.
"""
resume_file = r"E:\python\practice\sample python developer resume.pdf"

if resume_file.endswith(".pdf"):
    resume_text = read_pdf(resume_file)

elif resume_file.endswith(".docx"):
    resume_text = read_docx(resume_file)

else:
    raise ValueError("Only PDF and DOCX files are supported.")

result = analyze_resume(
    resume_text,
    job_description
)
lines = result.splitlines()

values = []

for line in lines:
    if "." in line:
        value = line.split(".", 1)[1].strip()
        values.append(value)

table = pd.DataFrame(
    [values],
    columns=[
        "Rank ",
        "Candidate ",
        "Match Score ",
        "Key Skills Match ",
        "Experience Match ",
        "Recommendation "
    ]
)
print(table)
