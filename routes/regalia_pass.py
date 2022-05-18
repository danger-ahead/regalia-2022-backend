from fastapi import APIRouter, Depends, HTTPException, Response
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config
from models.regalia_pass import Pass
from models.other_body import OtherBody
from unique_id import generate_unique_id
from routes.resend_email_scripts import generate_pass


route = APIRouter(prefix="/pass", tags=["pass"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.post("/", status_code=201)
def add_pass(
    response: Response,
    regalia_pass: Pass,
    count_of_bands: int = 0,
    token: str = Depends(oauth2_scheme),
):
    try:
        if check_token(token):
            passes = config.regalia22_db["pass"]
            uni_id = generate_unique_id()
            pass_obj = passes.find_one({"email": regalia_pass.email})
            if pass_obj is None:
                passes.insert_one(
                    {
                        "_id": uni_id,
                        "name": regalia_pass.name,
                        "phone_number": regalia_pass.phone_number,
                        "email": regalia_pass.email,
                        "allowed": regalia_pass.allowed,
                        "day_1_validity": regalia_pass.day_1_validity,
                        "day_2_validity": regalia_pass.day_2_validity,
                        "roll_number": regalia_pass.roll_number,
                        "count_of_bands_day_1": count_of_bands,
                        "count_of_bands_day_2": count_of_bands,
                    }
                )

                if regalia_pass.server:
                    generate_pass.makeCertificate(
                        regalia_pass.email,
                        regalia_pass.name,
                        regalia_pass.roll_number,
                        regalia_pass.allowed,
                    )

                return {
                    "_id": uni_id,
                    "name": regalia_pass.name,
                    "phone_number": regalia_pass.phone_number,
                    "email": regalia_pass.email,
                    "allowed": regalia_pass.allowed,
                    "day_1_validity": regalia_pass.day_1_validity,
                    "day_2_validity": regalia_pass.day_2_validity,
                    "roll_number": regalia_pass.roll_number,
                    "count_of_bands_day_1": count_of_bands,
                    "count_of_bands_day_2": count_of_bands,
                    "created_now": True,
                }

            else:
                response.status_code = 401
                pass_obj["created_now"] = False
                return pass_obj

        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))


@route.patch("/resend_mail", status_code=201)
def resend_pass(
    response: Response, other_body: OtherBody, token: str = Depends(oauth2_scheme)
):
    try:
        if check_token(token):
            passes = config.regalia22_db["pass"]
            pass_obj = passes.find_one({"_id": other_body.uid})
            if pass_obj is None:
                response.status_code = 401
                return {"message": "Not Found"}
            else:
                passes.update_one(
                    {"_id": other_body.uid},
                    {"$set": {"email": other_body.email}},
                )
                generate_pass.makeCertificate(
                    other_body.email,
                    pass_obj["name"],
                    pass_obj["roll_number"],
                    pass_obj["allowed"],
                )

                return {"message": "mail sent"}

    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
