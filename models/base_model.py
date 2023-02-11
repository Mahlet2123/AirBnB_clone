#!/usr/bin/python3
"""class BaseModel"""

import models
import uuid
from datetime import datetime

date = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """the constructor of a BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key == "created_at":
                    self.created_at = datetime. \
                                      strptime(value, date)
                elif key == "updated_at":
                    self.updated_at = datetime. \
                                      strptime(value, date)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """str method"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}]"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(date)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(date)
        return new_dict
