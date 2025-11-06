# app/auth/service.py
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app import models, schemas, utils
from app.auth.jwt_handler import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


# ✅ 회원가입
def register_user(db: Session, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="이미 등록된 이메일입니다.")

    hashed_pw = utils.hash_password(user.password)
    new_user = models.User(email=user.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ✅ 로그인
def login_user(db: Session, email: str, password: str):
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not utils.verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="이메일 또는 비밀번호가 잘못되었습니다.")

    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


# ✅ 비밀번호 변경
def update_user(db: Session, user: models.User, new_password: str):
    hashed_pw = utils.hash_password(new_password)
    user.hashed_password = hashed_pw
    db.commit()
    db.refresh(user)
    return user


# ✅ 회원탈퇴
def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()
    return {"message": "계정이 삭제되었습니다."}
