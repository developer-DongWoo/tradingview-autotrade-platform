# app/board/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

class BoardBase(BaseModel):
    title: str = Field(..., json_schema_extra={"example": "첫 번째 게시글"})
    content: str = Field(..., json_schema_extra={"example": "내용을 입력하세요"})

class BoardCreate(BoardBase):
    pass

class BoardUpdate(BoardBase):
    pass

# app/board/schemas.py
class BoardResponse(BoardBase):
    id: int
    author: str | None = None  # ✅ None 허용
    created_at: datetime | None = None
    updated_at: datetime | None = None

    model_config = ConfigDict(from_attributes=True)

