from typing import Any, List
from app import crud, models, schemas
from app.api import deps
from fastapi import APIRouter, UploadFile, HTTPException, File, Depends
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.post("/{product_id}", response_model=List[schemas.Image])
def upload_image(
    *,
    db: Session = Depends(deps.get_db),
    product_id: int,
    images: List[UploadFile] = File(...),
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Upload images for product.
    """
    product = crud.product.get(db=db, id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = crud.image.create_multi(db=db, images=images, product_id=product_id)
    return product
