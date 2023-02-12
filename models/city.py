#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel


class City(BaseModel):
    """class City that inherits from BaseModel"""

    state_id = ""
    name = ""
