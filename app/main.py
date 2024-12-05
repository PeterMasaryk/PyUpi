from contextlib import asynccontextmanager
from fastapi import FastAPI

from .dependencies import create_db_and_tables
from .routers import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(users.router)