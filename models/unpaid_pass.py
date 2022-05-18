from pydantic import Field, BaseModel


class Unpaid_pass(BaseModel):
    name: str = Field(...)
    roll_number: str = ""
    passing_year: str = ""
    phone: str = ""
    email: str = ""
    department: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
