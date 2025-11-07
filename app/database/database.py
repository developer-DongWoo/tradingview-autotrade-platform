# app/database/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./app/users.db"  # ✅ DB 파일 경로 명확히 지정

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ 공통 DB 세션 함수 추가
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
