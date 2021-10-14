from typing import Any, List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from sqlalchemy.orm.session import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


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
    category = crud.category.create(db=db, obj_in=category_in)
    return category
