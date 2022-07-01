#!/usr/bin/python3
"""
Review Class (Models' module)
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """inherits from BaseModel and defines an review"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """initialize Super class"""
        super().__init__(*args, **kwargs)
