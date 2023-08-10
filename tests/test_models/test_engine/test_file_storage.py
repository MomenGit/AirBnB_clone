#!/usr/bin/python3
"""FileStorage UnitTest Module"""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """FileStorage Unit Test Case"""

    def setUp(self) -> None:
        self.storage = FileStorage()
        self.storage.reload()
        return super().setUp()

    def test_all(self):
        """Tests the all function returns the objects dict"""
        model = BaseModel()
        model.name = "all_model"

        self.storage.new(model)
        self.storage.save()

        all_objects = self.storage.all()
        self.assertIn(model, list(self.storage.all().values()))

    def test_reload(self):
        """Tests the reload function works as intended"""
        model = BaseModel()
        model.name = "reload_model"

        self.storage.new(model)
        self.storage.save()

        self.storage.reload()
        self.assertIsNotNone(self.storage.all().get(
            type(model).__name__+'.'+model.id))

    def test_new_model(self):
        """Tests that the newly created model is present in objects dict"""
        model = BaseModel()
        model.name = "reload_model"

        self.storage.new(model)

        self.assertIn(model, list(self.storage.all().values()))

    def test_save(self):
        """Tests that the saved file exists"""
        import os
        model = BaseModel()
        model.name = "reload_model"

        self.storage.new(model)
        self.storage.save()

        self.assertTrue(os.path.exists('file.json'))

    def test_stored_id_format(self):
        """Tests that the id stored in the objects dict
        is correctly formatted
        """
        model = BaseModel()
        model.name = "reload_model"

        self.storage.new(model)
        self.storage.save()

        self.assertIn("{}.{}".format(type(model).__name__,
                      model.id), list(self.storage.all().keys()))


if __name__ == '__main__':
    unittest.main()
