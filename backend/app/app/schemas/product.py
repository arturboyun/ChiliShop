from typing import List, Optional

from pydantic import BaseModel
from app.schemas.image import Image

# Shared properties
class ProductBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[int] = None
    quantity: Optional[int] = None


# Properties to receive on item creation
class ProductCreate(ProductBase):
    title: str
    price: int
    quantity: int


# Properties to receive on item update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int
    title: str
    price: int
    quantity: int
    creator_id: int
    images: List[Image]

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass
