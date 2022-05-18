from datetime import datetime
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

from models.guest import Guest

route = APIRouter(prefix="/guests", tags=["guest"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.get("/", status_code=200)
def get_guests(token: str = Depends(oauth2_scheme)):
    if check_token(token):
        guests = config.regalia22_db["guest"]
        guests = list(guests.find())
        return guests
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@route.post("/", status_code=201)
def add_guest(guest: Guest = Body(...), token: str = Depends(oauth2_scheme)):
    try:
        if check_token(token):
            guests = config.regalia22_db["guest"]
            guests.insert_one({"name": guest.name, "_id": str(datetime.now())})
            return guest
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
