#!/usr/bin/python3
"""
User Class (Models' module)
"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherits from BaseModel and defines a user"""

    first_name = ""
    last_name = ""
    email = ""
    password = ""

    def __init__(self, *args, **kwargs):
        """initialize Super class"""
        super().__init__(*args, **kwargs)
