from sqlalchemy import Column, Integer, String

from .base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(String)
    Surname = Column(String)
    Patronymic = Column(String)
    Number = Column(Integer)
    Role = Column(String)
    Username = Column(String, unique=True)
    Password = Column(String)
