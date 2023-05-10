#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import console
import pycodestyle


class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_exit(unittest.TestCase):
    """ unnittests for EOF and quit """
    def test_eof(self):
        """ test EOF method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("EOF")
        self.assertEqual("\n", output.getvalue())
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_quit(self):
        """ test for the quit method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("EOF")
        self.assertEqual("\n", output.getvalue())
        self.assertTrue(HBNBCommand().onecmd("quit"))

class TestHBNBCommand_doc_style(unittest.TestCase):
    """ unittests for pycodestyle and documentation"""
    def test_console_conformity_pycode(self):
        """Tests console.py's adherence to pycodestyle."""
        pycode = pycodestyle.StyleGuide(quiet=True)
        res = pycode.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Tests existence of console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = "Creates a new instance of BaseModel"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "Hit ctrl+D (EOF) to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = "Prints the string representation of an instance"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = "Deletes an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = "Prints all string representation of all instances"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        h = "Retrieves the number of instances of a class"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = "Updates an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help(self):
        """Tests help command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help")
        h  = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""

class TestHBNBCommand_create(unittest.TestCase):
    """ unittest for the create method """
    def test_error1(self):
        """ class name missing error """
        h = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
        self.assertEqual(h, output.getvalue().strip())

    def test_error2(self):
        """ class does not exist """
        h = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(h, output.getvalue().strip())

    def test_create_basemodel(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        key = "BaseModel.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("BaseModel.create()")
        s = "*** Unknown syntax: BaseModel.create()"
        self.assertEqual(s, output.getvalue().strip())

    def test_create_user(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
        key = "User.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_city(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
        key = "City.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_state(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
        key = "State.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_place(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
        key = "Place.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_amenity(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
        key = "Amenity.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_review(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
        key = "Review.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())
