#!/usr/bin/python3
""" File storage module"""
import json


class FileStorage():
    """ serializes instances to a JSON file and
    deserializes JSON file to instances"""
    
    def __init__(self):
        """ init method """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        for_json = {}
        for key, value in self.__objects.items():
            for_json[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as w:
            json.dump(for_json, w)

    def classes_dict(self):
        """collection of classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        classes_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        return classes_dict

    def reload(self):
        """ deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised) """
        try:
            data = {}
            with open(self.__file_path, 'r', encoding="UTF-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    obj = self.classes_dict()[value["__class__"]](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
