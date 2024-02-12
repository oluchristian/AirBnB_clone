#!/usr/bin/python3

""" The Test case for the console """

from io import StringIO
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from datetime import datetime
from unittest import TestCase, mock
from console import HBNBCommand
from cmd import Cmd


class TestConsole(TestCase):
    """ The TestConsole Class """

    def setUp(self) -> None:
        """ The setUp method """
        self.console1 = HBNBCommand()

    def tearDown(self) -> None:
        """ The tearDown Method"""
        pass

    def test_the_prompt(self):
        """ Checks if the prompt is hbnb """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    def test_the_instance_of_prompt_variable(self):
        """ Check the instance of the prompt attribute """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIsInstance(HBNBCommand.prompt, str)

    def test_return_value_of_EOF(self):
        """ Check the return value of the EOF """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertEqual(HBNBCommand().do_EOF("BaseModel"), True)

    def test_instance_of_EOF_return_value(self):
        """ Check the return instance of the EOF() """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIsInstance(HBNBCommand().do_EOF("BaseModel"), bool)

    def test_is_HBNB_sub_Cmd(self):
        """ Test to see if the HBNB is a sub class of Cmd """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertTrue(issubclass(HBNBCommand, Cmd))

    def test_class_of_console1(self):
        """ Test to see the class the instance console1 belongs to """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIsInstance(self.console1, Cmd)

class TestDictInclusionHBNB(TestCase):
    "This class Test for Dictionary Inclusion "

    def test_if_default_is_in_dict_of_HBNB(self):
        """ Test if the default method is in the HBNB dictionary"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn("default", HBNBCommand.__dict__)

    def test_registered_models_not_in_dict(self):
        """ Tests for attributes not in the HBNBDictionary """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertNotIn("__registered_models", HBNBCommand.__dict__)
        self.assertNotIn("registered_models", HBNBCommand.__dict__)

    def test_show_in_dict(self):
        """ Test for the show command inclusion in dict """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn("do_show", HBNBCommand.__dict__)

    def test_all_in_dict(self):
        """ Test if the all command is in the HBNBCommand dictionary """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn("do_all", HBNBCommand.__dict__)

    def test_destroy_in_dict(self):
        """ Test if the destroy command is in the HBNBCommand dictionary """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn("do_destroy", HBNBCommand.__dict__)

    def test_create_in_dict(self):
        """ Test if the create command is in the HBNBCommand dictionary """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn("do_create", HBNBCommand.__dict__)

    def test_update_in_dict(self):
        """ Test if the create command is in the HBNBCommand dictionary """
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIn("do_update", HBNBCommand.__dict__)

    def test_handle_model_not_in_dict(self):
        """ Test if the handle_model is not in the HBNBCommand dictionary"""
        with mock.patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
        self.assertIsNot("__handle_model", HBNBCommand.__dict__)
