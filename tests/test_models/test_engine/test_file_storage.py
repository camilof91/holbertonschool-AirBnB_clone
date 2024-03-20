#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up test environment after testing."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    # def test_all_empty_initially(self):
    #     """Test if all() method returns an empty dictionary initially."""
    #     all_objects = self.storage.all()
    #     self.assertEqual(all_objects, {})

    def test_all_empty_initially(self):
        """Test if all() method returns an empty dictionary initially."""
        all_objects = self.storage.all()
        self.assertEqual(all_objects, {})

    def test_save_method(self):
        """Test if save() method saves the objects to the JSON file."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(FileStorage._FileStorage__file_path, 'r') as file:
            data = file.read()
            self.assertIn(obj.id, data)

    # def test_reload_method(self):
    #     """Test if reload() method loads objects from the JSON file."""
    #     obj = BaseModel()
    #     self.storage.new(obj)
    #     self.storage.save()
    #     new_storage = FileStorage()
    #     new_storage.reload()
    #     all_objects = new_storage.all()
    #     self.assertIn(obj.id, all_objects)


if __name__ == '__main__':
    unittest.main()
