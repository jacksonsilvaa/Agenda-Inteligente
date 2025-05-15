from sqlalchemy import Column, Integer, String
from db.base import Base


class Consult(Base):
    __tablename__ = "consult"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
