#!/usr/bin/python3
"""Defining the BaseModel module"""
from datetime import datetime
import uuid

class BaseModel:

    def __init__(self, *args, **kwargs):
        """ initaizing BaseModel instance """
        if kwargs:
             for key, value in kwarg.items():
                if key == "__class__":
                    continue
                if (key == "created_at") or (key == "updated_at"):
                    kwarg[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__dict__[key] = value
        else:
            self.id = str(uuyid.uuid4())
            self.crated_at = datetime.now()
            self.updated_at = datetime.now()
