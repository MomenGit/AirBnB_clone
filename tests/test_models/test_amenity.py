#!/usr/bin/python3
"""Test module for amenity"""

import unittest
from models import storage
from datetime import datetime
from models.amenity import Amenity


class TestAmenityModule(unittest.TestCase):
    """Unit test for Amenity class"""

    def setUp(self):
        self.test_model = Amenity()

    def tearDown(self):
        pass

    def test_obj_creation(self):
        self.assertEqual(type(self.test_model), Amenity)

    def test_obj_has_id(self):
        self.assertEqual(type(self.test_model.id), str)

    def test_created_at(self):
        self.assertEqual(type(self.test_model.created_at),
                         datetime)

    def test_name_str(self):
        self.assertEqual(type(self.test_model.name),
                         str)

    def test_obj_in_storage(self):
        self.assertIn(self.test_model, storage.all().values())

    def test_two_obj_diff_id(self):
        """
        Check if two objects have diffrent ids
        """
        obj1 = Amenity()
        obj2 = Amenity()
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
