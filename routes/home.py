from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config
from datetime import date

route = APIRouter(prefix="/home", tags=["Home"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.get("/", status_code=200)
def home(token: str = Depends(oauth2_scheme)):
    if check_token(token):
        pass_obj = config.regalia22_db["pass"]

        today = str(date.today())

        today = today.split("-")[2]

        label = ""
        total = 0
        cse_count = 0
        ece_count = 0
        ee_count = 0
        it_count = 0
        aeie_count = 0

        if today == config.days[0]:
            label = "Day 1"
            total = pass_obj.count_documents(
                {"day_1_validity": {"$not": {"$regex": "^$"}}}
            )  # initial time stamp will be empty
            cse_count = pass_obj.count_documents(
                {
                    "day_1_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "cse", "$options": "i"},
                }
            )
            ece_count = pass_obj.count_documents(
                {
                    "day_1_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "ece", "$options": "i"},
                }
            )
            ee_count = pass_obj.count_documents(
                {
                    "day_1_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "ee", "$options": "i"},
                }
            )
            it_count = pass_obj.count_documents(
                {
                    "day_1_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "it", "$options": "i"},
                }
            )
            aeie_count = pass_obj.count_documents(
                {
                    "day_1_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "aeie", "$options": "i"},
                }
            )

        elif today == config.days[1]:
            label = "Day 2"
            total = pass_obj.count_documents(
                {"day_2_validity": {"$not": {"$regex": "^$"}}}
            )
            cse_count = pass_obj.count_documents(
                {
                    "day_2_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "cse", "$options": "i"},
                }
            )
            ece_count = pass_obj.count_documents(
                {
                    "day_2_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "ece", "$options": "i"},
                }
            )
            ee_count = pass_obj.count_documents(
                {
                    "day_2_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "ee", "$options": "i"},
                }
            )
            it_count = pass_obj.count_documents(
                {
                    "day_2_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "it", "$options": "i"},
                }
            )
            aeie_count = pass_obj.count_documents(
                {
                    "day_2_validity": {"$not": {"$regex": "^$"}},
                    "roll_number": {"$regex": "aeie", "$options": "i"},
                }
            )

        return {
            "label": label,
            "total": total,
            "categorized": {
                "cse_count": cse_count,
                "ece_count": ece_count,
                "ee_count": ee_count,
                "it_count": it_count,
                "aeie_count": aeie_count,
            },
        }

    else:
        raise HTTPException(status_code=401, detail="Unauthorized")
