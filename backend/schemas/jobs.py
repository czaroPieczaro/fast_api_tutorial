from datetime import date
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# shared properties
class JobBase(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    company_url: Optional[str] = None
    location: Optional[str] = "Remote"
    description: Optional[str] = None
    date_posted: Optional[date] = datetime.now().date()


class JobCreate(JobBase):
    title: str
    company: str
    location: str
    description: str


class ShowJob(JobCreate, JobBase):
    class Config:  # tells pydantic to convert even non dict obj to json
        orm_mode = True
