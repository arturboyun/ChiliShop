import uuid
import shutil
from pathlib import Path
from typing import Any, List

from app.core.config import settings
from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.datastructures import URL
from .base import CRUDBase

from app.models.image import Image
from app.schemas.image import ImageCreate, ImageUpdate


class CRUDImage(CRUDBase[Image, ImageCreate, ImageUpdate]):
    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100, base_url: URL
    ) -> List[Image]:
        images = db.query(self.model).offset(skip).limit(limit).all()
        for image in images:
            image.src = str(base_url)[:-1] + image.src
        return images

    def create(self, db: Session, *, image: UploadFile, product_id: int) -> Image:
        db_image = self.save_image_to_media(db, image, product_id)
        return db_image

    def save_image_to_media(self,db: Session, image: UploadFile, product_id: int) -> Image:
        """Saves the image to media folder and returns the path"""
        file_extension = image.filename.split('.')[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        save_path = Path(settings.IMAGES_PATH) / unique_filename

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        db_image = Image(src=str(save_path), product_id=product_id).save(db)
        return db_image


image = CRUDImage(Image)
