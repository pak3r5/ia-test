from sqlalchemy.orm import Session

from app.models.entities.order import Order


def select_order_by_status(db: Session, status: int):
    return db.query(Order).filter(Order.status == status).all()


def select_order_by_id(db: Session, id: int):
    return db.query(Order).filter(Order.id == id).first()


def insert_order(db: Session, order: Order):
    db.add(order)
    db.commit()
    return order


def update_order(db: Session, order: Order):
    db.commit()
    return order


def select_order(db: Session):
    return db.query(Order)

