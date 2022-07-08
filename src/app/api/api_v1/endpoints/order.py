from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.sql_app.database import get_db
from app.schemas.order_schema import OrderSchema, OrderSchemaComplete
from app.services.order_service import get_order_id, create_order, get_order_by_status, change_order

router = APIRouter()


@router.post("/", response_model=OrderSchemaComplete, status_code=201)
def new_order(body: OrderSchema, db: Session = Depends(get_db)):
    """
        API Endpoint for Create new order
    """
    return create_order(db, body)


@router.get("/{order_id}", response_model=OrderSchemaComplete, status_code=200)
def search_order_by_id(order_id: int, db: Session = Depends(get_db)):
    """
        API Endpoint for Get order by id
    """
    return get_order_id(db, order_id)


@router.get("", response_model=List[OrderSchemaComplete], status_code=200)
def search_order_by_status(status: str, db: Session = Depends(get_db)):
    """
        API Endpoint for Get orders by status
    """
    return get_order_by_status(db, status)


@router.put("/{order_id}", response_model=OrderSchema, status_code=200)
def edit_user(order_id: int, status: str, db: Session = Depends(get_db)):
    """
        API Endpoint for change status of order
    """
    return change_order(order_id, status, db)