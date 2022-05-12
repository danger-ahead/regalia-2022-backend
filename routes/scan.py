from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

route = APIRouter(prefix="/scan", tags=["scan"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@route.get("/{id}", status_code=200)
def get_pass(id:str,token: str = Depends(oauth2_scheme)):
    if check_token(token):
        passes = config.regalia22_db["pass"]
        regalia_pass = passes.find_one({"_id": id})
        if regalia_pass is None:
            raise HTTPException(status_code=401, detail="Not found")
        return regalia_pass
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
