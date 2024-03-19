#!/usr/bin/python3
import unittest
from datetime import datetime
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Test instantiation of the City class."""

    def test_instance_creation(self):
        """Test if instance of City is properly created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_id_is_string(self):
        """Test if id attribute is a string."""
        city = City()
        self.assertIsInstance(city.id, str)

    def test_created_at_is_datetime(self):
        """Test if created_at attribute is a datetime object."""
        city = City()
        self.assertIsInstance(city.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at attribute is a datetime object."""
        city = City()
        self.assertIsInstance(city.updated_at, datetime)

    def test_name_is_empty_string(self):
        """Test if name attribute is initialized as an empty string."""
        city = City()
        self.assertEqual(city.name, "")

    def test_state_id_is_empty_string(self):
        """Test if state_id attribute is initialized as an empty string."""
        city = City()
        self.assertEqual(city.state_id, "")


if __name__ == '__main__':
    unittest.main()
