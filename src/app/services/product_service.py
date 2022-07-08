from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.product import select_product_by_id, insert_product, select_product_by_sku, update_product
from app.models.entities.product import Product
from app.schemas.product_schema import ProductSchema


def get_product_id(db: Session, id: int):
    get = select_product_by_id(db, id)
    if get:
        return transform_model_to_schema(get)
    raise HTTPException(status_code=404, detail="Product not found")


def create_product(db: Session, product: ProductSchema):
    get_product = select_product_by_sku(db, product.sku)
    if get_product:
        raise HTTPException(status_code=409, detail="Product already registered")
    new_product = Product(sku=product.sku, name=product.name, stock=product.stock)
    return transform_model_to_schema(insert_product(db, new_product))


def get_product_by_sku(db: Session, sku: str):
    get = select_product_by_sku(db, sku)
    if get:
        return transform_model_to_schema(get)
    raise HTTPException(status_code=404, detail="Product not found")


def change_product(id: int, db: Session, product: ProductSchema):
    get_product = select_product_by_id(db, id)
    if get_product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    get_product.sku = product.sku
    get_product.name = product.name
    get_product.stock = product.stock
    return transform_model_to_schema(update_product(db, get_product))


def transform_model_to_schema(product: Product):
    return ProductSchema(sku=product.sku, name=product.name, stock=product.stock)