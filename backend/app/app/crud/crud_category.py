from typing import Any, List, Optional
from app.models import Category
from app.models.product import Product
from app.schemas import CategoryCreate, CategoryUpdate
from sqlalchemy.orm.session import Session
from .base import CRUDBase


class CRUDCategory(CRUDBase[Category, CategoryCreate, CategoryUpdate]):
    
    def get(self, db: Session, id: Any) -> Optional[Category]:
        return db.query(self.model).outerjoin(Product).filter(self.model.id == id).first()
        
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> List[Category]:
        return db.query(self.model).filter_by(parent_id=None).offset(skip).limit(limit).all()


category = CRUDCategory(Category)
