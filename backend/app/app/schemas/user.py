from typing import Optional

from pydantic import BaseModel, validator


# Shared properties
class UserBase(BaseModel):
    username: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None

    @validator('username')
    def username_length(cls, value: str) -> str:
        if len(value) > 64:
            raise ValueError('must be less than 64 symbols.')
        return value


# Properties to receive via API on creation
class UserCreate(UserBase):
    username: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass



# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
