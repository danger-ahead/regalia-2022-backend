from pydantic import Field, BaseModel


class Guest(BaseModel):
    name: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
