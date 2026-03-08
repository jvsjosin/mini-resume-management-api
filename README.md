# Mini Resume Management API

A FastAPI project to manage candidate resumes with database persistence using SQLite and SQLAlchemy.

---

## Features

- Upload candidate resume (PDF, DOC, DOCX) along with metadata
- Store candidate details in SQLite database
- Filter candidates by skill, experience, and graduation year
- Retrieve candidate by ID
- Delete candidate
- Automatic API docs via Swagger UI

---

## Tech Stack

- **FastAPI** - web framework
- **SQLite** - database
- **SQLAlchemy** - ORM
- **Pydantic** - data validation
- **python-multipart** - for file uploads

---

## Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/jvsjosin/mini-resume-management-api.git
cd mini-resume-management-api
