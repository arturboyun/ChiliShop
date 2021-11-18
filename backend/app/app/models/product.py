from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from sqlalchemy.sql.sqltypes import DECIMAL, ARRAY

if TYPE_CHECKING:
    from .user import User  # noqa: F401
    from .category import Category  # noqa: F401
    from .image import Image  # noqa: F401


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, index=True, unique=True, nullable=False)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(DECIMAL(15, 2), nullable=False)
    quantity = Column(Integer, nullable=False)
    top_sizes = Column(ARRAY(String))
    sizes = Column(ARRAY(String))

    creator_id = Column(Integer, ForeignKey("user.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    
    category = relationship("Category", back_populates="products")
    creator = relationship("User", back_populates="products")
    images = relationship("Image", back_populates='product')
