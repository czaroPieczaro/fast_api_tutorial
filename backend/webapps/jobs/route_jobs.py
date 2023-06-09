from db.repository.jobs import list_jobs
from db.repository.jobs import retrieve_job
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

templates = Jinja2Templates(directory="templates")
router = APIRouter(
    include_in_schema=False
)  # Since, It is not an API, It does not makes much sense to see the result of


# this router in the OpenAPI documentation. That's why we have made include_in_schema = False.


@router.get("/details/{id}")
def job_detail(id: int, request: Request, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    return templates.TemplateResponse(
        "jobs/details.html", {"request": request, "job": job}
    )


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    jobs = list_jobs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "jobs": jobs, "msg": msg}
    )
