from app.db.session import SessionLocal
from app.models.consult_models import Consult

def consult_scheduling():
    db = SessionLocal()
    users = db.query(Consult).all()
    db.close()
    return users