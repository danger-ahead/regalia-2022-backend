from pydantic import Field, BaseModel


class Pass(BaseModel):
    name: str = Field(...)
    roll_number: str = Field(...)
    email: str = Field(...)
    allowed: int = Field(...)
    phone_number: str = ""
    day_1_validity: str = Field(...)
    day_2_validity: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
