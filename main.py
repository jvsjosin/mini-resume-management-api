from fastapi import FastAPI, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
import shutil
import os
import uuid

from database import SessionLocal, engine
import models
from schemas import CandidateResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Resume Management API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXTENSIONS = ["pdf", "doc", "docx"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/candidates/", response_model=CandidateResponse)
def create_candidate(
    full_name: str = Form(...),
    dob: str = Form(...),
    contact_number: str = Form(...),
    contact_address: str = Form(...),
    education: str = Form(...),
    graduation_year: int = Form(...),
    experience: float = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    extension = resume.filename.split(".")[-1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")

    unique_filename = f"{uuid.uuid4()}.{extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(resume.file, buffer)

    candidate = models.Candidate(
        full_name=full_name,
        dob=dob,
        contact_number=contact_number,
        contact_address=contact_address,
        education=education,
        graduation_year=graduation_year,
        experience=experience,
        skills=skills,
        resume_file=file_path
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


@app.get("/candidates/", response_model=list[CandidateResponse])
def list_candidates(
    skill: str = None,
    experience: float = None,
    graduation_year: int = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Candidate)

    if skill:
        query = query.filter(models.Candidate.skills.contains(skill))
    if experience:
        query = query.filter(models.Candidate.experience >= experience)
    if graduation_year:
        query = query.filter(models.Candidate.graduation_year == graduation_year)

    return query.all()


@app.get("/candidates/{candidate_id}", response_model=CandidateResponse)
def get_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    return candidate


@app.delete("/candidates/{candidate_id}")
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.query(models.Candidate).filter(
        models.Candidate.id == candidate_id
    ).first()

    if not candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")

    db.delete(candidate)
    db.commit()

    return {"message": "Candidate deleted successfully"}
