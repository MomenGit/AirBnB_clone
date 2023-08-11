#!/usr/bin/python3
"""state module"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
