from typing import Optional

from sqlalchemy.orm import Session

from app import crud, models
from app.schemas.product import ProductCreate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def create_random_product(db: Session, *, creator_id: Optional[int] = None) -> models.Product:
    if creator_id is None:
        user = create_random_user(db)
        creator_id = user.id
    title = random_lower_string()
    description = random_lower_string()
    item_in = ProductCreate(title=title, description=description, id=id)
    return crud.product.create_with_owner(db=db, obj_in=item_in, creator_id=creator_id)
