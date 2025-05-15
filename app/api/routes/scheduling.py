# app/api/routes/scheduling.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Consult Check")
def health_check():
    return {"status": "ok"}