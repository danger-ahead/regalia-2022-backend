from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

route = APIRouter(prefix="/search", tags=["Search"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.get("/{email}", status_code=200)
def search_email(email: str, token: str = Depends(oauth2_scheme)):
    if check_token(token):
        pass_obj = config.regalia22_db["pass"]

        pass_obj = pass_obj.find_one({"email": email})

        if pass_obj is None:
            return {"message": "No pass found"}
        return pass_obj

    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
