import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def test_attributes_existence(self):
        """Test if State instance has the required attributes."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_default_attribute_values(self):
        """Test if State instance attributes have the correct default values."""
        state = State()
        self.assertEqual(state.name, "")

    def test_update_attribute(self):
        """Test updating an attribute of a State instance."""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_to_dict(self):
        """Test conversion of State instance to dictionary."""
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict['name'], "California")

    def test_create_instance_with_arguments(self):
        """Test creating a State instance with specific arguments."""
        state = State(name="New York")
        self.assertEqual(state.name, "New York")


if __name__ == '__main__':
    unittest.main()