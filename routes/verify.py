from itertools import count
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List, Optional
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
from config import days
import config
from datetime import date, datetime
from models.team import Team

route = APIRouter(prefix="/verify", tags=["Verify"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.patch("/{unique_id}", status_code=204)
def verify_pass(
    unique_id: str,
    token: str = Depends(oauth2_scheme),
    count_of_bands: int | None = None,
):
    # try:
        if check_token(token):
            passes = config.regalia22_db["pass"]
            if passes.count_documents({"_id": unique_id}) == 1:
                today = str(date.today())
                today = today.split("-")[2]
                if count_of_bands:
                    if today == config.days[0]:
                        if passes.count_documents({
                                "_id": unique_id,
                                "day_1_validity": {"$regex": "^$"},
                            }) == 1:
                            passes.update_one(
                                {
                                    "_id": unique_id
                                },
                                {
                                    "$set": {
                                        "day_1_validity": str(datetime.now()),
                                        "count_of_bands": count_of_bands,
                                    }
                                },
                            )
                        else:
                            raise HTTPException(
                                status_code=406,
                                detail="already verified",
                            )
                    elif today == config.days[1]:
                        if passes.count_documents({
                                "_id": unique_id,
                                "day_2_validity": {"$regex": "^$"},
                            }) == 1:
                            passes.update_one(
                                {
                                    "_id": unique_id
                                },
                                {
                                    "$set": {
                                        "day_2_validity": str(datetime.now()),
                                        "count_of_bands": count_of_bands,
                                    }
                                },
                            )
                        else:
                            raise HTTPException(
                                status_code=406,
                                detail="already verified",
                            )
                else:
                    if today == config.days[0]:
                        if passes.count_documents({
                                "_id": unique_id,
                                "day_1_validity": {"$regex": "^$"},
                            }) == 1:
                            passes.update_one(
                                {
                                    "_id": unique_id
                                },
                                {
                                    "$set": {
                                        "day_1_validity": str(datetime.now()),
                                    }
                                },
                            )
                        else:
                            raise HTTPException(
                                status_code=406,
                                detail="already verified",
                            )
                    elif today == config.days[1]:
                        if passes.count_documents({
                                "_id": unique_id,
                                "day_2_validity": {"$regex": "^$"},
                            }) == 1:
                            passes.update_one(
                                {
                                    "_id": unique_id
                                },
                                {
                                    "$set": {
                                        "day_2_validity": str(datetime.now()),
                                    }
                                },
                            )
                        else:
                            raise HTTPException(
                                status_code=406,
                                detail="already verified",
                            )
            else:
                return {"message": "not found"}
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    # except Exception as e:
    #     raise HTTPException(status_code=409, detail=str(e))
