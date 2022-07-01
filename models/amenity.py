#!/usr/bin/python3
"""
Amenity Class (Models' module)
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """inherits from BaseModel and defines an amenity"""

    name = ""

    def __init__(self, *args, **kwargs):
        """initialize Super class"""
        super().__init__(*args, **kwargs)
