from datetime import date
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    email: str = Field(max_length=100)
    phone: str = Field(max_length=15)
    birthday: date


class ContactModel(ContactBase):
    description: str = Field(max_length=150)


class ContactUpdate(ContactModel):
    ...


class ContactResponse(ContactBase):
    id: int
    
    class Config:
        from_attributes = True
