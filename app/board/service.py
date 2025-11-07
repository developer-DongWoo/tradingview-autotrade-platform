# app/board/service.py
from sqlalchemy.orm import Session
from app.board import models, schemas
from app.auth.jwt_handler import get_current_user
from fastapi import HTTPException, status
from app.database.models import User

def create_post(db: Session, post: schemas.BoardCreate, user_id: int):
    new_post = models.Board(title=post.title, content=post.content, author_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    # ✅ author.email 명시적으로 포함
    author = db.query(User).filter(User.id == user_id).first()

    return {
        "id": new_post.id,
        "title": new_post.title,
        "content": new_post.content,
        "author": author.email if author else None,
        "created_at": new_post.created_at,
        "updated_at": new_post.updated_at,
    }




def get_all_posts(db: Session):
    return db.query(models.Board).all()

def get_post(db: Session, post_id: int):
    post = db.query(models.Board).filter(models.Board.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return post

def update_post(db: Session, post_id: int, post_update: schemas.BoardUpdate, user_id: int):
    post = db.query(models.Board).filter(models.Board.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="본인 글만 수정할 수 있습니다.")

    post.title = post_update.title
    post.content = post_update.content
    db.commit()
    db.refresh(post)
    return post

def delete_post(db: Session, post_id: int, user_id: int):
    post = db.query(models.Board).filter(models.Board.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    if post.author_id != user_id:
        raise HTTPException(status_code=403, detail="본인 글만 삭제할 수 있습니다.")

    db.delete(post)
    db.commit()
    return {"message": "게시글이 삭제되었습니다."}
