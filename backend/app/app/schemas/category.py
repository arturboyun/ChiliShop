from typing import ForwardRef, List, Optional
from app.schemas.product import Product

from pydantic import BaseModel, validator


# Shared properties
class CategoryBase(BaseModel):
    name: Optional[int] = None
    title: Optional[str] = None
    slug: Optional[str] = None
    parent_id: Optional[int] = None

    @validator('parent_id')
    def parent_id_none_if_zero_provided(cls, v):
        if v == 0:
            v = None
        return v


# Properties to receive on item creation
class CategoryCreate(CategoryBase):
    name: str
    title: str
    slug: str

    @validator('slug')
    def slug_in_lowercase(cls, v):
        if v:
            v = v.lower()
        return v


# Properties to receive on item update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int
    name: str
    title: str
    slug: str
    children: List['Category'] = []

    class Config:
        orm_mode = True


# Properties to return to client
class Category(CategoryInDBBase):
    pass


# Properties to return to client (category props with products)
class CategoryDetail(CategoryInDBBase):
    products: List[Product] = []


# Properties properties stored in DB
class CategoryInDB(CategoryInDBBase):
    pass


Category.update_forward_refs()
CategoryDetail.update_forward_refs()
