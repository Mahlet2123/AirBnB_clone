#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime


class BaseModel():
	""" defines all common attributes/methods for other classes"""
	def __init__(self, *args, **kwargs):
		""" the constructor of a BaseModel """
		if kwargs:
			for key, value in kwargs.items():
				date_format = "%Y-%m-%dT%H:%M:%S.%f"
				if key == "__class__":
					pass
				elif key == "created_at":
					self.created_at = datetime.strptime(value, date_format)
				elif key == "updated_at":
					self.updated_at = datetime.strptime(value, date_format)
				else:
					setattr(self, key, value)
		else:		
			self.id = str(uuid.uuid4())
			self.created_at = str(datetime.now())
			self.updated_at = str(datetime.now())

	def __str__(self):
		"""str method"""
		return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

	def save(self):
		""" updates the public instance attribute updated_at with the current datetime"""
		self.updated_at = str(datetime.now())

	def to_dict(self):
		""" returns a dictionary containing all keys/values of __dict__ of the instance"""
		new_dict = self.__dict__.copy()
		new_dict["__class__"] = self.__class__.__name__
		new_dict["created_at"] = datetime.now().isoformat()
		new_dict["updated_at"] = datetime.now().isoformat()
		return new_dict
