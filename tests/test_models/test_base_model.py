#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
import copy
"""
Here we are testing the file base_model
"""


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        objeto = BaseModel()
        initial_time = copy.deepcopy(objeto.updated_at)
        sleep(1)
        objeto.save()
        time_after_save = objeto.updated_at
        self.assertNotEqual(initial_time, time_after_save)
        self.assertIsInstance(time_after_save, datetime)

    def test_str(self):
        objeto = BaseModel()
        result = str(objeto)
        self.assertEqual(
            result, f"[BaseModel] ({objeto.id}) {objeto.__dict__}")
