#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """the constructor"""
        if kwargs:
            for key, value in kwargs.items():
                if not hasattr(BaseModel, key):
                    setattr(self, key, value)
        else:
            super().__init__()
