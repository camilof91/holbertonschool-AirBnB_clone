#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime
"""
    Represents a sample class with attributes
    for identification and timestamps.

    Attributes:
        id (uuid.UUID): Unique identifier generated using uuid.uuid4().
        created_at (datetime.datetime):
            Date and time when the instance is created.
        updated_at (datetime.datetime):
            Date and time of the last update of the instance.
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the class.
        This function assigns initial values to the instance attributes
        """

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != '__class__':
                    setattr(self, key, value)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            """New objects can only be included in storage when
            the objects do not come from the JSON file (Point 5)"""

    def __str__(self):
        """
        Returns the form in which the information should be printed
        """
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save the date current
        """
        self.updated_at = datetime.now()
        """Call the save function to update the file
            in case there are changes(point 5)"""
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert the instance to a dictionary.

        Returns:
        dict: A dictionary containing all attributes of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
