from sqlalchemy.orm import Session
from app.board import models, schemas

def create_post(db: Session, post: schemas.BoardCreate):
    new_post = models.Board(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all_posts(db: Session):
    return db.query(models.Board).order_by(models.Board.created_at.desc()).all()

def get_post_by_id(db: Session, post_id: int):
    return db.query(models.Board).filter(models.Board.id == post_id).first()

def delete_post(db: Session, post_id: int):
    post = db.query(models.Board).filter(models.Board.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False
