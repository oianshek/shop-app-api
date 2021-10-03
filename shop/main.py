from fastapi import FastAPI
from . import crud
from .db.db import SessionLocal, engine
from models import models
from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello"}

# @app.get("/users", response_model=List[])
# async def get_users():