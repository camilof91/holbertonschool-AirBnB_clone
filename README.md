# AirBnB Clone Project
### Description

This project aims to build a command-line interface (CLI) to manage AirBnB objects, such as users, states, cities, places, amenities, and reviews. This project is the first step towards building a full web application, involving HTML/CSS templating, database storage, API, and front-end integration.
Command Interpreter

The command interpreter allows you to manage the objects of the AirBnB project. It provides functionalities to:

    Create a new object
    Retrieve an object from a file or database
    Perform operations on objects (count, compute stats, etc.)
    Update attributes of an object
    Destroy an object

### How to Start

To start the command interpreter, execute the console.py script.

```bash
$ ./console.py
```

### How to Use

Once in the interpreter, you can use the following commands:

    help: Display available commands and their descriptions.
    create: Create a new instance of a specified class.
    show: Display the string representation of an instance based on class name and ID.
    destroy: Delete an instance based on class name and ID.
    all: Print string representations of all instances or of instances of a specified class.
    update: Update an instance's attributes based on class name and ID.

#### Examples

```bash
$ ./console.py
(hbnb) create BaseModel
a54f32b1-6b0b-4f70-9299-b62f1d49357d
(hbnb) show BaseModel a54f32b1-6b0b-4f70-9299-b62f1d49357d
[BaseModel] (a54f32b1-6b0b-4f70-9299-b62f1d49357d) {'id': 'a54f32b1-6b0b-4f70-9299-b62f1d49357d', 'created_at': '2024-03-12T15:30:00.000000', 'updated_at': '2024-03-12T15:30:00.000000'}
(hbnb) quit
$
```

### Requirements

    Python 3.8.5 or later
    pycodestyle 2.7.* for code style checking

## Project Structure

The project repository contains the following structure:

```markdown

### holbertonschool-AirBnB_clone/
├── README.md
├── AUTHORS
├── console.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   └── review.py
└── tests/
    └── test_models/
        ├── test_base_model.py
        ├── test_user.py
        ├── test_state.py
        ├── test_city.py
        ├── test_amenity.py
        ├── test_place.py
        └── test_review.py
```

### Testing

Unit tests are provided for all classes and functionalities. To run the tests, execute the following command:

```bash
$ python3 -m unittest discover tests
```

## Authors

<p><strong><big>Nataly Rodriguez</big></strong></p>

<div>
    <a href="https://www.linkedin.com/in/camilo-fetecua">
        <img src="https://github.com/camilof91/imagenes/blob/master/icons-linkedin.png?raw=true" style="display: inline-block; margin-right: 20px; vertical-align: middle;" width="60">
    </a>
    <a href="https://github.com/camilof91">
        <img src="https://github.com/camilof91/imagenes/blob/master/big-%20GitHub-logo.png?raw=true" style="display: inline-block; vertical-align: middle;" width="100">
    </a>
</div>

<p><strong><big>Jesenia Bernal</big></strong></p>

<div>
    <a href="https://www.linkedin.com/in/camilo-fetecua">
        <img src="https://github.com/camilof91/imagenes/blob/master/icons-linkedin.png?raw=true" style="display: inline-block; margin-right: 20px; vertical-align: middle;" width="60">
    </a>
    <a href="https://github.com/camilof91">
        <img src="https://github.com/camilof91/imagenes/blob/master/big-%20GitHub-logo.png?raw=true" style="display: inline-block; vertical-align: middle;" width="100">
    </a>
</div>

<p><strong><big>Camilo Fetecua</big></strong></p>

<div>
    <a href="https://www.linkedin.com/in/camilo-fetecua">
        <img src="https://github.com/camilof91/imagenes/blob/master/icons-linkedin.png?raw=true" style="display: inline-block; margin-right: 20px; vertical-align: middle;" width="60">
    </a>
    <a href="https://github.com/camilof91">
        <img src="https://github.com/camilof91/imagenes/blob/master/big-%20GitHub-logo.png?raw=true" style="display: inline-block; vertical-align: middle;" width="100">
    </a>
</div>

