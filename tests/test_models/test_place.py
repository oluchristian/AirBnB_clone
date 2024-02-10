#!/usr/bin/python3

""" The test place module """

from models.place import Place
from unittest import TestCase


class TestPlace(TestCase):
    """ The module test place class """

    def setUp(self) -> None:
        self.test_1 = Place()

    def tearDown(self) -> None:
        pass

    def test_unrecognized_attribute(self):
        """ The test unrecognized attribute """
        with self.assertRaises(AttributeError):
            self.test_1.no_attribute

    def test_unrecognized_method(self):
        """ The test unrecognized method """
        with self.assertRaises(AttributeError):
            self.test_1.no_method()

    def test_instance_of_test_1(self):
        """ The test instance of the """
        self.assertIsInstance(self.test_1, Place)

    def test_city_id(self):
        """ Test the city Id """
        self.assertEqual(self.test_1.city_id, "")

    def test_user_id(self):
        """ Test the user Id"""
        self.assertEqual(self.test_1.user_id, "")

    def test_name(self):
        """ Test the name attribure """
        self.assertEqual(self.test_1.name, "")

    def test_description(self):
        """ Test the description attribute """
        self.assertEqual(self.test_1.description, "")

    def test_other_attributes(self):
        """ Test the number_room variable """
        self.assertEqual(self.test_1.number_bathrooms, 0)
        self.assertEqual(self.test_1.max_guest, 0)
        self.assertEqual(self.test_1.price_by_night, 0)
        self.assertEqual(self.test_1.latitude, 0.0)
        self.assertEqual(self.test_1.longitude, 0.0)
        self.assertEqual(self.test_1.amenity_ids, [])

    def test_instance_of_amenity_attribute(self):
        """ Checks the instance of the amenity attribute """
        self.assertIsInstance(self.test_1.amenity_ids, list)
