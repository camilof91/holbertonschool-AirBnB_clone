#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
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
        key = obj.__class__.__name__
        self.__objects["{}.{}".format(key, obj.id)] = obj

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
                from models.base_model import BaseModel
                from models.user import User  
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review
                for key, value in serialized_objects.items():
                    if value['__class__'] != "NoneType":
                        class_name = value['__class__']
                        if class_name == "BaseModel":
                            self.__objects[key] = BaseModel(**value)
                        elif class_name == "User":  
                            self.__objects[key] = User(**value)
                        elif class_name == "Place":
                            self.__objects[key] = Place(**value)
                        elif class_name == "State":
                            self.__objects[key] == State(**value)
                        elif class_name == "City":
                            self.__objects[key] == City(**value)
                        elif class_name == "Amenity":
                            self.__objects == Amenity(**value)
                        elif class_name == "Review":
                            self.__objects == Review(**value)
        except FileNotFoundError:
            pass
