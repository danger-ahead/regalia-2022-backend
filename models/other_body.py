from pydantic import Field, BaseModel


class OtherBody(BaseModel):
    roll_no: str = Field(...)
    email: str = ""

    class Config:
        arbitrary_types_allowed = True