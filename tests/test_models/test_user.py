#!/usr/bin/python3


""" The test_user module """


from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """ The TestUser Class """

    def setUp(self) -> None:
        """ The setup method"""
        self.test_1 = User()

    def tearDown(self) -> None:
        """ The teardown method"""
        pass

    def test_unrecognized_method(self):
        """ Tests unrecognized method """
        with self.assertRaises(AttributeError):
            self.test_1.no_method()

    def test_unrecognized_attribute(self):
        """ Test Unrecognized attributes """
        with self.assertRaises(AttributeError):
            self.test_1.no_attribute

    def test_instance_of_test_1(self):
        """ Check the instance of the test_1 """
        self.assertIsInstance(self.test_1, User)

    def test_class_attribute(self):
        """ Test the class attributes of the class test_1"""
        self.assertEqual(self.test_1.email, "")
        self.assertEqual(self.test_1.password, "")
        self.assertEqual(self.test_1.first_name, "")
        self.assertEqual(self.test_1.last_name, "")
