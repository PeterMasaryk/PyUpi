from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from fastapi import Depends

db_url = 'postgresql://postgres:postgres@localhost:5432/fastapi'
engine = create_engine(db_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
