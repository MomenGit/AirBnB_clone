#!/usr/bin/python3
"""Defines the Review Module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """A class represents a Review Object"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
