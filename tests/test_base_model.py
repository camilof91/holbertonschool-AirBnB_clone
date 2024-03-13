#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""
Here we are testing the file base_model
"""


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        objeto = BaseModel()
        result = str(objeto)
        self.assertEqual(
            result, f"[BaseModel] ({objeto.id}) {objeto.__dict__}")
