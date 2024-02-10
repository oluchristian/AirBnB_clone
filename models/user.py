#!/usr/bin/python3
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
