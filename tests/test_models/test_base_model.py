#!/usr/bin/python3
"""
Tests for the BaseModel
"""
import unittest
import datetime
from models.base_model import BaseModel
import pycodestyle
import models.base_model


class TestBaseModel(unittest.TestCase):
    """Contains the actual tests"""
    def test_basemodel_conformity_pycode(self):
        """Tests base_model.py's adherence to pycodestyle."""
        pycode = pycodestyle.StyleGuide(quiet=True)
        res = pycode.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_basemodel_module_docstring(self):
        """Tests existence of basemodel.py module docstring"""
        self.assertIsNot(models.base_model.__doc__, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(models.base_model.__doc__) >= 1,
                        "base_model.py needs a docstring")
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
