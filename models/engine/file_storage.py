#!/usr/bin/python3
"""File Storage Module"""
import json


class FileStorage:
    """
    A class that serializes instances to a JSON file
    and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj.id in self.__objects:
            return
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as file:
            objects = {}
            for key, value in self.__objects.items():
                objects[key] = value.to_dict()
            json.dump(objects, file)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn't exist, no exception should be raised)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        dispatch_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "City": City,
            "State": State,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        try:
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
                for key, value in self.__objects.items():
                    self.__objects[key] = dispatch_dict[value["__class__"]](
                        **value)
        except Exception as e:
            pass
