# app/main.py
from fastapi import FastAPI
from app import database, models
from app.auth import routes as auth_routes

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="JWT Email Auth API")

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Hello, Email-based FastAPI JWT!"}
