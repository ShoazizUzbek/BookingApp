from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    surname: str


class UserData(BaseModel):
    id: int
    name: str
    surname: str
