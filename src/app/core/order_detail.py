from sqlalchemy.orm import Session

from app.models.entities.order_detail import OrderDetail
from app.models.entities.product import Product


def select_order_detail_by_status(db: Session, status: int):
    return db.query(OrderDetail).filter(OrderDetail.status == status)


def select_order_detail_by_order_id(db: Session, order_id: int):
    return db.query(OrderDetail).join(Product, Product.id == OrderDetail.product_id).filter(OrderDetail.order_id == order_id).all()


def insert_order(db: Session, order: OrderDetail):
    db.add(order)
    db.commit()
    return order


def update_order_detail(db: Session, order: OrderDetail):
    db.commit()
    return order

