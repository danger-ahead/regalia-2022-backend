from pydantic import Field, BaseModel


class Participant(BaseModel):
    name: str = Field(...)
    event: str = Field(...)

    class Config:
        arbitrary_types_allowed = True
