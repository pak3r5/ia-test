from pydantic import BaseModel


class OrderDetail(BaseModel):
    id: int
    order_id: int
    status: int
    quantity: int
    product_id: int

    class Config:
        orm_mode = True
