# AirBnB Clone Project

## Background

Welcome to the AirBnB clone project! This repository contains the initial steps and requirements for building an AirBnB clone web application.

### Command Interpreter

The first step in this project is to develop a command interpreter. This command interpreter will facilitate the management of AirBnB objects within the application. It is a crucial step as the functionality built here will be utilized in subsequent projects such as HTML/CSS templating, database storage, API integration, and front-end development.

The objectives of this step are as follows:

- Implement a parent class called BaseModel to handle the initialization, serialization, and deserialization of all future instances.
- Establish a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> File.
- Create all the necessary classes for AirBnB (e.g., User, State, City, Place) as subclasses of the BaseModel.
- Develop the first abstracted storage engine for the project, which is the File storage.
- Create comprehensive unit tests to validate all classes and the storage engine.

#### Command Interpreter Overview

The command interpreter serves as an interactive shell, similar to the Shell in Unix, allowing you to manage the objects of the AirBnB project. Some of the supported operations include:

- Creating a new object (e.g., User, Place).
- Retrieving objects from files or databases.
- Performing operations on objects (e.g., counting, computing stats).
- Updating object attributes.
- Deleting objects.

### Learning resources

- cmd module documentation
- cmd module in-depth guide
- Python modules and packages documentation
- uuid module
- datetime module
- unittest module
- args/kwargs in Python
- Python test cheatsheet
- cmd module on the Python Wiki
- Python unittest documentation

### Learning Objectives

- Create a Python package for a project.
- Develop a command interpreter using the cmd module in Python.
- Understand the concept of unit testing and implement it in a large project.
- Serialize and deserialize a class object.
- Read and write data to JSON files.
- Manage datetime objects.
- Work with UUIDs (Universally Unique Identifiers).
- Utilize *args and **kwargs in function signatures.
- Handle named arguments in functions effectively.

## Requirements

### Python Scripts

- All files interpreted/compiled using Python 3.8.5 on Ubuntu 20.04 LTS.
- Code adhere to pycodestyle (version 2.8.*) guidelines.
- All files  executable.
- All modules, classes, and functions include proper documentation.
- Documentation is descriptive and complete.

### Python Unit Tests

All test files are stored in a tests folder.
Unit tests use the unittest module.
All test files and folders start with test_.
Test file organization mirrors the project hierarchy.
To execute all tests, run

```bash
python3 -m unittest discover tests
```

Individual test files can be run using the command

```bash
python3 -m unittest tests/test_models/test_base_model.py
```

All tests include proper documentation.

## Execution

The command interpreter can be used interactively or in non-interactive mode. Below are examples of both:

Interactive Mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
```

Non-interactive Mode (using a file):

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

Non-interactive Mode (redirecting input):

```bash
$ cat test_help
help
```

```bash
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
```

All tests also pass in non-interactive mode:

```Bash
echo "python3 -m unittest discover tests" | bash
```
