from fastapi import APIRouter, Depends, HTTPException
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config
from datetime import date, datetime

route = APIRouter(prefix="/verify", tags=["Verify"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.patch("/{unique_id}", status_code=200)
def verify_pass(
    unique_id: str,
    token: str = Depends(oauth2_scheme),
    count_of_bands: int | None = None,
):
    if check_token(token):
        passes = config.regalia22_db["pass"]
        today = str(date.today())
        today = today.split("-")[2]
        if count_of_bands:
            if today == config.days[0]:
                if (
                    passes.count_documents(
                        {
                            "_id": unique_id,
                            "day_1_validity": {"$regex": "^$"},
                        }
                    )
                    == 1
                ):
                    passes.update_one(
                        {"_id": unique_id},
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
                        detail="already verified or not found",
                    )
            elif today == config.days[1]:
                if (
                    passes.count_documents(
                        {
                            "_id": unique_id,
                            "day_2_validity": {"$regex": "^$"},
                        }
                    )
                    == 1
                ):
                    passes.update_one(
                        {"_id": unique_id},
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
                        detail="already verified or not found",
                    )
            else:
                return {"message": "invalid date"}

        else:
            if today == config.days[0]:
                if (
                    passes.count_documents(
                        {
                            "_id": unique_id,
                            "day_1_validity": {"$regex": "^$"},
                        }
                    )
                    == 1
                ):
                    passes.update_one(
                        {"_id": unique_id},
                        {
                            "$set": {
                                "day_1_validity": str(datetime.now()),
                            }
                        },
                    )
                else:
                    raise HTTPException(
                        status_code=406,
                        detail="already verified or not found",
                    )
            elif today == config.days[1]:
                if (
                    passes.count_documents(
                        {
                            "_id": unique_id,
                            "day_2_validity": {"$regex": "^$"},
                        }
                    )
                    == 1
                ):
                    passes.update_one(
                        {"_id": unique_id},
                        {
                            "$set": {
                                "day_2_validity": str(datetime.now()),
                            }
                        },
                    )
                else:
                    raise HTTPException(
                        status_code=406,
                        detail="already verified or not found",
                    )
            else:
                return {"message": "invalid date"}

        return {"message": "verified"}

    else:
        raise HTTPException(status_code=401, detail="unauthorized")
