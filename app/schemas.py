# app/schemas.py
from pydantic import BaseModel, EmailStr, Field, field_validator

class UserCreate(BaseModel):
    email: EmailStr = Field(..., description="이메일 형식의 아이디")
    password: str = Field(..., min_length=8, max_length=50)

    @field_validator("password")
    def validate_password(cls, v):
        if not any(c.isdigit() for c in v) or not any(c.isalpha() for c in v):
            raise ValueError("비밀번호에는 숫자와 문자가 모두 포함되어야 합니다.")
        return v



class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    new_password: str = Field(..., min_length=8, max_length=50)
