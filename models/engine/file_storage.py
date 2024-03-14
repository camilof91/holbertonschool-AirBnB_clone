#!/usr/bin/python3
import json
"""
In this file we are going to serialize instances into a JSON file and
deserialize the JSON file into instances
"""


class FileStorage:
    """
    This class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as open_file:
            json.dump(serialized_objects, open_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as open_file:
                serialized_objects = json.load(open_file)
                for key, value in serialized_objects.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
