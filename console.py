#!/usr/bin/python3
"""Defines the HBnB console."""
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class.
    This class provides an interactive command interpreter.
    """
    prompt = "(hbnb) "
    List_classes = ["BaseModel",
                    "User",
                    "Place",
                    "State",
                    "City",
                    "Amenity",
                    "Review"]

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when Ctrl + D is pressed"""
        print("")
        return True

    def do_help(self, arg):
        """Show help"""
        if arg == "quit":
            print("Quit command to exit the program")
        else:
            cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        pass

    def do_create(self, line):
        """Creates a new instance of a specified class."""
        argl = line.split()
        if not argl:
            print("** class name missing **")
            return

        class_name = argl[0]
        if class_name not in self.List_classes:
            print("** class doesn't exist **")
            return

        try:
            # Crear instancia de la clase
            new_instance = globals()[class_name]()
            # Configurar atributos si es necesario
            # new_instance.attr = value
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
        except Exception as e:
            print("Error creating instance:", str(e))

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        argl = arg.split()
        if not argl:
            print("** class name missing **")
            return

        class_name = argl[0]
        if class_name not in self.List_classes:
            print("** class doesn't exist **")
            return

        if len(argl) < 2:
            print("** instance id missing **")
            return

        key = class_name + '.' + argl[1]
        objects = models.storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class
        name and id (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        data = arg.split()
        if data[0] not in self.List_classes:
            print("** class doesn't exist **")
            return
        if len(data) == 1:
            print("** instance id missing **")
            return
        class_id = data[0] + "." + data[1]
        if class_id in storage.all().keys():
            with open("file.json", "w", encoding="utf-8"):
                storage.all().pop(class_id)
                storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based
        or not on the class name"""
        try:
            if arg:
                eval(arg)
            list_obj = [index.__str__() for index in storage.all().values()]
            print(list_obj)
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            print([str(obj) for obj in models.storage.all().values()])
            return
        argl = arg.split()
        if len(argl) == 0:
            print("** class name missing **")
            return
        class_name = argl[0]
        try:
            instances = [str(obj) for obj in models.storage.all().values()
                         if isinstance(obj, eval(class_name))]
            print(instances)
        except NameError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)"""

        if not arg:
            print("** class name missing **")
            return

        data = arg.split()
        if data[0] not in self.List_classes:
            print("** class doesn't exist **")
            return

        if len(data) == 1:
            print("** instance id missing **")
            return

        if len(data) == 2:
            print("** attribute name missing **")
            return

        if len(data) == 3:
            print("** value missing **")
            return

        class_id = data[0] + "." + data[1]
        atrr_name = data[2]
        if class_id not in storage.all().keys():
            print("** no instance found **")
            return

        for key, value in storage.all().items():
            if class_id == key:
                value.__dict__[atrr_name] = data[3]
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
