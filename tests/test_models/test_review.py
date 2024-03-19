#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review


class TestReviewInstantiation(unittest.TestCase):
    """Test instantiation of the Review class."""

    def test_instance_creation(self):
        """Test if instance of Review is properly created."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_id_is_string(self):
        """Test if id attribute is a string."""
        review = Review()
        self.assertIsInstance(review.id, str)

    def test_created_at_is_datetime(self):
        """Test if created_at attribute is a datetime object."""
        review = Review()
        self.assertIsInstance(review.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test if updated_at attribute is a datetime object."""
        review = Review()
        self.assertIsInstance(review.updated_at, datetime)

    def test_place_id_is_empty_string(self):
        """Test if place_id attribute is initialized as an empty string."""
        review = Review()
        self.assertEqual(review.place_id, "")

    def test_user_id_is_empty_string(self):
        """Test if user_id attribute is initialized as an empty string."""
        review = Review()
        self.assertEqual(review.user_id, "")

    def test_text_is_empty_string(self):
        """Test if text attribute is initialized as an empty string."""
        review = Review()
        self.assertEqual(review.text, "")


if __name__ == '__main__':
    unittest.main()