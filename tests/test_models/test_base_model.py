#!/usr/bin/python3
"""
Applying Unit Test for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from models import base_model
import inspect
import pycodestyle
import os
from datetime import datetime


class TestDocs_BaseModel(unittest.TestCase):
    """Class for testing docs in BaseModel"""

    all_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_doc_file(self):
        """check for documentation"""
        expected = "\nBaseModel Class (Models' module)\n"
        actual = base_model.__doc__
        print(actual)
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """check documentation for the class"""
        expected = "defines the abstract class BaseModel"
        actual = BaseModel.__doc__
        self.assertEqual(expected, actual)

    def test_all_function_docs(self):
        """check for documentation in all functions"""
        all_functions = TestDocs_BaseModel.all_funcs
        for function in all_functions:
            self.assertIsNotNone(function[1].__doc__)

    def test_pep8_base_model(self):
        """checks base_model.py conforms to pycode Style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        errors = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(errors.total_errors, 0, errors.messages)

    def test_file_is_executable(self):
        """checks executability"""
        file_stat = os.stat('models/base_model.py')
        permissions = str(oct(file_stat[0]))
        actual = int(permissions[5:-2]) >= 5
        self.assertTrue(actual)


class TestBaseModel_Instantiation(unittest.TestCase):
    """Testing instances and variables thereof"""

    def setUp(self):
        """new instance for each individual testing"""
        self.model = BaseModel()

    def test_instance_generation(self):
        """checks proper instantiation"""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        """check save function should add updated_at attribute"""
        self.model.save()
        actual = type(self.model.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    def test_to_string(self):
        """checks if BaseModel is casted to string"""
        my_str = str(self.model)
        my_list = ['BaseModel', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_id_evolution(self):
        """checks for a reasonable id evolution"""
        test = BaseModel()
        # print(test)
        # print(self.model)
        # print(test.id.split("-")[0])
        # print(self.model.id.split("-")[0])
        # map = zip(test.id.split("-"), self.model.id.split("-"))
        # for (id_t, id_m) in map.item():
        #     print(id_t, id_m)
        self.assertTrue(test.id != self.model.id)
