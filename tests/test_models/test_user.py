#!/usr/bin/python3
"""
Applying Unit Test for User Class
"""
import unittest
from models.base_model import BaseModel
from models.user import User


class testUser(unittest.TestCase):
    """ Testing User class """

    def test_issubclass(self):
        """ checks if it is subclass of BaseModel """
        self.assertTrue(issubclass(User, BaseModel))

    def test_save(self):
        """ checks if it saves correctly """
        user = User()
        user.save()
        self.assertNotEqual(user.created_at, user.updated_at)

    def test_attrs(self):
        """ checks the attributes """
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))

    def test_attrs_types(self):
        """ checks if it has the correct data types """
        user = User()
        self.assertEqual(type(user.email), str)
        self.assertEqual(type(user.password), str)
        self.assertEqual(type(user.first_name), str)
        self.assertEqual(type(user.last_name), str)

    def test_values(self):
        """ checks if it has the correct values """
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_str(self):
        """ checks if it has the correct repr """
        user = User()
        string = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(user.__str__(), string)


if __name__ == '__main__':
    unittest.main()
