#!/usr/bin/python3
"""
Applying Unit Test for State Class
"""
import unittest
import models
from models.state import State


class Test_State_init(unittest.TestCase):
    """ Testing instantiation """

    def test_init(self):
        self.assertIs(State, type(State()))

    def test_attrs(self):
        """ checks the attributes """
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_attrs_types(self):
        """ checks if it has the correct data types """
        state = State()
        self.assertEqual(type(state.name), str)

    def test_values(self):
        """ checks if it has the correct values """
        state = State()
        self.assertEqual(state.name, "")


class Test_State_Save(unittest.TestCase):
    """ Unittest for testing save"""

    def test_save(self):
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_update(self):
        state = State()
        state.save()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)

    def test_json(self):
        state = State()
        state.save()
        self.assertIs(type(state.to_dict()), dict)


if __name__ == "__main__":
    unittest.main()
