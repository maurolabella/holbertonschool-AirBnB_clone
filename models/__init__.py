#!/usr/bin/python3
"""Filestorage Requirements"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
