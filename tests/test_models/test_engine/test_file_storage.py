#!/usr/bin/python3


""" The Test Module for the FileStorage Class """


from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCase):
    """ The Class that Tests the Storage of Our json strings """

    def setUp(self):
        """ The Setup Method"""
        self.test_1 = FileStorage()

    def tearDown(self) -> None:
        """ The tearDown Method"""
        pass

    def test_unrecognized_all_method_arguement(self):
        """ This test checks if the arguement entered is an attribute"""
        with self.assertRaises(TypeError):
            self.test_1.all(2)

    def test_unrecognized_new_method_arguement(self):
        """ This test checks if the arguement entered is an attribute """
        with self.assertRaises(TypeError):
            self.test_1.new(3, 3)

    def test_all_returns_dict_object(self):
        """ Test if the all method returns a dictionary """
        self.assertIsInstance(self.test_1.all(), dict)

    def test_unrecognized_attribute_of_test_1(self):
        """ Test that the class attribute "object" is not accessible outside
            The class
        """
        with self.assertRaises(AttributeError):
            self.obj = self.test_1.objects
            self.file = self.test_1.file_path
