from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey

from .base import Base


class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Author = Column(Integer, ForeignKey('users.id'))
    Title = Column(String)
    Text = Column(String)
    Checked = Column(Boolean)
    Create_date = Column(DateTime)
