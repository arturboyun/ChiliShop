from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product  # noqa: F401


class Image(Base):
    id = Column(Integer, primary_key=True, index=True)
    src = Column(String(255), nullable=False)

    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="images")
