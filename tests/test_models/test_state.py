#!/usr/bin/python3


""" The test_state module """

from models.state import State
from unittest import TestCase


class TestState(TestCase):
    """ The Test case for """

    def setUp(self) -> None:
        """ The setup method"""
        self.test_1 = State()

    def tearDown(self) -> None:
        """ The teardown method """
        pass

    def test_unrecognized_attribute(self):
        """ The test unrecognized attribute """
        with self.assertRaises(AttributeError):
            self.test_1.no_attribute

    def test_unrecognized_method(self):
        """ The test unrecognized method"""
        with self.assertRaises(AttributeError):
            self.test_1.no_method

    def test_class_attributes(self):
        """ Test class attributes"""
        self.assertEqual(self.test_1.name, "")

    def test_instance_of_test_1(self):
        """ Test the class instance """
        self.assertIsInstance(self.test_1, State)
