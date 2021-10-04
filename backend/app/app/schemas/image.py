from typing import Optional

from pydantic import BaseModel


# Shared properties
class ImageBase(BaseModel):
    src: Optional[str] = None
    product_id: Optional[int] = None


# Properties to receive on item creation
class ImageCreate(ImageBase):
    src: str
    product_id: int


# Properties to receive on item update
class ImageUpdate(ImageBase):
    pass


# Properties shared by models stored in DB
class ImageInDBBase(ImageBase):
    id: int
    src: str
    product_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Image(ImageInDBBase):
    pass


# Properties properties stored in DB
class ImageInDB(ImageInDBBase):
    pass
