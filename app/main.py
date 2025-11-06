from fastapi import FastAPI, Depends
from app import database, models, schemas
from app.auth import routes as auth_routes
from app.auth.jwt_handler import get_current_user  # ✅ 경로 확인

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="JWT Login API - Clean Structure")

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Hello, FastAPI JWT!"}


# ✅ /users/me 엔드포인트 (핵심)
@app.get("/users/me", response_model=schemas.UserResponse)
def read_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user
