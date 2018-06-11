#!/usr/bin/python3
from models.base_model import BaseModel
import json

"""File Storage Module
   This modules will allow us to
   preserve our class instances into a data store
"""


class FileStorage:
    """handles serialization and deserialization of BaseModel class objects"""
    __file_path = "file.json"
    __objects = {}

    def reload(self):
        """ returns the dictionary __objects
        try/except with file not found error -> pass
        """
        try:
            with open(self.__file_path, 'r') as f:
                dicts = json.load(f)
            for key, value in dicts.items():
                obj1 = eval(value['__class__']) (**value)
                self.__objects[key] = obj1
        except FileNotFoundError:
            pass

    def all(self):
        """ sets in __objects the obj with key <obj class name>.id """
        return self.__objects

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new_dict = {}
        if (self.__objects):
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            with open(self.__file_path, 'w+') as f:
                json.dump(new_dict, f)

    def new(self, obj):
        """ deserializes the JSON file to __objects (only if the JSON file
        exists ; otherwise, do nothing) """
        new_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[new_key] = obj