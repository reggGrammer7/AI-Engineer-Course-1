from pyexpat import model

from pydantic import BaseModel, field_validator, model_validator
from datetime import datetime

class Prson(BaseModel):
    first_name : str
    last_name : str
    @field_validator('first_name','last_name')
    def names_must_be_capitalized(cls,v):
        if not v.istitle():
            raise ValueError("Names must be capitalized")
        return v



class DatRange(BaseModel):
    start_date : datetime
    end_date : datetime
    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('end date must be after start date')
        return values





























































