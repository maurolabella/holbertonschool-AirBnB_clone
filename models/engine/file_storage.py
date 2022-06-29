#!/usr/bin/python3
"""data/file/instances serialization, JSON writing,
reading, and storing"""

import json
from models import base_model
from datetime import datetime

to_dict = base_model.BaseModel.to_dict


class FileStorage():
    """serializes instances to a JSON file
    and deserializes JSON files to instances"""
    __file_path = 'storage.json'
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
