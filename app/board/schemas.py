from pydantic import BaseModel, Field
from datetime import datetime

class BoardBase(BaseModel):
    title: str = Field(..., example="첫 번째 게시글")
    content: str = Field(..., example="내용을 입력하세요")
    author: str = Field(..., example="dongwoo")

class BoardCreate(BoardBase):
    pass

class BoardResponse(BoardBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
