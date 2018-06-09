#!/usr/bin/python3
""" Base module for Holberton BnB """
import datetime
import json
import uuid
import models.engine

class BaseModel:
    """initializes the Base method
    Args:
    """

    def __init__(self, *args, **kwargs):

        attrs = ['id', 'created_at', 'updated_at']
        defaults = [str(uuid.uuid4()), 
                  datetime.datetime.now(), 
                  datetime.datetime.now()]

        for a, v in zip(attrs, defaults):
            if a in kwargs:
                if a == 'created_at' or a == 'updated_at':
                    val = datetime.strptime(kwargs[a], datetime.isoformat())
                else:
                    val = kwargs[a]
                setattr(self, a, val)
            else:
                setattr(self, a, v)

    def to_dict(self):
        self.__dict__['updated_at'] = str(self.updated_at.isoformat())
        self.__dict__['created_at'] = str(self.created_at.isoformat())
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

#       @updated_at.setter
#       def save(self):
#           self.updated_at = datetime.datetime.now()

    def __str__(self):
        """override the string displayed by __str__ method"""
        return("[{}] ({}) {}".format
                (self.__class__.__name__, self.id,
                 self.__dict__))



def test():
    h = Base()
    print(h)
    print()
if __name__ == '__main__':
    test()