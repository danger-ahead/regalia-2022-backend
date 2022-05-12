from pydantic import Field, BaseModel


class Team(BaseModel):
    id: str = Field(...)
    image: str = Field(...)
    name: str = Field(...)
    role: str = Field(...)
    contact: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
