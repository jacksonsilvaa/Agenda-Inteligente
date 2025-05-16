from sqlalchemy import Column, Integer, String
from app.db.base import Base


class Consult(Base):
    __tablename__ = "user_agend"

    id = Column(Integer, primary_key=True, index=True)
    name_user = Column(String)
    age = Column(String)

    '''def __repr__(self):
        return f"id={self.id}, name_user='{self.name_user}', age={self.age})"'''