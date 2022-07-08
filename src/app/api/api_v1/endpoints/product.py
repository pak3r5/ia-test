from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.sql_app.database import get_db
from app.schemas.product_schema import ProductSchema
from app.services.product_service import get_product_id, create_product, get_product_by_sku, change_product

router = APIRouter()


@router.post("/", response_model=ProductSchema, status_code=201)
def new_product(body: ProductSchema, db: Session = Depends(get_db)):
    """
        API Endpoint for Create new product
    """
    return create_product(db, body)


@router.get("/{product_id}", response_model=ProductSchema, status_code=200)
def search_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """
        API Endpoint for Get product by id
    """
    return get_product_id(db, product_id)


@router.get("", response_model=ProductSchema, status_code=200)
def search_product_by_sku(sku: str, db: Session = Depends(get_db)):
    """
        API Endpoint for Get product by sku
    """
    return get_product_by_sku(db, sku)


@router.put("/{product_id}", response_model=ProductSchema, status_code=200)
def edit_product(product_id: int, body: ProductSchema, db: Session = Depends(get_db)):
    """
        API Endpoint for Update product
    """
    return change_product(product_id, db, body)