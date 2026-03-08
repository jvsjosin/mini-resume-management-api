from pydantic import BaseModel
from typing import Optional

class CandidateResponse(BaseModel):
    id: int
    full_name: str
    dob: Optional[str]
    contact_number: Optional[str]
    contact_address: Optional[str]
    education: Optional[str]
    graduation_year: Optional[int]
    experience: Optional[float]
    skills: Optional[str]
    resume_file: Optional[str]

    class Config:
        from_attributes = True
