#!/usr/bin/python3
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):

    def test_default_name(self):
        """Test that the default name attribute is an empty string."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_name_assignment(self):
        """Test that the name attribute can be assigned a value."""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")

if __name__ == '__main__':
    unittest.main()
