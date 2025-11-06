# app/tests/conftest.py
import os
import pytest
from app import database, models

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown_db():
    """각 테스트 전후로 users.db 초기화"""

    # ✅ 항상 app 디렉토리 내부의 users.db를 대상으로 함
    db_path = os.path.join(os.path.dirname(__file__), "..", "users.db")
    db_path = os.path.abspath(db_path)

    # 테스트 시작 전에 DB 제거
    if os.path.exists(db_path):
        os.remove(db_path)

    # 새 DB 생성
    models.Base.metadata.create_all(bind=database.engine)

    yield  # 👈 테스트 실행 시점

    # 테스트 끝난 후 DB 제거
    if os.path.exists(db_path):
        os.remove(db_path)
