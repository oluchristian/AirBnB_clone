#!/usr/bin/python3

""" The review Module """

from models.review import Review
from models.base_model import BaseModel
from unittest import TestCase


class TestReview(TestCase):
    """ Test Review Class """

    def setUp(self) -> None:
        self.test_1 = Review()

    def tearDown(self) -> None:
        pass

    def test_class_attribures(self):
        """Test the class attributes of Review"""
        self.assertEqual(self.test_1.place_id, "")
        self.assertEqual(self.test_1.user_id, "")
        self.assertEqual(self.test_1.text, "")

    def test_instance_of_test_1(self):
        """ Check the instance of test_1"""
        self.assertIsInstance(self.test_1, (Review, BaseModel))

    def test_unrecognized_attribute(self):
        """ Test The unrecognized attribute"""
        with self.assertRaises(AttributeError):
            self.test_1.no_attribute

    def test_unrecognized_method(self):
        """" Test the unrecognized method"""
        with self.assertRaises(AttributeError):
            self.test_1.no_method()
