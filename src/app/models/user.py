from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True
