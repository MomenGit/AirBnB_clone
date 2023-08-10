#!/usr/bin/python3
"""Models Module"""
__all__ = ["base_model", "amenity", "city", "place", "review", "state", "user"]
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
