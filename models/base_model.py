#!/usr/bin/python3

""" This is the base Module"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """BaseModel that defines all common attributes/methods for other classes
    """
    def __str__(self):
        """A method invoked when an instance of Basemodel class is printed

            Returns:
            formatted string: returns class name, instance uuid and
            attributes
            """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with
            the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance

        Returns:
        dictionary: All key / values of __dict__
        """
        dictionary = self.__dict__.copy()
        # Adds a key __class__ and class name of the object to dictionary
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary

    def __init__(self, *args, **kwargs):
        """Method to assign attributes when a basemodel class is instantiated

        Args:
        id (str): a unique and randomly generated uuid for each instance
            of Basemodel
        created_at (datetime): Current date and time for a new instance
              of Basemodel
        updated_at (datetime): Current date and time when an instance of
        Basemodel is created or updated
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                # convert date time strings into datetime object
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                    # __class__ should not be added as an attribute
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
