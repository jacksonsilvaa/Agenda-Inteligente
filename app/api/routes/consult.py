# app/api/routes/consult.py
from fastapi import APIRouter
#from services.consult_service import consult_scheduling

router = APIRouter()

@router.get("/", summary="scheduling Check")
def consult_scheduling():
    return {"status": "consult ok"}
    #return consult_scheduling()