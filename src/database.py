from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


engine = create_engine('sqlite:///mtuci-test.db', echo=False)

Session = sessionmaker(autoflush=False, bind=engine)

with Session(autoflush=False, bind=engine) as session:
    pass


Base.metadata.create_all(engine)
