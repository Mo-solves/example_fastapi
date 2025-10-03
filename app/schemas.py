from pydantic import BaseModel, EmailStr

from pydantic.types import conint
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    email: EmailStr


class CreateUser(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    created_at: datetime


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse


class PostOut(BaseModel):
    Post: PostResponse
    likes: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None


class Vote(BaseModel):
    dir: bool
