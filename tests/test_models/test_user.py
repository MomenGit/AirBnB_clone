#!/usr/bin/python3
"""Test module for user"""

import uinttest
from models import storage
from datetime import datetime
from models.user import User


class TestUserModule(unittest.TestCase):
    """Unit test for User class"""

    def SetUp(self):
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

    def test_name_is_str(self):
        self.asserEqual(type(self.test_model.name),
                        str)

    def test_email_(self):
        self.assertEqual(type(self.test_model.email),
                         str)

    def test_password_(self):
        sefl.assertEqual(type(self.test_model.password),
                         str)

    def test_first_name_(self):
        self.assertEqual(type(self.test_model.first_name),
                         str)

    def test_last_name_(self):
        self.assertEqual(type(self.test_model.last_name),
                         str)

    def test_obj_in_storage(self):
        self.assertIn(self.test_model, storage.all().values())


if __name__ == "__main__":
    unittest.main()
