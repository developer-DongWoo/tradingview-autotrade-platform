# app/auth/routes.py
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import database
from app.database import schemas
from app.auth.jwt_handler import get_current_user
from app.auth import service

router = APIRouter(tags=["Auth"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ 회원가입
@router.post("/auth/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.register_user(db, user)

# ✅ 로그인
@router.post("/auth/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return service.login_user(db, form_data.username, form_data.password)

# ✅ 내 정보 조회
@router.get("/users/me", response_model=schemas.UserResponse)
def read_current_user(current_user = Depends(get_current_user)):
    return current_user

# ✅ 비밀번호 변경
@router.put("/users/me", response_model=schemas.UserResponse)
def update_me(data: schemas.UserUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    updated_user = service.update_user(db, current_user, data.new_password)
    return updated_user

# ✅ 회원탈퇴
@router.delete("/users/me")
def delete_me(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return service.delete_user(db, current_user)
