#!/usr/bin/python3

""" The Amenity Module """


from models.city import City
from unittest import TestCase


class TestCity(TestCase):
    """ The Test City class """

    def setUp(self) -> None:
        """ The setup method"""
        self.test_1 = City()

    def tearDown(self) -> None:
        pass

    def test_state_id_attribute(self):
        """ The test state id attribute method """
        self.assertEqual(self.test_1.state_id, "")

    def test_name_attribute(self):
        """ The test name attribute method """
        self.assertEqual(self.test_1.name, "")

    def test_instance_of_test_1(self):
        """ The test_1 instance method """
        self.assertIsInstance(self.test_1, City)

    def test_unrecognized_attribute(self):
        """ Test unrecognized attribute"""
        with self.assertRaises(AttributeError):
            self.test_1.no_name

    def test_unrecognized_method(self):
        """ Test unrecognized method """
        with self.assertRaises(AttributeError):
            self.test_1.no_method()
