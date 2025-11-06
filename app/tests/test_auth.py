# app/tests/test_auth.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # 회원가입
    register_data = {"email": "testuser@example.com", "password": "test1234"}
    response = client.post("/auth/register", json=register_data)
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

    # 로그인
    login_data = {"username": "testuser@example.com", "password": "test1234"}
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200
    token = response.json().get("access_token")
    assert token is not None

    # 토큰으로 사용자 정보 확인
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_update_password():
    # 로그인해서 토큰 얻기
    login_data = {"username": "testuser@example.com", "password": "test1234"}
    response = client.post("/auth/login", data=login_data)
    token = response.json().get("access_token")

    # 비밀번호 변경
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/users/me", json={"new_password": "newpass123"}, headers=headers)
    assert response.status_code == 200

    # 새 비밀번호로 로그인 시도
    login_data["password"] = "newpass123"
    response = client.post("/auth/login", data=login_data)
    assert response.status_code == 200

def test_delete_user():
    # 로그인해서 토큰 얻기
    login_data = {"username": "testuser@example.com", "password": "newpass123"}
    response = client.post("/auth/login", data=login_data)
    token = response.json().get("access_token")

    # 회원탈퇴
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/users/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["message"] == "계정이 삭제되었습니다."
