#!/usr/bin/python3
"""Test module for user"""

import unittest
from models import storage
from datetime import datetime
from models.user import User


class TestUserModule(unittest.TestCase):
    """Unit test for User class"""

    def setUp(self):
        self.test_model = User()

    def tearDown(self):
        pass

    def test_user_obj_creation(self):
        self.assertEqual(type(self.test_model), User)

    def test_user_has_id(self):
        self.assertEqual(type(self.test_model.id), str)

    def test_created_at(self):
        self.assertEqual(type(self.test_model.created_at),
                         datetime)

    def test_email_(self):
        self.assertEqual(type(self.test_model.email),
                         str)

    def test_password_(self):
        self.assertEqual(type(self.test_model.password),
                         str)

    def test_first_name_(self):
        self.assertEqual(type(self.test_model.first_name),
                         str)

    def test_last_name_(self):
        self.assertEqual(type(self.test_model.last_name),
                         str)

    def test_obj_in_storage(self):
        self.assertIn(self.test_model, storage.all().values())

    def test_two_obj_diff_id(self):
        """
        Check if two objects have diffrent ids
        """
        obj1 = User()
        obj2 = User()
        self.assertNotEqual(obj1.id, obj2.id)
        del obj1
        del obj2

    def test_save(self):
        updated_before = self.test_model.updated_at
        self.test_model.save()
        self.assertNotEqual(updated_before,
                            self.test_model.updated_at)


if __name__ == "__main__":
    unittest.main()
