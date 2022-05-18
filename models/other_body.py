from pydantic import Field, BaseModel


class OtherBody(BaseModel):
    roll_no: str = ""
    email: str = ""
    uid: str = ""

    class Config:
        arbitrary_types_allowed = True
