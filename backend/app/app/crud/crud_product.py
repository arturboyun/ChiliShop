import logging
from typing import Any, List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.image import Image
from app.schemas.product import ProductCreate, ProductUpdate
from starlette.datastructures import URL

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):

    def get(self, db: Session, id: Any, base_url: URL) -> Optional[Product]:
        product = db.query(self.model).outerjoin(Image).filter(self.model.id == id).first()
        for image in product.images:
                image.src = str(base_url)[:-1] + image.src
        return product

    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, base_url: URL
    ) -> List[Product]:
        products = db.query(self.model).outerjoin(Image).offset(skip).limit(limit).all()
        logger.info(products)
        for product in products:
            for image in product.images:
                image.src = str(base_url)[:-1] + image.src
        return products
        
    def create_with_owner(
        self, db: Session, *, obj_in: ProductCreate, creator_id: int
    ) -> Product:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, creator_id=creator_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


product = CRUDProduct(Product)
