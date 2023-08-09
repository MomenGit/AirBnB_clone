#!/usr/bin/python3
"""Defining the BaseModel module"""
from datetime import datetime
import uuid

class BaseModel:
    """
    A class BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ initaizing BaseModel instance """
        if kwargs:
            for key, value in kwarg.items():
                if key == "__class__":
                    continue
                if (key == "created_at") or (key == "updated_at"):
                    kwarg[key] = datetime.strptime(value, 
                                                   "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuyid.uuid4())
            self.crated_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation or the instance
        should print:
        [<class name>] (<self.id>) <self.__dict__>
        """
        str = "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id,
                                    self.__dict__)
        return (str)

    def save(self):
        """
         updates the public instance attribute
         updated_at: with the current datetime
         """
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing
        all keys/values of __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return (new_dict)
