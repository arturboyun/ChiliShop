import uuid
import shutil
from pathlib import Path
from typing import List

from app.core.config import settings
from fastapi import UploadFile
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from .base import CRUDBase

from app.models.image import Image
from app.schemas.image import ImageCreate, ImageUpdate


class CRUDImage(CRUDBase[Image, ImageCreate, ImageUpdate]):

    def create_multi(self, db: Session, *, images: List[UploadFile], product_id: int) -> List[Image]:
        images_list = []
        for image in images:
            db_image = self.save_image_to_media(db, image, product_id)
            images_list.append(db_image)
        return images_list

    def save_image_to_media(self,db: Session, image: UploadFile, product_id: int) -> List[Image]:
        """Saves the image to media folder and returns the path"""
        file_extension = image.filename.split('.')[-1]
        unique_filename = f"{uuid.uuid4()}.{file_extension}"
        save_path = Path(settings.IMAGES_PATH) / unique_filename

        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        image_db_obj = Image(src=str(save_path), product_id=product_id).save(db)
        return image_db_obj


image = CRUDImage(Image)
