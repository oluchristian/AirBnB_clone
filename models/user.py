#!/usr/bin/python3

"The user Module"

from models.base_model import BaseModel


class User(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): A sub class of the BaseModel
        parent class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
