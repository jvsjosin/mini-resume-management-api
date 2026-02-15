	# Mini Resume Management API

## Features
- Upload Resume (PDF/DOC/DOCX)
- Store Candidate Metadata
- Filter by Skill, Experience, Graduation Year
- Get Candidate by ID
- Delete Candidate

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite

## Setup Instructions

1. Create Virtual Environment
   python -m venv venv

2. Activate
   venv\Scripts\activate

3. Install Dependencies
   pip install -r requirements.txt

4. Run Server
   uvicorn main:app --reload

5. Open Swagger
   http://127.0.0.1:8000/docs
