from pydantic import BaseModel


class Order(BaseModel):
    id: int
    status: int

    class Config:
        orm_mode = True
