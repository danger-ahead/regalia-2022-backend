from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config
from models.regalia_pass import Pass
from unique_id import generate_unique_id


route = APIRouter(prefix="/pass", tags=["pass"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@route.post("/", status_code=201)
def add_pass(regalia_pass:Pass,token: str = Depends(oauth2_scheme)):
    try:
        if check_token(token):
            passes = config.regalia22_db["pass"]
            uni_id = generate_unique_id()
            passes.insert_one(
                {
                    "_id": uni_id,
                    "name": regalia_pass.name,
                    "phone_number": regalia_pass.phone_number,
                    "email": regalia_pass.email,
                    "allowed":regalia_pass.allowed,
                    "day_1_validity":regalia_pass.day_1_validity,
                    "day_2_validity":regalia_pass.day_2_validity,
                    "roll_number":regalia_pass.roll_number
                }
            )
            return regalia_pass
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
