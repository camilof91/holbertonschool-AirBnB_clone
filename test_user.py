#!/usr/bin/python3
""" Unit tests for class User """
import unittest
from models.user import User
from datetime import datetime

class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_attributes_existence(self):
        """Test if User instance has the required attributes."""
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_default_attribute_values(self):
        """Test if User instance attributes have the correct default values."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        
    def test_instantiate(self):
        """ Happy pass instantiation """
        self.assertEqual(User, type(User()))

    def test_id(self):
        """ Happy pass public id string format """
        self.assertEqual(str, type(User().id))

    def test_created_at(self):
        """ Happy pass created at datetime """
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at(self):
        """ Happy pass updated at datetime """
        self.assertEqual(datetime, type(User().updated_at))

    def test_uid(self):
        """ UID created at each instantiation """
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_email(self):
        """ Happy pass email """
        user1 = User()
        self.assertEqual(str, type(User.email))
        self.assertTrue(hasattr(user1, "email"))

    def test_password(self):
        """ Happy pass password """
        user1 = User()
        self.assertEqual(str, type(User.password))
        self.assertTrue(hasattr(user1, "password"))

    def test_first_name(self):
        """ Happy pass first name """
        user1 = User()
        self.assertEqual(str, type(User.first_name))
        self.assertTrue(hasattr(user1, "first_name"))

    def test_last_name(self):
        """ Happy pass last name """
        user1 = User()
        self.assertEqual(str, type(User.last_name))
        self.assertTrue(hasattr(user1, "last_name"))


if __name__ == '__main__':
    unittest.main()
