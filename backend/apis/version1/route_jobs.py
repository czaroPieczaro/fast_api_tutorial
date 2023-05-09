from typing import List

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.jobs import create_new_job
from db.repository.jobs import delete_job_by_id
from db.repository.jobs import list_jobs
from db.repository.jobs import retrieve_job
from db.repository.jobs import update_job_by_id
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.jobs import JobCreate
from schemas.jobs import ShowJob
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_job(
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = create_new_job(job=job, db=db, owner_id=current_user.id)
    return job


@router.get("/{id}", response_model=ShowJob)
def read_job(id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with id {id} does not exist.",
        )
    return job


@router.get("/all/", response_model=List[ShowJob])
def read_jobs(db: Session = Depends(get_db)):
    jobs = list_jobs(db)
    return jobs


@router.put("/update/{id}")
def update_job(
    id: int,
    job: JobCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    message = update_job_by_id(id=id, job=job, db=db, current_user_id=current_user.id)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    return {"msg": "Successfully updated data."}


@router.delete("/delete/{id}")
def delete_job(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user_from_token),
):
    job = retrieve_job(id, db)
    if not job:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with id {id} not found"
        )
    print("dupa", job.owner_id, current_user.id)
    if job.owner_id != current_user.id and not current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You're not authorized to do this.",
        )
    delete_job_by_id(id=id, db=db)
    return {"msg": "Successfully deleted data."}
