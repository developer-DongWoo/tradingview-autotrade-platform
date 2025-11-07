from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.board import service, schemas

router = APIRouter(prefix="/board", tags=["Board"])

@router.post("/", response_model=schemas.BoardResponse)
def create_board(post: schemas.BoardCreate, db: Session = Depends(get_db)):
    return service.create_post(db, post)

@router.get("/", response_model=list[schemas.BoardResponse])
def list_boards(db: Session = Depends(get_db)):
    return service.get_all_posts(db)

@router.get("/{post_id}", response_model=schemas.BoardResponse)
def read_board(post_id: int, db: Session = Depends(get_db)):
    post = service.get_post_by_id(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="게시글을 찾을 수 없습니다.")
    return post

@router.delete("/{post_id}")
def delete_board(post_id: int, db: Session = Depends(get_db)):
    success = service.delete_post(db, post_id)
    if not success:
        raise HTTPException(status_code=404, detail="삭제할 게시글이 없습니다.")
    return {"message": "게시글이 삭제되었습니다."}
