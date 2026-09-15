# AI-Powered Resume Ranking System

An AI-based resume analysis system built with Python that compares a candidate's resume with a job description and generates an AI-based evaluation.

## Overview

This project uses document processing and a Large Language Model (LLM) to analyze resumes against job requirements. It extracts text from PDF or DOCX files, sends the resume content to an AI model, and presents the analysis in a structured format.

The current implementation processes one resume at a time.

## Features

* Supports PDF and DOCX resume files
* Extracts text from resume documents
* Compares resume content with job requirements
* Identifies key skill matches
* Evaluates experience match
* Generates a percentage-based match score
* Provides an AI-based recommendation
* Converts AI output into a structured Pandas DataFrame
* Integrates a Qwen LLM through the Hugging Face API

## Technologies Used

* Python
* PyPDF
* python-docx
* Pandas
* Hugging Face Hub
* Qwen LLM
* Prompt Engineering

## Job Requirements

The current system evaluates resumes for a Python Developer position with the following requirements:

* Python
* SQL
* REST API
* FastAPI
* Git

## Workflow

```text
Resume File
    ↓
PDF / DOCX Text Extraction
    ↓
Resume Content
    ↓
Job Description
    ↓
Qwen LLM
    ↓
Resume Analysis
    ↓
Match Score + Skills + Experience
    ↓
Recommendation
    ↓
Pandas DataFrame
```

## AI Analysis

The system asks the LLM to evaluate the resume based on:

1. Candidate rank
2. Candidate name
3. Match score
4. Key skills match
5. Experience match
6. Recommendation

Example output:

| Rank | Candidate | Match Score | Key Skills Match | Experience Match | Recommendation |
| ---- | --------- | ----------- | ---------------- | ---------------- | -------------- |
| 1    | Candidate | 60%         | Partial          | Partial          | Consider       |

## Project Highlights

* Uses an LLM for resume evaluation rather than relying only on basic keyword matching.
* Demonstrates practical integration of a hosted AI model with Python.
* Combines document text extraction with Generative AI.
* Uses prompt engineering to control the structure of AI-generated results.
* Converts unstructured LLM output into structured tabular data.
* Demonstrates a practical AI application for resume screening.

## Installation

Install the required dependencies:

```bash
pip install pypdf python-docx huggingface_hub pandas
```

## Hugging Face API

The project uses the Hugging Face Inference API to access the Qwen model.

Before running the application, configure your Hugging Face API key securely.

Do not commit your API key to GitHub.

## Running the Project

1. Install the required Python packages.
2. Configure your Hugging Face API key.
3. Provide the path to a PDF or DOCX resume.
4. Run the Python program.
5. The system extracts the resume content and sends it for AI analysis.
6. The final evaluation is displayed as a Pandas table.

## Future Enhancements

* Multiple resume processing
* Automatic ranking of multiple candidates
* Missing skill detection
* Improved scoring methodology
* Dynamic job description input
* FastAPI integration
* Web-based interface
* Excel/CSV report generation
* Database integration
* More detailed candidate analysis

## Purpose

The project demonstrates how Python, document processing, APIs, prompt engineering, and Large Language Models can be combined to build a practical AI-powered application for resume screening.
