from pydantic import BaseModel, Field


class UserSchema(BaseModel):
    """
    User Schema response/request for this example

    Attributes:
        name: String name of user.
        last_name: String last name of user.
        username: String unique username of user.
        password: String encrypted.
    """
    name: str = Field(..., description='Name of user')
    last_name: str = Field(..., description='Last name of user')
    username: str = Field(..., description='Username of user')
    password: str = Field(..., description='Password of user')

    class Config:
        the_schema = {
            'example': {
                'name': 'Juan',
                'last_name': 'Perez',
                'username': '1234',
                'password': 'password',
            }
        }
