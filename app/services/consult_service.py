from db.session import SessionLocal
from models.consult_models import Consult

def consult_scheduling():
    db = SessionLocal()
    users = db.query(Consult).all()
    db.close()
    return users
