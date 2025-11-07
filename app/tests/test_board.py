# app/tests/test_board.py
import uuid

def test_board_crud(client):
    """게시판 CRUD 전체 테스트"""

    # 1️⃣ 고유 이메일 생성
    unique_email = f"boarduser_{uuid.uuid4().hex[:6]}@example.com"

    register_data = {"email": unique_email, "password": "test1234"}
    res = client.post("/auth/register", json=register_data)
    assert res.status_code == 200

    # 2️⃣ 로그인
    login_data = {"username": unique_email, "password": "test1234"}
    res = client.post("/auth/login", data=login_data)
    assert res.status_code == 200
    token = res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 3️⃣ 게시글 작성
    post_data = {"title": "첫 번째 글", "content": "테스트 내용입니다."}
    res = client.post("/board/", json=post_data, headers=headers)
    assert res.status_code == 200
    post_id = res.json()["id"]

    # 4️⃣ 조회
    res = client.get(f"/board/{post_id}")
    assert res.status_code == 200
    assert res.json()["title"] == "첫 번째 글"

    # 5️⃣ 수정
    update_data = {"title": "수정된 제목", "content": "수정된 내용입니다."}
    res = client.put(f"/board/{post_id}", json=update_data, headers=headers)
    assert res.status_code == 200
    assert res.json()["title"] == "수정된 제목"

    # 6️⃣ 삭제
    res = client.delete(f"/board/{post_id}", headers=headers)
    assert res.status_code == 200
    assert res.json()["message"] == "게시글이 삭제되었습니다."
