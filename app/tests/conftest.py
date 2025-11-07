# app/tests/conftest.py
import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.database import Base, get_db

@pytest.fixture(scope="function")
def client():
    """⚙️ 각 테스트마다 독립된 임시 DB를 생성하고, 테스트 완료 시 자동 삭제"""
    # 1️⃣ 임시 파일 기반 SQLite DB 생성
    db_fd, db_path = tempfile.mkstemp()
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

    # 2️⃣ SQLAlchemy 엔진 & 세션 구성
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
    TestingSessionLocal = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )

    # 3️⃣ DB 스키마 생성
    Base.metadata.create_all(bind=engine)

    # 4️⃣ 의존성 주입 오버라이드
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db

    # 5️⃣ FastAPI 테스트 클라이언트 생성
    test_client = TestClient(app)

    yield test_client

    # 6️⃣ 테스트 종료 후 DB 정리
    os.close(db_fd)
    os.unlink(db_path)
