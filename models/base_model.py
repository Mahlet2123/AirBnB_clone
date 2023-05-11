#!/usr/bin/python3
""" BaseModel Module """
import uuid
import datetime


class BaseModel():
    """ The BaseModel class """
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = value
                elif key == "updated_at":
                    self.updated_at = value
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ string representation of objects """
        #should print: [<class name>] (<self.id>) <self.__dict__>
        return "[{}]({}){}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime """
        updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
        of __dict__ of the instance """
        #setattr(self.__dict__, "__class__", self.__class__.__name__)
        self.__dict__["__class__"] = self.__class__.__name__
        return self.__dict__
