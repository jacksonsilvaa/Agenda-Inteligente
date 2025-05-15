from fastapi import APIRouter
from app.api.routes import scheduling
from app.api.routes import consult

api_router = APIRouter()
api_router.include_router(scheduling.router, prefix="/scheduling", tags=["scheduling"])
api_router.include_router(consult.router, prefix="/consult", tags=["consult"])