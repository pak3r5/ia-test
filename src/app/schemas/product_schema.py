from pydantic import BaseModel, Field, conint


class ProductSchema(BaseModel):
    """
    Product Schema response/request for this example

    Attributes:
        sku: String unique identifier of product.
        name: String name/ description of product.
        stock: Integer containing the stock of product.
    """
    sku: str = Field(..., description='SKU of product')
    name: str = Field(..., description='Name of product')
    stock: conint(gt=0, lt=999999) = Field(..., description='Stock of product')

    class Config:
        the_schema = {
            'example': {
                'sku': 'ABC123',
                'name': 'Coca-Cola',
                'stock': 0
            }
        }
