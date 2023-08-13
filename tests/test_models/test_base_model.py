#!/usr/bin/python3
"""UnitTest Module for base_model"""
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """UnitTest for BaseModel"""

    def setUp(self):
        """Setting up test"""
        self.test_model = BaseModel()
        self.test_model.name = "test_model"

    def test_crating_model(self):
        """Check if model exist and is BaseModel instance"""
        self.assertEqual(type(self.test_model), BaseModel)

    def test_id_type(self):
        """Check if id type is string"""
        self.assertEqual(type(self.test_model.id), str)

    def test_id_two_obj(self):
        """Check if two object has the same id"""
        test_model_2 = BaseModel()
        self.assertNotEqual(self.test_model.id, test_model_2.id)

    def test_created_at_type(self):
        """check if created at attribute is datetime type"""
        self.assertEqual(type(self.test_model.created_at), datetime.datetime)

    def test_created_at_two_obj(self):
        """Check if two objects has diffrent created at time"""
        test_model_2 = BaseModel()
        self.assertTrue(self.test_model.created_at < test_model_2.created_at)

    def test_updated_at_type(self):
        """Check updated at type"""
        self.assertEqual(type(self.test_model.updated_at), datetime.datetime)

    def test_change_updated_at(self):
        """Check if updated_at changed when using .save()"""
        self.test_model.save()
        self.assertTrue(self.test_model.created_at <
                        self.test_model.updated_at)

    def test__str__(self):
        """Check if __str___ gives the correct format"""
        self.assertEqual(str(self.test_model), "[{}] ({}) {}"
                         .format(self.test_model.__class__.__name__,
                                 self.test_model.id, self.test_model.__dict__))

    def test_args(self):
        """Check if using arguments when crateing
        an instance it will not be used"""
        test_model_2 = BaseModel("test_arg")
        self.assertNotIn("test_arg", self.test_model.__dict__.values())

    def test_creating_kwarg(self):
        """Check creating BaseModel instance using dicionary (**kwargs)"""
        test_dict = self.test_model.to_dict()
        new_model = BaseModel(**test_dict)
        self.assertEqual(self.test_model.name, new_model.name)


if __name__ == '__main__':
    unittest.main()
