from typing import List, Optional

from pydantic import BaseModel, Field

from app.models.enums import OrderType
from app.schemas.details_schema import Detail


class OrderSchema(BaseModel):
    """
    Order Schema response/request for this example

    Attributes:
        status: OrderType of order status.
        quantity: Integer of product to add in the order.
        product: String sku of product.
    """
    status: OrderType = Field(..., description='Status of product')
    products: Optional[List[Detail]] = Field(..., description='List of detail')

    class Config:
        the_schema = {
            'example': {
                'status': 'PENDING',
                'products': [{
                    'quantity': '1',
                    'product': 'ABC123'
                }]
            }
        }


class OrderSchemaComplete(OrderSchema):
    """
    Order Schema response/request for this example

    Attributes:
        id: ID of order.
        status: OrderType of order status.
        quantity: Integer of product to add in the order.
        product: String sku of product.
    """
    id: int = Field(..., description='ID of product')

    class Config:
        the_schema = {
            'example': {
                'id': '1',
                'status': 'PENDING',
                'products': [{
                    'quantity': '1',
                    'product': 'ABC123'
                }]
            }
        }
