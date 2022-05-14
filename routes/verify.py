from itertools import count
from fastapi import APIRouter, Body, Depends, HTTPException
from typing import List,Optional
from auth import check_token
from fastapi.security import OAuth2PasswordBearer
import config

from models.team import Team

route = APIRouter(prefix="/verify", tags=["Verify"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@route.patch("/{unique_id}", status_code=204)
def verify_pass(unique_id : str,token: str = Depends(oauth2_scheme),count_of_bands : Optional[str] = ""):
    if count_of_bands :



    else :
        

