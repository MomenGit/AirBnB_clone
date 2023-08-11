#!/usr/bin/python3
"""Test module for Place"""

import unittest
from models import storage
from datetime import datetime
from models.place import Place


class TestPlaceModule(unittest.TestCase):
    """Unit test for Place class"""

    def setUp(self):
        self.test_model = Place()

    def tearDown(self):
        pass

    def test_obj_creation(self):
        self.assertEqual(type(self.test_model), Place)

    def test_obj_has_id(self):
        self.assertEqual(type(self.test_model.id), str)

    def test_created_at(self):
        self.assertEqual(type(self.test_model.created_at),
                         datetime)

    def test_city_id_(self):
        self.assertEqual(type(self.test_model.city_id),
                         str)

    def test_user_id_(self):
        self.assertEqual(type(self.test_model.user_id),
                         str)

    def test_name_str(self):
        self.assertEqual(type(self.test_model.name),
                         str)

    def test_description_str(self):
        self.assertEqual(type(self.test_model.description),
                         str)

    def test_description_str(self):
        self.assertEqual(type(self.test_model.description),
                         str)

    def test_number_rooms_int(self):
        self.assertEqual(type(self.test_model.number_rooms),
                         int)

    def test_number_bathrooms_int(self):
        self.assertEqual(type(self.test_model.number_bathrooms),
                         int)

    def test_max_guest_int(self):
        self.assertEqual(type(self.test_model.max_guest),
                         int)

    def test_price_by_night_int(self):
        self.assertEqual(type(self.test_model.price_by_night),
                         int)

    def test_latitude_float(self):
        self.assertEqual(type(self.test_model.latitude),
                         float)

    def test_longitude_float(self):
        self.assertEqual(type(self.test_model.longitude),
                         float)

    def test_amenity_ids_float(self):
        self.assertEqual(type(self.test_model.amenity_ids),
                         list)   

    def test_obj_in_storage(self):
        self.assertIn(self.test_model, storage.all().values())

    def test_two_obj_diff_id(self):
        """
        Check if two objects have diffrent ids
        """
        obj1 = Place()
        obj2 = Place()
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
