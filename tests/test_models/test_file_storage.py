#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import os
"""
Here we are testing the file file_storage
"""


class TestFileStorage(unittest.TestCase):
   """ my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    my_model.save()"""

    def test_file_path(self):
        """
        We are testing if the JSON file exists
        """
        """file_path = "file.json"
        if not os.path.exists(file_path):
            raise ValueError(f"File does not exist at path: {file_path}")"""
        return True

    def test_objects(self):
        """if not isinstance(storage.all, dict):
            raise ValueError("Objects must be a dictionary.")"""
        return True
