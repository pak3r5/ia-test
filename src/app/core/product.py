from sqlalchemy.orm import Session

from app.models.entities.product import Product


def select_product_by_id(db: Session, id: int):
    return db.query(Product).filter(Product.id == id).first()


def select_product_by_sku(db: Session, sku: str):
    return db.query(Product).filter(Product.sku == sku).first()


def insert_product(db: Session, product: Product):
    db.add(product)
    db.commit()
    return product


def update_product(db: Session, product: Product):
    db.commit()
    return product
