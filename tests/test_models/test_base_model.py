#!/usr/bin/python3

""" The Base Model Test Module"""

from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ The test case class for base_model class """

    def setUp(self):
        """ The setup method"""
        self.base_1 = BaseModel()
        self.base_1.name = "Israel"
        self.base_1.age = 25
        self.base_1.sex = "Male"

        self.dictionary = self.base_1.to_dict()
        self.base_2 = self.base_1.to_dict()

    def tearDown(self) -> None:
        """ The tear Down Method"""
        pass

    def test_check_equal_values(self):
        """ This check if attributes of the instance base_1 are correct"""
        self.assertEqual(self.base_1.name, "Israel")
        self.assertEqual(self.base_1.age, 25)
        self.assertEqual(self.base_1.sex, "Male")

    def test_check_unrecognized_attribute(self):
        """ Raises an attribute error if an instance tries to access an
        an attribute that is not available"""

        with self.assertRaises(AttributeError):
            self.base_1.school
            self.base_1.house

    def test_check_base_1_instance(self):
        """ Checks if the base_1 model is an instance of the BaseModel Class"""
        self.assertIsInstance(self.base_1, BaseModel)

    def test_unwritable_datetime_attribute_created_at(self):
        """ Raises an Attribute Error if a user tries to access a datetime
            Attribute, since it is not writeable
        """
        with self.assertRaises(AttributeError):
            self.base_1.created_at.year = 2022

    def test_unwritable_datetime_attribute_updated_at(self):
        """ Raises an Attribute Error if a user tries to access a datetime
            Attribute, since it is not writeable
        """
        with self.assertRaises(AttributeError):
            self.base_1.updated_at.year = 2022

    def test_check_instance_of_created_at_attribute(self):
        """ Checks if the instance of the created_at attribute is
            and instance of the datetime class
        """
        self.assertIsInstance(self.base_1.created_at, datetime)

    def test_check_instance_of_updated_at_attribute(self):
        """ Checks if the instance of the updated_at attribute is an
            is an instance of the datetime class
        """
        self.assertIsInstance(self.base_1.updated_at, datetime)

    def test_unrecognized_parameter_passed_save_method(self):
        """ Passing another arguement to the save method Raises a Type Error"""
        with self.assertRaises(TypeError):
            self.base_1.save(2, 4)

    def test_unrecognized_parameter_passed_to_dict_method(self):
        """ Passing another arguement to to_dict method Raises a Type Error"""
        with self.assertRaises(TypeError):
            self.base_1.to_dict(2, 4)

    def test_instance_of_to_dict_return_value(self):
        """ Checks if the the Return value of the to_dict method is a dict"""
        self.assertIsInstance(self.base_2, dict)

    def test_instance_of_id_attribute(self):
        """ Checks the instance of the id attribute"""
        self.assertIsInstance(self.base_1.id, str)

    def test_instance_of_created_at_key(self):
        """ This tests for the instance of the created_at key of the to_dict
            Return Value
        """
        self.assertIsInstance(self.dictionary["created_at"], str)

    def test_instance_of_updated_at_key(self):
        """ This tests for the instance of the created_at key of the to_dict
            Return Value
        """
        self.assertIsInstance(self.dictionary["updated_at"], str)
