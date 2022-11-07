from fastapi import Depends, status
from typing import List, Dict
from sqlalchemy.orm import Session

from main import app

from settings.dbconfig import get_db
from settings.utlitis import Hash

from .schemas import *
from .models import User


@app.post('/',status_code=status.HTTP_201_CREATED,response_model=ShowRegisterSchema)
def register(request: RegisterSchema, db: Session = Depends(get_db)):
    new_user = User(
        first_name=request.first_name,
        last_name=request.last_name,
        username=request.username,
        access_info=str(request.access_info),
        email=request.email,
        hashed_password=Hash.make_hash(request.password),
        is_active=True
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    # return {
    #     "message": "You are successfully registered",
    #     "data": 
    # }
    return Dict(new_user)


@app.post('/login/', status_code=status.HTTP_201_CREATED)
def login(request: LoginSchema, db: Session = Depends(get_db)):
    return {"message": "Login Success!!"}


@app.get('/logout/')
def logout():
    return {"message": "Logout Success!"}


@app.get('/floor/', response_model=List[FloorPostSchema])
def floor():
    return {"message": "Get to floor"}


@app.post('/floor/', status_code=status.HTTP_201_CREATED)
def floor():
    return {"message": "Post to floor"}


@app.get('/nft/', response_model=List[NftPostSchema])
def nft():
    return {"message": "Post to nft"}


@app.post('/nft/', status_code=status.HTTP_201_CREATED)
def nft():
    return {"message": "Post to nft"}


@app.get('/loan/', response_model=List[LoanPostSchema])
def loan():
    return {"message": "Post to loan"}


@app.post('/loan/', status_code=status.HTTP_201_CREATED)
def loan():
    return {"message": "Post to loan"}
