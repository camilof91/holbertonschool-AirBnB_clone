#!/usr/bin/python3
from models.engine.file_storage import FileStorage
"""
We are going to create an instance of FileStorage, a component
that will be responsible for handling the serialization and
deserialization of objects in a JSON file(POINT 5).
"""
storage = FileStorage()
storage.reload()
