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
        if today == config.days[0]:
            pass_obj = passes.find_one({"_id": unique_id})
            if pass_obj["day_1_validity"] == "":
                passes.update_one(
                    {"_id": unique_id}, {"$set": {"day_1_validity": str(datetime.now())}}
                )

            if pass_obj["count_of_bands_day_1"] == pass_obj["allowed"]:
                raise HTTPException(status_code=401, detail="Exhausted")
            elif (
                pass_obj["count_of_bands_day_1"] + count_of_bands <= pass_obj["allowed"]
            ):
                passes.update_one(
                    {"_id": unique_id},
                    {"$set": {
                        "count_of_bands_day_1": pass_obj["count_of_bands_day_1"]
                        + count_of_bands
                    },}
                )
            elif (
                pass_obj["count_of_bands_day_1"] + count_of_bands > pass_obj["allowed"]
            ):
                raise HTTPException(status_code=401, detail="Not Allowed")

        elif today == config.days[1]:
            pass_obj = passes.find_one({"_id": unique_id})
            if pass_obj["day_2_validity"] == "":
                passes.update_one(
                    {"_id": unique_id}, {"$set": {"day_2_validity": str(datetime.now())}}
                )

            if pass_obj["count_of_bands_day_2"] == pass_obj["allowed"]:
                raise HTTPException(status_code=401, detail="Exhausted")
            elif (
                pass_obj["count_of_bands_day_2"] + count_of_bands <= pass_obj["allowed"]
            ):
                passes.update_one(
                    {"_id": unique_id},
                    {"$set": {
                        "count_of_bands_day_2": pass_obj["count_of_bands_day_2"]
                        + count_of_bands
                    },}
                )
            elif (
                pass_obj["count_of_bands_day_2"] + count_of_bands > pass_obj["allowed"]
            ):
                raise HTTPException(status_code=401, detail="Not Allowed")

        return {"message": "verified"}

    else:
        raise HTTPException(status_code=401, detail="unauthorized")
