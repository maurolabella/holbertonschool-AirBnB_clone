#!/usr/bin/python3
"""
Applying Unit Test for FileStorage class
"""
import unittest
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class Test_FileStorage(unittest.TestCase):
    """ Testing FileStorage class """

    def test_classes(self):
        """ class created check """
        self.assertIsInstance(models.engine.file_storage.FileStorage(),
                              models.engine.file_storage.FileStorage)

    def test_new(self):
        """ method new check """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().new)

    def test_all(self):
        """ method all check """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().all)

    def test_save(self):
        """ method save check """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().save)

    def test_reload(self):
        """ method reload check """
        self.assertIsNotNone(models.engine.file_storage.FileStorage().reload)

    def test_models_all(self):
        """ models storage all check """
        self.assertIsNotNone(models.storage.all())

    def test_docstring(self):
        """ docstrings check """
        self.assertIsNotNone(models.engine.file_storage.FileStorage.
                             __doc__)
        self.assertIsNotNone(models.engine.file_storage.
                             __doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.all.
                             __doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.__init__.
                             __doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.new.
                             __doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.save.
                             __doc__)
        self.assertIsNotNone(models.engine.file_storage.FileStorage.reload.
                             __doc__)

    def test_docmodule(self):
        """ checking doc module """
        self.assertGreater(len(models.engine.file_storage.__doc__), 1)

    def test_docclass(self):
        """checking doc class"""
        self.assertGreater(len(models.engine.file_storage.
                           FileStorage.__doc__), 1)

    def test_attrd(self):
        """test for presence of attributes"""
        self.assertEqual(dict, type(models.storage.all()))


if __name__ == "__main__":
    unittest.main()
