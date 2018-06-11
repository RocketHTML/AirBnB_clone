#!/usr/bin/python3
""" Base module for Holberton BnB
 """
import datetime
import json
import models
import uuid

class BaseModel:
    """initializes the Base method
    Args: init, to_dict, __str__, save
    """

    def __init__(self, *args, **kwargs):
        """init method for base_model"""
        if not (kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            models.storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

    def to_dict(self):
        """adjust format used by dict to use a string form of datetime with
        isoformat, add class = class name
        """
        self.__dict__['updated_at'] = str(self.updated_at.isoformat())
        self.__dict__['created_at'] = str(self.created_at.isoformat())
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        """override the string displayed by __str__ method"""
        return("[{}] ({}) {}".format
                (self.__class__.__name__, self.id,
                 self.__dict__))

    def save(self):
        """update updated_at time and date"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def update(self):
        """updates"""
        if not (kwargs):
            pass

        else:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
