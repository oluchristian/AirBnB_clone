#!/usr/bin/python3

""" Documentation for the filestorage """
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """ The FileStorage class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns classes in __object

        Returns:
            dictionary: returns a dictionary in __objects attribute
        """
        return self.__objects

    def new(self, obj):
        """Creates a dictionary representation of all instance
            of a class and saves it in __object attribute

        Args:
            obj (_type of class_): this is an instance of a class
        """
        # The key of each instance is stored as <obj class name>.id
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Converts the obj to a dictionary representation
        """
        serializable_objects = {}
        # Modify the created_at, updated_at attr and add __class__
        # attr to an instance using the to_dict() method in BaseModel
        for key, value in self.__objects.items():
            serializable_objects[key] = value.to_dict()
        # open the file in __file_path in write mode
        with open(self.__file_path, 'w') as file:
            # converts the dictionary into json format
            json.dump(serializable_objects, file)

    def reload(self):
        """Deserailize a json file containing
        """
        if self.__file_path:
            try:
                # open the file in __file_path in read mode
                with open(self.__file_path, 'r') as file:
                    # converts the json file into a python dictionary
                    deserialized_json = json.load(file)
                for classnameAndId, object_dict in deserialized_json.items():
                    # By using tuple unpacking, we can get the class name
                    class_name, object_id = classnameAndId.split('.', 1)
                    # obj_dict contains a dictionary of all attr in obj
                    obj = eval(class_name)(**object_dict)
                    self.__objects[classnameAndId] = obj
            except FileNotFoundError:
                pass
