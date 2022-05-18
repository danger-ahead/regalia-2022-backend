from datetime import datetime
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

from models.participant import Participant

route = APIRouter(prefix="/participants", tags=["participants"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.get("/", status_code=200)
def get_participants(token: str = Depends(oauth2_scheme)):
    if check_token(token):
        participants = config.regalia22_db["participant"]
        participants = list(participants.find())
        return participants
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@route.post("/", status_code=201)
def add_participant(
    participant: Participant = Body(...), token: str = Depends(oauth2_scheme)
):
    try:
        if check_token(token):
            participants = config.regalia22_db["participant"]
            participants.insert_one(
                {
                    "name": participant.name,
                    "event": participant.event,
                    "_id": str(datetime.now()),
                }
            )
            return participant
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")
    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
