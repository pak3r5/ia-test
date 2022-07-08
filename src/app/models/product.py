from pydantic import BaseModel


class Product(BaseModel):
    id: int
    sku: str
    name: str
    stock: int

    class Config:
        orm_mode = True
