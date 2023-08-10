#!/usr/bin/python3
"""Defines the Amenity Module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """A class represents an Amenity Object"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
