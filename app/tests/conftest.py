# app/tests/conftest.py
import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database.database import Base, get_db

# ✅ 모든 모델 import 강제 (테이블 누락 방지)
from app.database import models as user_models
from app.board import models as board_models

@pytest.fixture(scope="function")
def client():
    db_fd, db_path = tempfile.mkstemp()
    SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
    )
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # ✅ 모든 테이블 생성
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    test_client = TestClient(app)

    yield test_client

    os.close(db_fd)
    os.unlink(db_path)
