from fastapi import FastAPI, Depends
from app import database, models
from app.auth import routes as auth_routes
from app.auth.jwt_handler import get_current_user

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="JWT Login API - Clean Structure")

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI JWT!"}

@app.get("/users/me")
def read_current_user(current_user = Depends(get_current_user)):
    return {"username": current_user.username}