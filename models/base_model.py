#!/usr/bin/python3
"""
BaseModel Class (Models' module)
"""
from rich import inspect
import models
import json
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """defines the abstract class BaseModel"""

    def __init__(self, *args, **kwargs):
        """
        __init__ for BaseModel Class
        """
        if kwargs:
            self.__mount_attrib(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __mount_attrib(self, attrib_d):
        """
        private__sets attr
        """
        for key, value in attrib_d.items():
            if key == "id":
                self.id = value
                continue
            if key == "created_at":
                self.__dict__["created_at"] = datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f')
                continue
            if key == "updated_at":
                self.__dict__["updated_at"] = datetime.strptime(
                    value, '%Y-%m-%dT%H:%M:%S.%f')
                continue
            if key == '__class__':
                continue
            setattr(self, key, value)

    def __str__(self):
        """
        function defining the string type representation of an
        instance
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates and save instance
        """
        self.updated_at = datetime.now()
        """calling save method of storage"""
        models.storage.save()

    def __check_to_serial(self, obj_rec):
        """
        private_finds out about an object is json-serializable
        """
        try:
            test = json.dumps(obj_rec)
            if test is not None and isinstance(test, str):
                return True
            else:
                return False
        except Exception:
            return False

    def to_dict(self):
        """
        Dictionary Generation
        """
        tmp = self.__dict__.copy()
        tmp['created_at'] = self.created_at.isoformat()
        tmp['updated_at'] = self.updated_at.isoformat()
        tmp['__class__'] = type(self).__name__
        """
        dict_r = {key: val if self.__check_to_serial(val) else str(val)
                  for key, val in tmp.items()}
        """
        return(tmp)
