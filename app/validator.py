from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    surname: str


class UserData(BaseModel):
    id: int
    name: str
    surname: str

class EventData(BaseModel):
    remain: int
    title: str
    description: str
    price: int

class CouponData(BaseModel):
    event_id: int
