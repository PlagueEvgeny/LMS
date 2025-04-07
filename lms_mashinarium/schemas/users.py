import uuid

from fastapi import HTTPException
from pydantic import BaseModel
from pydantic import constr
from pydantic import EmailStr
from pydantic import validator

from schemas.base import TunedModel


class ShowUser(TunedModel):
    user_id: uuid.UUID
    name: str
    surname: str
    patronymic: str
    email: EmailStr
    telegram: str
    is_active: bool
