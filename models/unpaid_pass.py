from pydantic import Field, BaseModel


class Unpaid_pass(BaseModel):
    name: str = Field(...)
    roll: str  = ""
    passing_year: str = ""
    department: str = Field(...)

    class Config:
        arbitrary_types_allowed = True