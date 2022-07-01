#!/usr/bin/python3
"""
State Class (Models' module)
"""
from models.base_model import BaseModel


class State(BaseModel):
    """inherits from BaseModel and defines a state"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initialize Super class"""
        super().__init__(*args, **kwargs)
