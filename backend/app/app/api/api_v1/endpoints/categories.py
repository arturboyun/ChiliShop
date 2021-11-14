import logging
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from slugify import slugify
from sqlalchemy.orm.session import Session

from app import crud, models, schemas
from app.api import deps
from app.schemas import Msg
from app.utils import random_lower_string

router = APIRouter()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router.get("/", response_model=List[schemas.Category])
def read_categories(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve categories.
    """
    categories = crud.category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.get("/{id}", response_model=schemas.CategoryDetail)
def read_category(*, db: Session = Depends(deps.get_db), id: int) -> Any:
    """
    Retrieve category.
    """
    category = crud.category.get(db, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category


@router.get("/slug/{slug}", response_model=schemas.CategoryDetail)
def read_category_by_slug(*, db: Session = Depends(deps.get_db), slug: str) -> Any:
    """
    Retrieve category by slug.
    """
    category = crud.category.get_by_slug(db, slug)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    return category


@router.post('/', response_model=schemas.Category)
def create_category(
    *, db: Session = Depends(deps.get_db),
    category_in: schemas.CategoryCreate,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Create new category.
    """
    if category_in.parent_id:
        parent_category = crud.category.get(db=db, id=category_in.parent_id)
        if not parent_category:
            raise HTTPException(404, 'Parent category not found')

    if not category_in.slug:
        category_in.slug = slugify(category_in.name)

    category = crud.category.get_by_slug(db=db, slug=category_in.slug)
    if category:
        category_in.slug += "-" + random_lower_string(8)

    print(str(category_in.json()))

    category = crud.category.get_by_slug(db=db, slug=category_in.slug)
    if category:
        raise HTTPException(400, 'Category with this slug already exists.')

    category = crud.category.create(db=db, obj_in=category_in)
    return category


@router.put("/{id}", response_model=schemas.Category)
def update_category(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    category_in: schemas.CategoryUpdate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update an category.
    """
    if category_in.parent_id:
        parent_category = crud.category.get(db=db, id=category_in.parent_id)
        if not parent_category:
            raise HTTPException(404, 'Parent category not found')

    category = crud.category.get(db, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")

    category = crud.category.update(db=db, db_obj=category, obj_in=category_in)
    return category


@router.delete('/{id}', response_model=Msg)
def delete_category(
    *,
    db: Session = Depends(deps.get_db),
    id: Any,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete category.
    """
    category = crud.category.get(db=db, id=id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found.")
    category = crud.category.remove(db=db, id=id)
    return Msg(msg='Category Deleted')
