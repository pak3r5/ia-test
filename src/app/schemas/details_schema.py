from pydantic import BaseModel, Field


class Detail(BaseModel):
    """
    Order Schema response/request for this example

    Attributes:
        quantity: Integer of product to add in the order.
        product: String sku of product.
    """
    quantity: int = Field(..., description='Quantity of product')
    product: str = Field(..., description='SKU of product')

    class Config:
        the_schema = {
            'example': {
                'quantity': '1',
                'product': 'ABC123'
            }
        }
