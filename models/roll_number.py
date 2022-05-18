from pydantic import Field, BaseModel


class Roll_Number(BaseModel):
    roll_no: str = Field(...)

    class Config:
        arbitrary_types_allowed = True