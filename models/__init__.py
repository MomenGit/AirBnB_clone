#!/usr/bin/python3
"""Models Module"""
import engine.file_storage as file_storage

__all__ = ["base_model", "amenity", "city", "place", "review", "state", "user"]

storage = file_storage.FileStorage()
storage.reload()
