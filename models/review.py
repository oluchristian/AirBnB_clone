#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): A sub class of the BaseModel
        parent class
    """
    place_id = ""
    user_id = ""
    text = ""
