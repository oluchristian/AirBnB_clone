#!/usr/bin/python3

""" Module for the console """


import cmd
import re
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """HBNBCommand - Custom Command Interpreter for HBNB Project

    A command-line interpreter based on the cmd module for
    the HBNB project.
    This interpreter supports custom commands.

    Attributes:
        prompt (str): The custom prompt displayed to the user.

    Args:
        cmd (Cmd): _description_
    """
    prompt = "(hbnb) "
    __registered_models = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def default(self, line):
        """
        Handles unknown syntax and special cases.

        Args:
            line (str): The command string entered by the user.

        Returns:
            None

        This method is called when an unrecognized command is entered.
        It checks if the input matches the expected pattern for model
        method calls.
        (e.g., "class_name.method_name(arguement)"). If a match is found,
        it constructs the command using the '__handle_model' method and
        passes it to the 'onecmd' method for execution. Otherwise, it prints
        an error message about the unknown syntax.

        Example:
            (hbnb) User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
            Command: show User "38f22813-2753-4d42-b37c-57a17f1e4f88"
        """
        match = re.match(pattern=r"(\w+)\.(\w+)\((.*)\)", string=line)
        if match:
            # Match found, construct the command using '__handle_model'
            command = self.__handle_model(match.groups())
            # Pass the command to 'onecmd' for execution
            # print(f"Command: {command}")
            # split_command = command.split()
            self.onecmd(command)
        else:
            # No match found, print an error message
            print(f"*** Unknown syntax: {line.strip()}")
            return

    def help_default(self):
        """Help function for do_default method
        """
        print("Handles unknown syntax and special cases.")

    def __handle_model(self, groups):
        """
        Construct a command string based on the provided groups.

        Args:
            groups (tuple): A tuple containing the model name, method name,
                            and arguments.

        Returns:
            str: The formatted command string.

        This private method takes a tuple of groups
        (model_name, method_name, arguments)
        and constructs a command string in the format
        "method_name model_name arguments".
        It is used by the 'default' method to generate the command to be
        executed.

        Example:
            __handle_model(('User', 'show', '"38f22813-2753-4d42"'))
            Output: "show User \"38f22813-2753-4d42\""
        """
        # Unpack groups into model_name, method_name, and arguments
        model_name, method_name, arguement = groups
        # Remove surrounding quotes from the arguments
        # Check if the method requires quotes around the arguments
        if method_name in ['show', 'destroy']:
            arguement = arguement.strip('"')
        if method_name == 'update':
            id, attr_dict = re.match(r'"([^"]+)",\s(.*)', arguement).groups()
        # Ensure double-quoted property names in the attribute dictionary
            attribute_dict = json.loads(attr_dict.replace("'", "\""))
        # Construct the command string
            arguement = f'{id} {json.dumps(attribute_dict)}'

        # Construct the command string using the provided format
        return f"{method_name} {model_name} {arguement}"

    def help___handle_model(self):
        """Help function for __handle_model private class method
        """
        print("Construct a command string based on the provided groups.")

    def do_EOF(self, line):
        """End of file command

        Args:
            line (string): ctrl + D

        Returns:
            _type_: returns true and exits the program
        """
        # Print a newline for better output formatting
        print("")
        return True

    def help_EOF(self):
        """provides EOF command documentation

        Args:
            line (string): the string "help EOF"
        """
        print("This is the end of file command")

    def do_quit(self, line):
        """Exit the program

        Args:
            line (string): "quit" passed to the terminal

        Returns:
            _type_: returns true and exit the program
        """
        return True

    def help_quit(self):
        """provides quit command documentation

        Args:
            line (string): the string "help quit"
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """Do nothing if an empty line is passed as command
        """
        pass

    def help_emptyline(self):
        """Do nothing if an empty line is passed as command
        """
        print("This is an empty line. Do nothing")

    def do_create(self, line):
        """Creates a new instance of a class, saves it, and
            prints its id

        Args:
            line (str): The full command line passed by the user
        """
        # Check if class name is missing
        if not line:
            print("** class name missing **")
        else:
            # Get the registered models
            registered_models = HBNBCommand.__registered_models
            # Check if the class exists in registered models
            if line in registered_models:
                # Create a new instance of the class
                new_instance = registered_models[line]()
                # Save the new instance
                new_instance.save()
                # Print the id of the new instance
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def help_create(self):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
            and prints the id

            Usage:
                show [class_name] [id]
        """
        print(self.help_create.__doc__)

    def do_show(self, line):
        """Prints the string representation of an instance
            based on class name and id

        Args:
            line (_type_): _description_
        """
        # Split the command line into arguments
        args = line.split()
        # Check if class name is missing
        if not args:
            print("** class name missing **")
            return
        # Extract class name from arguments
        className = args[0]
        # Get the registered models
        registered_models = HBNBCommand.__registered_models
        # Check if the class exists in registered models
        if className not in registered_models:
            print("** class doesn't exist **")
            return
        # Check if instance id is missing
        if len(args) < 2:
            print("** instance id missing **")
            return
        # Extract instance id from arguments
        instance_id = args[1]
        # Create a key for the instance based on class name and id
        key = "{}.{}".format(className, instance_id)
        # Check if the key exists in the storage (storage.__objects)
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        else:
            # Print the string representation of the instance
            print(storage.all()[key])

    def help_show(self):
        """
        Print help information for the 'show' command.

        Usage:
            show [class_name] [id]

        Description:
            Prints the string representation of an instance based on the
                class name and id.
            The 'class_name' argument is the name of the class.
            The 'id' argument is the unique identifier of the instance.

        Examples:
            $ show BaseModel 1234-1234-1234
                Prints the information for the instance of 'BaseModel'
                with the given ID.

        Error Handling:
            - If 'class_name' is missing, print "** class name missing **".
            - If 'class_name' doesn't exist, print "** class doesn't exist **".
            - If 'id' is missing, print "** instance id missing **".
            - If the instance of the class name doesn't exist for the id,
                print "** no instance found **".
        """
        print(self.help_show.__doc__)

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id

        Args:
            line (_type_): The full command line passed by the user
        """
        # Split the command line into a list of arguments
        args = line.split()
        # Check if class name is missing
        if not args:
            print("** class name missing **")
            return
        # Extract class name from arguments
        className = args[0]
        # Check if the class exists in registered models
        if className not in HBNBCommand.__registered_models:
            print("** class doesn't exist **")
            return
        # Check if instance id is missing

        if len(args) < 2:
            print("** instance id missing **")
            return
        # Extract instance id from arguments
        instance_id = args[1]
        # Create a key using class name and instance id
        key = "{}.{}".format(className, instance_id)
        # Check if the instance exists
        if key not in storage.all():
            print("** no instance found **")
        else:
            # Delete the instance from the storage and save changes
            del storage.all()[key]
            storage.save()
            return

    def help_destroy(self):
        """
        Print help message for the destroy command.
        Usage:
            destroy <class name> <id>
        Deletes an instance based on the class name and id.
        Saves the change into the JSON file.

        Example: $ destroy BaseModel 1234-1234-1234
        If the class name is missing, print ** class name missing **
            (ex: $ destroy)
        If the class name doesn't exist, print ** class doesn't exist **
            (ex: $ destroy MyModel)
        If the id is missing, print ** instance id missing **
            (ex: $ destroy BaseModel)
        If the instance of the class name doesn't exist for the id,
        print ** no instance found **
            (ex: $ destroy BaseModel 121212)
        """
        print(self.help_destroy.__doc__)

    def do_all(self, line):
        """Prints string representations of instances based on
            class name or all instances

        Args:
            line (str): The full command line passed by the user
        """
        # Split the command line into arguments
        args = line.split()
        # Check if there are arguments
        if args:
            # Extract class name from arguments
            className = args[0]
            # Check if the class exists in registered models
            if className not in HBNBCommand.__registered_models:
                print("** class doesn't exist **")
                return
            # Iterate through all instances and print those
            # belonging to the specified class
            for key, value in storage.all().items():
                if key.split('.')[0] == className:
                    print(value)
        else:
            # If no arguments, print string representations of all instances
            for instance in storage.all().values():
                print(instance)

    def help_all(self):
        """
        Print all string representations of instances based on the class name.

        Usage: all [class_name]

        Example:
            - Print all instances of BaseModel: all BaseModel
            - Print all instances of a specified class: all MyModel

        If the class name doesn't exist, print ** class doesn't exist **.
        """
        print(self.help_all.__doc__)

    def do_update(self, line):
        """Updates an instance based on class name and id by
            adding or updating an attribute

        Args:
            line (str): The full command line passed by the user
        """
        dict_check = re.match(pattern=r"(\w+)\s(.*)\s({.*})", string=line)
        if dict_check:
            class_name, instance_id, dictionary_str = dict_check.groups()
            attribute_dict = json.loads(dictionary_str)
            # attribute_dict = json.loads(dictionary_str.replace("'", "\""))
            # Retrieve the instance from storage
            key = "{}.{}".format(class_name, instance_id)
            
            if key not in storage.all():
                print("** no instance found **")
                return

            obj = storage.all()[key]

            # Update instance attributes based on the dictionary
            for attribute, value in attribute_dict.items():
                setattr(obj, attribute, value)

            # Save the changes to storage
            storage.save()
        else:    
            # Split the command line into arguments
            args = line.split()
            # Check if there are arguments
            if not args:
                print("** class name missing **")
                return
            # Extract class name from arguments
            class_name = args[0]
            # Check if the class exists in registered models
            registered_models = HBNBCommand.__registered_models
            if class_name not in registered_models:
                print("** class doesn't exist **")
                return
            # Check if instance id is missing
            if len(args) < 2:
                print("** instance id missing **")
                return
            # Extract instance id from arguments
            instance_id = args[1]
            # Create a string representing the combination
            # of class name and instance id
            class_and_id = "{}.{}".format(class_name, instance_id)
            # Check if the instance exists in storage
            if class_and_id not in storage.all():
                print("** no instance found **")
                return
            # Check if attribute name is missing
            if len(args) < 3:
                print("** attribute name missing **")
                return
            # Extract attribute name from arguments
            attribute_name = args[2]
            # Check if value is missing
            if len(args) < 4:
                print("** value missing **")
                return
            # Extract attribute value from arguments
            attribute_value = args[3]
            # Retrieve the instance from storage
            obj = storage.all()[class_and_id]
            # Set the attribute value using setattr
            setattr(obj, attribute_name, attribute_value)
            # Save the changes to storage
            storage.save()

    def help_update(self):
        """Display help messages for the 'update' command

        Args:
            line (str): The command for which help is requested (update)

        Update an instance based on the class name and id by adding or
        updating attributes
        Usage:
            update <class name> <id> <attribute name> '<attribute value>'
        Only one attribute can be updated at a time

        Arguments:
            <class name> - The name of the class of the instance
        <id> - The id of the instance to be updated
        <attribute name> - The name of the attribute to be updated
        '<attribute value>' - The new value for the attribute
            (enclosed in single quotes)
        Example:
            update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        print(self.help_update.__doc__)
        
    def do_count(self, line):
        """
        Retrieve the number of instances of a class.

        Args:
            line (str): The full command line passed by the user.

        Example:
            (hbnb) User.count()
        """
        # Split the command line into arguments
        args = line.split()
        # Check if class name is missing
        if not args:
            print("** class name missing **")
            return
        # Extract class name from arguments
        class_name = args[0]
        # Get the registered models
        registered_models = HBNBCommand.__registered_models
        # Check if the class exists in registered models
        if class_name not in registered_models:
            print("** class doesn't exist **")
            return
        # Count the number of instances of the specified class
        count = sum(1 for key in storage.all() if key.startswith(f"{class_name}."))
        print(count)
        
    def help_update(self):
        """Counts the number of class instances
        """
        print("This counts numbers of instances of a class")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
