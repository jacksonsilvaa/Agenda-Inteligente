# app/api/routes/consult.py
from fastapi import APIRouter
from app.services.consult_service import consult_scheduling


router = APIRouter()

@router.get("/", summary="scheduling Check")
def consult_funct():

    #return f"Segue resultado:\n{consult_scheduling()}"
    return consult_scheduling()