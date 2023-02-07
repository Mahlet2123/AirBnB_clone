#!/usr/bin/python3
""" the file storage module """
import json

class FileStorage():
	""" serializes instances to a JSON file and deserializes JSON file to instances """
	__file_path = "file.json"
	__objects = {}
	
	def all(self):
		""" returns the dictionary __objects """
		return FileStorage.__objects

	def new(self, obj):
		""" sets in __objects the obj with key <obj class name>.id """
		FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

	def save(self):
		""" serializes __objects to the JSON file (path: __file_path) """
		with open( "__file_path" , "w" ) as write:
			json.dump(self.__objects , write)

	def reload(self):
		""" deserializes the JSON file to __objects
		(only if the JSON file (__file_path) exists ;
		otherwise, do nothing. If the file doesn’t exist, no exception should be raised) """
		if self.__file_path is not None:
			with open( "__file_path" , "r" ) as read:
				json.loads(self.__file_path)
		else:
			pass
