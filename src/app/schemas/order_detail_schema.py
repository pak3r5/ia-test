from pydantic import BaseModel, Field

from app.models.enums import OrderType


class OrderDetailSchema(BaseModel):
    """
    Order Detail Schema response/request for this example

    Attributes:
        order: Integer of order.
        status: OrderType of order status.
        quantity: Integer of product to add in the order.
        product: String sku of product.
    """
    order: int = Field(..., description='Order Parent')
    status: OrderType = Field(..., description='Status of product')
    quantity: int = Field(..., description='Quantity of product')
    product: str = Field(..., description='SKU of Product list')

    class Config:
        the_schema = {
            'example': {
                'order': '1',
                'status': 'PENDING',
                'quantity': '1',
                'product': 'ABC123',
            }
        }
