from pydantic import BaseModel, Field


class Good(BaseModel):
    g_id: int
    name: str = Field(max_length=32)
    description: str = Field(max_length=256)
    price: float


class GoodIn(BaseModel):
    name: str = Field(max_length=32)
    description: str = Field(max_length=256)
    price: float


class Order(BaseModel):
    o_id: int
    u_id: int
    data: str = Field(max_length=10)
    status: str = Field(max_length=16)


class OrderIn(BaseModel):
    u_id: int
    data: str = Field(max_length=10)
    status: str = Field(max_length=16)


class User(BaseModel):
    u_id: int
    name: str = Field(max_length=16)
    sur_name: str = Field(max_length=16)
    email: str = Field(max_length=16)
    password: str = Field(max_length=16)


class UserIn(BaseModel):
    name: str = Field(max_length=16)
    sur_name: str = Field(max_length=16)
    email: str = Field(max_length=16)
    password: str = Field(max_length=16)
