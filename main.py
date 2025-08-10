from fastapi import FastAPI
from .database import engine
from . import models
from .api import cases, ai

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(cases.router, prefix = "/api")
app.include_router(ai.router, prefix = "/api/ai")

@app.get("/")
def read_root():
  return {"message": "Surgical Registry API"}