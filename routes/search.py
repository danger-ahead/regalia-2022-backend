from fastapi import APIRouter, Body, Depends, HTTPException
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config
from models.other_body import OtherBody


route = APIRouter(prefix="/search", tags=["Search"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.get("/", status_code=200)
def search_email(other_body:OtherBody = Body(...) , token: str = Depends(oauth2_scheme)):
    if check_token(token):
        pass_obj = config.regalia22_db["pass"]

        pass_obj = pass_obj.find_one({"roll_number": {"$regex": other_body.roll_no , "$options":"i"}})

        if pass_obj is None:
            return {"message": "No pass found"}
        return pass_obj

    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
