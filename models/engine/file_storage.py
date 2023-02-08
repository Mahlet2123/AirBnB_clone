#!/usr/bin/python3
""" the file storage module """
import json


class FileStorage:
	"""
	serializes instances to a JSON file
	and deserializes JSON file to instances
	"""

	__file_path = "file.json"
	__objects = {}

	def all(self):
		"""returns the dictionary __objects"""
		return FileStorage.__objects

	def new(self, obj):
		"""sets in __objects the obj with key <obj class name>.id"""
		FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

		# print("--->", FileStorage.__objects, "<---")
		# {'BaseModel.15a72150-6ed8-47c1-9b7a-3c6bda8b0d69': <models
		# .base_model.BaseModel object at 0x7f7a3053b3a0>}

	def save(self):
		"""serializes __objects to the JSON file (path: __file_path)"""
		with open(FileStorage.__file_path, "w", encoding="UTF-8") as w:
			dct = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
			json.dump(dct, w)
		# print("--->", dct, "<---")
		# {'BaseModel.11b9feda-2553-4ffc-8792-4cb0c7cf7a54': {'id': '...'
		# , ... '__class__': 'BaseModel'}}

	def classes_dict(self):
		"""Returns the available classes to avoid circular import"""
		from models.base_model import BaseModel

		classes_dict = {"BaseModel": BaseModel}
		return classes_dict

	def reload(self):
		"""
		deserializes the JSON file to __objects
		(only if the JSON file (__file_path) exists ;
		otherwise, do nothing. If the file doesn’t exist,
		no exception should be raised)
		"""
		try:
			with open(FileStorage.__file_path, "r", encoding="UTF-8") as r:
				r_dict = json.load(r)
				r_dict = {k: self.classes_dict()[v["__class__"]](**v)
							for k, v in r_dict.items()}
				FileStorage.__objects = r_dict
				#print("--->",FileStorage.__objects, "<---")
				# reverse process of the save method ^^^ 
		except FileNotFoundError:
			pass
