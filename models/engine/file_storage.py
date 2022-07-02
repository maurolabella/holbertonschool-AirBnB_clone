#!/usr/bin/python3
"""data/file/instances serialization, JSON writing,
reading, and storing"""


from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
import json


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON files to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            index = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[index] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        temp = {}
        for key, value in self.__objects.items():
            temp[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(temp, file)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r') as file:
                for key, value in (json.load(file).items()):
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass
