#!/usr/bin/python3
"""
City Class (Models' module)
"""
from models.base_model import BaseModel


class City(BaseModel):
    """inherits from BaseModel and defines a city"""

    state_id = ""
    name = ""
