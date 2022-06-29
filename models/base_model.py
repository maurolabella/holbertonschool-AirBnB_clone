#!/usr/bin/python3
"""
BaseModel Class (Models' module)
"""
from rich import inspect
import models
import subprocess
import json
from uuid import uuid4, UUID
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
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)

    def __mount_attrib(self, attrib_d):
        """
        private__sets attr
        """
        if 'id' not in attrib_d:
            attrib_d['id'] = str(uuid4())
        if 'created_at' not in attrib_d:
            attrib_d['created_at'] = datetime.utcnow()
        elif not isinstance(attrib_d['created_at'], datetime):
            attrib_d['created_at'] = datetime.strptime(
                attrib_d['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' not in attrib_d:
            attrib_d['updated_at'] = datetime.utcnow()
        elif not isinstance(attrib_d['updated_at'], datetime):
            attrib_d['updated_at'] = datetime.strptime(
                attrib_d['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        attrib_d.pop('__class__', None)
        for attr, val in attrib_d.items():
            setattr(self, attr, val)

    def __str__(self):
        """
        function defining the string type representation of an
        instance
        """
        return '[{}] ({}) {}'.format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        updates and save instance
        """
        self.updated_at = datetime.utcnow()
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
        dict_r = {key: val if self.__check_to_serial(val) else str(val)
                  for key, val in tmp.items()}
        return(dict_r)
