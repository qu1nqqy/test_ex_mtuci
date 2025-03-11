from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from src.database import Base


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Author = Column(Integer, ForeignKey('users.id'))
    Title = Column(String)
    Text = Column(String)
    Checked = Column(Boolean)
    Create_date = Column(DateTime)
