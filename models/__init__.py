#!/usr/bin/python3
"""Models Module"""
__all__ = ["base_model", "amenity", "city", "place", "review", "state", "user"]
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


def dispatch_dict():
    """Returns a dictionary mapping
    classes constructors to their names
    """

    from .base_model import BaseModel
    # from models.user import User
    # from models.city import City
    # from models.state import State
    from .amenity import Amenity
    from .place import Place
    from .review import Review

    return {
        "BaseModel": BaseModel,
        # "User": User,
        # "City": City,
        # "State": State,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }
