from typing import Any, List
from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, UploadFile, HTTPException, File, Depends
from sqlalchemy.orm.session import Session
from starlette.requests import Request

router = APIRouter()


@router.get("/", response_model=List[schemas.Image])
def read_images(
    request: Request,
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve images.
    """
    images = crud.image.get_multi(db, skip=skip, limit=limit, base_url=request.base_url)
    return images


@router.post("/{product_id}", response_model=schemas.Image)
def upload_image(
    *,
    request: Request,
    db: Session = Depends(deps.get_db),
    product_id: int,
    image: UploadFile = File(...),
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Upload image for product.
    """
    product = crud.product.get(db=db, id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    image = crud.image.create(db=db, image=image, product_id=product_id)
    image.src = f'{str(request.base_url)[:-1]}{image.src}'
    return image


@router.delete("/{id}", response_model=schemas.Image)
def delete_image(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user)
) -> Any:
    """
    Delete image.
    """
    image = crud.image.get(db=db, id=id)
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")
    image = crud.image.remove(db=db, id=id)
    return image
