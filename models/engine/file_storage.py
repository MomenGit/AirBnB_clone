#!/usr/bin/python3
"""File Storage Module"""
from models import *
import json

dispatch_dict = {
    "BaseModel": base_model.BaseModel,
    "Amenity": amenity.Amenity,
    "City": city.City,
    "Place": place.Place,
    "Review": review.Review,
    "State": state.State,
    "User": user.User,
}


class FileStorage:
    """A class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if getattr(obj, "id", False):
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            objects = {}
            for key, value in self.__objects.items():
                objects[key] = value.to_dict()
            json.dump(objects, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        """
        try:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
                for key, value in self.__objects.items():
                    self.__objects[key] = dispatch_dict[value["__class__"]](
                        **value)
        except Exception as e:
            pass
