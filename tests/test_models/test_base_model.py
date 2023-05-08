#!/usr/bin/python3
"""
Tests for the BaseModel
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Contains the actual tests"""

    def setUp(self):
        self.model1 = BaseModel()
        self.model2 = BaseModel()

    def tearDown(self):
        del self.model1
        del self.model2

    def test_instance(self):
        self.assertIsInstance(self.model1, BaseModel)

    def test_initMethod(self):
        self.assertTrue(hasattr(self.model1, "id"))
        self.assertTrue(hasattr(self.model1, "created_at"))
        self.assertTrue(hasattr(self.model1, "updated_at"))

    def test_uuid(self):
        self.assertNotEqual(self.model1.id, self.model2.id)
        self.assertEqual(type(self.model1.id), str)

    def test_datetime(self):
        self.assertEqual(type(self.model1.created_at), datetime.datetime)
        self.assertEqual(type(self.model1.updated_at), datetime.datetime)

    def test_time(self):
        self.assertEqual(self.model1.created_at, self.model1.updated_at)
        self.model1.save()
        self.assertNotEqual(self.model1.created_at, self.model1.updated_at)

    def test_todict(self):
        dict1 = self.model1.to_dict()
        self.assertIsInstance(dict1, dict)
        self.assertEqual(type(dict1['created_at']), str)
        self.assertEqual(type(dict1['updated_at']), str)

if __name__ == '__main__':
    unittest.main()        
