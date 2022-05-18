from datetime import datetime
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

from models.unpaid_pass import Unpaid_pass

route = APIRouter(prefix="/unpaid_pass", tags=["unpaid_pass"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@route.post("/", status_code=201)
def add_unpaid_pass(
    unpaid_pass: Unpaid_pass = Body(...), token: str = Depends(oauth2_scheme)
):
    try:
        if check_token(token):
            unpaid_passes = config.regalia22_db["unpaid_pass"]
            unpaid_passes.insert_one(
                {
                    "name": unpaid_pass.name,
                    "roll_number": unpaid_pass.roll_number,
                    "passing_year":unpaid_pass.passing_year,
                    "department":unpaid_pass.department,
                    "_id": str(datetime.now()),
                }
            )
            return unpaid_pass
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
