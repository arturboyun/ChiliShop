from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base
from sqlalchemy.sql.sqltypes import DECIMAL

if TYPE_CHECKING:
    from .user import User  # noqa: F401


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(DECIMAL(15,2), nullable=False)
    quantity = Column(Integer, nullable=False)

    creator_id = Column(Integer, ForeignKey("user.id"))
    creator = relationship("User", back_populates="products")
    images = relationship("Image", back_populates='product')
