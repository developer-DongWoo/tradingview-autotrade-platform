# app/main.py

from fastapi import FastAPI, Depends
from app.database import database, models
from app.auth import routes as auth_routes
from app.auth.jwt_handler import get_current_user
from app.board import routes as board_routes  # ✅ 게시판 기능 추가

# ✅ FastAPI 인스턴스 생성 (가장 먼저)
app = FastAPI(title="FastAPI Modular Backend")

# ✅ DB 테이블 생성
models.Base.metadata.create_all(bind=database.engine)

# ✅ 라우터 등록
app.include_router(auth_routes.router)
app.include_router(board_routes.router)

# ✅ 기본 엔드포인트
@app.get("/")
def root():
    return {"message": "FastAPI Modular Backend Running 🚀"}

# ✅ 현재 로그인된 유저 정보
@app.get("/users/me")
def read_current_user(current_user=Depends(get_current_user)):
    return {"email": current_user.email}
