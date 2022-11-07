from typing import List
from pydantic import BaseModel


class RegisterSchema(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:str
    access_info:List[str]
    password:str


class ShowRegisterSchema(BaseModel):
    first_name:str
    last_name:str
    username:str
    email:str
    access_info:List[str]

    class Config:
        orm_mood=True


class LoginSchema(BaseModel):
    username:str
    password:str


class FloorPostSchema(BaseModel):
    name:str
    slug:str
    time:str
    price:str

    class Config:
        orm_mood=True


class NftPostSchema(BaseModel):
    name:str
    slug:str
    time:str
    price:str

    class Config:
        orm_mood=True


class LoanPostSchema(BaseModel):
    name:str
    slug:str
    time:str
    price:str

    class Config:
        orm_mood=True
