from typing import List

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.order import select_order_by_id, insert_order, select_order_by_status, update_order
from app.core.order_detail import select_order_detail_by_order_id
from app.models.entities.order import Order
from app.models.enums import OrderType, get_status_to_int, get_status_to_order_type, get_status_str_to_order_type
from app.models.entities.order_detail import OrderDetail
from app.schemas.order_detail_schema import OrderDetailSchema
from app.schemas.order_schema import OrderSchema, OrderSchemaComplete


def get_order_id(db: Session, id: int):
    get = select_order_by_id(db, id)
    if get:
        return transform_model_to_schema(get)
    raise HTTPException(status_code=404, detail="Order not found")


def get_order_by_status(db: Session, status: str):
    sts = get_status_to_int(get_status_str_to_order_type(status))
    get = select_order_by_status(db, sts)
    if get:
        return tranform_to_list(get)
    raise HTTPException(status_code=204, detail="Order is empty")


def create_order(db: Session, order: OrderSchema):
    ###
    ### check stock
    ###
    # get_product =
    # if get_product:
    #     raise HTTPException(status_code=409, detail="sold out")
    new_order = Order(status=get_status_to_int(OrderType.PENDING))
    return transform_model_to_schema(insert_order(db, new_order), None)


def change_order(id: int, status: str, db: Session):
    get_order = select_order_by_id(db, id)
    if get_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    sts = get_status_to_int(get_status_str_to_order_type(status))
    get_order.status = sts
    return transform_model_to_schema(update_order(db, get_order))


def transform_model_to_schema(get: Order)->OrderSchemaComplete:
    p: List[OrderDetailSchema] = []
    for product in get.products:
        p.append(OrderDetailSchema(order=product.order_id, status=get_status_to_order_type(product.status),
                                       quantity=product.quantity, product=product.product.name))
    return OrderSchemaComplete(id=get.id, status=get_status_to_order_type(get.status), products=p)


def tranform_to_list(list:List[Order])->List[OrderSchemaComplete]:
    res: List[OrderSchemaComplete] = []
    for get in list:
        p: List[OrderDetailSchema] = []
        for product in get.products:
            p.append(OrderDetailSchema(order=product.order_id, status=get_status_to_order_type(product.status),
                                   quantity=product.quantity, product=product.product.name))
        res.append(OrderSchemaComplete(id=get.id, status=get_status_to_order_type(get.status), products=p))
    return res
