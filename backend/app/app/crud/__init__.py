from .crud_product import product
from .crud_user import user
from .crud_image import image
from .crud_category import category

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Product
# from app.schemas.item import ProductCreate, ProductUpdate

# item = CRUDBase[Product, ProductCreate, ProductUpdate](Product)
