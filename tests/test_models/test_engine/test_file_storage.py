#!/usr/bin/python3
"""
Tests for File Storage
"""
import unittest
import datetime
import pycodestyle
from models.engine.file_storage import FileStorage


class TestFilestorage (unittest.TestCase):
    """ class for testing the file storage module """
    def test_filestorage_confirm_pycode(self):
        """ test adherance to pycodestyle """
        pycode = pycodestyle.StyleGuide(quiet=True)
        result = pycode.check_files(['file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                "Found code style errors (and warnings).")

    def test_filestorage_doc_string(self):
        """ test the existence of file_storage's docstring """
        self.assertIsNot(file_storage.__doc__, None,
                "file_storage needs a docstring")
        self.assertEqual(len(file_storage.__doc__) >= 1,
                "file_storage needs a docstring")
