import logging
from typing import Any, List, Optional

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.datastructures import URL

from app.crud.base import CRUDBase
from app.models import Category
from app.models.image import Image
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):

    def get_with_images(self, db: Session, id: Any, base_url: URL) -> Optional[Product]:
        db_obj = db.query(self.model).outerjoin(Image).filter(self.model.id == id).first()
        if db_obj:
            for image in db_obj.images:
                image.src = str(base_url)[:-1] + image.src
        return db_obj

    def get_by_slug(self, db: Session, slug: str) -> Optional[Product]:
        db_obj = db.query(self.model).filter(self.model.slug == slug).first()
        return db_obj

    def get_by_slug_with_images(self, db: Session, slug: str, base_url: URL) -> Optional[Product]:
        db_obj = db.query(self.model).outerjoin(Image).filter(self.model.slug == slug).first()
        if db_obj:
            for image in db_obj.images:
                image.src = str(base_url)[:-1] + image.src
        return db_obj

    def get_multi(
            self, db: Session, *, skip: int = 0, limit: int = 100, base_url: URL
    ) -> List[Product]:
        db_objs = db.query(self.model).outerjoin(Image).offset(skip).limit(limit).all()
        for db_obj in db_objs:
            for image in db_obj.images:
                image.src = str(base_url)[:-1] + image.src
        return db_objs

    def get_multi_by_category_id(
            self, db: Session, *, category_id: int, skip: int = 0, limit: int = 100, base_url: URL
    ) -> List[Product]:
        db_objs = db.query(self.model).outerjoin(Image).join(Category)\
            .filter(Category.id == category_id)\
            .offset(skip).limit(limit).all()
        for db_obj in db_objs:
            for image in db_obj.images:
                image.src = str(base_url)[:-1] + image.src
        return db_objs

    def get_multi_by_category_slug(
            self, db: Session, *, category_slug: int, skip: int = 0, limit: int = 100, base_url: URL
    ) -> List[Product]:
        db_objs = db.query(self.model).outerjoin(Image).join(Category)\
            .filter(Category.slug == category_slug)\
            .offset(skip).limit(limit).all()
        for db_obj in db_objs:
            for image in db_obj.images:
                image.src = str(base_url)[:-1] + image.src
        return db_objs

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
