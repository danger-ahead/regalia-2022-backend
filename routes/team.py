from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

from models.team import Team

route = APIRouter(prefix="/teams", tags=["Teams"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@route.get("/{id}", status_code=200)
def get_teams(id: str, token: str = Depends(oauth2_scheme)):
    if check_token(token):
        team = config.regalia22_db["team"]
        team = team.find_one({"_id": id})
        if team is None:
            raise HTTPException(status_code=401, detail="You are not authorized")
        return team
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@route.post("/", status_code=201)
def add_member(team: Team = Body(...), token: str = Depends(oauth2_scheme)):
    try:
        if check_token(token):
            teams = config.regalia22_db["team"]

            teams.insert_one(
                {
                    "_id": team.id,
                    "name": team.name,
                    "contact": team.contact,
                    "image": team.image,
                    "role": team.role,
                }
            )
            return team
        else:
            raise HTTPException(status_code=401, detail="Unauthorized")

    except Exception as e:
        raise HTTPException(status_code=409, detail=str(e))
