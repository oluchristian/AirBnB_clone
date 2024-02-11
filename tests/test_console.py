#!/usr/bin/python3

""" The Test case for the console """

from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from datetime import datetime
from unittest import TestCase
from console import HBNBCommand
from cmd import Cmd


class TestConsole(TestCase):
    """ The TestConsole Class """

    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        """ The tearDown Method"""
        pass

    def test_the_prompt(self):
        """ Checks if the prompt is hbnb """
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_the_instance_of_prompt_variable(self):
        self.assertIsInstance(HBNBCommand.prompt, str)

    def test_if_match_is_in_dict_of_HBNB(self):
        self.assertIn("default", HBNBCommand.__dict__)

    def test_registered_models_not_in_dict(self):
        self.assertNotIn("__registered_models", HBNBCommand.__dict__)
        self.assertNotIn("registered_models", HBNBCommand.__dict__)
