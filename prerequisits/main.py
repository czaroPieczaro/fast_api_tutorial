# 1
# from fastapi import FastAPI, HTTPException, status, Depends
#
# development_db = ["DB for Development"]
#
#
# def get_db_session():
#     return development_db
#
#
# app = FastAPI()
#
#
# @app.get("/add-item/")
# def add_item(item: str, db=Depends(get_db_session)):
#     db.append(item)
#     print(db)
#     return {"message": f"added item {item}"}
# 2
# This implementation is not possible using function
from fastapi import Depends
from fastapi import FastAPI

app = FastAPI()

dummy_db = {
    "1": "SDE1 at Google",
    "2": "SDE2 at Amazon",
    "3": "Backend dev. at Spotify",
    "4": "Senior Engineer at Alphabet",
    "5": "Devops at Microsoft",
}


class GetObjectOrGetFeatured:
    def __init__(self, featured_job: str):
        self.featured_job = featured_job

    def __call__(self, id: str):
        value = dummy_db.get(id)
        if not value:
            value = dummy_db.get(self.featured_job)
        return value


@app.get("/job/{id}")
def get_job_by_id(job_title: str = Depends(GetObjectOrGetFeatured("2"))):
    return job_title
