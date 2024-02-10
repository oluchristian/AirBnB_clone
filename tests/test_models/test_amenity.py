#!/usr/bin/python3

""" The Amenity Module """

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """ The Amenity Class """
    def setUp(self):
        "The Setup method"
        self.name = Amenity()

    def tearDown(self):
        """ The tearDown Method """
        pass

    def test_name_variable(self):
        """ Test the name Variable """
        self.assertEqual(Amenity().name, "")

    def test_instance_of_name(self):
        """ Tests the name instance"""
        self.assertIsInstance(self.name, Amenity)

    def test_unrecognized_instance_attribute(self):
        """ The tests for unrecognized attribute"""
        with self.assertRaises(AttributeError):
            self.name.age

    def test_unrecognized_method(self):
        """ The tests for unrecognized method """
        with self.assertRaises(AttributeError):
            self.name.no_method()
