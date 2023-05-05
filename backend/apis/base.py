from fastapi import APIRouter

from apis.version1 import route_general_pages, route_users


api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router, prefix="", tags=["general_pages"])
api_router.include_router(route_users.router, prefix="/users", tags=["general_pages"])