from typing import TYPE_CHECKING
from app.db.base_class import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

if TYPE_CHECKING:
    from .product import Product  # noqa: F401


class Category(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True, nullable=False)
    parent_id = Column(Integer, ForeignKey('category.id'))

    children = relationship("Category", backref=backref('parent', remote_side=[id]))
    products = relationship("Product", back_populates="category")
