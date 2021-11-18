from typing import List, Optional

from pydantic import BaseModel, validator
from app.schemas.image import Image


# Shared properties
class ProductBase(BaseModel):
    slug: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None
    top_sizes: Optional[List[str]] = None
    sizes: Optional[List[str]] = None
    category_id: Optional[int] = None


# Properties to receive on item creation
class ProductCreate(ProductBase):
    title: str
    price: int
    quantity: int
    category_id: int
    top_sizes: Optional[str] = None
    sizes: str

    @validator('top_sizes', 'sizes')
    def parse_csv_sizes(cls, v):
        if v:
            v = v.replace(" ", "").split(',')
        return v


# Properties to receive on item update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    slug: str
    title: str
    price: int
    quantity: int
    top_sizes: Optional[List[str]] = None
    sizes: Optional[List[str]] = None
    creator_id: int
    category_id: Optional[int] = None
    images: List[Image]

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
