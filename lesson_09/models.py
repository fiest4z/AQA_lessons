from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):
    __tablename__ = "student"

    user_id = Column(Integer, primary_key=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)
