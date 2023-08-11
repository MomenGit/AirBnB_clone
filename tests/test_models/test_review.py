#!/usr/bin/python3
"""Test module for Review"""

import unittest
from models import storage
from datetime import datetime
from models.review import Review


class TestReviewModule(unittest.TestCase):
    """Unit test for Review class"""

    def setUp(self):
        self.test_model = Review()

    def tearDown(self):
        pass

    def test_obj_creation(self):
        self.assertEqual(type(self.test_model), Review)

    def test_obj_has_id(self):
        self.assertEqual(type(self.test_model.id), str)

    def test_created_at(self):
        self.assertEqual(type(self.test_model.created_at),
                         datetime)

    def test_text_str(self):
        self.assertEqual(type(self.test_model.text),
                         str)

    def test_place_id_(self):
        self.assertEqual(type(self.test_model.place_id),
                         str)

    def test_user_id_(self):
        self.assertEqual(type(self.test_model.user_id),
                         str)

    def test_obj_in_storage(self):
        self.assertIn(self.test_model, storage.all().values())

    def test_two_obj_diff_id(self):
        """
        Check if two objects have diffrent ids
        """
        obj1 = Review()
        obj2 = Review()
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
