from typing import ForwardRef, List, Optional
from app.schemas.product import Product

from pydantic import BaseModel


# Shared properties
class CategoryBase(BaseModel):
    name: Optional[int] = None
    title: Optional[str] = None
    parent_id: Optional[int] = None


# Properties to receive on item creation
class CategoryCreate(CategoryBase):
    title: str
    name: str


# Properties to receive on item update
class CategoryUpdate(CategoryBase):
    pass


# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):
    id: int
    name: str
    title: str
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