"""File Storage Module

   This modules will allow us to 
   preserve our class instances into a data store
"""
import json

class FileStorage:
	"""Class which stores and restores objects with file"""
	__file_path = "file.json"
	__objects = {}

	def __init__(self):
		try:
			with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
				print("made it: {}".format(FileStorage.__file_path))
		except (FileNotFoundError):
			with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
				json.dump([], f)

	def reload(self):
		"""Deserializes from file to __objects"""
		obj_dicts = []
		with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
			obj_dicts = json.load(f)
		for obj in obj_dicts:
			uuid = obj['id']
			cname = obj['__class__']
			self.__objects[uuid+'.'+cname] = eval(cname)(**obj)

	def all(self):
		"""Returns __objects"""
		return self.__objects

	def save(self):
		"""Serializes objects to file"""
		obj_dicts = []
		for k, v in self.__objects.items():
			obj_dicts.append(v.to_dict)
		with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
			json.dump(obj_dicts, f)

	def new(self, obj):
		"""Adds obj to __objects"""
		uuid = obj.id
		cname = obj.__class__.__name__
		self.__objects[uuid+'.'+cname] = obj