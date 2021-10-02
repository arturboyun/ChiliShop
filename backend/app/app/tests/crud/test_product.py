from sqlalchemy.orm import Session

from app import crud
from app.schemas.product import ProductCreate, ProductUpdate
from app.tests.utils.user import create_random_user
from app.tests.utils.utils import random_lower_string


def test_create_product(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    product_in = ProductCreate(title=title, description=description)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, creator_id=user.id)
    assert product.title == title
    assert product.description == description
    assert product.creator_id == user.id


def test_get_product(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    product_in = ProductCreate(title=title, description=description)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, creator_id=user.id)
    stored_product = crud.product.get(db=db, id=product.id)
    assert stored_product
    assert product.id == stored_product.id
    assert product.title == stored_product.title
    assert product.description == stored_product.description
    assert product.creator_id == stored_product.creator_id


def test_update_product(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    product_in = ProductCreate(title=title, description=description)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, creator_id=user.id)
    description2 = random_lower_string()
    product_update = ProductUpdate(description=description2)
    product2 = crud.product.update(db=db, db_obj=product, obj_in=product_update)
    assert product.id == product2.id
    assert product.title == product2.title
    assert product2.description == description2
    assert product.creator_id == product2.creator_id


def test_delete_product(db: Session) -> None:
    title = random_lower_string()
    description = random_lower_string()
    product_in = ProductCreate(title=title, description=description)
    user = create_random_user(db)
    product = crud.product.create_with_owner(db=db, obj_in=product_in, creator_id=user.id)
    product2 = crud.product.remove(db=db, id=product.id)
    product3 = crud.product.get(db=db, id=product.id)
    assert product3 is None
    assert product2.id == product.id
    assert product2.title == title
    assert product2.description == description
    assert product2.creator_id == user.id
