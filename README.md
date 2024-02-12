# AirBnB Clone Project

## Project Description

This project is an AirBnB clone, which includes a custom command-line interpreter (console) for managing and interacting with instances of various classes. The command interpreter provides functionality for creating, updating, deleting, and querying instances of different classes in the AirBnB application.

## Command Interpreter Description

The custom command interpreter, named console.py, is designed for the AirBnB project. It allows users to interact with the system through a command-line interface, executing commands to manipulate and retrieve information about instances of classes such as User, State, City, Amenity, Place, Review, and BaseModel.

## How to Start the Command Interpreter
To start the command interpreter, run the following command in the terminal:

## Installation

To start the command interpreter, run the following command in the terminal:

```bash
./console.py
```

This will launch the console, and you'll see a prompt (hbnb) indicating that you are inside the command interpreter.

## How to Use the Command Interpreter
Once inside the command interpreter, you can use various commands to interact with the system. Here are some examples of supported commands:

```python
# Create an Instance:
create <class_name>

# Show Instance Information:
show <class_name> <instance_id>

# Destroy an Instance:
destroy <class_name> <instance_id>

# Show All Instances or Instances of a Class:
all [<class_name>]

# Update an Instance:
update <class_name> <instance_id> <attribute_name> '<attribute_value>'

# Count Instances of a Class:
<class_name>.count()
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

