#!/usr/bin/python3
""" User module"""
from models.base_model import BaseModel


class City(BaseModel):
	""" class City that inherits from BaseModel """
	state_id = ""
	name = ""

	def __init__(self, *args, **kwargs):
		""" the constructor """
		if kwargs:
			for key, value in kwargs.items():
				if not hasattr(BaseModel, key):
					setattr(self, key, value)
		else:
			super().__init__()
