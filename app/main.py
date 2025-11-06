# app/main.py

from fastapi import FastAPI, Depends
from app.database import database, models, schemas
  # ✅ 이 줄이 반드시 있어야 함
from app.auth import routes as auth_routes
from app.auth.jwt_handler import get_current_user

# ✅ 이 시점에 models.User가 import되어야 테이블이 생성됨
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="JWT Email Auth API")

app.include_router(auth_routes.router)

@app.get("/")
def root():
    return {"message": "Hello, Email-based FastAPI JWT!"}

@app.get("/users/me", response_model=schemas.UserResponse)
def read_current_user(current_user: models.User = Depends(get_current_user)):
    return current_user
