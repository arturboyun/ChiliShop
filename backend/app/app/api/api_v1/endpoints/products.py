import logging
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from slugify import slugify
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from starlette.requests import Request

from app.utils import random_lower_string

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[schemas.Product])
def read_products(
    request: Request,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve products.
    """
    products = crud.product.get_multi(db, skip=skip, limit=limit, base_url=request.base_url)
    return products


@router.get("/category/{category_id}", response_model=List[schemas.Product])
def read_products_by_category_id(
    request: Request,
    category_id: int,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve products by category id.
    """
    products = crud.product.get_multi_by_category_id(
        db, category_id=category_id, skip=skip, limit=limit, base_url=request.base_url
    )
    return products


@router.get("/category/slug/{category_slug}", response_model=List[schemas.Product])
def read_products_by_category_slug(
    request: Request,
    category_slug: str,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve products by category slug.
    """
    products = crud.product.get_multi_by_category_slug(
        db, category_slug=category_slug, skip=skip, limit=limit, base_url=request.base_url
    )
    return products


@router.post("/", response_model=schemas.Product)
def create_product(
    *,
    db: Session = Depends(deps.get_db),
    product_in: schemas.ProductCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new product.
    """
    if not crud.category.get(db=db, id=product_in.category_id):
        raise HTTPException(status_code=404, detail="Category not found")

    if not product_in.slug:
        product_in.slug = slugify(product_in.title)

    product = crud.product.get_by_slug(db=db, slug=product_in.slug)
    if product:
        product_in.slug += random_lower_string(8)

        product = crud.product.get_by_slug(db=db, slug=product_in.slug)
        if product:
            raise HTTPException(400, 'Category with this slug already exists.')

    product = crud.product.create_with_owner(db=db, obj_in=product_in, creator_id=current_user.id)
    return product


@router.put("/{id}", response_model=schemas.Product)
def update_product(
    *,
    request: Request,
    db: Session = Depends(deps.get_db),
    id: int,
    product_in: schemas.ProductUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    logger.info(product_in.json())

    if product_in.category_id is not None:
        category = crud.category.get(db=db, id=product_in.category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

    product = crud.product.update(db=db, db_obj=product, obj_in=product_in)
    return product


@router.get("/{id}", response_model=schemas.Product)
def read_product(
    *,
    request: Request,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get product by ID.
    """
    product = crud.product.get_with_images(db=db, id=id, base_url=request.base_url)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/slug/{slug}", response_model=schemas.Product)
def read_product_by_slug(
    *,
    request: Request,
    db: Session = Depends(deps.get_db),
    slug: str,
) -> Any:
    """
    Get product by SLUG.
    """
    product = crud.product.get_by_slug_with_images(db=db, slug=slug, base_url=request.base_url)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.delete("/{id}", response_model=schemas.Product)
def delete_product(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete an product.
    """
    product = crud.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.product.remove(db=db, id=id)
    return product
