# app/board/routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.board import service, schemas
from app.database.database import get_db
from app.auth.jwt_handler import get_current_user

router = APIRouter(prefix="/board", tags=["Board"])

@router.post("/", response_model=schemas.BoardResponse)
def create_post(
    post: schemas.BoardCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return service.create_post(db, post, current_user.id)


@router.get("/", response_model=List[schemas.BoardResponse])
def get_posts(db: Session = Depends(get_db)):
    return service.get_all_posts(db)

@router.get("/{post_id}", response_model=schemas.BoardResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    return service.get_post(db, post_id)

@router.put("/{post_id}", response_model=schemas.BoardResponse)
def update_post(post_id: int, post: schemas.BoardUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return service.update_post(db, post_id, post, current_user.id)

@router.delete("/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return service.delete_post(db, post_id, current_user.id)
